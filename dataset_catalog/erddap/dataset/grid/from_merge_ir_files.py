"""
Gridded datasets from aggregated MergeIR files from NASA

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromMergeIRFiles
"""
from typing import Literal

from pydantic_xml import attr

from .from_files import GridFromFiles

EDDGridFromMergeIRFiles = Literal["EDDGridFromMergeIRFiles"]


class GridFromMergeIRFiles(GridFromFiles):
    """
    Gridded datasets from aggregated MergeIR files from NASA

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromMergeIRFiles
    """

    type: EDDGridFromMergeIRFiles = attr()
