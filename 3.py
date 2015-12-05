import os
for file in os.listdir("/Users/pradeepwason/Downloads/Pics"):
	time = file.split("-", 2)[-1].split(".",1)
	print(time[0])
