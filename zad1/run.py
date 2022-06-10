import sys

def main():
    vystup = ''
    vstup = ''
    heslo = ''
    check=0
    check2=0
    for i in range(len(sys.argv)):
        if sys.argv[i] =='-s':
            check+=1
        if sys.argv[i] =='-d':
            check+=1
    if check != 1:
        print('chyba')
        quit()

    for i in range(len(sys.argv)):
        if sys.argv[i] == '-s':
            check2 += 1
        if sys.argv[i] == '-d':
            check2 += 1
        if sys.argv[i] == '-p':
            check2 += 1
        if sys.argv[i] == '-i':
            check2 += 1
        if sys.argv[i] == '-o':
            check2 += 1
    if check2!=4:
        print('chyba')
        exit()


    try:
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-o':
                vystup = sys.argv[i + 1]
            if sys.argv[i] == '-i':
                vstup = sys.argv[i + 1]
            if sys.argv[i] == '-p':
                heslo = sys.argv[i + 1]

    except:
        print('chyba')
        exit()

    if (heslo[0] == '-' or vstup[0] == '-' or vystup[0] == '-' or heslo == '' or vstup == '' or vystup == ''):
        print('chyba')
        exit()

    for i in range(len(sys.argv)):
        if sys.argv[i] =='-s':
            encrypt(vstup,vystup,heslo)
        if sys.argv[i] =='-d':
            decrypt(vstup,vystup,heslo)


def encrypt(vstup,vystup,heslo):
    try:
        f = open(vstup, 'r',encoding=('utf-8'))
    except:
        print('chyba')
        exit()
    text = f.readlines()
    totaltext=''
    totalheslo=''
    encryptedstring=''
    f.close()

    for i in text:
        totaltext+=i

    for i in range(int(len(totaltext)/len(heslo))):
        totalheslo+=heslo

    if(len(totaltext)!=len(totalheslo)):
        for i in range(len(totaltext)-len(totalheslo)):
            totalheslo+=heslo[i]

    for i in range(len(totaltext)):
        b= ord(totaltext[i])+ord(totalheslo[i])
        encryptedstring += chr(b)

    print(totaltext)
    print(totalheslo)
    print(encryptedstring)

    x = open(vystup, "w",encoding=('utf-8'))
    x.write(encryptedstring)
    x.close()

def decrypt(vstup,vystup,heslo):
    try:
        f = open(vstup, 'r',encoding=('utf-8'))
    except:
        print('chyba')
        exit()
    text = f.readlines()
    totaltext = ''
    totalheslo = ''
    decryptedstring = ''
    f.close()

    for i in text:
        totaltext += i

    for i in range(int(len(totaltext) / len(heslo))):
        totalheslo += heslo

    if (len(totaltext) != len(totalheslo)):
        for i in range(len(totaltext) - len(totalheslo)):
            totalheslo += heslo[i]

    for i in range(len(totaltext)):
        b = ord(totaltext[i]) - ord(totalheslo[i])
        decryptedstring += chr(b)

    print(totaltext)
    print(totalheslo)
    print(decryptedstring)

    x = open(vystup, "w",encoding=('utf-8'))
    x.write(decryptedstring)
    x.close()


if __name__ == "__main__":
    main()