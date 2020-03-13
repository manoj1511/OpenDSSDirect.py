# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ._utils import CheckForError, api_util, Iterable


class ICNData(Iterable):
    """Experimental API extension exposing CNData objects"""

    _api_prefix = "CNData"
    __slots__ = []
    _columns = [
        "Name",
        "Idx",
        "NormAmps",
        "EmergAmps",
        "Rdc",
        "Rac",
        "ResistanceUnits",
        "GMRac",
        "GMRUnits",
        "Radius",
        "Diameter",
        "RadiusUnits",
        "EpsR",
        "InsLayer",
        "DiaIns",
        "DiaCable",
        "DiaStrand",
        "RStrand",
        "k",
    ]

    def EmergAmps(self, *args):
        """Emergency ampere rating"""
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_EmergAmps()

        # Setter
        Value, = args
        self._lib.CNData_Set_EmergAmps(Value)
        self.CheckForError()

    def NormAmps(self, *args):
        """Normal Ampere rating"""
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_NormAmps()

        # Setter
        Value, = args
        self._lib.CNData_Set_NormAmps(Value)
        self.CheckForError()

    def Rdc(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_Rdc()

        # Setter
        Value, = args
        self._lib.CNData_Set_Rdc(Value)
        self.CheckForError()

    def Rac(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_Rac()

        # Setter
        Value, = args
        self._lib.CNData_Set_Rac(Value)
        self.CheckForError()

    def GMRac(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_GMRac()

        # Setter
        Value, = args
        self._lib.CNData_Set_GMRac(Value)
        self.CheckForError()

    def GMRUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_GMRUnits()

        # Setter
        Value, = args
        self._lib.CNData_Set_GMRUnits(Value)
        self.CheckForError()

    def Radius(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_Radius()

        # Setter
        Value, = args
        self._lib.CNData_Set_Radius(Value)
        self.CheckForError()

    def RadiusUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_RadiusUnits()

        # Setter
        Value, = args
        self._lib.CNData_Set_RadiusUnits(Value)
        self.CheckForError()

    def ResistanceUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_ResistanceUnits()

        # Setter
        Value, = args
        self._lib.CNData_Set_ResistanceUnits(Value)
        self.CheckForError()

    def Diameter(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_Diameter()

        # Setter
        Value, = args
        self._lib.CNData_Set_Diameter(Value)
        self.CheckForError()

    def EpsR(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_EpsR()

        # Setter
        Value, = args
        self._lib.CNData_Set_EpsR(Value)
        self.CheckForError()

    def InsLayer(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_InsLayer()

        # Setter
        Value, = args
        self._lib.CNData_Set_InsLayer(Value)
        self.CheckForError()

    def DiaIns(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_DiaIns()

        # Setter
        Value, = args
        self._lib.CNData_Set_DiaIns(Value)
        self.CheckForError()

    def DiaCable(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_DiaCable()

        # Setter
        Value, = args
        self._lib.CNData_Set_DiaCable(Value)
        self.CheckForError()

    def k(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_k()

        # Setter
        Value, = args
        self._lib.CNData_Set_k(Value)
        self.CheckForError()

    def DiaStrand(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_DiaStrand()

        # Setter
        Value, = args
        self._lib.CNData_Set_DiaStrand(Value)
        self.CheckForError()

    def GmrStrand(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_GmrStrand()

        # Setter
        Value, = args
        self._lib.CNData_Set_GmrStrand(Value)
        self.CheckForError()

    def RStrand(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CNData_Get_RStrand()

        # Setter
        Value, = args
        self._lib.CNData_Set_RStrand(Value)
        self.CheckForError()


_CNData = ICNData(api_util)

# For backwards compatibility, bind to the default instance
EmergAmps = _CNData.EmergAmps
NormAmps = _CNData.NormAmps
Rdc = _CNData.Rdc
Rac = _CNData.Rac
GMRac = _CNData.GMRac
GMRUnits = _CNData.GMRUnits
Radius = _CNData.Radius
RadiusUnits = _CNData.RadiusUnits
ResistanceUnits = _CNData.ResistanceUnits
Diameter = _CNData.Diameter
EpsR = _CNData.EpsR
InsLayer = _CNData.InsLayer
DiaIns = _CNData.DiaIns
DiaCable = _CNData.DiaCable
k = _CNData.k
DiaStrand = _CNData.DiaStrand
GmrStrand = _CNData.GmrStrand
RStrand = _CNData.RStrand
Idx = _CNData.Idx
First = _CNData.First
Next = _CNData.Next
AllNames = _CNData.AllNames
Count = _CNData.Count
Name = _CNData.Name
_columns = _CNData._columns
__all__ = [
    "EmergAmps",
    "NormAmps",
    "Rdc",
    "Rac",
    "GMRac",
    "GMRUnits",
    "Radius",
    "RadiusUnits",
    "ResistanceUnits",
    "Diameter",
    "EpsR",
    "InsLayer",
    "DiaIns",
    "DiaCable",
    "k",
    "DiaStrand",
    "GmrStrand",
    "RStrand",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
]
