# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import api_util, Base


class IElement(Base):
    __slots__ = ["Properties"]
    _api_prefix = "DSSElement"
    _columns = ["AllPropertyNames", "Name", "NumProperties"]

    def AllPropertyNames(self):
        """(read-only) Array of strings containing the names of all properties for the active DSS object."""
        return self._get_string_array(self._lib.DSSElement_Get_AllPropertyNames)

    def Name(self):
        """(read-only) Full Name of Active DSS Object (general element or circuit element)."""
        return self._get_string(self._lib.DSSElement_Get_Name())

    def NumProperties(self):
        """(read-only) Number of Properties for the active DSS object."""
        return self._lib.DSSElement_Get_NumProperties()


_Element = IElement(api_util)

# For backwards compatibility, bind to the default instance
AllPropertyNames = _Element.AllPropertyNames
Name = _Element.Name
NumProperties = _Element.NumProperties
_columns = _Element._columns
__all__ = ["AllPropertyNames", "Name", "NumProperties"]
