# 📘 KASBA: k-means Accelerated Stochastic Subgradient Barycentre Averaging
**Official Repository for the KASBA Time Series Clustering Paper**

This repository accompanies the paper:

> **Rock the KASBA: Blazingly Fast and Accurate Time Series Clustering**
>
> Data Mining and Knowledge Discovery, 2026. https://doi.org/10.1007/s10618-026-01189-9

KASBA is a $k$-means clustering algorithm that uses the Move-Split-Merge (MSM) elastic distance at all stages of clustering, applies a randomised stochastic subgradient descent to find barycentre centroids, links each stage of clustering to accelerate convergence and exploits the metric property of MSM distance to avoid a large proportion of distance calculations. It is a versatile and scalable clusterer designed for real-world TSCL applications. It allows practitioners to balance  runtime and clustering performance when similarity is best measured by an elastic distance.

KASBA delivers state-of-the-art clustering performance while achieving 1–3 orders of magnitude speedups over existing elastic distance–based k-means algorithms.

This repository contains the exact model configurations, experiment scripts, and visualisation tools used to produce the results in the paper.

---

## 📁 Repository Structure

    kasba-clustering-2026/
    ├── README.md                   # This file
    ├── _utils.py                   # Internal utilities used across the project
    ├── _model_configuration.py     # Definitions of all models and configurations used in experiments
    ├── _experiment_script.py       # Script used to run experiments on datasets
    ├── kasba.ipynb                 # Notebook demonstrating how to run KASBA
    ├── result_visualisation.ipynb  # Notebook for generating CD diagrams, MCM plots, etc.
    └── results/                    # Raw CSV result files used in the paper
        └── combined                # Subfolder for combined results
            └── k-shape-compare     # Subfolders results in section 5.4
            └── section-5.1         # Subfolders results in section 5.1
        └── train-test              # Subfolders for train and test results
            └── section-5.1         # Subfolders results in section 5.1
            └── section-5.2         # Subfolders results in section 5.2
            └── section-5.3         # Subfolders results in section 5.3


## 🚀 Getting Started

### Install dependencies

Create and activate a virtual environment in this repository:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

The results in the paper were produced with a development branch of aeon. To
install that version, run:

    pip uninstall aeon
    pip install git+https://github.com/aeon-toolkit/aeon@65115e407f1a4baed47180ba4142c65269f2c07d#egg=aeon

Note: The project uses aeon, numpy, matplotlib, and other standard scientific Python packages.

---

## 🧪 Running KASBA

Minimal example from the kasba.ipynb notebook:

    from aeon.clustering import KASBA
    from aeon.datasets import load_dataset

    X, y = load_dataset("GunPoint")

    model = KASBA(
        n_clusters=2,
        distance="msm",
        distance_params={
            "c": 1.0
        },
    )

    labels = model.fit_predict(X)

The notebook demonstrates:

- How to use KASBA with different elastic distances
- How to cluster multivariate or unequal-length time series
- How to run multiple initialisations
- How to inspect convergence behaviour

---

## 📊 Reproducing Figures (CD & MCM)

Use the result_visualisation.ipynb notebook to generate:

- Critical Difference diagrams
- Model Comparison Matrices
- Ranking curves and statistical tests

---

## 📜 Citation

If you use KASBA in academic work, please cite the paper:

```bibtex
@article{holder2026rock,
  title={Rock the KASBA: blazingly fast and accurate time series clustering},
  author={Holder, Christopher and Bagnall, Anthony},
  journal={Data Mining and Knowledge Discovery},
  volume={40},
  number={2},
  pages={21},
  year={2026},
  publisher={Springer},
  doi={10.1007/s10618-026-01189-9}
}
```

---

## 🤝 Contact

For questions about the paper or this repository, feel free to email the authors or
contact us on the [aeon Discord](https://discord.gg/D6rzqHGKRJ).
