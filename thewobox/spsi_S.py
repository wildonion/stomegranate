

#***************************************************************************************************************************************************************************************************************************************************************************************************************************************************
# WARNING: use fodhelper.exe bug(KrY.py) to bypass UAC and for bypassing AVs just create ur virus(like download and execute shellcode or any shellcode from a dirty jab with memory ) in assembly then make shellcode from ur assembly code finally inject it using python ctypes lib through a complicated way like Multi Threading into MAN memory  
# WARNING: IN THIS PROJECT YOU HAVE TO BUILD YOUR EXPLOIT WITH ITS SHELLCODE TO FUCK THE TARGET AND BYPASS ANTI-VIRUSES
# WARNING: use Violent Python - A Cookbook for Hackers, Forensic Analysts, Penetration Testers and Security Engineers.pdf book page 75 to see how to send the shellcode through socket(a buffer overflow attack)
# WARNING: this code contains all infos about hacking website; also do some session hijacking and session decryption
# WARNING: with this file we can check the injection of our shellcode in target memeroy using socket => see the WARNING and spsi_C.py file for injecting shellcode : give the spsi_C.py file to ur vic then send ur shellcode and control the injection using this file
# WARNING: see README.txt in this directory to complete this project for binary exploit concepts and its algorithms
# WARNING: finish this projet to inject shellcode of the reverse shell or bind shell virus or other shellcodes 
#***************************************************************************************************************************************************************************************************************************************************************************************************************************************************


# SOURCES:
# Your Exploit is Mine_Automatic Shellcode pdf book
# pentest.blog/art-of-anti-detection-1-introduction-to-av-detection-techniques/
# https://thehackernews.com/2019/01/linux-apt-http-hacking.html
# https://thehackernews.com/2018/11/facebook-vulnerability-hack.html
# https://thehackernews.com/2018/09/browser-address-spoofing-vulnerability.html
# https://thehackernews.com/2018/09/facebook-account-hack.html
# https://thehackernews.com/2018/09/facebook-account-hacked.html
# https://www.youtube.com/watch?v=feK4H_khS3I
# https://thehackernews.com/2018/09/wd-my-cloud-nas-hacking.html
# https://stackoverflow.com/questions/37582444/jwt-vs-cookies-for-token-based-authentication
# https://www.securityweek.com/remotely-exploitable-vulnerability-discovered-mikrotiks-routeros
# https://adsecurity.org/?p=3592
# https://www.computerworld.com/article/2960738/cybercrime-hacking/researchers-show-how-to-steal-windows-active-directory-credentials-from-the-internet.html
# https://mashable.com/2018/08/13/instagram-hack-locked-out-of-account/
# https://thehackernews.com/2018/08/hack-instagram-accounts.html
# https://thehackernews.com/2018/08/microsoft-office365-phishing.html
# https://thehackernews.com/2018/08/mikrotik-router-hacking.html
# https://thehackernews.com/2018/03/slingshot-router-hacking.html
# https://github.com/BasuCert/WinboxPoC
# https://github.com/0ki/mikrotik-tools
# https://null-byte.wonderhowto.com/how-to/hack-like-pro-spoof-dns-lan-redirect-traffic-your-fake-website-0151620/
# https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/
# https://thehackernews.com/2018/08/hack-reddit-account.html
# https://thehackernews.com/2018/05/linux-dhcp-hacking.html
# https://thehackernews.com/2018/05/electron-node-integration.html
# https://thehackernews.com/2018/05/signal-desktop-hacking.html
# https://thehackernews.com/2018/05/signal-messenger-code-injection.html
# https://thehackernews.com/2018/09/mega-file-upload-chrome-extension.html
# https://thehackernews.com/2018/05/facebook-cryptocurrency-hacking.html => build a malicious Chrome extension to inject some js script into vic sites for stealing cryptocurrency and bank account credentials and injecting miners on the web page for mining cryptocurrency using a C&C server 
# https://thehackernews.com/2018/06/vpnfilter-router-malware.html
# https://thehackernews.com/2018/05/vpnfilter-router-hacking.html
# https://thehackernews.com/2018/06/redis-server-hacking.html
# https://thehackernews.com/2018/05/vpnfilter-botnet-malware.html
# https://en.wikipedia.org/wiki/Code_injection
# https://thehackernews.com/2018/07/russia-election-hacking.html => phishing technique
# https://github.com/eastee/rebreakcaptcha
# https://www.youtube.com/watch?v=jmgsgjPn1vs&list=PLhixgUqwRTjx2BmNF5-GddyqZcizwLLGP
# https://www.youtube.com/watch?v=memPcI94YGA
# https://www.youtube.com/watch?v=PGVNja2MNws
# https://thehackernews.com/2018/07/timehop-data-breach.html
# https://secapps.com/tutorials/html-injection
# https://routersecurity.org/bugs.php
# https://thehackernews.com/2018/07/windows-adobe-zero-exploit.html
# https://www.reuters.com/article/us-usa-cyber-routers/fbi-warns-russians-hacked-hundreds-of-thousands-of-routers-idUSKCN1IQ2DY
# https://medium.com/@shadowbrokerss/dont-forget-your-base-867d304a94b1
# https://blogs.microsoft.com/on-the-issues/2017/05/14/need-urgent-collective-action-keep-people-safe-online-lessons-last-weeks-cyberattack/#sm.0000mpb068eggcqczh61fx32wtiui
# https://www.thewindowsclub.com/smb-port-what-is-port-445-port-139-used-for
# https://en.wikipedia.org/wiki/Asynchronous_procedure_call
# https://www.csoonline.com/article/3227906/ransomware/what-is-wannacry-ransomware-how-does-it-infect-and-who-was-responsible.html
# https://glammingspace.blogspot.com/2017/09/creating-linux-backdoor-using-python.html
# https://thehackernews.com/2018/07/coinhive-shortlink-crypto-mining.html
# https://blog.rapid7.com/2017/04/18/the-shadow-brokers-leaked-exploits-faq/
# https://github.com/DonnchaC/shadowbrokers-exploits
# https://www.guru99.com/how-to-hack-web-server.html
# https://thehackernews.com/2018/06/magento-security-hacking.html
# https://www.offensive-security.com/metasploit-unleashed/msfencode/
# https://advisories.dxw.com/advisories/stored-xss-wp-ulike/
# https://github.com/r00t-3xp10it/venom
# http://www.securitytube-training.com/online-courses/index.html
# https://n0where.net/post-exploitation-toolkit-p0wnedshell
# https://en.wikipedia.org/wiki/Shellcode
# https://stackoverflow.com/questions/6287918/how-to-decompile-an-exe-file-compiled-by-py2exe
# https://docs.python.org/3/library/ssl.html#module-ssl
# https://docs.python.org/3/library/socketserver.html#module-socketserver
# https://nmap.org/book/nse-usage.html
# https://docs.python.org/3/library/socket.html
# https://www.offensive-security.com/metasploit-unleashed/generating-payloads/
# https://medium.com/@AntiSec_Inc/combining-the-power-of-python-and-assembly-a4cf424be01d
# https://www.youtube.com/results?search_query=networking+exploiting
# https://www.youtube.com/results?search_query=hack+mikrotik+kali+linux
# https://www.youtube.com/watch?v=RlMyRa0d2uw
# https://www.youtube.com/watch?v=YCCrVtvAu2I
# https://www.youtube.com/watch?v=AbVbqF-UmHc
# https://www.youtube.com/watch?v=4DC3BgB1vNc
# https://www.youtube.com/watch?v=viPOmfGLzFU&list=PLu4qKK3kHtHmtK54CGbFWZkLSkRgbLchI
# https://www.youtube.com/watch?v=iVLeYsgdBNw&list=PLp4w7b_XLssSa0I4z6-pz_z48e9am14fg
# https://www.youtube.com/watch?v=GX1go9PDnWY
# https://www.youtube.com/watch?v=bRn6ViFAomY
# https://www.youtube.com/watch?v=td-2rN4PgRw
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
# http://liveoverflow.com/binary_hacking/
# https://trailofbits.github.io/ctf/web/exploits.html
# https://security.stackexchange.com/questions/94356/can-malicious-code-trigger-without-the-user-executing-or-opening-the-file
# https://newtecservices.com/malware-exploit-attacks-explained/
# https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/
# https://www.youtube.com/watch?v=akCce7vSSfw
# https://null-byte.wonderhowto.com/how-to/exploit-development-learn-binary-exploitation-with-protostar-0181154/
# https://hackernoon.com/binary-exploitation-eli5-part-1-9bc23855a3d8
# https://opensourceforu.com/2015/12/the-basics-of-binary-exploitation/
# https://security.stackexchange.com/questions/49320/difference-between-binary-exploitation-and-reverse-engineering
# https://github.com/RPISEC/MBE
# https://www.esentire.com/blog/cyber-threats-101-how-to-prevent-file-based-malware-and-botnets/
# https://www.wired.com/2015/04/hacker-lexicon-spear-phishing/
# https://thehackernews.com/2018/06/browser-cross-origin-vulnerability.html


# NOTE: u can send your shellcode with your server socket only: give the spsi_C.py to the victim to recv the payload with s.recv() in client file then inject it into memory means we don't need third file virus.exe or virus.py; only two files!
# NOTE: find an open port in your target machine using nmap or ur pscanner script then use that port to send your shellcode for your target cause the port is open & is listening for incomming 
# NOTE: the trutle folder and its files is kind of a botnet
# NOTE: shellcodes are commonly used to download malware (e.g., a remote administration tool and a Trojan horse) from the Internet and to infect the target computer with the malware
# NOTE: Then an Exploit is how, or the entry way for, the Malware to enter your computer
# NOTE: use binary exploits shellcodes to inject malware into memory | Common Binary Executables: exe , dll , msi => PE files
# NOTE: cause the time of the server is very important rule for os(planing an attack according to the time of the os)
# NOTE: More secure socket connection using SSL
# NOTE: scan open ports and send or spread itself(shellcode) using ssl socket through that port with s.send() method

# TODOS: 
# work with js to create malicious Chrome extension for stealing user's browser data like bank account in site hacking section
# find a bug in vps to write exploit for it to get into the real server; also crack the ssh/ftp password of linux vps with my python script or sentry MBA; how to get into the real server from a vps => access A(main) from B(vps)
# nuttering on burpsuite to use its payload feature and https://github.com/romanzaikin/BurpExtension-WhatsApp-Decryption-CheckPoint
# hack using google dork(spotify app in windows) => kali (exploit-db.com/google-hacking-database/)
# read all codes in python-for-hackers(github) folder and Python_Reverse_TCP folder
# build smt like stuxnet for PLCes even worst than stuxnet => assembly + C + shellcoding
# mikrotik router exploit(rop concept & chimay red exploit[https://github.com/BigNerd95/Chimay-Red]) => binary exploits, work with stack registers and opcode in python(look evalmath file)
# know all about routers and how they really work(send raw shellcode/payload using python socket programming or requests module) => router exploit
# jab on soroush app using nmap & open port msf shellcoding also send payload through burpsuite
# exploiting routers sites servers using python like mikrotik exploit using open ports msf, socket programming, burpsuite & rop concept(build exploit for mikrotik router using python, nmap, rop)
# find a bug in umz windows server 2012 r2[vce](443/tcp  open   ssl/http Microsoft IIS httpd 8.5) & exploit it using open ports with nmap => attack through an open port with msf shellcoding
# bypass umz mikrotik router vpn login page(Bypass MAC Filtering) => https://www.youtube.com/results?search_query=bypass+filtering+using+dns+changing
# exploit and jab on dormitory light using NSE(nmap & lua) => https://null-byte.wonderhowto.com/how-to/hack-like-pro-using-nmap-scripting-engine-nse-for-reconnaissance-0158681/
# all about hacking websites of any type & servers with full of efforts first by using information gathering => kali owasp, msf backdoor like backdoor.asp backdoor.py backdoor.php( upload it in target server then control the session in msf), dirbuster, burpsuite, nmap & open ports msf shellcoding, advanced phishing using SEToolkit & hydra & ngrok, Database Assessment tools in Application menu kali, DVWA, beef, xsschef
# hack all wp sites using wpscan => first scan the site with wpscan then find a vuln in whole site fianlly attack with those vuln: discover all wordpress bugs for all version
# web hacking with python and nodejs AD like RESRT VS GraphQl & Websocket VS HTTP: exploiting modern web app and hacking nosql DBs => https://www.youtube.com/watch?v=3cT0uE7Y87s
# hack through open ports using nmap NSE feature for sending shellcodes viruses botnets and exploits


import os, socket, sys