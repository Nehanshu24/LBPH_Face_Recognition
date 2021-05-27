# import required module
import cv2
import os

# assign directory
path = r"C:\Users\nehan\Documents\Mega Sync\VJTI\Sum Pro\LBPH\training-data\s1"
path1 = r"C:\Users\nehan\Documents\Mega Sync\VJTI\Sum Pro\LBPH\training-data\s2"
path2 = r"C:\Users\nehan\Documents\Mega Sync\VJTI\Sum Pro\LBPH\training-data\s3"
path4 = r"C:\Users\nehan\Documents\Mega Sync\VJTI\Sum Pro\LBPH\training-data"
filen = len(os.listdir(path))
ls = [i for i in range(filen)]

reso = (350,400)
#for i in range(filen):
#for fileName in os.listdir(path):
filepath = os.path.join(path,"1.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("1.jpg",ffn)

filepath = os.path.join(path,"2.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("2.jpg",ffn)

filepath = os.path.join(path,"3.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("3.jpg",ffn)

filepath = os.path.join(path,"4.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("4.jpg",ffn)

filepath = os.path.join(path,"5.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("5.jpg",ffn)

filepath = os.path.join(path,"6.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("6.jpg",ffn)

filepath = os.path.join(path,"7.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("7.jpg",ffn)

filepath = os.path.join(path,"8.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("8.jpg",ffn)

filepath = os.path.join(path,"9.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("9.jpg",ffn)

filepath = os.path.join(path,"10.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("10.jpg",ffn)

filepath = os.path.join(path,"11.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("11.jpg",ffn)

filepath = os.path.join(path,"12.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("12.jpg",ffn)

filepath = os.path.join(path,"13.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("13.jpg",ffn)

filepath = os.path.join(path,"14.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("14.jpg",ffn)

filepath = os.path.join(path,"15.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("15.jpg",ffn)

filepath = os.path.join(path,"16.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("16.jpg",ffn)

filepath = os.path.join(path,"17.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("17.jpg",ffn)

filepath = os.path.join(path,"18.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("18.jpg",ffn)

filepath = os.path.join(path,"19.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("19.jpg",ffn)

filepath = os.path.join(path,"20.jpg")
fn = cv2.imread(filepath)
ffn = cv2.resize(fn,reso)
cv2.imwrite("20.jpg",ffn)