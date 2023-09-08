"""
Base ERDDAP dataset model
"""
from pydantic_xml import BaseXmlModel, attr


class BaseDataset(BaseXmlModel, tag="dataset", search_mode="unordered"):
    """
    Base ERDDAP dataset model
    """

    type: str = attr()
    dataset_id: str = attr(name="datasetID")
    active: bool = attr(default=True)
