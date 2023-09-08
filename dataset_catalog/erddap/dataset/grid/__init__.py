"""
ERDDAP gridded datasets
"""

from typing import Union

from .base import BaseGrid
from .from_aggregate_existing_dimension import (
    EDDGridAggregateExistingDimension,
    GridAggregateExistingDimension,
)
from .from_audio_files import EDDGridFromAudioFiles, GridFromAudioFiles
from .from_copy import EDDGridCopy, GridCopy
from .from_dap import EDDGridFromDap, GridFromDap
from .from_edd_table import EDDGridFromEDDTable, GridFromEDDTable
from .from_erddap import EDDGridFromErddap, GridFromErddap
from .from_etopo import EDDGridFromEtopo, GridFromEtopo
from .from_files import EDDGridFromFiles, GridFromFiles
from .from_lon_pm_180 import EDDGridLonPM180, GridLonPM180
from .from_lon_pm_360 import EDDGridLon0360, GridLon0360
from .from_merge_ir_files import EDDGridFromMergeIRFiles, GridFromMergeIRFiles
from .from_nc_files import EDDGridFromNcFiles, GridFromNcFiles
from .from_nc_files_unpacked import (
    EDDGridFromNcFilesUnpacked,
    GridFromNcFilesUnpacked,
)
from .from_side_by_side import EDDGridSideBySide, GridSideBySide

grid_types: dict[str, BaseGrid] = {
    EDDGridFromAudioFiles: GridFromAudioFiles,
    EDDGridFromDap: GridFromDap,
    EDDGridFromEDDTable: GridFromEDDTable,
    EDDGridFromErddap: GridFromErddap,
    EDDGridFromEtopo: GridFromEtopo,
    EDDGridFromFiles: GridFromFiles,
    EDDGridFromMergeIRFiles: GridFromMergeIRFiles,
    EDDGridFromNcFiles: GridFromNcFiles,
    EDDGridFromNcFilesUnpacked: GridFromNcFilesUnpacked,
    EDDGridLonPM180: GridLonPM180,
    EDDGridLon0360: GridLon0360,
    EDDGridSideBySide: GridSideBySide,
    EDDGridAggregateExistingDimension: GridAggregateExistingDimension,
    EDDGridCopy: GridCopy,
}

GridDatasets = Union[
    GridFromAudioFiles,
    GridFromDap,
    GridFromEDDTable,
    GridFromErddap,
    GridFromEtopo,
    GridFromFiles,
    GridFromMergeIRFiles,
    GridFromNcFiles,
    GridFromNcFilesUnpacked,
    GridLonPM180,
    GridLon0360,
    GridSideBySide,
    GridAggregateExistingDimension,
    GridCopy,
]
