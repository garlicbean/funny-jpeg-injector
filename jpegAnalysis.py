from markerDict import markerDict
def getMarkers(binary):
#Outputs a list of tuples (Marker ID, Index) in a binary

	outList = []
	tupleDict = {}
	[tupleDict.update({markerDict[i][0] : i})for i in markerDict]
	[outList.append(((tupleDict[binary[x], binary[x+1]]), x)) for x, i in enumerate(binary) if binary[x] == 255 if (binary[x], binary[x+1]) in tupleDict]
	return outList

def getMarkerLength(binary, getMarkersOutput):
#Calculates the length of the data following a marker(s) (including length bytes)
#Outputs tuple: (Marker ID, Index, Length)
	outList = []
	[outList.append((i[0], i[1], ((binary[i[1]+2] << 2) + binary[i[1]+3]))) for i in getMarkersOutput if markerDict[i[0]][3] == 1]
	return outList

def getData(binary, index, length, flag=0):

#flags:
#0 - Returns marker bytes, length bytes, and data
#1 - Returns length bytes and data
#2 - Returns data
        match flag:
                case 0:
                        return binary[(index):(index+length)]
                case 1:
                        return binary[(index+2):(index+length)]
                case 2:
                        return binary[(index+4):(index+length)]
