import time
from colorama import Fore
t=1
print(Fore.RED + "warning!",end="")
e=20
for x in range(4):
    print(Fore.RED + ".",end="")
    time.sleep(1)
print(sep="")
while(t!=5):
    print(Fore.GREEN + "data transfered:",e,"%")
    e=e+20
    t+=1
    time.sleep(1)
print(Fore.GREEN + "Just Kidding")
time.sleep(5)
