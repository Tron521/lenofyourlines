import argparse
import os
import enum
def if_legal(dir):
	if os.path.exists(dir):
		return True
	else :
		return False
def get_allfiles(dir,filter):
	for index_dir,_,filenames in os.walk(dir):
		for filename in filenames:
			pathandfile = os.path.join(index_dir,filename)
			ext = os.path.splitext(pathandfile)[1]
			if ext in filter:
				yield pathandfile
def get_lines(pathandfile):
	with open(pathandfile,"r",encoding="utf-8",errors="ignore") as f:
		lines = 0
		print('正在分析文件：%s...' % pathandfile)
		for index,line in enumerate(f):
			if line.isspace():
				continue
			lines+=1
		return lines
def main():
	parser = argparse.ArgumentParser(description = "By Tron")
	parser.add_argument("--dir","-d")
	parser.add_argument("--filter","-f",type=str,nargs="+")
	args = parser.parse_args()
	dir = args.dir
	filter = args.filter
	if if_legal(dir):
		line = 0
		for pathandfile in get_allfiles(dir,filter):
			line += get_lines(pathandfile)
		print(f"your lines of code are {line}")
	else:
		print("your dir is not existed!")
if __name__ == "__main__":
	main()
