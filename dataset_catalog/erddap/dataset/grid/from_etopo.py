"""
ERDDAP built in gridded elevation data

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromEtopo
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseGrid

EDDGridFromEtopo = Literal["EDDGridFromEtopo"]


class GridFromEtopo(BaseGrid):
    """
    ERDDAP built in gridded elevation data

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromEtopo
    """

    type: EDDGridFromEtopo = attr()
