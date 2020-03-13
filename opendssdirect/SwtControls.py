# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ._utils import codec, CheckForError, api_util, Iterable


class ISwtControls(Iterable):
    __slots__ = []
    _api_prefix = "SwtControls"
    _columns = [
        "Name",
        "Idx",
        "Action",
        "Delay",
        "IsLocked",
        "NormalState",
        "State",
        "SwitchedObj",
        "SwitchedTerm",
    ]

    def Reset(self):
        self._lib.SwtControls_Reset()

    def Action(self, *args):
        """Open or Close the switch. No effect if switch is locked.  However, Reset removes any lock and then closes the switch (shelf state)."""
        # Getter
        if len(args) == 0:
            return self._lib.SwtControls_Get_Action()

        # Setter
        Value, = args
        self._lib.SwtControls_Set_Action(Value)
        self.CheckForError()

    def Delay(self, *args):
        """Time delay [s] betwen arming and opening or closing the switch.  Control may reset before actually operating the switch."""
        # Getter
        if len(args) == 0:
            return self._lib.SwtControls_Get_Delay()

        # Setter
        Value, = args
        self._lib.SwtControls_Set_Delay(Value)
        self.CheckForError()

    def IsLocked(self, *args):
        """The lock prevents both manual and automatic switch operation."""
        # Getter
        if len(args) == 0:
            return self._lib.SwtControls_Get_IsLocked() != 0

        # Setter
        Value, = args
        self._lib.SwtControls_Set_IsLocked(Value)
        self.CheckForError()

    def NormalState(self, *args):
        """
    Get/set Normal state of switch (see actioncodes) dssActionOpen or dssActionClose
    """
        # Getter
        if len(args) == 0:
            return self._lib.SwtControls_Get_NormalState()

        # Setter
        Value, = args
        self._lib.SwtControls_Set_NormalState(Value)
        self.CheckForError()

    def State(self, *args):
        """Set it to force the switch to a specified state, otherwise read its present state."""
        # Getter
        if len(args) == 0:
            return self._lib.SwtControls_Get_State()

        # Setter
        Value, = args
        self._lib.SwtControls_Set_State(Value)
        self.CheckForError()

    def SwitchedObj(self, *args):
        """Full name of the switched element."""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.SwtControls_Get_SwitchedObj())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.SwtControls_Set_SwitchedObj(Value)
        self.CheckForError()

    def SwitchedTerm(self, *args):
        """Terminal number where the switch is located on the SwitchedObj"""
        # Getter
        if len(args) == 0:
            return self._lib.SwtControls_Get_SwitchedTerm()

        # Setter
        Value, = args
        self._lib.SwtControls_Set_SwitchedTerm(Value)
        self.CheckForError()


_SwtControls = ISwtControls(api_util)

# For backwards compatibility, bind to the default instance
Reset = _SwtControls.Reset
Action = _SwtControls.Action
AllNames = _SwtControls.AllNames
Count = _SwtControls.Count
Delay = _SwtControls.Delay
First = _SwtControls.First
IsLocked = _SwtControls.IsLocked
Name = _SwtControls.Name
Next = _SwtControls.Next
NormalState = _SwtControls.NormalState
State = _SwtControls.State
SwitchedObj = _SwtControls.SwitchedObj
SwitchedTerm = _SwtControls.SwitchedTerm
Idx = _SwtControls.Idx
_columns = _SwtControls._columns
__all__ = [
    "Reset",
    "Action",
    "AllNames",
    "Count",
    "Delay",
    "First",
    "IsLocked",
    "Name",
    "Next",
    "NormalState",
    "State",
    "SwitchedObj",
    "SwitchedTerm",
    "Idx",
]
