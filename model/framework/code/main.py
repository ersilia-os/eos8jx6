import os
import sys

import numpy as np
import pandas as pd

root        = os.path.dirname(os.path.abspath(__file__))
checkpoints = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))
input_file  = sys.argv[1]
output_file = sys.argv[2]

# LazyQSAR locates featurizer weights via $HOME/.lazyqsar/ — point it at our
# bundled copy. lazyqsar >=3.2.2 internally isolates MPLCONFIGDIR so matplotlib's
# font cache doesn't land under this HOME (see lazy-qsar#30).
os.environ["HOME"] = os.path.join(checkpoints, "featurizer_weights_home")

from lazyqsar.api.classifier_predict import predict as lqsar_predict
from ersilia_pack_utils.core import read_smiles, write_out

MODEL_NAMES = [
    "individual_ec50_decoys",
    "individual_mic_decoys_b",
    "individual_mic_decoys_a",
    "merged_mic80_decoys_a",
    "merged_iz_decoys_b",
    "merged_mic50_decoys_a",
    "merged_mic80_decoys_c",
    "merged_mic80_decoys_b",
    "merged_mic_decoys_d",
    "merged_iz_decoys_d",
    "merged_iz_decoys_c",
    "merged_mic_decoys_c",
    "merged_mic50_decoys_b",
    "merged_mic_decoys_b",
    "merged_mic_decoys_f",
    "merged_mic_decoys_e",
    "merged_mic80_decoys_d",
    "merged_mic_decoys_a",
    "merged_iz_decoys_a",
    "merged_ic50_decoys",
    "merged_gi_decoys",
    "general_mic",
    "general_mic80_decoys",
    "general_ec50_decoys",
    "general_inhibition",
    "general_iz",
    "general_activity_decoys",
    "general_ic50",
    "general_gi_decoys",
    "general_mic50",
    "general_mic90",
    "pubchem_a",
]
model_dir_dict = {m: os.path.join(checkpoints, "models", m) for m in MODEL_NAMES}

# In-memory I/O via ersilia-pack-utils (handles .csv and .bin).
_, smiles_list = read_smiles(input_file)
R, cols_ordered = lqsar_predict(
    model_dir=model_dir_dict,
    smiles=smiles_list,
    predict_type="rank",
)

# Index columns by name so we don't depend on dict-insertion order.
name_to_idx = {c: i for i, c in enumerate(cols_ordered)}
prob_ranks = np.nan_to_num(R[:, [name_to_idx[m] for m in MODEL_NAMES]], nan=0.0)

# Consensus (mirrors chembl-antimicrobial-models/scripts/14_consensus_scoring.py).
reports = pd.read_csv(os.path.join(checkpoints, "reports.csv")).set_index("model_name")
W_COLS = ["w1", "w2", "w3", "w4", "w5", "w6", "w7"]
W_ALL_WEIGHTS = np.ones(len(W_COLS) + 1)

w_quality  = np.array([reports.loc[m, W_COLS].values for m in MODEL_NAMES], dtype=float)
cutoffs    = np.array([reports.loc[m, "decision_cutoff_rank"] for m in MODEL_NAMES], dtype=float)

# w8: per-compound weight — 0 at/below decision cutoff, linear 0->1 above it.
c  = np.clip(cutoffs[np.newaxis, :], 0.0, 1.0 - 1e-9)
w8 = np.where(prob_ranks <= c, 0.0, (prob_ranks - c) / (1.0 - c))

n, M = prob_ranks.shape
w_all = np.empty((n, M, len(W_ALL_WEIGHTS)))
w_all[:, :, :len(W_COLS)] = w_quality
w_all[:, :,  len(W_COLS)] = w8
w_eff = np.average(w_all, axis=-1, weights=W_ALL_WEIGHTS)

consensus_raw = (prob_ranks * w_eff).sum(axis=1) / w_eff.sum(axis=1)

# Tanh IQR-restoring transform — k depends only on number of sub-models.
_TANH_A, _TANH_TAU = 1.156, 6.47
k = 2.0 * (1.0 + _TANH_A * (1.0 - np.exp(-M / _TANH_TAU)))
consensus = 0.5 + 0.5 * np.tanh(k * (consensus_raw - 0.5)) / np.tanh(k / 2)

results = np.round(np.column_stack([consensus, prob_ranks]), 4)
header  = ["consensus_score"] + MODEL_NAMES
write_out(results, header, output_file)
