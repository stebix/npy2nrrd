import dataclasses
import numpy as np

from collections.abc import Mapping
from pathlib import Path


@dataclasses.dataclass
class NumpyWriteJob:
    data: np.ndarray
    path: Path
    force: bool



@dataclasses.dataclass
class DetachedHeaderWriteJob:
    header: Mapping
    path: Path
    force: bool



@dataclasses.dataclass
class NRRDWriteJob:
    data: np.ndarray
    path: Path
    header: Mapping | None