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
sleep(0.5)
print("tester by\nAlp Eren Yilmaz\n\n\n")
sleep(1)
true=0
false=0
print(Fore.BLUE+Style.BRIGHT+"TEST 1")
print("")
print(Fore.CYAN+Style.NORMAL+"INPUT")
print("---------------------------------")
print(open("tests/5-input.txt","r").read())
print("---------------------------------")

with open('tests/5-input.txt') as f:
    data=Popen([executable],stdout=PIPE,stdin=f).communicate()[0]
f=open("tests/5-output.txt","r")
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
    false+=1
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
print(Fore.BLUE+Style.BRIGHT+"TEST 2")
print("")
print(Fore.CYAN+Style.NORMAL+"INPUT")
print("---------------------------------")
print(open("tests/4-input.txt","r").read())
print("---------------------------------")

with open('tests/4-input.txt') as f:
    data=Popen([executable],stdout=PIPE,stdin=f).communicate()[0]
f=open("tests/4-output.txt","r")
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
    false+=1
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
print(Fore.BLUE+Style.BRIGHT+"TEST 3")
print("")
print(Fore.CYAN+Style.NORMAL+"INPUT")
print("---------------------------------")
print(open("tests/3-input.txt","r").read())
print("---------------------------------")

with open('tests/3-input.txt') as f:
    data=Popen([executable],stdout=PIPE,stdin=f).communicate()[0]
f=open("tests/3-output.txt","r")
contents=f.read()
sleep(1)
if(contents==(data)):
    true+=1
    print(Fore.GREEN+Style.BRIGHT+"TRUE")
    print("")
    sleep(0.5)
    print(Style.NORMAL+"ANSWER:")
    print("---------------------------------")
    print(contents)
    print("---------------------------------")
else:
    false+=1
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
print(Fore.BLUE+Style.BRIGHT+"TEST 4")
print("")
print(Fore.CYAN+Style.NORMAL+"INPUT")
print("---------------------------------")
print(open("tests/2-input.txt","r").read())
print("---------------------------------")

with open('tests/2-input.txt') as f:
    data=Popen([executable],stdout=PIPE,stdin=f).communicate()[0]
f=open("tests/2-output.txt","r")
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
    false+=1
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
print(Fore.BLUE+Style.BRIGHT+"TEST 5")
print("")
print(Fore.CYAN+Style.NORMAL+"INPUT")
print("---------------------------------")
print(open("tests/1-input.txt","r").read())
print("---------------------------------")

with open('tests/1-input.txt') as f:
    data=Popen([executable],stdout=PIPE,stdin=f).communicate()[0]
f=open("tests/1-output.txt","r")
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
    false+=1
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
if true==5:
    print(Style.BRIGHT+Fore.GREEN+"All of them is true!")
else:
    print(Fore.CYAN+Style.BRIGHT+"You have " +str(false)+ " wrong answer")
try:
    input("Press enter to continue")
except SyntaxError:
    pass

