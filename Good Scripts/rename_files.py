#!/usr/bin/env python
import os

def main():
   path = os.chdir('/Users/ayo/Downloads')
   print("Current directory " + str(os.getcwd()))
   files = os.listdir(os.getcwd())
   for names in files:
	file_name, file_ext = os.path.splitext(names)
	if file_ext == '.pdf':
		choice = input('Do you want to change the name of ' + file_name)
		if choice == 'y':
			print('yes')
		else:
			print('No')
		
#	print(file_ext)
if __name__ == '__main__':
   main()
