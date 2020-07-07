import time
import image_slicer
import math
from mpi4py import MPI
import sys
from Ga_decry import Ga_decry
import os
#n=int(input("Enter the number of image slices"))
comm = MPI.COMM_WORLD
my_rank=comm.Get_rank()
p=comm.Get_size()
# This is going to accomodate all the decrypted messages and print the complete message
if my_rank==0:
	hiddenMessage=""
	for i in range(1,p):
		hiddenMessage=hiddenMessage+comm.recv(source=i)
		print("Message from ",my_rank,": Got the message from ",p)
	print("The hidden message is:",hiddenMessage)
	f=open("hiddenMessage","w")
	f.write(hiddenMessage)
	f.close()	
# This is to get the hidden message from image slices
else:
	plain_text=""
	obj=Ga_decry(my_rank-1)
	plain_text=plain_text+obj.messe()
	comm.send(plain_text, dest=0)
	print("Message from ",my_rank,": Have sent the plain_text to the master process")