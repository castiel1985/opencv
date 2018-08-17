#encoding: utf-8
import SocketServer
import time
import struct
import binascii
import os,sys
import logging


from SocketServer import StreamRequestHandler as SRH
from time import ctime

host = '0.0.0.0'
port = 8509
addr = (host, port)
l_port ={}     #all port

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                datefmt=' %Y-%m-%d %H:%M:%S',
                filename='myapp.log',
                filemode='w')

#data deal
def strtofloat(str):
    k = '%s%s' % (str[4:],str[0:4])
    p = struct.unpack('!f', k.decode('hex'))[0]   #change to float
    return p



def sendtozabbix(dtu,type,value):
    s = ' -s "%s" -z 127.0.0.1 -k %s -o %f' % (dtu,type,value)
    cmd = '/opt/zabbix/bin/zabbix_sender '+s
    os.system(cmd)
    #logging.info('run the cmd is:'+cmd)


#sendtozabbix('2016032611_oxygen_1','oxygenvalue',83)
def gettype(str):
    l={}
    if str[0]== '1':
        if str[1]=='0':
            dtu_s = '_oxygen_'
            type = 'oxygenvalue'
        elif str[1]=='1':
            dtu_s = '_oxygen_'
            type = 'oxygenratio'
        elif str[1]=='2':
            dtu_s = '_oxygen_'
            type = 'oxygentemp'
        elif str[1]=='3':
            dtu_s = '_oxygen_'
            type = 'oxygensalt'
        elif str[1]=='4':
            dtu_s = '_ph_'
            type = 'phvalue'
        elif str[1]=='5':
            dtu_s = '_salt_'
            type = 'phvalue'
        elif str[1]=='6':
            dtu_s = '_orp_'
            type = 'orpvalue'
        num = int(str[2:],16)
        a = '%s%d' % (dtu_s ,num)
        l[0] = type
        l[1] = a
        return l
    else:
        return False


def getfloatdata(data,dtu):
    s=data[6:len(data)-4]
    i = 0
    while i<(len(s)/12):
        j=i*12
        k=j+12
        i = i + 1
        #print s[j:k]
        value = strtofloat(s[j:k][4:])
        str = s[j:k][0:4]
        l = gettype(str)
        #print str
        if l:
            dtu_s = dtu+l[1]
            sendtozabbix(dtu_s,l[0],value)
            #s = '%s<%s>%d' % (dtu_s,l[0],value)
            #logging.info(s)
        else:
            logging.info(dtu+":data error")


#CRC  get crc code and verify
class crc16:
    auchCRCHi = [0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, \
                 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, \
                 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, \
                 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, \
                 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, \
                 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, \
                 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, \
                 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, \
                 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, \
                 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, \
                 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, \
                 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, \
                 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, \
                 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, \
                 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, \
                 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, \
                 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, \
                 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, \
                 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, \
                 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40]

    auchCRCLo = [0x00, 0xC0, 0xC1, 0x01, 0xC3, 0x03, 0x02, 0xC2, 0xC6, 0x06, \
                 0x07, 0xC7, 0x05, 0xC5, 0xC4, 0x04, 0xCC, 0x0C, 0x0D, 0xCD, \
                 0x0F, 0xCF, 0xCE, 0x0E, 0x0A, 0xCA, 0xCB, 0x0B, 0xC9, 0x09, \
                 0x08, 0xC8, 0xD8, 0x18, 0x19, 0xD9, 0x1B, 0xDB, 0xDA, 0x1A, \
                 0x1E, 0xDE, 0xDF, 0x1F, 0xDD, 0x1D, 0x1C, 0xDC, 0x14, 0xD4, \
                 0xD5, 0x15, 0xD7, 0x17, 0x16, 0xD6, 0xD2, 0x12, 0x13, 0xD3, \
                 0x11, 0xD1, 0xD0, 0x10, 0xF0, 0x30, 0x31, 0xF1, 0x33, 0xF3, \
                 0xF2, 0x32, 0x36, 0xF6, 0xF7, 0x37, 0xF5, 0x35, 0x34, 0xF4, \
                 0x3C, 0xFC, 0xFD, 0x3D, 0xFF, 0x3F, 0x3E, 0xFE, 0xFA, 0x3A, \
                 0x3B, 0xFB, 0x39, 0xF9, 0xF8, 0x38, 0x28, 0xE8, 0xE9, 0x29, \
                 0xEB, 0x2B, 0x2A, 0xEA, 0xEE, 0x2E, 0x2F, 0xEF, 0x2D, 0xED, \
                 0xEC, 0x2C, 0xE4, 0x24, 0x25, 0xE5, 0x27, 0xE7, 0xE6, 0x26, \
                 0x22, 0xE2, 0xE3, 0x23, 0xE1, 0x21, 0x20, 0xE0, 0xA0, 0x60, \
                 0x61, 0xA1, 0x63, 0xA3, 0xA2, 0x62, 0x66, 0xA6, 0xA7, 0x67, \
                 0xA5, 0x65, 0x64, 0xA4, 0x6C, 0xAC, 0xAD, 0x6D, 0xAF, 0x6F, \
                 0x6E, 0xAE, 0xAA, 0x6A, 0x6B, 0xAB, 0x69, 0xA9, 0xA8, 0x68, \
                 0x78, 0xB8, 0xB9, 0x79, 0xBB, 0x7B, 0x7A, 0xBA, 0xBE, 0x7E, \
                 0x7F, 0xBF, 0x7D, 0xBD, 0xBC, 0x7C, 0xB4, 0x74, 0x75, 0xB5, \
                 0x77, 0xB7, 0xB6, 0x76, 0x72, 0xB2, 0xB3, 0x73, 0xB1, 0x71, \
                 0x70, 0xB0, 0x50, 0x90, 0x91, 0x51, 0x93, 0x53, 0x52, 0x92, \
                 0x96, 0x56, 0x57, 0x97, 0x55, 0x95, 0x94, 0x54, 0x9C, 0x5C, \
                 0x5D, 0x9D, 0x5F, 0x9F, 0x9E, 0x5E, 0x5A, 0x9A, 0x9B, 0x5B, \
                 0x99, 0x59, 0x58, 0x98, 0x88, 0x48, 0x49, 0x89, 0x4B, 0x8B, \
                 0x8A, 0x4A, 0x4E, 0x8E, 0x8F, 0x4F, 0x8D, 0x4D, 0x4C, 0x8C, \
                 0x44, 0x84, 0x85, 0x45, 0x87, 0x47, 0x46, 0x86, 0x82, 0x42, \
                 0x43, 0x83, 0x41, 0x81, 0x80, 0x40]

    def __init__(self):
        pass

    def createcrc(self, array):
        crchi = 0xff
        crclo = 0xff
        for i in range(0, len(array)):
            crcIndex = crchi ^ array[i]
            crchi = crclo ^ self.auchCRCHi[crcIndex]
            crclo = self.auchCRCLo[crcIndex]
        return (crchi << 8 | crclo)

    def createarray(self, array):     #get crc code
        crcvalue = self.createcrc(array)
        array.append(crcvalue >> 8)
        array.append(crcvalue & 0xff)
        return array

    def calcrc(self, array):          #verify
        crchi = 0xff
        crclo = 0xff
        lenarray = len(array)
        for i in range(0, lenarray - 2):
            crcIndex = crchi ^ array[i]
            crchi = crclo ^ self.auchCRCHi[crcIndex]
            crclo = self.auchCRCLo[crcIndex]
        if crchi == array[lenarray - 2] and crclo == array[lenarray - 1]:
            return 0
        else:
            return 1


class Servers(SRH):
    timeout =115
    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)
                #print "RECV from ", self.client_address
                s1 = "RECV from ", self.client_address
                logging.info(s1)
            except:
                #print "recv error"
                logging.info("recv error")
                break
            else:
                if not data:
                    break
              #  print da
                # cd pyt
                # ta[0:3]
                if data[0:3] == 'ZWG' :
                    s = struct.unpack('!11s9s12s9s11s', data)
                    #print "the DTU is",s[4][0:10]
                    s2 = "the DTU is",s[4][0:10]
                    logging.info(s2)
                    time.sleep(58)
                    l_port[self.client_address[1]] = s[4][0:10]
                    a = [0x01, 0x03, 0x00, 0x00, 0x00, 0x01, 0x84, 0x0A]
                    b = ""
                    for i in range(len(a)):
                        b += chr(a[i])
                    #time.sleep(1)
                    self.request.send(b)
                    logging.info(a)
                    data = ''
                else:
                    #print "this is MSG"
                    logging.info("this is MSG")
                    #c = [0x01,0x03,0x00,0x01,0x00,0x15,0xd5,0xc5]
                    #d = ""
                    #for i in range(len(c)):
                        #d += chr(c[i])
                    #self.request.send(d)
                    s = str(binascii.b2a_hex(data))
                    logging.info(s)
                    f = '01030001'
                    logging.info('%s data is %s' % (l_port[self.client_address[1]],s))
                    if s[0:6]=='010302':
                        crc = crc16()
                        f = f + s[6:10]
                        n = binascii.unhexlify(f)
                        h = [ord(x) for x in n]
                        b = crc.createcrc(h)
                        cmd = f + hex(b)[2:]
                        logging.info(cmd)
                        #p = binascii.unhexlify(cmd)
                        #print 'p is ',p
                        d = binascii.unhexlify(cmd)
                        p = [ord(x) for x in d]
                        m = ""
                        for i in range(len(p)):
                            m += chr(p[i])
                        self.request.send(m)
                    elif s:
                        getfloatdata(s, l_port[self.client_address[1]])
                        del l_port[self.client_address[1]]
			            break
                    else:
                        break
                    data = ''
                    time.sleep(45)
            s3 = "all port is ",l_port
            logging.info(s3)


    def handle_timeout(self):
        #print "port %s is timeout" % self.client_address[1]
        logging.info("port %s is timeout" % self.client_address[1])
        l_port.remove(self.client_address[1])
        del l_port[self.client_address[1]]

    def finish(self):
        #print "port %s is lost" % self.client_address[1]
        logging.info("port %s is lost" % self.client_address[1])
        l_port.remove(self.client_address[1])
        del l_port[self.client_address[1]]


def daemon():
    pid = os.fork()
    if pid > 0:
        sys.exit(0)
    # 修改子进程工作目录
    os.chdir("/")
    # 创建新的会话，子进程成为会话的首进程
    os.setsid()
    # 修改工作目录的umask
    os.umask(0)
    # 创建孙子进程，而后子进程退出
    pid = os.fork()
    if pid > 0:
        sys.exit(0)
    # 重定向标准输入流、标准输出流、标准错误
    sys.stdout.flush()
    sys.stderr.flush()
    si = file("/dev/null", 'r')
    so = file("/dev/null", 'a+')
    se = file("/dev/null", 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())


if __name__ =="__main__":
    daemon()
    #print 'server is running....'
    logging.info('server is running....')
    server = SocketServer.ThreadingTCPServer(addr, Servers)
    server.daemon_threads = True
    server.serve_forever()
