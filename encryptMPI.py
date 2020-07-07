import time
import image_slicer
import math
from mpi4py import MPI
import sys
from Ga_Encry import Encrypt
import os
# Return the name of the corresponding image
def getName(my_rank):
	f=open("nameImage","r")
	names=f.readlines()
	f.close()
	return names[my_rank][:len(names[my_rank])-1]
# Return the message to be hidden inside the image
def getMessage(my_rank):
	f=open("messages","r")
	messages=f.readlines()
	f.close()
	return messages[my_rank][:len(messages[my_rank])-1]

comm = MPI.COMM_WORLD
my_rank=comm.Get_rank()
p=comm.Get_size()
# Get the name of the image
imageName=getName(my_rank)
# print("Name:",imageName)
# Get the message to hide
messageHide=getMessage(my_rank)
#print("message:",messageHide)
Encrypt(imageName,messageHide,my_rank)

# MPI.finalize