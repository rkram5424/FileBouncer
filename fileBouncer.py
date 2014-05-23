import sys
import os
from os import listdir, walk

def main():
	if (sys.argv[1] == '-h'):
		print('WARNING! This program deletes files! Do not use it in a directory with files you do not wish to delete.')
		print('This program\'s purpose is to delete files above and below a certain threshold, either as they populate the directory or as a one-time cleansweep.\n')
		print('Instructions:\n')
		print('Run the program with the 3 following arguments: min size(in KB\'s), max size(in KB\'s), and the directory.')
		print('fileBouncer.py [min size] [max size] [directory]')
		sys.exit()
	if (len(sys.argv) != 4) and (sys.argv[1] != '-h'):
		print('Usage: fileBouncer.py min-filesize max-filesize path-to-directory\n')
		print('For help, run \'fileBouncer.py -h\'')
		sys.exit()
	watch()
	return 0

def watch():
	minSize = float(sys.argv[1]) * 1000.0
	maxSize = float(sys.argv[2]) * 1000.0
	directory = sys.argv[3]
	dirList = []
	for (dirpath, dirnames, filenames) in walk(directory):
		dirList.extend(filenames)
		break
	for i in range(0, len(dirList)):
		if (os.path.getsize(directory + dirList[i]) < minSize or os.path.getsize(directory + dirList[i]) > maxSize):
			os.remove(directory + dirList[i])
	return 0

if __name__ == '__main__':
	main()

