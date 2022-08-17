from markerDict import *

### Functions for analyzing jpeg


def getMarkers(binary):
#Outputs a list of tuples (Marker ID, Index) in a binary
	outList = []
	[outList.append((markerTupleDict[(binary[x], binary[x+1])][0], x)) for x, i in enumerate(binary) if binary[x] == 255 if (binary[x], binary[x+1]) in markerTupleDict]
	return outList
"""
ARGS:
binary - the binary data of a JPEG
"""
def getData(binary, *index):
#Extracts data from binaries, returns a list
##NOTE: Make sure you reference the index of the data you want
	outList = []
	sortedIndex = []
	[sortedIndex.append(i) for i in index if i not in sortedIndex]
	sortedIndex.sort(reverse=True)
	for i in sortedIndex:
		datalen = ((binary[i+2] << 8) + (binary[i+3]))
		outList.append(binary[(i):(i+datalen+2)])
	return outList
"""
ARGS:
binary - the binary data of a JPEG
index - index # of the start of the marker in the JPEG
"""
###Functions for modification of JPEGs


def assembleMessage(markername, bytepayload, bytetag=b'\x45\x45\x45\x45\x04\x02'):
#Formats bytes to be placed gently inside of a jpeg file, places a tag for later extraction
	payloadLenBits = bin(len(bytepayload) + len(bytetag) + 2).lstrip('0b').zfill(16)
	payloadLenBits = int(payloadLenBits[0:7], 2), int(payloadLenBits[8:16], 2)
	message = bytearray(markerDict[markername][0]) + bytes(payloadLenBits) + bytetag + bytepayload
	return bytes(message)

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
"""
ARGS:
binary - the binary data of a JPEG
index - index # of the start of the marker in the JPEG
"""

###Functons for extracting/injecting data into JPEGS

def insertData(binary, data, index):
#Returns binary with data inserted into a specified index position
	outbin = bytearray(binary)
	outbin[index:index] = data
	return bytes(outbin)

def extractData(binary, datatag=b'\x45\x45\x45\x45\x04\x02'):
#Searches for a tag and returns the data from the section that contains it
	index = binary.find(datatag) - 4
	taglen = len(datatag)
	return(getData(binary, index)[0][taglen+4::])