### stomegranate openlab in Qt for crangel cloud server

##### op0
---
_stomegranate craqt client app (python:socket) <----Stomegranate SecureSocketServer Cli----> stomegranate crangel cloud server (dart:io) ; the integration or sending requests in TearMode(WO DIMENSION) with crangel server from craqt client app is done by a cli inside the craqt client app which has its own command line language called crangel and the process of parsing to run the command is done on the crangel server; the login process for TearMode(WO DIMENSION) is done by answering some random questions each time you want to enter to this mode_

##### op1
---
_the auth process inside craqt client app is done by mailing the password every ```hardcodedInServer``` seconds from the server to the ```hardcodedInServer``` email and you can switch between password generation algos or change the email and password generation time only in TearMode(WO DIMENSION) by running their related commands after a successful login_

##### op2
---
_this app takes the asm(fasm/nasm/cython/c++) code and extract its shellcode then generate a packed PE by upx and nuitka or pyinstaller in which it uses ctypes to inject the sehllcode into another process in the memory_

##### op3
---
_this app will download the Orcus backdoor from stomegranate crangel cloud server and bypass it using atombombing, buffer(heap)overflow, earlyBird, doubleagent or other code injection techniques , you can also generate your backdoor here and control victims in stomegranate crangel cloud server_

##### op4
---
_you can write linux kernel module using the kplugs in kernel scripting editor inside the app and execute them directly from user space_

##### op5
---
_you can write and run bash script in bash scripting editor inside the app to eat hardware stuff better using manjaro!_

##### op6
---
_this app has llvm integration section to play with llvm tools_

##### op7
---
_this app has vhdl integration section using the myHDL in HDL scripting editor for coding and handling iot and hardware programming projects_

##### op8
---
_this app has a trained (on colab , raspi or neural stick 2 intel using tf.keras) toolkits list of all your AI and ML ideas and kaggle challenges in which you can solve your problems like ```op12``` issue with its related kit and also you can manage your toolkits only on TearMode(WO DIMENSION)_

##### op9
---
_this app has AIF (Application Integration Framework) section for cruaduct server only on TearMode(WO DIMENSION), wodrone and whole iot stuff, your new code injection technique using ghidra or IDA pro(PE structure), hhwo DIY like defcon, stackVM , OS, forked & ColdRice repos and wompiler (template engine) that you want to build on top of another only on TearMode(WO DIMENSION)_

##### op10
---
_you can upload/download all of your algorithms on/from stomegranate crangel cloud server based on your protocol and only on TearMode(WO DIMENSION)_

##### op11
---
_you can activate the novacrash virus only on TearMode(WO DIMENSION) of the craqt client app_

##### op12
---
_platform malware detection and encryption system based on AI in craqt client app using tf.keras and neural stick 2 intel on TearMode(WO DIMENSION)_


__get asm code using g++ from main.cpp file__

```g++ -S main.cpp```

__get shellcode from main.out using objdump__

```objdump -d ./main | grep -Po '\s\K[a-f0-9]{2}(?=\s)' | sed 's/^/\\x/g' | perl -pe 's/\r?\n//' | sed 's/$/\n/' > shellcode.txt```

__get asm cod from binary files using objdump__

```objdump -S -M intel -D main.exe > main.s```

__get opcode/hexcode from binary file using hexdump__

```hexdump [options] <file>```

__get shellcode from binary__

```objdump -d ./PROGRAM|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g > shellcode'```
