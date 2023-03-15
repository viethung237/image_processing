import pydicom 
from PIL import Image
import numpy as np
#read somedata from dicom image
path = 'image-00000.dcm'
ds = pydicom.dcmread(path)
patient_name = ds.PatientName
patient_id = ds.PatientID
study_date = ds.StudyDate
modality = ds.Modality
data =str(patient_name) +'\n' + str(patient_id) + '\n' + str(study_date) + '\n' + str(modality)
with open('user_data.txt','w',encoding = 'UTF-8') as data_file:
    data_file.write(data)

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
#steganography