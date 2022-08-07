from markerDict import *
def getMarkers(binary):
#Outputs a list of tuples (Marker ID, Index) in a binary
	outList = []
	[outList.append((markerTupleDict[(binary[x], binary[x+1])][0], x)) for x, i in enumerate(binary) if binary[x] == 255 if (binary[x], binary[x+1]) in markerTupleDict]
	return outList

def getData(binary, *index, flag=0):

	#flags:
	#0 - Returns marker bytes, length bytes, and data
	#1 - Returns length bytes and data
	#2 - Returns data

	outList = []
	sortedIndex = []
	[sortedIndex.append(i) for i in index if i not in sortedIndex]
	sortedIndex.sort(reverse=True)
	for i in sortedIndex:
		datalen = ((binary[i+2] << 8) + (binary[i+3]))
		match flag:
			case 0:
				outList.append(binary[(i):(i+datalen)])
			case 1:
				outList.append(binary[(i+2):(i+datalen)])
			case 2:
				outList.append(binary[(i+4):(i+datalen)])
	return outList
