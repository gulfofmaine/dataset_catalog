"""
Tables from Thredds Files

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDTableFromThreddsFiles
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseTable

EDDTableFromThreddsFiles = Literal["EDDTableFromThreddsFiles"]


class TableFromThreddsFiles(BaseTable):
    """
    Tables from Thredds Files

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDTableFromThreddsFiles
    """

    type: EDDTableFromThreddsFiles = attr()
