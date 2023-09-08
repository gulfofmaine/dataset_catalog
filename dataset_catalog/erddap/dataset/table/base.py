"""
Base ERDDAP tabular dataset
"""

from ..base import BaseDataset


class BaseTable(BaseDataset):
    """
    Base ERDDAP tabular dataset

    Subclasses should implement .to_dataframe() to load
    their data into Pandas dataframes.
    """

    def to_dataframe(self):
        """Load dataset into a Pandas Dataframe"""
        raise NotImplementedError
