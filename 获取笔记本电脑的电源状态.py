# 检测笔记本电脑的供电状态、电池电量和电池寿命等。
# 来源：https://cloud.tencent.com/developer/ask/49007/answer/78869

import ctypes
from ctypes import wintypes


class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ACLineStatus', wintypes.BYTE),
        ('BatteryFlag', wintypes.BYTE),
        ('BatteryLifePercent', wintypes.BYTE),
        ('Reserved1', wintypes.BYTE),
        ('BatteryLifeTime', wintypes.DWORD),
        ('BatteryFullLifeTime', wintypes.DWORD),
    ]


SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)
GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
GetSystemPowerStatus.restype = wintypes.BOOL

status = SYSTEM_POWER_STATUS()
if not GetSystemPowerStatus(ctypes.pointer(status)):
    raise ctypes.WinError()
print('ACLineStatus', status.ACLineStatus)  # 0表示没有接通电源（不在充电） 1表示接通电源（在充电）
print('BatteryFlag', status.BatteryFlag)
print('BatteryLifePercent', status.BatteryLifePercent)
print('BatteryLifeTime', status.BatteryLifeTime)
print('BatteryFullLifeTime', status.BatteryFullLifeTime)
