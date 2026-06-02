# Antimicrobial activity prediction against Candida albicans from public ChEMBL and PubChem data

Bioactivity prediction of growth inhibition in Candida albicans, trained as binary (active/inactive) classifiers from publicly available data in ChEMBL and PubChem. Independent models are trained on multiple bioactivity datasets, corresponding to single-point (percent inhibition) and dose-response (MIC) assays, among others. A ranking score is provided for each model alongside a combined consensus score.

This model was incorporated on 2026-05-19.Last packaged on 2026-06-02.

## Information
### Identifiers
- **Ersilia Identifier:** `eos8jx6`
- **Slug:** `antimicrobial-activity-calbicans`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Candidiasis`
- **Target Organism:** `Candida albicans`
- **Tags:** `Antimicrobial activity`, `ChEMBL`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `35`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of antimicrobial activity against Candida albicans from 34 ChEMBL- and PubChem-trained sub-models, plus a quality-weighted consensus score.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| consensus_score | float | high | Tanh-transformed quality-weighted consensus probability across the 34 sub-models. Recommended threshold: 0.955. |
| individual_ec50_decoys | float | high | Probability from sub-model trained on ChEMBL assay CHEMBL1614164 (EC50 measurements; cutoff 10 uM; n=10870). Recommended threshold: 0.769. |
| individual_mic_decoys_b | float | high | Probability from sub-model trained on ChEMBL assay CHEMBL3266258 (MIC measurements; cutoff 10 uM; n=1110). Recommended threshold: 0.9. |
| individual_mic_decoys_a | float | high | Probability from sub-model trained on ChEMBL assay CHEMBL3266259 (MIC measurements; cutoff 10 uM; n=1060). Recommended threshold: 0.887. |
| merged_mic80_decoys_a | float | high | Probability from sub-model trained on MIC80 measurements merged across 12 ChEMBL assays (cutoff 10 uM; n=3180 incl. decoys). Recommended threshold: 0.889. |
| merged_iz_decoys_b | float | high | Probability from sub-model trained on IZ measurements merged across 10 ChEMBL assays (cutoff 10 mm; n=2070 incl. decoys). Recommended threshold: 0.896. |
| merged_mic50_decoys_a | float | high | Probability from sub-model trained on MIC50 measurements merged across 13 ChEMBL assays (cutoff 10 uM; n=1600 incl. decoys). Recommended threshold: 0.87. |
| merged_mic80_decoys_c | float | high | Probability from sub-model trained on MIC80 measurements merged across 3 ChEMBL assays (cutoff 10 uM; n=1590 incl. decoys). Recommended threshold: 0.879. |
| merged_mic80_decoys_b | float | high | Probability from sub-model trained on MIC80 measurements merged across 7 ChEMBL assays (cutoff 10 uM; n=1480 incl. decoys). Recommended threshold: 0.864. |
| merged_mic_decoys_b | float | high | Probability from sub-model trained on MIC measurements merged across 8 ChEMBL assays (cutoff 10 uM; n=1430 incl. decoys). Recommended threshold: 0.854. |

_10 of 35 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8jx6](https://hub.docker.com/r/ersiliaos/eos8jx6)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8jx6.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8jx6.zip)

### Resource Consumption
- **Model Size (Mb):** `647`
- **Environment Size (Mb):** `1896`
- **Image Size (Mb):** `3017.87`

**Computational Performance (seconds):**
- 10 inputs: `56.86`
- 100 inputs: `56.92`
- 10000 inputs: `1660.93`

### References
- **Source Code**: [https://github.com/ersilia-os/chembl-antimicrobial-models](https://github.com/ersilia-os/chembl-antimicrobial-models)
- **Publication**: [https://github.com/ersilia-os/chembl-antimicrobial-models](https://github.com/ersilia-os/chembl-antimicrobial-models)
- **Publication Type:** `Other`
- **Publication Year:** `2026`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos8jx6
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos8jx6
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
