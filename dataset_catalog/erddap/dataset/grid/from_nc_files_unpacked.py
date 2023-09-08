"""
Gridded datasets with additional transformations from aggregated NetCDFs

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromNcFilesUnpacked
"""
from typing import Literal

from pydantic_xml import attr

from .from_files import GridFromFiles

EDDGridFromNcFilesUnpacked = Literal["EDDGridFromNcFilesUnpacked"]


class GridFromNcFilesUnpacked(GridFromFiles):
    """
    Gridded datasets with additional transformations from aggregated NetCDFs

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromNcFilesUnpacked
    """

    type: EDDGridFromNcFilesUnpacked = attr()
