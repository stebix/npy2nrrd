"""
Basic converter functions for npy2nrrd package.

@Author: Jannik Stebani 2024
"""
from collections.abc import Mapping
from pathlib import Path

import json
import numpy as np
import nrrd


def read_detached_header(path: Path) -> Mapping:
    """
    Read detached header from JSON file.

    Parameters
    ----------

    path : Path
        Path to the input JSON file.

    Returns
    -------

    Mapping
        Detached header read from the JSON file.
    """
    with open(path, mode='r') as f:
        return json.load(f)



def read_npy(path: Path) -> np.ndarray:
    """
    Read NPY file to numpy array.

    Parameters
    ----------

    path : Path
        Path to the input NPY file.

    Returns
    -------

    np.ndarray
        Numpy array read from the NPY file.
    """
    return np.load(path)



def write_nrrd(data: np.ndarray, path: Path,
               header: Mapping | None = None,
               force: bool = False) -> Path:
    """
    Write NRRD file from numpy array.

    Parameters
    ----------

    data : np.ndarray
        Numpy array to be written to NRRD file.

    path : Path
        Path to the output NRRD file.

    header : Mapping | None
        Optional header for the NRRD file.

    force : bool
        Overwrite output file if it exists.

    Returns
    -------

    Path
        Path to the output NRRD file.
    """
    if path.exists() and not force:
        raise FileExistsError(f'File \'{path.resolve()}\' already exists. Use --force to overwrite.')
    nrrd.write(str(path), data, header=header)
    return path