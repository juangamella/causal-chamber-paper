# The Causal Chambers: Experiment Repository

This repository contains the code to reproduce the case studies of the 2024 paper [*The Causal Chambers: Real Physical Systems as a Testbed for AI Methodology*](<https://placehold.co/600x400?text=Placeholder:\nArxiv link!>) by Juan L. Gamella, Jonas Peters and Peter Bühlmann.

For the datasets, mechanistic models, datasheets and resources to build the chambers, please visit [causalchamber.org](https://causalchamber.org).

## Repository Structure

The code is contained in well-documented Jupyter notebooks, which make use of the [causalchamber](https://pypi.org/project/causalchamber/) package to load the pertaining datasets. The following table serves as an index.

| Path            | Description   |
|---------------:|:-------------|
| [`case_studies/causal_discovery_iid.ipynb`](case_studies/causal_discovery_iid.ipynb) | Case study for causal discovery from i.i.d. data (tasks a1 and a2 in [Fig. 5](<https://placehold.co/600x400?text=Placeholder:\nArxiv link!>)) |
| [`case_studies/causal_discovery_time.ipynb`](case_studies/causal_discovery_time.ipynb) | Case study for causal discovery from time-series data (task a3 in [Fig. 5](<https://placehold.co/600x400?text=Placeholder:\nArxiv link!>))
| [`case_studies/ood_sensors.ipynb`](case_studies/ood_sensors.ipynb) | Task b1 (sensor measurements) of the OOD-generalization case study. ([Fig. 5b](<https://placehold.co/600x400?text=Placeholder:\nArxiv link!>))|
| [`case_studies/ood_images.ipynb`](case_studies/ood_images.ipynb) | Task b2 (images) of the OOD-generalization case study. ([Fig. 5b](<https://placehold.co/600x400?text=Placeholder:\nArxiv link!>))|
| [`case_studies/ood_impulses.ipynb`](case_studies/ood_impulses.ipynb) |  Task b3 (impulse-response curves) of the OOD-generalization case study. ([Fig. 5b](<https://placehold.co/600x400?text=Placeholder:\nArxiv link!>))|
| [`case_studies/changepoints.ipynb`](case_studies/changepoints.ipynb) | Change point detection case study ([Fig. 5c](<https://placehold.co/600x400?text=Placeholder:\nArxiv link!>))|
| [`case_studies/ica.ipynb`](case_studies/ica.ipynb) | Case study for independent component analysis (tasks d1, d2 and d3 in [Fig. 6](<https://placehold.co/600x400?text=Placeholder:\nArxiv link!>))|
| [`case_studies/symbolic_regression.ipynb`](case_studies/symbolic_regression.ipynb) | Symbolic regression case study ([Fig. 6e](<https://placehold.co/600x400?text=Placeholder:\nArxiv link!>)) |
| [`case_studies/mechanistic_models.ipynb`](case_studies/mechanistic_models.ipynb) | Contains examples of running the mechanistic models described in appendix IV, including the code for the case study in ([Fig. 6f](<https://placehold.co/600x400?text=Placeholder:\nArxiv link!>)) and the additional plots in appendix IV. |
| [`plots_appendices.ipynb`](plots_appendices.ipynb) | Contains the code to produce figures 7-15 in appendix III and compute the calibrated reference voltages in Table 3. |
| [`causal_validation.ipynb`](causal_validation.ipynb) | Contains the code to produce Tables 5-8 in appendix V of the manuscript. |

The directory `case_studies/src` contains supporting code for the notebooks, such as a wrapper for UT-IGSP<sup>[[1]](#references)</sup> and the code for the symbolic regression algorithm<sup>[[2]](#references)</sup> used in the corresponding case study.

## Licenses

All code is shared under the [MIT license](https://opensource.org/license/mit/). A copy of the license can also be found in [LICENSE.txt](LICENSE.txt).

## References

[1] Squires, Chandler, Yuhao Wang, and Caroline Uhler. "Permutation-based causal structure learning with unknown intervention targets." Conference on Uncertainty in Artificial Intelligence. PMLR, 2020.

[2] Kamienny, Pierre-Alexandre, et al. "End-to-end symbolic regression with transformers." Advances in Neural Information Processing Systems 35 (2022): 10269-10281.
