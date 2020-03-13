# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ._utils import codec, CheckForError, api_util, Iterable


class ICapControls(Iterable):
    __slots__ = []
    _api_prefix = "CapControls"
    _columns = [
        "Name",
        "Idx",
        "Capacitor",
        "CTRatio",
        "PTRatio",
        "DeadTime",
        "Delay",
        "DelayOff",
        "Vmin",
        "Vmax",
        "UseVoltOverride",
        "Mode",
        "MonitoredObj",
        "MonitoredTerm",
        "OFFSetting",
        "ONSetting",
    ]

    def Reset(self):
        self._lib.CapControls_Reset()

    def CTRatio(self, *args):
        """Transducer ratio from pirmary current to control current."""
        # Getter
        if len(args) == 0:
            return self._lib.CapControls_Get_CTratio()

        # Setter
        Value, = args
        self._lib.CapControls_Set_CTratio(Value)
        self.CheckForError()

    def Capacitor(self, *args):
        """Name of the Capacitor that is controlled."""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.CapControls_Get_Capacitor())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.CapControls_Set_Capacitor(Value)
        self.CheckForError()

    def DeadTime(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.CapControls_Get_DeadTime()

        # Setter
        Value, = args
        self._lib.CapControls_Set_DeadTime(Value)
        self.CheckForError()

    def Delay(self, *args):
        """Time delay [s] to switch on after arming.  Control may reset before actually switching."""
        # Getter
        if len(args) == 0:
            return self._lib.CapControls_Get_Delay()

        # Setter
        Value, = args
        self._lib.CapControls_Set_Delay(Value)
        self.CheckForError()

    def DelayOff(self, *args):
        """Time delay [s] before swithcing off a step. Control may reset before actually switching."""
        # Getter
        if len(args) == 0:
            return self._lib.CapControls_Get_DelayOff()

        # Setter
        Value, = args
        self._lib.CapControls_Set_DelayOff(Value)
        self.CheckForError()

    def Mode(self, *args):
        """Type of automatic controller."""
        # Getter
        if len(args) == 0:
            return self._lib.CapControls_Get_Mode()

        # Setter
        Value, = args
        self._lib.CapControls_Set_Mode(Value)
        self.CheckForError()

    def MonitoredObj(self, *args):
        """Full name of the element that PT and CT are connected to."""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.CapControls_Get_MonitoredObj())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.CapControls_Set_MonitoredObj(Value)
        self.CheckForError()

    def MonitoredTerm(self, *args):
        """Terminal number on the element that PT and CT are connected to."""
        # Getter
        if len(args) == 0:
            return self._lib.CapControls_Get_MonitoredTerm()

        # Setter
        Value, = args
        self._lib.CapControls_Set_MonitoredTerm(Value)
        self.CheckForError()

    def OFFSetting(self, *args):
        """Threshold to switch off a step. See Mode for units."""
        # Getter
        if len(args) == 0:
            return self._lib.CapControls_Get_OFFSetting()

        # Setter
        Value, = args
        self._lib.CapControls_Set_OFFSetting(Value)
        self.CheckForError()

    def ONSetting(self, *args):
        """Threshold to arm or switch on a step.  See Mode for units."""
        # Getter
        if len(args) == 0:
            return self._lib.CapControls_Get_ONSetting()

        # Setter
        Value, = args
        self._lib.CapControls_Set_ONSetting(Value)
        self.CheckForError()

    def PTRatio(self, *args):
        """Transducer ratio from primary feeder to control voltage."""
        # Getter
        if len(args) == 0:
            return self._lib.CapControls_Get_PTratio()

        # Setter
        Value, = args
        self._lib.CapControls_Set_PTratio(Value)
        self.CheckForError()

    def UseVoltOverride(self, *args):
        """Enables Vmin and Vmax to override the control Mode"""
        # Getter
        if len(args) == 0:
            return self._lib.CapControls_Get_UseVoltOverride() != 0

        # Setter
        Value, = args
        self._lib.CapControls_Set_UseVoltOverride(Value)
        self.CheckForError()

    def Vmax(self, *args):
        """With VoltOverride, swtich off whenever PT voltage exceeds this level."""
        # Getter
        if len(args) == 0:
            return self._lib.CapControls_Get_Vmax()

        # Setter
        Value, = args
        self._lib.CapControls_Set_Vmax(Value)
        self.CheckForError()

    def Vmin(self, *args):
        """With VoltOverride, switch ON whenever PT voltage drops below this level."""
        # Getter
        if len(args) == 0:
            return self._lib.CapControls_Get_Vmin()

        # Setter
        Value, = args
        self._lib.CapControls_Set_Vmin(Value)
        self.CheckForError()


_CapControls = ICapControls(api_util)

# For backwards compatibility, bind to the default instance
Reset = _CapControls.Reset
AllNames = _CapControls.AllNames
CTRatio = _CapControls.CTRatio
Capacitor = _CapControls.Capacitor
Count = _CapControls.Count
DeadTime = _CapControls.DeadTime
Delay = _CapControls.Delay
DelayOff = _CapControls.DelayOff
First = _CapControls.First
Mode = _CapControls.Mode
MonitoredObj = _CapControls.MonitoredObj
MonitoredTerm = _CapControls.MonitoredTerm
Name = _CapControls.Name
Next = _CapControls.Next
OFFSetting = _CapControls.OFFSetting
ONSetting = _CapControls.ONSetting
PTRatio = _CapControls.PTRatio
UseVoltOverride = _CapControls.UseVoltOverride
Vmax = _CapControls.Vmax
Vmin = _CapControls.Vmin
Idx = _CapControls.Idx
_columns = _CapControls._columns
__all__ = [
    "Reset",
    "AllNames",
    "CTRatio",
    "Capacitor",
    "Count",
    "DeadTime",
    "Delay",
    "DelayOff",
    "First",
    "Mode",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "Next",
    "OFFSetting",
    "ONSetting",
    "PTRatio",
    "UseVoltOverride",
    "Vmax",
    "Vmin",
    "Idx",
]
