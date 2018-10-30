import sys
import os
import zipfile
import optparse
from threading import Thread

os.system("clear")
os.system("figlet Anon ZIP Cracker")

print 
print "+========================================+"
print "|-----------[Anon ZIP Cracker]-----------|"
print "+========================================+"
print "|         Creator : Anon6372098          |"
print "|      Thanks to  : Tuan c4rt00nw4r      |"
print "|         Github  : /Anon6372098         |"
print "|Team : D4RK SYST3M F41LUR3 S33K3R (DSFS)|"
print "+========================================+"
print "|-----------[Anon ZIP Cracker]-----------|"
print "+----------------------------------------+"
print "Use Command Below to Use This Tool/Gunakan Perintah Dibawah Ini"
print

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Brute Force Successful: ' + password + '\n'
        return password
    except:
        return
def main():
    parser = optparse.OptionParser('usage: python2 zipcracker.py ' + '-f <zipfile> -w <wordlist>')
    parser.add_option('-f', dest='zname',type='string',help='specify zip file')
    parser.add_option('-w', dest='wname',type='string',help='specify wordlist file')
    (options,args) = parser.parse_args()
    if (options.zname == None) | (options.wname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        wname = options.wname
    zFile = zipfile.ZipFile(zname)
    passFile = open(wname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()
