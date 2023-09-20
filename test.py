import os
import shutil
import time

op = 10

if op < 10:
	op = "0" + str(op)
	print(op)
else:
	op = str(op)
	print(op)