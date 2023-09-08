"""
Aggregate child datasets along a dimension

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridAggregateExistingDimension
"""
from typing import Literal

from pydantic_xml import attr

from .base import BaseGrid

EDDGridAggregateExistingDimension = Literal["EDDGridAggregateExistingDimension"]


class GridAggregateExistingDimension(BaseGrid):
    """
    Aggregate child datasets along a dimension

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridAggregateExistingDimension
    """

    type: EDDGridAggregateExistingDimension = attr()
