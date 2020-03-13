# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ._utils import codec, CheckForError, api_util, Iterable


class IRelays(Iterable):
    __slots__ = []
    _api_prefix = "Relays"
    _columns = [
        "Name",
        "Idx",
        "MonitoredObj",
        "MonitoredTerm",
        "SwitchedObj",
        "SwitchedTerm",
    ]

    def MonitoredObj(self, *args):
        """Full name of object this Relay is monitoring."""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.Relays_Get_MonitoredObj())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.Relays_Set_MonitoredObj(Value)
        self.CheckForError()

    def MonitoredTerm(self, *args):
        """Number of terminal of monitored element that this Relay is monitoring."""
        # Getter
        if len(args) == 0:
            return self._lib.Relays_Get_MonitoredTerm()

        # Setter
        Value, = args
        self._lib.Relays_Set_MonitoredTerm(Value)
        self.CheckForError()

    def SwitchedObj(self, *args):
        """Full name of element that will be switched when relay trips."""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.Relays_Get_SwitchedObj())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.Relays_Set_SwitchedObj(Value)
        self.CheckForError()

    def SwitchedTerm(self, *args):
        """Terminal number of the switched object that will be opened when the relay trips."""
        # Getter
        if len(args) == 0:
            return self._lib.Relays_Get_SwitchedTerm()

        # Setter
        Value, = args
        self._lib.Relays_Set_SwitchedTerm(Value)
        self.CheckForError()


_Relays = IRelays(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _Relays.AllNames
Count = _Relays.Count
First = _Relays.First
MonitoredObj = _Relays.MonitoredObj
MonitoredTerm = _Relays.MonitoredTerm
Name = _Relays.Name
Next = _Relays.Next
SwitchedObj = _Relays.SwitchedObj
SwitchedTerm = _Relays.SwitchedTerm
Idx = _Relays.Idx
_columns = _Relays._columns
__all__ = [
    "AllNames",
    "Count",
    "First",
    "MonitoredObj",
    "MonitoredTerm",
    "Name",
    "Next",
    "SwitchedObj",
    "SwitchedTerm",
    "Idx",
]
