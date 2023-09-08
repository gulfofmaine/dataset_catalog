"""
Gridded dataset from aggregated GRIB, HDF, NcML, or NetCDF files

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromNcFiles
"""
from typing import Literal

from pydantic_xml import attr

from .from_files import GridFromFiles

EDDGridFromNcFiles = Literal["EDDGridFromNcFiles"]


class GridFromNcFiles(GridFromFiles):
    """
    Gridded dataset from aggregated GRIB, HDF, NcML, or NetCDF files

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromNcFiles
    """

    type: EDDGridFromNcFiles = attr()
