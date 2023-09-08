"""
Tables from aggregated CF DSG compliant NetCDFs

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDTableFromNcCFFiles
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseTable

EDDTableFromNcCFFiles = Literal["EDDTableFromNcCFFiles"]


class TableFromNcCFFiles(BaseTable):
    """
    Tables from aggregated CF DSG compliant NetCDFs

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDTableFromNcCFFiles
    """

    type: EDDTableFromNcCFFiles = attr()
