from markerDict import *

### Functions for analyzing jpeg


def getMarkers(binary):
#Outputs a list of tuples (Marker ID, Index) in a binary
	outList = []
	[outList.append((markerTupleDict[(binary[x], binary[x+1])][0], x)) for x, i in enumerate(binary) if binary[x] == 255 if (binary[x], binary[x+1]) in markerTupleDict]
	return outList

def getData(binary, *index):
	outList = []
	sortedIndex = []
	[sortedIndex.append(i) for i in index if i not in sortedIndex]
	sortedIndex.sort(reverse=True)
	for i in sortedIndex:
		datalen = ((binary[i+2] << 8) + (binary[i+3]))
		outList.append(binary[(i):(i+datalen+2)])
	return outList

###Functions for modification of JPEGs


def assembleMessage(markername, bytepayload, bytetag=b'\x45\x45\x45\x45\x04\x02'):
#Formats bytes to be placed gently inside of a jpeg file, places a tag for later extraction
	outbin = []
	
	messagelen = len(bytepayload) + len(bytetag)
	if messagelen > 65535:
		raise ValueError('Message too long')
	markerBytes = markerDict[markername][0]
	lengthBytes = int(hex(messagelen).lstrip('0x').zfill(4) [0:2], 16), int(hex(messagelen).lstrip('0x').zfill(4)[2:4], 16)
	return bytes(markerBytes+lengthBytes+tuple(bytetag)+tuple(bytepayload))

def removeData(binary, *index, flag=0):
##flags:
#0 - preserves marker and sets length bytes == 2
#1 - removes marker and header

	binary = bytearray(binary)
	sortedIndex = []
	[sortedIndex.append(i) for i in index if i not in sortedIndex]
	sortedIndex.sort(reverse=True)
	for i in sortedIndex:
		datalen = ((binary[i+2] << 8) + (binary[i+3]))
		match flag:
			case 0:
				binary[i+2:i+4] = b'\x00\x02'
				del binary[i+4:i+datalen+2]
			case 1:
				del binary[i:i+datalen+2]
	return bytes(binary)
