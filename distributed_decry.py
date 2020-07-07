from PIL import Image
from PIL import Image
import image_slicer
import multiprocessing
#from dcba import Decryption
import math
from Ga_decry import Ga_decry
import os
import time
n = int(input("Enter the number of images slices: "))
# f=open("Number","w")
# f.write(n)
# f.close()
n+=1
startTime=time.time()
os.system("mpirun -np "+str(n)+" --hostfile machinefile python3 decryptMPI.py")
endTime=time.time()
print("Time taken:",endTime-startTime)
print("Extraction is complete")
# for i in range(0,n):
# 	obj=Ga_decry(i)
# 	plain_text=plain_text+obj.messe()

# print("Find text:",plain_text)
