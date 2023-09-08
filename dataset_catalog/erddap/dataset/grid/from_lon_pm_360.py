"""
Transform enclosed gridded dataset from -180 to 180 longitudes
to 0 to 360 longitudes

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridLon0360
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseGrid

EDDGridLon0360 = Literal["EDDGridLon0360"]


class GridLon0360(BaseGrid):
    """
    Transform enclosed gridded dataset from -180 to 180 longitudes
    to 0 to 360 longitudes

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridLon0360
    """

    type: EDDGridLon0360 = attr()
