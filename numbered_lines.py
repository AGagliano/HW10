#!/usr/bin/env python


def numbered_lines():
	'''Opens the file 'small.txt', reads each line 
	and writes each line numbered in a new file.
	'''
	with open('small.txt') as f:
		lines_in_f = f.readlines()
		lines_in_f = [line.strip() for line in lines_in_f]

	with open('numbered_lines.txt', 'w') as f:
		for i, line in enumerate(lines_in_f):
			f.write(str(i+1) + ' ' + line + '\n')

def main():
	numbered_lines()

if __name__ == "__main__":
	main()