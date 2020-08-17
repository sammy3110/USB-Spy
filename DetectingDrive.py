import win32file, time
drive_list = []

class UsbDetection:
    def __init__(self):
        pass
    def locate_usb(self):
        if len(drive_list) == 1:
            drive_list.clear()
        drivebits = win32file.GetLogicalDrives()
        for d in range(1, 26):
            mask = 1 << d
            if drivebits & mask:
                # here if the drive is at least there
                drname = '%c:\\' % chr(ord('A') + d)
                t = win32file.GetDriveType(drname)
                if t == win32file.DRIVE_REMOVABLE:
                    drive_list.append(drname)
    def isUsbDetected(self):
        while True:
            self.locate_usb()
            if len(drive_list) != 0:
                return drive_list[0]
            else:
                return None