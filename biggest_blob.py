'''
VERSION : 1.0
UPDATE : 1 SEPTEMBER 2023 
STAGE : POST-PROCESS 
PHASE : Pelvic Segmentation
INFO : Convert model generated body mask to applicable mask 
TASKS : rounds values to 0 and 1 - detects biggest blob on each slice - saves the biggest blob - removes holes
BUG : on leg slices , only one leg is masked 
INPUT CONDITIONS :  1) input array order must be at [number of slices , rows , columns]
                    2) input array values must be between 0 and 1 
                    3) input of the training set must be based on model 4 pre process data
'''
import numpy as np 
from skimage import measure
from scipy import ndimage
import os
import sys
from matplotlib import pyplot as plt

# USER INPUTS 
Input_NPY_Folder = "E:\\Dataset\\ct-body-mask-withCode\\store_all\\t\\Result"

Output_Folder = "E:\\Dataset\\ct-body-mask-withCode\\store_all\\t\\Result\\post_process_version"

if not(os.path.isdir(Output_Folder)) : os.mkdir(Output_Folder)

fileNames = os.listdir(Input_NPY_Folder)

for file in fileNames : 
    print('Proccessing file: ' + file)
    image = np.load(os.path.join(Input_NPY_Folder,file))
    image_copy = image.copy()
    # for index in range(image.shape[2]):
    for index in range(image.shape[0]):
        # label_image = measure.label(image[:,:,index], connectivity=1)
        # label_image = measure.label(np.round((image[index,:,:] + 1) / 2), connectivity=1)
        label_image = measure.label(np.round(image[index,:,:]), connectivity=1)
        num_blobs = np.max(label_image)
        regions = measure.regionprops(label_image)
        try:
            biggest_region = regions[np.argmax([region.area for region in regions])]
        except:
            print(index)
            plt.imshow(label_image)
            break
        # biggest_blob = image[:,:,index].copy()
        biggest_blob = image[index,:,:].copy()
        biggest_blob[label_image != biggest_region.label] = 0
        biggest_blob = ndimage.binary_fill_holes(biggest_blob)
        # image_copy[:,:,index] = biggest_blob
        image_copy[index,:,:] = biggest_blob
    # np.save(image_copy, os.path.join(Output_Folder, file))
    np.save(os.path.join(Output_Folder, file), image_copy)
    del image
        