from Ga_Encry import Encrypt
import time
import image_slicer
import math
from mpi4py import MPI
import sys
import os
# Generate the names of the image slices from the tuple returned by image_slicer
def imageName(image_slices):
	names=[]
	for i in image_slices:
		a=str(i).split('-')
		b=a[1][1:len(a[1])-1]
		names.append(b)
	return names


def sliceImage(image,number):
	image_pieces=image_slicer.slice(image, number)
	return image_pieces

# This module of code is used to split the string into n eq parts
def message_split(message,number):
	n=math.ceil(len(message)/number)
	ms=[]
	for i in range(number):
		if ((i+1)*n) < len(message) : 
			ms.append(message[i*n:(i+1)*n])
		else:
			ms.append(message[i*n:])
	return ms	
def main():
	names=["bird_100.jpg","bird_150.jpg","bird_200.jpg","bird_250.jpg","bird_300.jpg"]
	files=["answer_100","answer_150","answer_200","answer_250","answer_300"]
	for ads in range(0,len(names)):
		name=names[ads]
		f1=open(files[ads],"a")
		for number in range(2,31,2):
		#name=input("Enter the name of the image:")
			#number=int(input("Enter the number of slices"))
			image_slices = sliceImage(name,number)
			complete_message = "asdlfkj asldkfj  asd;fkljas ;lkasdfj ;lasdfkj  asl;dkfj laksfdj ;lasjkdf ;laskfj ;lakjf ;lakfj asdflkj klajsdfh aklsjdhf alsdjkfh lakjsdfh laksdjfh lajksfh asjdfhlajksfh "
			message = message_split(complete_message,number)
			print("The split message is:",message)
			nameImage = imageName(image_slices)
			# with pymp.Parallel(4) as p:
			
			# comm = MPI.COMM_WORLD
			# my_rank=comm.Get_rank()
			# p=comm.Get_size()
			# for i in range(len(nameImage)):
			# Encrypt(nameImage[my_rank],message[my_rank],my_rank)
			# Writing the broken messges into a file called message
			f = open("messages", "w")
			for i in range(len(message)):
				f.write(message[i])
				f.write("\n")
			f.close()
			# Writing the contents of nameImage into nameImage file
			f=open("nameImage","w")
			for i in range(len(nameImage)):
				f.write(nameImage[i])
				f.write("\n")
			f.close()

			print("Calling the mpi")
			# Now we need to call the mpirun command from here
			startTime = time.time()
			os.system("mpirun -np " + str(number) + " --hostfile machinefile python3 encryptMPI.py")
			endTime=time.time()
			print("Time taken for encryption:",endTime-startTime)
			f1.write("Processes:" + str(number) + " time=" + str(endTime-startTime) + "\n")
		f1.close()


if __name__=="__main__":
	main()
