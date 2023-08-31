import numpy as np 
from skimage import measure
from scipy import ndimage
import os
import sys
from matplotlib import pyplot as plt

# USER INPUTS 
Input_NPY_Folder = "E:\\Dataset\\ct-body-mask-withCode\\store_all\\temp\\machine_generated"

Output_Folder = "E:\\Dataset\\ct-body-mask-withCode\\store_all\\temp\\postproccessed"

if not(os.path.isdir(Output_Folder)) : os.mkdir(Output_Folder)


fill = '#' 
empty = '-'

fileNames = os.listdir(Input_NPY_Folder)

counter = 0
for file in fileNames : 
    percent = counter / len(fileNames)
    counter += 1
    filled = int(20 * percent)
    bar = fill * filled + empty * (20 - filled)
    sys.stdout.write(f'\rProgress : |{bar}| {percent * 100:.1f}%')
    
    image = np.load(os.path.join(Input_NPY_Folder,file))
    image_copy = image.copy()
    # for index in range(image.shape[2]):
    for index in range(image.shape[0]):
        # label_image = measure.label(image[:,:,index], connectivity=1)
        label_image = measure.label(np.round((image[index,:,:] + 1) / 2), connectivity=1)
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
    sys.stdout.flush()
        