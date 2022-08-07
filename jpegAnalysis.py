from markerDict import *
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
			outList.append(binary[(i):(i+datalen)])
	return outList
