"""
Make a copy of a remote ERDDAP grid dataset

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridCopy
"""

from typing import Literal

from pydantic_xml import attr

from .base import BaseGrid

EDDGridCopy = Literal["EDDGridCopy"]


class GridCopy(BaseGrid):
    """
    Make a copy of a remote ERDDAP grid dataset

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridCopy
    """

    type: EDDGridCopy = attr()
