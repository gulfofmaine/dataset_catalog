"""
Gridded dataset base
"""
from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    import xarray as xr

from ..base import BaseDataset


class BaseGrid(BaseDataset):
    """
    Base gridded datasets
    """

    pass


@runtime_checkable
class GridToXarrayProtocol(Protocol):
    """Gridded datasets that can be converted into Xarray Datasets"""

    def to_dataset(self) -> "xr.Dataset":
        """Return a dataset from a"""
