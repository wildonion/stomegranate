
# coding: utf-8
'''
	Designed By : 
 █     █░ ██▓ ██▓    ▓█████▄  ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █ 
▓█░ █ ░█░▓██▒▓██▒    ▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █ 
▒█░ █ ░█ ▒██▒▒██░    ░██   █▌▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
░█░ █ ░█ ░██░▒██░    ░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒
░░██▒██▓ ░██░░██████▒░▒████▓ ░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██
	 		>> ICFU by cL34n 3v3RytH!n9 0n 157hAu9us7 <<

'''


# TODO : defcon(ATM sniffing & payaneh hacking) and blackhat jabs using raspi along with ColdRice repo
# TODO : import all craqt cython modules here from api folder after they're built
# TODO : create all kinds of viruses using cython api to import them here 


import sys
import psutil
import ctypes
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide2.QtCore import QUrl, QTimer, QAbstractListModel
from PySide2.QtCore import QObject, Signal, Slot, Property, Qt


# shellcode = b""
# # Reserves or commits a region of pages in the virtual address space of the calling process.
# # use types windll.kernel32 for virtualalloc reserves region of pages in virtual addres sspace
# ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),
#                                           ctypes.c_int(len(shellcode)),
#                                           ctypes.c_int(0x3000),
#                                           ctypes.c_int(0x40))
# # use virtuallock to lock region for physical address space
# ctypes.windll.kernel32.VirtualLock(ctypes.c_int(ptr),
#                                    ctypes.c_int(len(shellcode)))
# # read in the buffer
# buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)
# # The RtlMoveMemory routine copies the contents of a source memory block to a destination
# # memory block, and supports overlapping source and destination memory blocks.
# # moved the memory in 4 byte blocks
# ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr),
#                                      buf,
#                                      ctypes.c_int(len(shellcode)))
# # Creates a __thread to execute within the virtual address space of the calling process
# # launch in a thread 
# ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
#                                          ctypes.c_int(0),
#                                          ctypes.c_int(ptr),
#                                          ctypes.c_int(0),
#                                          ctypes.c_int(0),
#                                          ctypes.pointer(ctypes.c_int(0)))
# # Waits until the specified object is in the signaled state or the time-out interval elapses.
# # waitfor singleobject
# ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht),ctypes.c_int(-1))


class CpuLoadModel(QAbstractListModel):
    def __init__(self):
        QAbstractListModel.__init__(self)

        self.__cpu_count = psutil.cpu_count()
        self.__cpu_load = [0] * self.__cpu_count

        self.__update_timer = QTimer(self)
        self.__update_timer.setInterval(1000)
        self.__update_timer.timeout.connect(self.__update)
        self.__update_timer.start()

        # The first call returns invalid data
        psutil.cpu_percent(percpu=True)

    def __update(self):
        self.__cpu_load = psutil.cpu_percent(percpu=True)
        self.dataChanged.emit(self.index(0,0), self.index(self.__cpu_count-1, 0))

    def rowCount(self, parent):
        return self.__cpu_count

    def data(self, index, role):
        if (role == Qt.DisplayRole and
            index.row() >= 0 and
            index.row() < len(self.__cpu_load) and
            index.column() == 0):
            return self.__cpu_load[index.row()]
        else:
            return None

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qmlRegisterType(CpuLoadModel, 'PsUtils', 1, 0, 'CpuLoadModel')
    engine.load(QUrl("app.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
