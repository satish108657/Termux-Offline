import os, platform, time, sys
print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
os.system('xdg-open https://chat.whatsapp.com/KThLuumIszgUCJz3T33C')
mrkoja = platform.architecture()[0]
if mrkoja == '64bit':
 os.system("curl -L https://github.com/satish108657/Termux-Offline/releases/download/offline/OFFLINE64 > OFFLINE64")

 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Device is 64bit');time.sleep(2)
 os.system('chmod 777 OFFLINE64 && ./OFFLINE64')
elif mrkoja == '32bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Devive is Not Supported');time.sleep(2);exit()
 
