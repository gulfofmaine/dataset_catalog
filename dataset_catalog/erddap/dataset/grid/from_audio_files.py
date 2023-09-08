"""
Aggregate a collection of audio files to treat as a gridded dataset

https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromAudioFiles
"""
from typing import Literal

from pydantic_xml import attr

from .from_files import GridFromFiles

EDDGridFromAudioFiles = Literal["EDDGridFromAudioFiles"]


class GridFromAudioFiles(GridFromFiles):
    """
    Aggregate a collection of audio files to treat as a gridded dataset

    https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#EDDGridFromAudioFiles
    """

    type: EDDGridFromAudioFiles = attr()
