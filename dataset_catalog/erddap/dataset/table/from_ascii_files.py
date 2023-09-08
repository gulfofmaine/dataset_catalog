"""
Table from aggregated comma, tab, semicolon, or space separated
ASCII files

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDTableFromAsciiFiles
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseTable

EDDTableFromAsciiFiles = Literal["EDDTableFromAsciiFiles"]


class TableFromAsciiFiles(BaseTable):
    """
    Table from aggregated comma, tab, semicolon, or space separated
    ASCII files

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDTableFromAsciiFiles
    """

    type: EDDTableFromAsciiFiles = attr()
