"""Test that the KASBA experiments run with each model configuration."""

import os

import pytest
from tsml_eval.testing.testing_utils import _TEST_DATA_PATH
from tsml_eval.utils.results_validation import validate_results_file

from _experiment_script import run_threaded_clustering_experiment

_REPO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_TEST_RESULTS_PATH = f"{_REPO_PATH}/test_output/"
_DATASET = "MinimalChinatown"


def _results_file(clusterer_name, split):
    return (
        f"{_TEST_RESULTS_PATH}{clusterer_name}/Predictions/{_DATASET}/"
        f"{split}Resample0.csv"
    )


@pytest.mark.parametrize(
    "clusterer_name",
    [
        "KASBA",
        "DBA",
        "shape-DBA",
        "MBA",
        "Euclid",
        "MSM",
        "k-SC",
        "KASBA-twe",
        "KASBA-vldb",
        "Euclid-vldb",
    ],
)
def test_run_experiment(clusterer_name):
    """Test each model from the paper runs on the default train/test split."""
    run_threaded_clustering_experiment(
        dataset=_DATASET,
        clusterer_name=clusterer_name,
        dataset_path=_TEST_DATA_PATH,
        results_path=_TEST_RESULTS_PATH,
        combine_test_train=False,
        resample_id=0,
    )

    for split in ["train", "test"]:
        file = _results_file(clusterer_name, split)
        assert validate_results_file(file)
        os.remove(file)


def test_run_experiment_combined():
    """Test an experiment on the combined train and test data."""
    run_threaded_clustering_experiment(
        dataset=_DATASET,
        clusterer_name="KASBA",
        dataset_path=_TEST_DATA_PATH,
        results_path=_TEST_RESULTS_PATH,
        combine_test_train=True,
        resample_id=0,
    )

    file = _results_file("KASBA", "train")
    assert validate_results_file(file)
    assert not os.path.exists(_results_file("KASBA", "test"))
    os.remove(file)


def test_run_experiment_invalid():
    """Test an unknown model name raises an error."""
    with pytest.raises(ValueError, match="Unknown clusterer_name"):
        run_threaded_clustering_experiment(
            dataset=_DATASET,
            clusterer_name="invalid",
            dataset_path=_TEST_DATA_PATH,
            results_path=_TEST_RESULTS_PATH,
            combine_test_train=False,
            resample_id=0,
        )
