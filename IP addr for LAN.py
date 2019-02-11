import os
import re


def check(chstr):
    if len(re.findall(r'\D', chstr)) == 0:
        result = 0
    else:
        print('Error: Write only digital')
        result = -1

    return result

def maskconv(mask):
    mask = int(mask)
    full_oct = mask // 8
    last_oct = mask % 8
    result = '255.' * full_oct
    if last_oct == 0:
        result = result + ('0.' * (4 - full_oct))
        result = result[:-1]
    else:
        result = result + str(256 - 2 ** (8 - last_oct))

        if full_oct < 3:
            result = result + '.'
            result = result + ('0.' * (4 - full_oct))
            result = result[:-1]

    return result

decision = -1
index = False

while decision != 0:
    print ('\n###############################################################\n'
       '0. Exit\n'
       '1. Change IP address\n'
       '2. Enable LAN\n'
       '3. Disable LAN\n'
       '4. Check IP addr\n'
       '5. ipconfig /all')

    while(index == False):
        decision = input()
        if check(decision) == 0:
            decision = int(decision)
            index = True
        else:
            index = False    
        
    if decision == 1:
        ipmask = input('IP mask\n')
        ipadd = ipmask.split(' ')[0]
        mask = ipmask.split(' ')[1]
        mask = maskconv(mask)
        os.system('netsh interface ip set address name="Local Area Connection" static '+ ipadd + ' ' + mask)

    elif decision == 2:
        os.system('netsh interface set interface name="Local Area Connection" admin=enable')

    elif decision == 3:
        os.system('netsh interface set interface name="Local Area Connection" admin=disable')

    elif decision == 4:
        os.system('ipconfig')

    elif decision == 5:
        os.system('ipconfig /all')
    	
    index = False
