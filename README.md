# Antimicrobial activity prediction against Candida albicans from public ChEMBL and PubChem data

Bioactivity prediction of growth inhibition in Candida albicans, trained as binary (active/inactive) classifiers from publicly available data in ChEMBL and PubChem. Independent models are trained on multiple bioactivity datasets, corresponding to single-point (Inhibition) and dose-response (MIC) assays, among others. A ranking score is provided for each model alongside a combined consensus score.

This model was incorporated on 2026-05-19.Last packaged on 2026-07-22.

## Information
### Identifiers
- **Ersilia Identifier:** `eos8jx6`
- **Slug:** `antimicrobial-activity-calbicans`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Candidiasis`, `Antimicrobial resistance`
- **Target Organism:** `Candida albicans`
- **Tags:** `Antimicrobial activity`, `ChEMBL`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `18`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of antimicrobial activity against Candida albicans from 17 ChEMBL- and PubChem-trained sub-models, plus a quality-weighted consensus score.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| consensus_score | float | high | Tanh-transformed quality-weighted consensus probability across the 17 sub-models. Recommended threshold: 0.897. |
| chembl_single_point_0 | float | high | Probability from sub-model trained on ChEMBL single-point signal-based pool of 174 assays (1717 compounds). Recommended threshold: 0.773. |
| chembl_single_point_1 | float | high | Probability from sub-model trained on ChEMBL single-point signal-based pool of 69 assays (949 compounds). Recommended threshold: 0.713. |
| chembl_single_point_2 | float | high | Probability from sub-model trained on ChEMBL single-point signal-based pool of 101 assays (842 compounds). Recommended threshold: 0.614. |
| chembl_single_point_3 | float | high | Probability from sub-model trained on ChEMBL single-point signal-based pool of 86 assays (695 compounds). Recommended threshold: 0.679. |
| chembl_single_point_4 | float | high | Probability from sub-model trained on ChEMBL single-point signal-based pool of 82 assays (627 compounds). Recommended threshold: 0.666. |
| chembl_dose_response_0 | float | high | Probability from sub-model trained on ChEMBL dose-response signal-based pool of 612 assays (7988 compounds). Recommended threshold: 0.782. |
| chembl_dose_response_1 | float | high | Probability from sub-model trained on ChEMBL dose-response signal-based pool of 628 assays (7670 compounds). Recommended threshold: 0.737. |
| chembl_dose_response_2 | float | high | Probability from sub-model trained on ChEMBL dose-response signal-based pool of 345 assays (4640 compounds). Recommended threshold: 0.678. |
| chembl_dose_response_3 | float | high | Probability from sub-model trained on ChEMBL dose-response signal-based pool of 79 assays (2490 compounds; incl. 88 added negatives). Recommended threshold: 0.468. |

_10 of 18 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8jx6](https://hub.docker.com/r/ersiliaos/eos8jx6)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8jx6.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8jx6.zip)

### Resource Consumption
- **Model Size (Mb):** `615`
- **Environment Size (Mb):** `7208`
- **Image Size (Mb):** `7952.88`

**Computational Performance (seconds):**
- 10 inputs: `81.54`
- 100 inputs: `82.49`
- 10000 inputs: `-1`

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
