"""
Load gridded dataset from remote DAP compatible servers

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromDap
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseGrid

EDDGridFromDap = Literal["EDDGridFromDap"]


class GridFromDap(BaseGrid):
    """
    Load gridded dataset from remote DAP compatible servers

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromDap
    """

    type: EDDGridFromDap = attr()
