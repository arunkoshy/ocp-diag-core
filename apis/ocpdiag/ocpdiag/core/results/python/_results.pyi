# Copyright 2022 Google LLC
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

from typing import Text, List, Optional

from google.protobuf import struct_pb2
from google.protobuf import message
from ocpdiag.core.results import results_pb2


def SetResultsLibFlags(
    ocpdiag_copy_results_to_stdout: bool,
    ocpdiag_results_filepath: Text,
    machine_under_test: Text,
    alsologtoocpdiagresults: bool,
    ocpdiag_strict_reporting: bool,
) -> None:
  ...


def InitTestRun(name: Text) -> TestRun:
  ...


class TestRun:

  def StartAndRegisterInfos(self,
                            dutinfos: List[DutInfo],
                            params: Optional[message.Message] = ...) -> None:
    ...

  def End(self) -> results_pb2.TestResult:
    ...

  def Skip(self) -> results_pb2.TestResult:
    ...

  def AddError(self, symptom: Text, message: Text) -> None:
    ...

  def AddTag(self, tag: Text) -> None:
    ...

  def Status(self) -> results_pb2.TestStatus:
    ...

  def Result(self) -> results_pb2.TestStatus:
    ...

  def Started(self) -> bool:
    ...

  def Ended(self) -> bool:
    ...

  def LogDebug(self, msg: Text) -> None:
    ...

  def LogInfo(self, msg: Text) -> None:
    ...

  def LogWarn(self, msg: Text) -> None:
    ...

  def LogError(self, msg: Text) -> None:
    ...

  def LogFatal(self, msg: Text) -> None:
    ...


def BeginTestStep(parent: TestRun, name: Text) -> TestStep:
  ...


class TestStep:

  def AddDiagnosis(self,
                   type: results_pb2.Diagnosis.Type,
                   symptom: Text,
                   message: Text,
                   records: List[HwRecord] = ...) -> None:
    ...

  def AddError(self,
               symptom: Text,
               message: Text,
               records: List[SwRecord] = ...) -> None:
    ...

  def AddMeasurement(self,
                     info: results_pb2.MeasurementInfo,
                     elem: results_pb2.MeasurementElement,
                     hwrec: Optional[HwRecord] = ...) -> None:
    ...

  def AddFile(self, file: results_pb2.File) -> None:
    ...

  def AddArtifactExtension(self, name: Text,
                           extension: message.Message) -> None:
    ...

  def LogDebug(self, msg: Text) -> None:
    ...

  def LogInfo(self, msg: Text) -> None:
    ...

  def LogWarn(self, msg: Text) -> None:
    ...

  def LogError(self, msg: Text) -> None:
    ...

  def LogFatal(self, msg: Text) -> None:
    ...

  def End(self) -> None:
    ...

  def Skip(self) -> None:
    ...

  def Ended(self) -> bool:
    ...

  def Status(self) -> int:
    ...

  def Id(self) -> Text:
    ...


class DutInfo:

  def __init__(self, name: Text):
    ...

  def AddHardware(self, info: results_pb2.HardwareInfo) -> HwRecord:
    ...

  def AddSoftware(self, info: results_pb2.SoftwareInfo) -> SwRecord:
    ...

  def AddPlatformInfo(self, info: Text) -> None:
    ...

  def Registered(self) -> bool:
    ...

  def ToProto(self) -> results_pb2.DutInfo:
    ...


class HwRecord:

  def Data() -> results_pb2.HardwareInfo:
    ...


class SwRecord:

  def Data() -> results_pb2.SoftwareInfo:
    ...


def BeginMeasurementSeries(
    parent: TestStep, hw: HwRecord,
    info: results_pb2.MeasurementInfo) -> MeasurementSeries:
  ...


class MeasurementSeries:

  def AddElement(self, value: struct_pb2.Value) -> None:
    ...

  def AddElementWithRange(self, val: struct_pb2.Value,
                          range: results_pb2.MeasurementElement.Range) -> None:
    ...

  def AddElementWithValues(self, val: struct_pb2.Value,
                           valid_values: List[struct_pb2.Value]) -> None:
    ...

  def Id(self) -> Text:
    ...

  def Ended(self) -> bool:
    ...

  def End(self) -> None:
    ...
