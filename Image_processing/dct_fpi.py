import cv2
import numpy as np
from scipy.fft import dct, idct
import glob
import os
filenames = glob.glob("3035118-6_Vid_3_Moment_2.jpg")
filenames=sorted(filenames)
count=0
for im in filenames:

    image_file = str(im.split("/")[-1].split(".")[-2])
    #print(image_file)
    img1=cv2.imread(im)
    # img2=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
    img=(img1[:,:,0])/255.0

    #img = cv2.resize(img,(1024,512)) / 255.0    # 1 channel, grayscale!

    # PREPROCESSING

    # DCT OPERATION
    dct_img = dct(dct(img.T, norm="ortho", workers=4).T, norm="ortho", workers=4) * 255

    #dct=np.asarray(dct)
    # DCT VALUES > 100 , MAKE IT 0
    #print(np.max(imgcv1),np.min(imgcv1))

    dct_img[np.abs(dct_img) > 100.0]=0
    


    #print(np.max(dct),np.min(dct))
    #dct=np.asnumpy(dct)
    # # INVERSE-DCT
    idct_img = idct(idct(dct_img.T, norm="ortho", workers=4).T, norm="ortho", workers=4)

    idct_img = (idct_img - np.min(idct_img)) / (np.max(idct_img) - np.min(idct_img))

    # # print(np.max(idct),np.min(idct),np.mean(idct))
    # # IDCT VALUES < 0.75 , MAKE IT 0

    idct_img[np.abs(idct_img) < 0.70] = 0

    # # CONVERT BACK TO 0 TO 255 RANGE
    idct_img = np.uint8(idct_img * 255)
##################################################################################################additional added to the dct####################
    # (T, threshInv) = cv2.threshold(idct_img, 200, 255,
	# cv2.THRESH_BINARY_INV)
    # contours, hierarchy = cv2.findContours(image=threshInv, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    # selected_cnts = []
    # for c in contours:
    #     area = cv2.contourArea(c)
    # #if(area>200):
    #     selected_cnts.append(c)
    # aa=cv2.drawContours(idct_img, contours=selected_cnts, contourIdx=-1, color=(0, 0, 255), thickness=5, lineType=cv2.LINE_AA)

    final_img = np.concatenate((img, idct_img), axis=1)
    count=count+1
    print(count)
    #print(image_file)
    #cv2.imwrite("/home/pradeep/Documents/FPI_honeywell/FPI-Skyharbor/Crops/all/nondefected/{}_defectless.jpg".format(image_file),idct_img)
    #cv2.imwrite("/home/pradeep/Desktop/dct/frame11_dct.jpg",idct_img)
    a=cv2.resize(idct_img,(1024,512))
    cv2.imshow("test",a)
    cv2.waitKey(0)
    print(image_file)
