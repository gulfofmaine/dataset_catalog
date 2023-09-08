"""
Convert underlying ERDDAP tabular dataset into a gridded one

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromEDDTable
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseGrid

EDDGridFromEDDTable = Literal["EDDGridFromEDDTable"]


class GridFromEDDTable(BaseGrid):
    """
    Convert underlying ERDDAP tabular dataset into a gridded one

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromEDDTable
    """

    type: EDDGridFromEDDTable = attr()
