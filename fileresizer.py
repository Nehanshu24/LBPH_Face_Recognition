# import required module
import cv2
import os

# assign directory
path = r"C:\Users\nehan\Documents\Mega Sync\VJTI\Sum Pro\LBPH\test-data"
path1 = r"C:\Users\nehan\Documents\Mega Sync\VJTI\Sum Pro\LBPH\training-data\s2"
path2 = r"C:\Users\nehan\Documents\Mega Sync\VJTI\Sum Pro\LBPH\training-data\s3"
path4 = r"C:\Users\nehan\Documents\Mega Sync\VJTI\Sum Pro\LBPH\training-data"
filen = len(os.listdir(path))
ls = [i for i in range(filen)]

reso = (350,400)
#for i in range(filen):
#for fileName in os.listdir(path):
filepath = os.path.join(path,"1.jpeg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("1.jpg",ffn)

filepath = os.path.join(path,"2.jpeg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("2.jpg",ffn)

filepath = os.path.join(path,"3.jpeg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("3.jpg",ffn)

filepath = os.path.join(path,"4.jpeg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("4.jpg",ffn)
