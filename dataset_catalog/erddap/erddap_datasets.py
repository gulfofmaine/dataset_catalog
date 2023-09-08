"""
Parse a full ERDDAP datasets.xml catalog
"""

from typing import Union

from pydantic import Field
from pydantic_xml import BaseXmlModel

from .dataset.base import BaseDataset
from .dataset.grid import GridDatasets, grid_types
from .dataset.table import TableDatasets, table_types


class ErddapDatasets(BaseXmlModel, tag="erddapDatasets", search_mode="unordered"):
    """
    Full ERDDAP dataset.xml catalog
    """

    datasets: list[Union[GridDatasets, TableDatasets]] = Field(
        ...,
        discriminator="type",
    )


dataset_types: dict[str, BaseDataset] = {**grid_types, **table_types}
