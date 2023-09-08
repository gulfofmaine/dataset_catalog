"""
Superclass of most xyz from files gridded datasets

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromFiles
"""
from pathlib import Path
from typing import Literal, Optional

from pydantic_xml import attr, element, wrapped

from ..attributes import Attribute
from ..variables import AxisVariable, DataVariable
from .base import BaseGrid

EDDGridFromFiles = Literal["EDDGridFromFiles"]


class GridFromFiles(BaseGrid):
    """
    Superclass of most xyz from files gridded datasets

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromFiles
    """

    type: EDDGridFromFiles = attr()

    accessible_to: Optional[list[str]] = element(tag="accessibleTo", default=None)
    # graphs_accessible_to
    reload_every_n_minutes: Optional[int] = element(
        tag="reloadEveryNMinutes",
        default=None,
    )
    # update_every_n_millis
    # default_data_query
    # default_graph_query
    # match_axis_n_digits
    # n_threads
    # dimension_values_in_memory
    # fgdc_file
    # iso_19115_file
    # on_change

    file_dir: Path = element(tag="fileDir")
    recursive: Optional[bool] = element(default=False)
    # path_regex
    file_name_regex: Optional[str] = element(tag="fileNameRegex", default=None)
    # accessible_via_files
    metadata_from: Literal["first", "last"] = element(tag="metadataFrom")
    file_table_in_memeory: Optional[bool] = element(
        tag="fileTableInMemory",
        default=None,
    )
    # cache_from_url
    # cache_size_gb

    add_attributes: list[Attribute] = wrapped("addAttributes", default=[])

    axis_variables: list[AxisVariable] = element(tag="axisVariable")
    data_variables: list[DataVariable] = element(tag="dataVariable")
