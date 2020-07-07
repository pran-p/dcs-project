# This is to import the modules required for this module of code
from PIL import Image
import image_slicer
import multiprocessing
from dcba import Decryption
import math


# Generate the names of the image slices from the tuple returned by image_slicer

n = int(input("Enter the number of images slices: "))
plain_text = ""

for i in range(0,n):
	plain_text =plain_text + Decrpytion(i) + " "

print(plain_text)