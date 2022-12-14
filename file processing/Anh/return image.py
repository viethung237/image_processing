import cv2
import aes_function
import numpy as np
with open('File chua gia tri chuyen doi.txt','r',encoding='UTF-8') as changetext, open('File chua gia tri tra ve.txt','w',encoding='UTF-8') as originaltext:
    pt = changetext.read()
    img = cv2.imread('tiger.jpg')

    #cv2.imshow('',img)
    r_lst =[]
    g_lst =[]
    b_lst =[]
    row,column = 599,900
    for i in range(0,len(pt),24):
        #r_lst.append(pt[i:i + 8])
        r_lst.append(aes_function.bintodec(int(pt[i:i+8])))
        g_lst.append(aes_function.bintodec(int(pt[i+8:i+16])))
        b_lst.append(aes_function.bintodec(int(pt[i+16:i+24])))

    e_img_r = (np.array([int(i) for i in r_lst], dtype=np.uint8)).reshape(img.shape[0],img.shape[1])
    e_img_g = (np.array([int(i) for i in g_lst], dtype=np.uint8)).reshape(img.shape[0],img.shape[1])
    e_img_b = (np.array([int(i) for i in b_lst], dtype=np.uint8)).reshape(img.shape[0],img.shape[1])

    # merge
    final = cv2.merge([e_img_b, e_img_g, e_img_r])
    print(final)
    cv2.imshow('return',final)
    #cv2.imshow('red',final)
    cv2.waitKey(0)