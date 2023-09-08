"""
Transform enclosed gridded dataset from 0 to 360 longitudes
to -180 to 180 longitudes

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridLonPM180
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseGrid

EDDGridLonPM180 = Literal["EDDGridLonPM180"]


class GridLonPM180(BaseGrid):
    """
    Transform enclosed gridded dataset from 0 to 360 longitudes
    to -180 to 180 longitudes

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridLonPM180
    """

    type: EDDGridLonPM180 = attr()
