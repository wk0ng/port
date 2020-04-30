#!/usr/bin/python
# Author : wkong
# Cleared port info
import os
import sys
def clearChar(chars):
    restr = ['\n','\r','\t',' ']
    data = chars
    for s in restr:
        data = data.replace(s,'')

    return data

def loadConfig():
    sevrConfig = 'SSH:RDP:SMB:MySQL:SQLServer:Oracle:FTP:MongoDB:Memcached:PostgreSQL:Telnet:SMTP:SMTP_SSL:POP3:POP3_SSL:IMAP:IMAP_SSL:VNC:Redis:Weblogic'
    portConfig = '22:3389:445:3306:1433:1521:21:27017:11211:5432:23:25:465:110:995:143:993:5900:6379:7001'

    sevrConfig = sevrConfig.split(':')
    portConfig = portConfig.split(':')

    sevrConfig.append('Other')

    return sevrConfig, portConfig

if __name__ == '__main__':
    try:
        
        fileName = sys.argv[1]

        if not os.path.exists(fileName+'_port'):
            os.makedirs(fileName+'_port')

        pFList = []
        sevrConfig, portConfig = loadConfig()

        pFile = open(fileName, 'r')

        for sevr in sevrConfig:
            pFList.append(open(fileName+'_port/'+sevr+'.txt', 'w+'))

        lines = pFile.readlines()

        for line in lines:
            line = clearChar(line)
            line = line.split(':')

            ip = line[0]
            port = line[1]

            if port in portConfig:
                indexof = portConfig.index(port)
                serverName = sevrConfig[indexof]
                
                print('[{}]{}'.format(serverName, ip))
                pFList[indexof].write(ip+'\n')
            else:
                indexof = sevrConfig.index('Other')
                print('[Other]{}'.format(ip))
                pFList[indexof].write(ip+':'+port+'\n')

        pFile.close()
        for pF in pFList:
            pF.close()
    except Exception as err:
        print('Useage: python port.py port.txt')
