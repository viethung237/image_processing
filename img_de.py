import cv2
import aes_function
import img_func
key = '0f1571c947d9e8590cb7add6af7f6798'
key = key.upper()
import numpy as np
#show anh & chia anh
img = cv2.imread('tiger-jpg.jpg',1)
red = img[:,:,2]
green = img[:,:,1]
blue  = img[:,:,0]
print(red)
print(green)
print(blue)
cv2.waitKey(0)
#test red image
#cv2.imshow('original',red)
r_lst ='' #luu chuoi hexa cua anh
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r_lst += aes_function.bintohex(np.binary_repr(red[i][j],width = 8))#tra ve chuoi hexa
#encryption
cipher_r =[]
count = ''#gia tri padding
cipher_r,count = img_func.en_img_c(r_lst)
e_img_r = (np.array([int(i) for i in cipher_r],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])

#decryption
d_lst=''
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        d_lst += aes_function.bintohex(np.binary_repr(e_img_r[i][j],width = 8))
d_cipher =[]
d_cipher = img_func.de_img(d_lst,count)
d_img_r = (np.array([int(i) for i in d_cipher],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
cv2.imshow('decrypt ',cv2.normalize(d_img_r,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.waitKey(0)