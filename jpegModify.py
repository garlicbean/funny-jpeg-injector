def removeData(binary, *index, flag=0):
##
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
