"""
Gridded dataset from a remote ERDDAP server

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromErddap
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseGrid

EDDGridFromErddap = Literal["EDDGridFromErddap"]


class GridFromErddap(BaseGrid):
    """
    Gridded dataset from a remote ERDDAP server

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromErddap
    """

    type: EDDGridFromErddap = attr()
