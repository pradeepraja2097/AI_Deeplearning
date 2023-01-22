import numpy as np
from patchify import patchify,unpatchify
import cv2
import glob

filenames=glob.glob("/home/pradeep/Downloads/train_orig/sticker_image_2021_12_30_0_1_18-3_3_8.png")

count=0
for i in filenames:
    name=i.split("/")[-1].split(".")[-2]
    image = cv2.imread(i,0)
    #image1= cv2.resize(image,(1024,512))
    

    patches = patchify(image, (128,128), step=128) 
    print(patches.shape)
    for i in range(patches.shape[0]):
        for j in range(patches.shape[1]):
            single_patch_img = patches[i, j, :,:]

            #flag=len(np.unique(single_patch_img))
            #if flag>1:
            cv2.imwrite("/home/pradeep/Desktop/test/image_{}_{}_{}.jpg".format(name,i,j),single_patch_img)
                #count+=1
        #reconstructed_image = unpatchify(patches, image.shape)
        #print("reconstructed_image")
        #reconstructed_image = unpatchify(patches, image.shape)
        #cv2.imshow("test",reconstructed_image)
        cv2.waitKey(0)

            
    print("new",count)






