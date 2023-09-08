"""
Table from aggregated multidimensional NetCDF files

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDTableFromMultidimNcFiles
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseTable

EDDTableFromMultidimNcFiles = Literal["EDDTableFromMultidimNcFiles"]


class TableFromMultidimNcFiles(BaseTable):
    """
    Table from aggregated multidimensional NetCDF files

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDTableFromMultidimNcFiles
    """

    type: EDDTableFromMultidimNcFiles = attr()
