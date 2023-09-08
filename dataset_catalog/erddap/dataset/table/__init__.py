"""
ERDDAP tabular datasets
"""
from typing import Union

from .base import BaseTable
from .from_ascii_files import EDDTableFromAsciiFiles, TableFromAsciiFiles
from .from_erddap import EDDTableFromErddap, TableFromErddap
from .from_multi_dim_nc_files import (
    EDDTableFromMultidimNcFiles,
    TableFromMultidimNcFiles,
)
from .from_nc_cf_files import EDDTableFromNcCFFiles, TableFromNcCFFiles
from .from_nc_files import EDDTableFromNcFiles, TableFromNcFiles
from .from_thredds_files import EDDTableFromThreddsFiles, TableFromThreddsFiles

table_types: dict[str, BaseTable] = {
    EDDTableFromAsciiFiles: TableFromAsciiFiles,
    EDDTableFromErddap: TableFromErddap,
    EDDTableFromMultidimNcFiles: TableFromMultidimNcFiles,
    EDDTableFromNcCFFiles: TableFromNcCFFiles,
    EDDTableFromNcFiles: TableFromNcFiles,
    EDDTableFromThreddsFiles: TableFromThreddsFiles,
}

TableDatasets = Union[
    TableFromAsciiFiles,
    TableFromErddap,
    TableFromMultidimNcFiles,
    TableFromNcCFFiles,
    TableFromNcFiles,
    TableFromThreddsFiles,
]
