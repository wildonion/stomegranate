



# Recover the private key to crack and decrypt the cipher text or the hashed password + (ocl)hashcat[hashcat.net/hashcat/] with aircrack-ng + John the Ripper
# use hashcat in kali for advanced password cracking and its ocl technology + Packet Capture app in my phone + also do some session hijacking and session decryption
# see Networking/~WOCAPP/README.txt for cryptography section and more info about ciphers
# reverse engineering handshakes folder using wireshark to find the wifi password => the .cap file
# how to get internet without ISP like using ANN to simulate the 802.* wifi radio waves; whats the difference between wireless, wifi wimax:

# SOURCES:
# https://github.com/SofianeHamlaoui/WD-Decrypte
# https://thehackernews.com/2018/08/whatsapp-modify-chat-fake-news.html
# https://thehackernews.com/2018/08/how-to-hack-wifi-password.html
# http://www.linuxsecurity.com/docs/SecurityAdminGuide/SecurityAdminGuide-9.html
# https://www.wordfence.com/learn/how-passwords-work-and-cracking-passwords/
# https://thehackernews.com/2018/05/signal-desktop-hacking.html
# https://thehackernews.com/2018/05/signal-messenger-code-injection.html
# https://en.wikipedia.org/wiki/SHA-3
# https://en.wikipedia.org/wiki/Preimage_attack
# http://e-spohn.com/blog/2012/08/02/pe-crypters-hyperion/
# https://searchsecurity.techtarget.com/definition/Advanced-Encryption-Standard
# https://en.wikipedia.org/wiki/Padding_(cryptography)
# https://www.youtube.com/watch?v=koIz9ObM3dQ
# https://asecuritysite.com/encryption/padding
# https://null-byte.wonderhowto.com/forum/check-for-succesful-capture-using-wireshark-cap-file-0164742/
# https://wiki.wireshark.org/HowToDecrypt802.11
# http://www.hackingarticles.in/3-ways-crack-wifi-using-pyrit-oclhashcat-cowpatty/
# https://en.wikipedia.org/wiki/Repetition_code
# https://security.stackexchange.com/questions/66008/how-exactly-does-4-way-handshake-cracking-work
# https://en.wikipedia.org/wiki/IEEE_802.11i-2004
# https://searchsecurity.techtarget.com/definition/CCMP-Counter-Mode-with-Cipher-Block-Chaining-Message-Authentication-Code-Protocol
# https://github.com/ricmoo/pyaes
# https://pypi.org/project/pycrypto/
# https://0day.work/how-i-recovered-your-private-key-or-why-small-keys-are-bad/
# https://www.boxcryptor.com/en/encryption/
# https://contest-2017.korelogic.com/
# https://null-byte.wonderhowto.com/how-to/create-encryption-program-with-python-0164249/
# https://security.stackexchange.com/questions/92532/what-can-my-isp-see-in-their-log-files-if-i-use-google-dns
# http://www.abovetopsecret.com/forum/thread1021068/pg1
# https://www.youtube.com/watch?v=PWLffkqw_yY
# https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle
# https://mgp25.com/AESIGE/
# https://www.thesslstore.com/blog/difference-sha-1-sha-2-sha-256-hash-algorithms/
# http://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art012
# https://thehackernews.com/2014/04/securing-passwords-with-bcrypt-hashing.html
# https://thehackernews.com/2013/05/cracking-16-character-strong-passwords.html
# https://www.youtube.com/watch?v=q1VPa58tinw => an algorithm for decrypting cookies! MUST WATCH!!!!
# https://www.youtube.com/watch?v=7XZdsR0jHjo
# https://www.youtube.com/results?search_query=bit+flipping+attack

'''
TODO:
reverse engineering cryptography algos and hack whatsapp messenger
read the Hacking.Secret.Ciphers.with.Python.B00WOY87ZU.pdf book
jab on iranian app like robica and other pussy poem app
decoding messages and texts to find the secret message
getting private key with python to crack the wifi password using its handshake and wireshark?? coding theory and cryptography differences in telecomunications and client server model RSA AES
message/channel decoding and cracking & applications of cryptography to be safe and not trackable(pycrypto lib) and signal course for telecomunications for its jabing purposes
coding theory in ftp transfer type(binary, ASCII)[build a ftp app] && decrypting cookies like chrome(SnatchChrome project) also decrypt Orcus backdoor cookies
break the crypto of encrypted traffic break the ssl tls https like what isp does
understanding coding theory and cryptography concepts in message and channel encoding
javad's idea about telegram client app to encrypt soroush app messages with telegram client key + break and find the ssl/tls handshake to find the plain thing => https://github.com/DrKLO/Telegram
hack soroush app break the ssl & AES & show them using wireshark concept (how sslstrip, ssl & mitmf work, bypass ssl)[sniffing, breaking & finding et with wireshark]
sniff the encrypted msg(hash pm) with wireshark and mitm(f) then try to decrypt it by finding private key concept or using reverse engineering concept and from there we can encrypt and decrypt every msg of our target!
break the igap encryption algo and other iranian chat app
create a fake ssl certificate and a DNS server to redirect all user infos to my fake secure website smt like advanced phishing[WAN & LAN]; like the answer to stuxnet virus
'''



'''
python telbot (scrapping bot, C&C bot)
python django (a telbot to send the post from my site to my channel[WOrld proj on kali] and a site to upload all of ur cvs icluding softwares and hardwares ops of ur team which has a chatapp)
python iot (raspi, nodemcu, iot cloud storages & django)
python AD (kivy like chatapp[SCA folder] for all platforms with its cli[buildozer vm; use p2p(pyp2p) or client/server model] and use neo4jDB with tkinter & other uis libs)
python ANN (tensorflow in hacking with raspi[cv.py])
python ciphers, exploiting (decrypting & coding theory/encrypting crypto lib, socket programming & networking libs like scapy, exploiting modules like rop libs & its concept with ctypes lib)
python p2p apps(chatapp & file sharing with pyp2p lib)
python gaming (pygame & other libs)
python assembly (sehllcode injection using ctypes lib)
python HardwareHacking (raspi tools and arduino stuffs, HHV videos, HID)
python simulation (simpy in networking and other majors) => search its books
host python code on pythonanywhere cloud or build your own server with raspi
Dapp creation like D-tube and steemit cuase it's new using below links and AI concepts
https://hackernoon.com/blockchain/home, https://storj.io/, https://ipfs.io/, https://sia.tech/, https://maidsafe.net/, https://filecoin.io/, https://www.mix-blockchain.org/

'''
