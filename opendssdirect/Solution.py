# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import codec, CheckForError, api_util, Base


class ISolution(Base):
    __slots__ = []
    _api_prefix = "Solution"
    _columns = [
        "MinIterations",
        "MaxIterations",
        "MaxControlIterations",
        "TotalIterations",
        "ControlIterations",
        "MostIterationsDone",
        "Number",
        "ProcessTime",
        "AddType",
        "GenkW",
        "DblHour",
        "Capkvar",
        "Seconds",
        "GenMult",
        "DefaultYearly",
        "IntervalHrs",
        "Converged",
        "ModeID",
        "TimeTimeStep",
        "TotalTime",
        "LoadModel",
        "EventLog",
        "Iterations",
        "GenPF",
        "Frequency",
        "LoadMult",
        "Random",
        "PctGrowth",
        "Year",
        "Algorithm",
        "Hour",
        "Convergence",
        "ControlMode",
        "LDCurve",
        "StepSize",
        "DefaultDaily",
        "ControlActionsDone",
        "Mode",
        "SystemYChanged",
    ]

    def BuildYMatrix(self, BuildOption, AllocateVI):
        self._lib.Solution_BuildYMatrix(BuildOption, AllocateVI)
        self.CheckForError()

    def CheckControls(self):
        self._lib.Solution_CheckControls()
        self.CheckForError()

    def CheckFaultStatus(self):
        self._lib.Solution_CheckFaultStatus()
        self.CheckForError()

    def Cleanup(self):
        self._lib.Solution_Cleanup()
        self.CheckForError()

    def DoControlActions(self):
        self._lib.Solution_DoControlActions()
        self.CheckForError()

    def FinishTimeStep(self):
        self._lib.Solution_FinishTimeStep()
        self.CheckForError()

    def InitSnap(self):
        self._lib.Solution_InitSnap()
        self.CheckForError()

    def SampleControlDevices(self):
        self._lib.Solution_SampleControlDevices()
        self.CheckForError()

    def SampleDoControlActions(self):
        self._lib.Solution_Sample_DoControlActions()
        self.CheckForError()

    def Solve(self):
        self._lib.Solution_Solve()
        self.CheckForError()

    def SolveDirect(self):
        self._lib.Solution_SolveDirect()
        self.CheckForError()

    def SolveNoControl(self):
        self._lib.Solution_SolveNoControl()
        self.CheckForError()

    def SolvePFlow(self):
        self._lib.Solution_SolvePflow()
        self.CheckForError()

    def SolvePlusControl(self):
        self._lib.Solution_SolvePlusControl()
        self.CheckForError()

    def SolveSnap(self):
        self._lib.Solution_SolveSnap()
        self.CheckForError()

    def AddType(self, *args):
        """Type of device to add in AutoAdd Mode: {dssGen (Default) | dssCap}"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_AddType()

        # Setter
        Value, = args
        self._lib.Solution_Set_AddType(Value)
        self.CheckForError()

    def Algorithm(self, *args):
        """Base Solution algorithm: {dssNormalSolve | dssNewtonSolve}"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_Algorithm()

        # Setter
        Value, = args
        self._lib.Solution_Set_Algorithm(Value)
        self.CheckForError()

    def Capkvar(self, *args):
        """Capacitor kvar for adding capacitors in AutoAdd mode"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_Capkvar()

        # Setter
        Value, = args
        self._lib.Solution_Set_Capkvar(Value)
        self.CheckForError()

    def ControlActionsDone(self, *args):
        """Flag indicating the control actions are done."""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_ControlActionsDone() != 0

        # Setter
        Value, = args
        self._lib.Solution_Set_ControlActionsDone(Value)
        self.CheckForError()

    def ControlIterations(self, *args):
        """Value of the control iteration counter"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_ControlIterations()

        # Setter
        Value, = args
        self._lib.Solution_Set_ControlIterations(Value)
        self.CheckForError()

    def ControlMode(self, *args):
        """{dssStatic* | dssEvent | dssTime}  Modes for control devices"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_ControlMode()

        # Setter
        Value, = args
        self._lib.Solution_Set_ControlMode(Value)
        self.CheckForError()

    def Converged(self, *args):
        """Flag to indicate whether the circuit solution converged"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_Converged() != 0

        # Setter
        Value, = args
        self._lib.Solution_Set_Converged(Value)
        self.CheckForError()

    def DefaultDaily(self, *args):
        """Default daily load shape (defaults to "Default")"""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.Solution_Get_DefaultDaily())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.Solution_Set_DefaultDaily(Value)
        self.CheckForError()

    def DefaultYearly(self, *args):
        """Default Yearly load shape (defaults to "Default")"""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.Solution_Get_DefaultYearly())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.Solution_Set_DefaultYearly(Value)
        self.CheckForError()

    def EventLog(self):
        """(read-only) Array of strings containing the Event Log"""
        return self._get_string_array(self._lib.Solution_Get_EventLog)

    def Frequency(self, *args):
        """Set the Frequency for next solution"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_Frequency()

        # Setter
        Value, = args
        self._lib.Solution_Set_Frequency(Value)
        self.CheckForError()

    def GenMult(self, *args):
        """Default Multiplier applied to generators (like LoadMult)"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_GenMult()

        # Setter
        Value, = args
        self._lib.Solution_Set_GenMult(Value)
        self.CheckForError()

    def GenPF(self, *args):
        """PF for generators in AutoAdd mode"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_GenPF()

        # Setter
        Value, = args
        self._lib.Solution_Set_GenPF(Value)
        self.CheckForError()

    def GenkW(self, *args):
        """Generator kW for AutoAdd mode"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_GenkW()

        # Setter
        Value, = args
        self._lib.Solution_Set_GenkW(Value)
        self.CheckForError()

    def Hour(self, *args):
        """Set Hour for time series solutions."""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_Hour()

        # Setter
        Value, = args
        self._lib.Solution_Set_Hour(Value)
        self.CheckForError()

    def IntervalHrs(self, *args):
        """
    (read) Get/Set the Solution.IntervalHrs variable used for devices that integrate
    (write) Get/Set the Solution.IntervalHrs variable for custom solution algorithms
    """
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_IntervalHrs()

        # Setter
        Value, = args
        self._lib.Solution_Set_IntervalHrs(Value)
        self.CheckForError()

    def Iterations(self):
        """(read-only) Number of iterations taken for last solution. (Same as TotalIterations)"""
        return self._lib.Solution_Get_Iterations()

    def LDCurve(self, *args):
        """Load-Duration Curve name for LD modes"""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.Solution_Get_LDCurve())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.Solution_Set_LDCurve(Value)
        self.CheckForError()

    def LoadModel(self, *args):
        """Load Model: {dssPowerFlow (default) | dssAdmittance}"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_LoadModel()

        # Setter
        Value, = args
        self._lib.Solution_Set_LoadModel(Value)
        self.CheckForError()

    def LoadMult(self, *args):
        """Default load multiplier applied to all non-fixed loads"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_LoadMult()

        # Setter
        Value, = args
        self._lib.Solution_Set_LoadMult(Value)
        self.CheckForError()

    def MaxControlIterations(self, *args):
        """Maximum allowable control iterations"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_MaxControlIterations()

        # Setter
        Value, = args
        self._lib.Solution_Set_MaxControlIterations(Value)
        self.CheckForError()

    def MaxIterations(self, *args):
        """Max allowable iterations."""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_MaxIterations()

        # Setter
        Value, = args
        self._lib.Solution_Set_MaxIterations(Value)
        self.CheckForError()

    def MinIterations(self, *args):
        """Minimum number of iterations required for a power flow solution."""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_MinIterations()

        # Setter
        Value, = args
        self._lib.Solution_Set_MinIterations(Value)
        self.CheckForError()

    def Mode(self, *args):
        """Set present solution mode (by a text code - see DSS Help)"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_Mode()

        # Setter
        Mode, = args
        self._lib.Solution_Set_Mode(Mode)
        self.CheckForError()

    def ModeID(self):
        """(read-only) ID (text) of the present solution mode"""
        return self._get_string(self._lib.Solution_Get_ModeID())

    def MostIterationsDone(self):
        """(read-only) Max number of iterations required to converge at any control iteration of the most recent solution."""
        return self._lib.Solution_Get_MostIterationsDone()

    def Number(self, *args):
        """Number of solutions to perform for Monte Carlo and time series simulations"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_Number()

        # Setter
        Value, = args
        self._lib.Solution_Set_Number(Value)
        self.CheckForError()

    def ProcessTime(self):
        """(read-only) Gets the time required to perform the latest solution (Read only)"""
        return self._lib.Solution_Get_Process_Time()

    def Random(self, *args):
        """Randomization mode for random variables "Gaussian" or "Uniform\""""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_Random()

        # Setter
        Random, = args
        self._lib.Solution_Set_Random(Random)
        self.CheckForError()

    def Seconds(self, *args):
        """Seconds from top of the hour."""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_Seconds()

        # Setter
        Value, = args
        self._lib.Solution_Set_Seconds(Value)
        self.CheckForError()

    def StepSize(self, *args):
        """Time step size in sec"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_StepSize()

        # Setter
        Value, = args
        self._lib.Solution_Set_StepSize(Value)
        self.CheckForError()

    def SystemYChanged(self):
        """(read-only) Flag that indicates if elements of the System Y have been changed by recent activity."""
        return self._lib.Solution_Get_SystemYChanged() != 0

    def TimeTimeStep(self):
        """(read-only) Get the solution process time + sample time for time step"""
        return self._lib.Solution_Get_Time_of_Step()

    def Convergence(self, *args):
        """Solution convergence tolerance."""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_Tolerance()

        # Setter
        Value, = args
        self._lib.Solution_Set_Tolerance(Value)
        self.CheckForError()

    def TotalTime(self, *args):
        """
    (read) Gets the accumulated time of the simulation
    (write) Sets the Accumulated time of the simulation
    """
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_Total_Time()

        # Setter
        Value, = args
        self._lib.Solution_Set_Total_Time(Value)
        self.CheckForError()

    def TotalIterations(self):
        """(read-only) Total iterations including control iterations for most recent solution."""
        return self._lib.Solution_Get_Totaliterations()

    def Year(self, *args):
        """Set year for planning studies"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_Year()

        # Setter
        Value, = args
        self._lib.Solution_Set_Year(Value)
        self.CheckForError()

    def DblHour(self, *args):
        """Hour as a double, including fractional part"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_dblHour()

        # Setter
        Value, = args
        self._lib.Solution_Set_dblHour(Value)
        self.CheckForError()

    def PctGrowth(self, *args):
        """Percent default  annual load growth rate"""
        # Getter
        if len(args) == 0:
            return self._lib.Solution_Get_pctGrowth()

        # Setter
        Value, = args
        self._lib.Solution_Set_pctGrowth(Value)
        self.CheckForError()

    def StepSizeHr(self, Value):
        """(write-only) Set Stepsize in Hr"""
        self._lib.Solution_Set_StepsizeHr(Value)
        self.CheckForError()

    def StepSizeMin(self, Value):
        """(write-only) Set Stepsize in minutes"""
        self._lib.Solution_Set_StepsizeMin(Value)
        self.CheckForError()

    def BusLevels(self):
        return self._get_int32_array(self._lib.Solution_Get_BusLevels)

    def IncMatrix(self):
        return self._get_int32_array(self._lib.Solution_Get_IncMatrix)

    def IncMatrixCols(self):
        return self._get_string_array(self._lib.Solution_Get_IncMatrixCols)

    def IncMatrixRows(self):
        return self._get_string_array(self._lib.Solution_Get_IncMatrixRows)

    def Laplacian(self):
        return self._get_int32_array(self._lib.Solution_Get_Laplacian)


_Solution = ISolution(api_util)

# For backwards compatibility, bind to the default instance
BuildYMatrix = _Solution.BuildYMatrix
CheckControls = _Solution.CheckControls
CheckFaultStatus = _Solution.CheckFaultStatus
Cleanup = _Solution.Cleanup
DoControlActions = _Solution.DoControlActions
FinishTimeStep = _Solution.FinishTimeStep
InitSnap = _Solution.InitSnap
SampleControlDevices = _Solution.SampleControlDevices
SampleDoControlActions = _Solution.SampleDoControlActions
Solve = _Solution.Solve
SolveDirect = _Solution.SolveDirect
SolveNoControl = _Solution.SolveNoControl
SolvePFlow = _Solution.SolvePFlow
SolvePlusControl = _Solution.SolvePlusControl
SolveSnap = _Solution.SolveSnap
AddType = _Solution.AddType
Algorithm = _Solution.Algorithm
Capkvar = _Solution.Capkvar
ControlActionsDone = _Solution.ControlActionsDone
ControlIterations = _Solution.ControlIterations
ControlMode = _Solution.ControlMode
Converged = _Solution.Converged
DefaultDaily = _Solution.DefaultDaily
DefaultYearly = _Solution.DefaultYearly
EventLog = _Solution.EventLog
Frequency = _Solution.Frequency
GenMult = _Solution.GenMult
GenPF = _Solution.GenPF
GenkW = _Solution.GenkW
Hour = _Solution.Hour
IntervalHrs = _Solution.IntervalHrs
Iterations = _Solution.Iterations
LDCurve = _Solution.LDCurve
LoadModel = _Solution.LoadModel
LoadMult = _Solution.LoadMult
MaxControlIterations = _Solution.MaxControlIterations
MaxIterations = _Solution.MaxIterations
MinIterations = _Solution.MinIterations
Mode = _Solution.Mode
ModeID = _Solution.ModeID
MostIterationsDone = _Solution.MostIterationsDone
Number = _Solution.Number
ProcessTime = _Solution.ProcessTime
Random = _Solution.Random
Seconds = _Solution.Seconds
StepSize = _Solution.StepSize
SystemYChanged = _Solution.SystemYChanged
TimeTimeStep = _Solution.TimeTimeStep
Convergence = _Solution.Convergence
TotalTime = _Solution.TotalTime
TotalIterations = _Solution.TotalIterations
Year = _Solution.Year
DblHour = _Solution.DblHour
PctGrowth = _Solution.PctGrowth
StepSizeHr = _Solution.StepSizeHr
StepSizeMin = _Solution.StepSizeMin
BusLevels = _Solution.BusLevels
IncMatrix = _Solution.IncMatrix
IncMatrixCols = _Solution.IncMatrixCols
IncMatrixRows = _Solution.IncMatrixRows
Laplacian = _Solution.Laplacian
_columns = _Solution._columns
__all__ = [
    "BuildYMatrix",
    "CheckControls",
    "CheckFaultStatus",
    "Cleanup",
    "DoControlActions",
    "FinishTimeStep",
    "InitSnap",
    "SampleControlDevices",
    "SampleDoControlActions",
    "Solve",
    "SolveDirect",
    "SolveNoControl",
    "SolvePFlow",
    "SolvePlusControl",
    "SolveSnap",
    "AddType",
    "Algorithm",
    "Capkvar",
    "ControlActionsDone",
    "ControlIterations",
    "ControlMode",
    "Converged",
    "DefaultDaily",
    "DefaultYearly",
    "EventLog",
    "Frequency",
    "GenMult",
    "GenPF",
    "GenkW",
    "Hour",
    "IntervalHrs",
    "Iterations",
    "LDCurve",
    "LoadModel",
    "LoadMult",
    "MaxControlIterations",
    "MaxIterations",
    "MinIterations",
    "Mode",
    "ModeID",
    "MostIterationsDone",
    "Number",
    "ProcessTime",
    "Random",
    "Seconds",
    "StepSize",
    "SystemYChanged",
    "TimeTimeStep",
    "Convergence",
    "TotalTime",
    "TotalIterations",
    "Year",
    "DblHour",
    "PctGrowth",
    "StepSizeHr",
    "StepSizeMin",
    "BusLevels",
    "IncMatrix",
    "IncMatrixCols",
    "IncMatrixRows",
    "Laplacian",
]
