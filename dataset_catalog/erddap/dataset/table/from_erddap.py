"""
Load a table from a remote ERDDAP server

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDTableFromErddap
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseTable

EDDTableFromErddap = Literal["EDDTableFromErddap"]


class TableFromErddap(BaseTable):
    """
    Load a table from a remote ERDDAP server

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDTableFromErddap
    """

    type: EDDTableFromErddap = attr()
