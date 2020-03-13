# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import codec, CheckForError, api_util, Base


class IProgress(Base):
    __slots__ = []
    _api_prefix = "DSSProgress"
    _columns = []

    def Close(self):
        self._lib.DSSProgress_Close()

    def Show(self):
        self._lib.DSSProgress_Show()

    def Caption(self, Value):
        """(write-only) Caption to appear on the bottom of the DSS Progress form."""
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.DSSProgress_Set_Caption(Value)
        self.CheckForError()

    def PctProgress(self, Value):
        """(write-only) Percent progress to indicate [0..100]"""
        self._lib.DSSProgress_Set_PctProgress(Value)
        self.CheckForError()


_Progress = IProgress(api_util)

# For backwards compatibility, bind to the default instance
Close = _Progress.Close
Show = _Progress.Show
Caption = _Progress.Caption
PctProgress = _Progress.PctProgress
_columns = _Progress._columns
__all__ = ["Close", "Show", "Caption", "PctProgress"]
