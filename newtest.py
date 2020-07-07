from visual_cryptography import visual_cryptography
from PIL import Image
from numpy import array
from cryptography.fernet import Fernet
from Utils import Utils
from Population import Population
from Chromosome import Chromosome
from Fitness import Fitness
from GA import GA
from Ga_Encry import Encrypt
from Pit import Pit
import time
import image_slicer
import multiprocessing
#from abcd import Steganography
import math
from multiprocessing import Process

# Generate the names of the image slices from the tuple returned by image_slicer
def imageName(image_slices):
	names=[]
	for i in image_slices:
		a=str(i).split('-')
		b=a[1][1:len(a[1])-1]
		names.append(b)
	return names

# This is to break the image iSPICMACAY NITK presents Hindustani Vocal Concert by Pt. Rajnish Mishra and Pt. Ritesh Mishra on 26th Octoberr 2019 (Saturday) in SJA at 10 AMSPICMACAY NITK presents Hindustani Vocal Concert by Pt. Rajnish Mishra and Pt. Ritesh Mishra on 26th Octoberr 2019 (Saturday) in SJA at 10 AMSPICMACAY NITK presents Hindustani Vocal Concert by Pt. Rajnish Mishra and Pt. Ritesh Mishra on 26th Octoberr 2019 (Saturday) in SJA at 10 AMSPICMACAY NITK presents Hindustani Vocal Concert by Pt. Rajnish Mishra and Pt. Ritesh Mishra on 26th Octoberr 2019 (Saturday) in SJA at 10 AMnto multiple slices
def sliceImage(image,number):
	image_pieces=image_slicer.slice(name, number)
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

name='test.jpg'
number=4
image_slices=sliceImage(name,number)
complete_message="comlpetemessagage"
message=message_split(complete_message,number)
print("The split message is:",message)
nameImage=imageName(image_slices)
	
p1 = Process(target = Encrypt(nameImage[0],message[0],0))
p2 = Process(target = Encrypt(nameImage[1],message[1],1))
p3 = Process(target = Encrypt(nameImage[2],message[2],2))
p4 = Process(target = Encrypt(nameImage[3],message[3],3))

p1.start()
p2.start()
p3.start()
p4.start()
p1.join()
p2.join()
p3.join()
p4.join()