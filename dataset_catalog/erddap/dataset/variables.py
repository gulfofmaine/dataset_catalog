"""
ERDDAP variables
"""

from pydantic_xml import BaseXmlModel, element, wrapped

from .attributes import Attribute


class Variable(BaseXmlModel):
    """
    Shared ERDDAP variable configuration
    """

    source_name: str = element(tag="sourceName")
    destination_name: str = element(tag="destinationName")
    add_attributes: list[Attribute] = wrapped("addAttributes", default=[])


class AxisVariable(Variable):
    """ERDDAP axis (Xarray coordinate/dimension) variables"""

    pass


class DataVariable(Variable):
    """ERDDAP data variables"""

    pass
