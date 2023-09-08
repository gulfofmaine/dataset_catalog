"""
Combine other datasets along an axis

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridSideBySide
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseGrid

EDDGridSideBySide = Literal["EDDGridSideBySide"]


class GridSideBySide(BaseGrid):
    """
    Combine other datasets along an axis

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridSideBySide
    """

    type: EDDGridSideBySide = attr()
