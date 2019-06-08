from subprocess import *
import os
from sys import *
from time import sleep
from colorama import *

if len(argv)==1:
    print("please give the executable")
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass
    exit()
executable=argv[1]
print(Fore.GREEN+Style.BRIGHT+"STARTING")
print("...")
print("...")
print("tester by\nAlp Eren Yilmaz\n\n\n")
sleep(1)
true=0
false=0
def tryy(testnumber,input,output,true):
    print(Fore.BLUE+Style.BRIGHT+"TEST "+str(testnumber))
    print("")
    print(Fore.CYAN+Style.NORMAL+"INPUT")
    print("---------------------------------")
    print(open(input,"r").read())
    print("---------------------------------")
    with open(input) as f:
        data=Popen([executable],stdout=PIPE,stdin=f).communicate()[0]
    f=open(output,"r")
    contents=f.read()
    sleep(1)
    if(contents==data):
        true+=1
        print(Fore.GREEN+Style.BRIGHT+"TRUE")
        print("")
        sleep(0.5)
        print(Style.NORMAL+"ANSWER:")
        print("---------------------------------")
        print(contents)
        print("---------------------------------")
    else:
        print(Fore.RED+Style.BRIGHT+"FALSE")
        print("")
        sleep(0.5)
        print(Style.NORMAL+"GIVEN RESULT:")
        print("---------------------------------")
        print(data)
        print("---------------------------------")
        print("ACTUAL RESULT:")
        print("---------------------------------")
        print(contents)
        print("---------------------------------")
    print("")
    print("")
    sleep(1)
    return true
true=tryy(1,"tests/makeup-1-input.txt","tests/makeup-1-output.txt",true)
true=tryy(2,"tests/makeup-2-input.txt","tests/makeup-2-output.txt",true)
true=tryy(3,"tests/makeup-3-input.txt","tests/makeup-3-output.txt",true)


if true==3:
    print(Style.BRIGHT+Fore.GREEN+"All of them is true!")
else:
    print(Fore.CYAN+Style.BRIGHT+"You have " +str(3-true)+ " wrong answer")
try:
    input("Press enter to continue")
except SyntaxError:
    pass

