# Using readlines()

class Text:
	def readfirst(file):
		file1 = open(file, 'r')
		first_line = file1.readline()
		file1.close()
		return first_line

	def deletefirst(file):
		file_read = open(file, 'r')
		first_line = file_read.readline()
		lines = file_read.readlines()
		file_read.close()
		file_to_write = open(file, 'w')
		for line in lines:
		    if line.strip("\n") != first_line:
		        file_to_write.write(line)
