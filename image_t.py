import img_func
import cv2
import aes_function
key = '0f1571c947d9e8590cb7add6af7f6798'
key = key.upper()
import numpy as np
#show anh & chia anh
img = cv2.imread('tiger-jpg.jpg',1)
red = img[:,:,2]
green = img[:,:,1]
blue  = img[:,:,0]
#test red image
#cv2.imshow('original',red)
r_lst ='' #luu chuoi hexa cua anh
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r_lst += aes_function.bintohex(np.binary_repr(red[i][j],width = 8))#tra ve chuoi hexa
#test green image
g_lst=''
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        g_lst += aes_function.bintohex(np.binary_repr(green[i][j],width = 8))#tra ve chuoi hexa
#test blue image
b_lst =''
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b_lst += aes_function.bintohex(np.binary_repr(red[i][j],width = 8))#tra ve chuoi hexa
#list r g b
cipher_r =[]
cipher_g =[]
cipher_b =[]
#encrypt
cipher_r = img_func.en_img(r_lst)
cipher_g = img_func.en_img(g_lst)
cipher_b = img_func.en_img(b_lst)



e_img_r = (np.array([int(i) for i in cipher_r],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
e_img_g = (np.array([int(i) for i in cipher_g],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
e_img_b = (np.array([int(i) for i in cipher_b],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
#merge
final = cv2.merge([e_img_r,e_img_g,e_img_r])

print(final)
cv2.imshow('encrypt ',cv2.normalize(final,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.waitKey(0)