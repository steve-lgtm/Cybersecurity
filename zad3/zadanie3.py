import os
import sys
import stat
import platform

def main():
    quit=0
    vstup=''
    folders=[]
    files=[]
    road=['root']
    while quit==0:

        vstup=input()
        slovo=''
        list=[]
        for j in vstup:
            if j == ' ':
                list.append(slovo)
                slovo=''
                continue
            slovo+=j
        list.append(slovo)
        for idx,j in enumerate(list):
            if j=='ls':
                preslo=False
                pravaok=False
                if len(road)>1:
                    for idx1, i in enumerate(folders):
                        if i[1] == road[len(road) - 1] and i[0] == road[len(road) - 2]:
                            if i[3] == 7 or i[3] == 6 or i[3] == 5 or i[3] == 4:
                                pravaok=True
                else:
                    pravaok=True
                if pravaok==False:
                    print("chyba")
                    break
                if len(list)==1:
                    for idx1, i in enumerate(folders):
                        if i[0]==road[len(road)-1]:
                                rights = ''
                                if i[3] == 7:
                                    rights = 'rwx'
                                elif i[3] == 6:
                                    rights = 'rw-'
                                elif i[3] == 4:
                                    rights = 'r--'
                                elif i[3] == 2:
                                    rights = '-w-'
                                elif i[3] == 1:
                                    rights = '--x'
                                elif i[3] == 3:
                                    rights = '-wx'
                                elif i[3] == 5:
                                    rights = 'r-x'
                                elif i[3] == 0:
                                    rights = '---'
                                print(i[1],i[2],rights)
                    for idx1, i in enumerate(files):
                        if i[0]==road[len(road)-1]:
                            rights = ''
                            if i[3] == 7:
                                rights = 'rwx'
                            elif i[3] == 6:
                                rights = 'rw-'
                            elif i[3] == 4:
                                rights = 'r--'
                            elif i[3] == 2:
                                rights = '-w-'
                            elif i[3] == 1:
                                rights = '--x'
                            elif i[3] == 3:
                                rights = '-wx'
                            elif i[3] == 5:
                                rights = 'r-x'
                            elif i[3] == 0:
                                rights = '---'
                            print(i[1],i[2],rights)
                else:
                    for idx1, i in enumerate(folders):
                        if i[1] == list[1]:
                            rights = ''
                            if i[3] == 7:
                                rights = 'rwx'
                            elif i[3] == 6:
                                rights = 'rw-'
                            elif i[3] == 4:
                                rights = 'r--'
                            elif i[3] == 2:
                                rights = '-w-'
                            elif i[3] == 1:
                                rights = '--x'
                            elif i[3] == 3:
                                rights = '-wx'
                            elif i[3] == 5:
                                rights = 'r-x'
                            elif i[3] == 0:
                                rights = '---'
                            preslo=True
                            print(i[1], i[2], rights)
                    for idx1, i in enumerate(files):
                            if i[1] == list[1]:
                                rights = ''
                                if i[3] == 7:
                                    rights = 'rwx'
                                elif i[3] == 6:
                                    rights = 'rw-'
                                elif i[3] == 4:
                                    rights = 'r--'
                                elif i[3] == 2:
                                    rights = '-w-'
                                elif i[3] == 1:
                                    rights = '--x'
                                elif i[3] == 3:
                                    rights = '-wx'
                                elif i[3] == 5:
                                    rights = 'r-x'
                                elif i[3] == 0:
                                    rights = '---'

                                print(i[1], i[2], rights)
                                preslo = True
                    if preslo==False:
                        print('chyba')
            if j=='quit':
                quit=1
            if j=='chown':
                if list[0]=='' or list[1]=='' or list[2]=='' or list[0]==' ' or list[1]==' ' or list[2]==' ':
                    print('chyba')
                    break
                changed=False
                for idx1, i in enumerate(folders):
                    if i[0]==road[len(road)-1] and i[1]==list[2]:
                        i[2]=list[1]
                        changed=True
                if changed==False:
                    for idx1, i in enumerate(files):
                        if i[0] == road[len(road) - 1] and i[1] == list[2]:
                            i[2] = list[1]
                            changed=True

                if changed==False:
                    print('chyba')
            if j=='vypis':
                if len(list)<=1:
                    print('chyba')
                    break
                if list[1]==' ' or list[1]=='':
                    print('chyba')
                    break
                changed=False
                for idx1, i in enumerate(folders):
                    if i[0] == road[len(road) - 1] and i[1]==list[1]:
                        if i[3] == 7 or i[3] == 6 or i[3] == 4 or i[3] == 5:
                            changed=True
                            print('ok')
                            break
                        else:
                            print('chyba')
                if changed==False:
                    for idx1, i in enumerate(files):
                        if i[0] == road[len(road) - 1] and i[1]==list[1]:
                            if i[3] == 7 or i[3] == 6 or i[3] == 4 or i[3] == 5:
                                changed=True
                                print('ok')
                                break
                            else:
                                print('chyba')
                if changed==False:
                    print('chyba')
            if j == 'rm':
                if len(list)<=1:
                    print('chyba')
                    break
                if list[1]==' ' or list[1]=='':
                    print('chyba')
                    break
                changed = False
                for idx1, i in enumerate(folders):
                    if i[0] == road[len(road) - 1] and i[1] == list[1]:
                        if i[3]==7 or i[3]==6 or i[3]==2 or i[3]==3:
                            folders.pop(idx1)
                            changed = True
                if changed == False:
                    for idx1, i in enumerate(files):
                        if i[0] == road[len(road) - 1] and i[1] == list[1]:
                            if i[3] == 7 or i[3] == 6 or i[3] == 2 or i[3] == 3:
                                files.pop(idx1)
                                changed = True
                if changed == False:
                    print('chyba')
            if j == 'chmod':
                if list[0]=='' or list[1]=='' or list[2]=='' or list[0]==' ' or list[1]==' ' or list[2]==' ':
                    print('chyba')
                    break
                list[1]=int(list[1])

                if list[1]<0 or list[1]>7:
                    print('chyba')
                    break
                changed=False
                for idx1, i in enumerate(files):
                    if i[0] == road[len(road) - 1] and i[1] == list[2]:
                        i[3] = list[1]
                        changed = True

                if changed==False:
                    for idx1, i in enumerate(folders):
                        if i[0] == road[len(road) - 1] and i[1] == list[2]:
                            i[3] = list[1]
                            changed = True
                if changed==False:
                    print('chyba')

            if j=='spusti':
                if len(list)<=1:
                    print('chyba')
                    break
                if list[1]==' ' or list[1]=='':
                    print('chyba')
                    break
                changed=False
                for idx1, i in enumerate(folders):
                    if i[0] == road[len(road) - 1] and i[1]==list[1]:
                        if i[3] == 7 or i[3] == 1 or i[3] == 3 or i[3] == 5:
                            changed=True
                            print('ok')
                            break
                        else:
                            print('chyba')
                for idx1, i in enumerate(files):
                    if i[0] == road[len(road) - 1] and i[1]==list[1]:
                        if i[3] == 7 or i[3] == 1 or i[3] == 3 or i[3] == 5:
                            changed=True
                            print('ok')
                            break
                        else:
                            print('chyba')
                if changed==False:
                    print('chyba')
            if j == 'zapis':
                if len(list) <= 1:
                    print('chyba')
                    break
                if list[1] == ' ' or list[1] == '':
                    print('chyba')
                    break
                preslo=False
                for idx1, i in enumerate(files):
                    if i[0] == road[len(road) - 1] and i[1] == list[1]:
                        if i[3] == 7 or i[3] == 6 or i[3] == 3 or i[3] == 2:
                            print('ok')
                            preslo = True
                            break
                        else:
                            preslo=True
                            print('chyba')

                if preslo==False:
                    for idx1, i in enumerate(folders):
                        if i[0] == road[len(road) - 1] and i[1] == list[1]:
                            if i[3] == 7 or i[3] == 6 or i[3] == 3 or i[3] == 2:
                                print('ok')
                                preslo = True
                                break
                            else:
                                print('chyba')
                if preslo==False:
                    print('chyba')
            if j=='mkdir':
                if len(list)<=1:
                    print('chyba')
                    break
                if list[1]==' ' or list[1]=='':
                    print('chyba')
                    break
                    je=0
                for idx1, i in enumerate(files):
                    if i[1]==list[1]:
                        print('chyba')
                exist=False
                if len(folders)==0:
                    if road[len(road)-1]=="root":
                        folders.append(["root", list[1], platform.node(), 7])
                        break
                else:
                    for idx1, i in enumerate(folders):
                        if i[1] == list[1] and i[0] == road[len(road) - 1]:
                            exist=True
                            break
                    if exist==True:
                        print("chyba")
                        break
                    for idx1, i in enumerate(folders):
                        if(len(road)>=2):
                            if i[1]==road[len(road)-1] and i[0]==road[len(road)-2]:
                                if i[3]==7 or i[3]==6 or i[3]==2 or i[3]==3:
                                    folders.append([road[len(road) - 1], list[1], platform.node(), 7])
                                    break
                                else:
                                    print("chyba")
                        if road[len(road)-1]=="root":
                            folders.append(["root", list[1], platform.node(), 7])
                            break
            if j=='cd':
                if list[1]=='..':
                    if len(road) > 1:
                        road.pop(len(road)-1)
                        break
                    else:
                        break
                posibleroads = []
                preslo=False
                for idx1, i in enumerate(folders):
                    if i[0]==road[len(road)-1]:
                        posibleroads.append([i[1],i[3]])
                for idx1, i in enumerate(posibleroads):
                    if i[0]==list[1]:
                        if (i[1] == 1 or i[1] == 3 or i[1] == 5 or i[1] == 7):
                            road.append(list[1])
                            preslo=True
                            break
                        else:
                            preslo=True
                            print('chyba')
                if preslo==False:
                   print("chyba")

            if j=='touch':
                if len(folders)==0:
                    if road[len(road)-1]=="root":
                        files.append(["root", list[1], platform.node(), 7])
                        break
                else:
                    for idx1, i in enumerate(folders):
                        if (len(road) >= 2):
                            if i[1] == road[len(road) - 1] and i[0] == road[len(road) - 2]:
                                if i[3] == 7 or i[3] == 6 or i[3] == 2 or i[3] == 3:
                                    files.append([road[len(road) - 1], list[1], platform.node(), 7])
                                    break
                                else:
                                    print("chyba")
                        if road[len(road)-1]=="root":
                            files.append(["root", list[1], platform.node(), 7])
                            break

if __name__ == "__main__":
    main()

"""
check = 0
if vstup == ' ':
    continue
if sys.argv[i] == 'ls':

if sys.argv[i] == '-d':
    check += 1
if sys.argv[i] == '-p':
    check += 1
if sys.argv[i] == '-i':
    check += 1
if sys.argv[i] == '-o':
    check += 1
"""
