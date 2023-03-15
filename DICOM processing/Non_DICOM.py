import pydicom 
from PIL import Image
import numpy as np
import cbc
import binascii
#read somedata from dicom image
path = 'image-00000.dcm'
ds = pydicom.dcmread(path)
patient_name = ds.PatientName
patient_id = ds.PatientID
study_date = ds.StudyDate
modality = ds.Modality
###du lieu
data =str(patient_name) +'\n' + str(patient_id) + '\n' + str(study_date) + '\n' + str(modality)
key = b'Sixteen byte key'
iv = b'Sixteen byte iv.'
with open('user_data.txt','w',encoding = 'UTF-8') as data_file:
    data_file.write(data)
##########

#convert to non dicom
"""
def convert_dcm_jpg(name):
    
    im = pydicom.dcmread(name)

    im = im.pixel_array.astype(float)

    rescaled_image = (np.maximum(im,0)/im.max())*255 # float pixels
    final_image = np.uint8(rescaled_image) # integers pixels

    final_image = Image.fromarray(final_image)
    final_image.save('non_Dicom_image.jpg')

    return final_image
"""
'''
#steganography
def aes_enc(data,key,iv):
        
    data_bytes = data.encode('utf-8')
    cbc_mode = cbc.CbcMode(key,iv)
    data_to_image = cbc_mode.encrypt(data_bytes)
    data_hex = binascii.hexlify(data_to_image).decode('utf-8')
    return data_hex
    #giai ma aes

def aes_dec(data,key,iv):
    data2 = binascii.unhexlify(data)
    cbc_mode = cbc.CbcMode(key,iv)
    data_decrypt = cbc_mode.decrypt(data2)
    return data_decrypt.decode('utf-8')
'''
class Steganography:
    data_encrypted = '5ff47082583b40e22e17e1d28dd35910d3ecd4d16fd7e3908c550031dfb6adbd'
    def generate_Data(self,data):
        new_data = []
        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data
    def modifypix(self,pix,data_encrypted):
        datalist = self.generate_Data(data_encrypted)
        datalen = len(datalist)
        imgdata = iter(pix)
        for i in range(datalen):
            pix = [imgdata.__next__() + imgdata.__next__() + imgdata.__next__() + imgdata.__next__() + imgdata.__next__()
                   + imgdata.__next__()+imgdata.__next__() + imgdata.__next__()+imgdata.__next__()]
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1 

                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            #gia tri pixel cuoi dung de danh dau phan ket thuc cua ma dc an vao
            if (i == datalen - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1
            yield pix[:1]
            yield pix[1:2]
            yield pix[2:3]
            yield pix[3:4]
            yield pix[4:5]
            yield pix[5:6]
            yield pix[6:7]
            yield pix[7:8]
            yield pix[8:9]
    def hiding_data(self,img,)

