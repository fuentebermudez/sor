
import struct
import re


traza=open("/Users/Miguel/Varios/traza.sor","rt")
traza=traza.read()

iMapSize=struct.unpack("<I",traza[6:10])

MapBlock=traza[0:207]
BlocksBlock=traza[12:iMapSize[0]]

#for i in range(len(BlocksBlock)):
    
#    if struct.unpack('c',BlocksBlock[i])[0]=='\x00':
#        print(struct.unpack("<H",BlocksBlock[10:12]))

#print(struct.unpack("cc",traza[12:14]))
#print(struct.unpack("c",traza[11]))

Bloques=["Map","GenParams","SubParams","FxdParams","KeyEvents","LnkParams","DataPts","Cksum"]

for Bloque in Bloques:
    
    m=re.search(Bloque,traza)
    if m is not None:
        print(Bloque)
