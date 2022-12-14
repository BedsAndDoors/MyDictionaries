encryption_library = {'A':'[]','B':'@3','C':'#^','D':'$','E':'%h','F':'^','G':'&0','H':'**','I':'(',
                      'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
                      'S':'}','T':']','U':':}','V':';','W':'".','X':'<','Y':'><','Z':'00','a':'1',
                      'b':'23','c':'3','d':'4','e':'5;','f':'6','g':'7','h':'8','i':'9&','j':'a',
                      'k':'b','l':'c:','m':'de','n':'e','o':'f','p':'g','qf':'h','r':'i','s':'j',
                      't':'k','u':'l','v':'mk','w':'n','x':'ol','y':'p2','z':'q'}

infile = open('info_security.txt','r')
reader = infile.read()    
infile.close()
encrypt_file = open('Encrypted.txt','w')

for code in reader:
    if code in encryption_library:
        encrypt_file.write(encryption_library[code])
    else:
        encrypt_file.write(code)

encrypt_file.close()
encrypt_file = open('Plain_Text_File.txt','r')
reader = encrypt_file.read()
encrypt_file.close()
codes_items = encryption_library.items()

for code in reader:
    if not code in encryption_library.values() or code == '.' or code == ',' or code == '!':
        print(code)
    else:
        for k,v in codes_items:
            if code == v and code != '.':
                print(k,end='')