
def main():
    print('meno: ')
    meno=input()
    print('heslo: ')
    hesloinput=input()
    print('overovaci kluc: ')
    kluc=input()

    heslo='haha'
    text = hesloinput
    totaltext = ''
    totalheslo = ''
    encryptedstring = ''

    for i in text:
        totaltext += i

    for i in range(int(len(totaltext) / len(heslo))):
        totalheslo += heslo

    if (len(totaltext) != len(totalheslo)):
        for i in range(len(totaltext) - len(totalheslo)):
            totalheslo += heslo[i]

    for i in range(len(totaltext)):
        b = ord(totaltext[i]) + ord(totalheslo[i])
        encryptedstring += chr(b)

    f = open('hesla.csv', 'r',encoding=('utf-8'))
    csv = f.readlines()



#meno
    finalkluci=''
    finalklucik=''
    finalmeno=''
    finalheslo=''
    pocet=0
    for i in csv:
        writecsv = ''
        checkmeno = False
        checkheslo = False
        checkkluc = False
        for j in i:
            if(j==':'):
                if(writecsv==meno and checkmeno==False):
                    checkmeno=True
                    finalmeno=writecsv
                    writecsv=''
                    continue
                if(writecsv==encryptedstring and checkheslo==False):
                    checkheslo=True
                    finalheslo=writecsv
                    writecsv=''
                    continue
            if j==',' or j==i[len(i)-1]:
                if (writecsv == kluc and checkkluc == False):
                    checkkluc = True
                    if j==',':
                        finalklucik=writecsv+','
                    if j==i[len(i)-1]:
                        finalklucik=','+writecsv

                    continue
                if (j == ','):
                    writecsv = ''
                    continue
            writecsv+=j

        if checkmeno==True and checkheslo==True and checkkluc==True:
            z=csv[pocet].replace(finalklucik,'')
            x = open("hesla.csv", "w", encoding=('utf-8'))
            for q in range(len(csv)):
                if q==pocet:
                    x.write(z)
                else:
                    x.write(csv[q])

            print("ok")
            break
        pocet += 1


    if checkmeno==False or checkheslo==False or checkkluc==False:
        print('chyba')

if __name__ == '__main__':
    main()