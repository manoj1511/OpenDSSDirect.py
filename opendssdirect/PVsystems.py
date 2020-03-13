# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ._utils import codec, CheckForError, api_util, Iterable


class IPVsystems(Iterable):
    __slots__ = []
    _api_prefix = "PVSystems"
    _columns = [
        "Name",
        "Idx",
        "pf",
        "Irradiance",
        "IrradianceNow",
        "Pmpp",
        "RegisterNames",
        "RegisterValues",
        "kVARated",
        "kW",
        "kvar",
        "daily",
        "duty",
        "yearly",
        "Tdaily",
        "Tduty",
        "Tyearly",
    ]

    def Irradiance(self, *args):
        """Get/set the present value of the Irradiance property in W/m²"""
        # Getter
        if len(args) == 0:
            return self._lib.PVSystems_Get_Irradiance()

        # Setter
        Value, = args
        self._lib.PVSystems_Set_Irradiance(Value)
        self.CheckForError()

    def pf(self, *args):
        """Get/set the power factor for the active PVSystem"""
        # Getter
        if len(args) == 0:
            return self._lib.PVSystems_Get_PF()

        # Setter
        Value, = args
        self._lib.PVSystems_Set_PF(Value)
        self.CheckForError()

    def RegisterNames(self):
        """(read-only) Array of PVSYSTEM energy meter register names"""
        return self._get_string_array(self._lib.PVSystems_Get_RegisterNames)

    def RegisterValues(self):
        """(read-only) Array of doubles containing values in PVSystem registers."""
        return self._get_float64_array(self._lib.PVSystems_Get_RegisterValues)

    def kVARated(self, *args):
        """Get/set Rated kVA of the PVSystem"""
        # Getter
        if len(args) == 0:
            return self._lib.PVSystems_Get_kVArated()

        # Setter
        Value, = args
        self._lib.PVSystems_Set_kVArated(Value)
        self.CheckForError()

    def kW(self):
        """(read-only) get kW output"""
        return self._lib.PVSystems_Get_kW()

    def kvar(self, *args):
        """Get/set kvar output value"""
        # Getter
        if len(args) == 0:
            return self._lib.PVSystems_Get_kvar()

        # Setter
        Value, = args
        self._lib.PVSystems_Set_kvar(Value)
        self.CheckForError()

    def daily(self, *args):
        """Name of the loadshape for a daily PVSystem profile."""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.PVSystems_Get_daily())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.PVSystems_Set_daily(Value)
        self.CheckForError()

    def duty(self, *args):
        """
    Name of the load shape to use for duty cycle dispatch simulations such as
    for solar ramp rate studies. Must be previously defined as a Loadshape
    object. Typically would have time intervals of 1-5 seconds.
    """
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.PVSystems_Get_duty())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.PVSystems_Set_duty(Value)
        self.CheckForError()

    def yearly(self, *args):
        """
    Dispatch shape to use for yearly simulations. Must be previously defined
    as a Loadshape object. If this is not specified, the Daily dispatch shape,
    if any, is repeated during Yearly solution modes. In the default dispatch
    mode, the PVSystem element uses this loadshape to trigger State changes.
    """
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.PVSystems_Get_yearly())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.PVSystems_Set_yearly(Value)
        self.CheckForError()

    def Tdaily(self, *args):
        """
    Temperature shape to use for daily simulations. Must be previously defined
    as a TShape object of 24 hrs, typically. The PVSystem element uses this
    TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree
    with the Pmpp vs T curve.
    """
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.PVSystems_Get_Tdaily())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.PVSystems_Set_Tdaily(Value)
        self.CheckForError()

    def Tduty(self, *args):
        """
    Temperature shape to use for duty cycle dispatch simulations such as for
    solar ramp rate studies. Must be previously defined as a TShape object.
    Typically would have time intervals of 1-5 seconds. Designate the number
    of points to solve using the Set Number=xxxx command. If there are fewer
    points in the actual shape, the shape is assumed to repeat. The PVSystem
    model uses this TShape to determine the Pmpp from the Pmpp vs T curve.
    Units must agree with the Pmpp vs T curve.
    """
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.PVSystems_Get_Tduty())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.PVSystems_Set_Tduty(Value)
        self.CheckForError()

    def Tyearly(self, *args):
        """
    Temperature shape to use for yearly simulations. Must be previously defined
    as a TShape object. If this is not specified, the Daily dispatch shape, if
    any, is repeated during Yearly solution modes. The PVSystem element uses
    this TShape to determine the Pmpp from the Pmpp vs T curve. Units must
    agree with the Pmpp vs T curve.
    """
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.PVSystems_Get_Tyearly())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.PVSystems_Set_Tyearly(Value)
        self.CheckForError()

    def IrradianceNow(self):
        """
    Returns the current irradiance value for the active PVSystem. Use it to 
    know what's the current irradiance value for the PV during a simulation.
    """
        return self._lib.PVSystems_Get_IrradianceNow()

    def Pmpp(self, *args):
        """
    Gets/sets the rated max power of the PV array for 1.0 kW/sq-m irradiance 
    and a user-selected array temperature of the active PVSystem.
    """
        # Getter
        if len(args) == 0:
            return self._lib.PVSystems_Get_Pmpp()

        # Setter
        Value, = args
        self._lib.PVSystems_Set_Pmpp(Value)
        self.CheckForError()


_PVsystems = IPVsystems(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _PVsystems.AllNames
Count = _PVsystems.Count
First = _PVsystems.First
Irradiance = _PVsystems.Irradiance
Name = _PVsystems.Name
Next = _PVsystems.Next
pf = _PVsystems.pf
RegisterNames = _PVsystems.RegisterNames
RegisterValues = _PVsystems.RegisterValues
Idx = _PVsystems.Idx
kVARated = _PVsystems.kVARated
kW = _PVsystems.kW
kvar = _PVsystems.kvar
daily = _PVsystems.daily
duty = _PVsystems.duty
yearly = _PVsystems.yearly
Tdaily = _PVsystems.Tdaily
Tduty = _PVsystems.Tduty
Tyearly = _PVsystems.Tyearly
IrradianceNow = _PVsystems.IrradianceNow
Pmpp = _PVsystems.Pmpp
_columns = _PVsystems._columns
__all__ = [
    "AllNames",
    "Count",
    "First",
    "Irradiance",
    "Name",
    "Next",
    "pf",
    "RegisterNames",
    "RegisterValues",
    "Idx",
    "kVARated",
    "kW",
    "kvar",
    "daily",
    "duty",
    "yearly",
    "Tdaily",
    "Tduty",
    "Tyearly",
    "IrradianceNow",
    "Pmpp",
]
