"""
ERDDAP dataset additional attributes
"""

from typing import Optional, Union

from pydantic_xml import BaseXmlModel, attr


class Attribute(BaseXmlModel, tag="att", search_mode="unordered"):
    """
    ERDDAP dataset additional attributes
    """

    name: str = attr(name="name")
    type: Optional[str] = attr(name="type", default=None)
    value: Union[str, int, float]
