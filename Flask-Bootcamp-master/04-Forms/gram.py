import os

directory = r'C:\Users\admin'

for filename in os.listdir(directory):
	if filename.endswith('.jpg'):
		print(os.path.join(directory,filename))
	else:
		continue
