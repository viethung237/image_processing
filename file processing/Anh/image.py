import cv2
import aes_function
import numpy as np
img = cv2.imread('tiger.jpg')

red = img[:,:,2]
green = img[:,:,1]
blue  = img[:,:,0]
print(red)
print(green)
print(blue)
#new_img = cv2.merge(red,green,blue)
#cv2.imshow('',new_img)
cv2.waitKey(0)
#test red image
#cv2.imshow('original',red)
r_lst ='' #luu chuoi hexa cua anh
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r_lst += np.binary_repr(red[i][j],width = 8)#tra ve chuoi hexa

#test green image
g_lst=''
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        g_lst += np.binary_repr(green[i][j],width = 8)#tra ve chuoi hexa
#test blue image
b_lst =''
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b_lst += np.binary_repr(blue[i][j],width = 8)#tra ve chuoi hexa

color_lst = []
for i in range(0,len(r_lst),8):
    color_lst.append(r_lst[i:i+8] + g_lst[i:i+8] + b_lst[i:i+8])
bin_str =''
for i in color_lst:
    bin_str += i


with open('File chua gia tri chuyen doi.txt','w',encoding = 'UTF-8') as changetext:
    changetext.write(bin_str)


