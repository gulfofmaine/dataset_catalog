"""
Table from aggregated NetCDF files

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDTableFromNcFiles
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseTable

EDDTableFromNcFiles = Literal["EDDTableFromNcFiles"]


class TableFromNcFiles(BaseTable):
    """
    Table from aggregated NetCDF files

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDTableFromNcFiles
    """

    type: EDDTableFromNcFiles = attr()
