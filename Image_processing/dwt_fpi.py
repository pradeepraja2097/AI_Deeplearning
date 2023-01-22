# import numpy as np
# import pywt
# import pywt.data
# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt


# img=mpimg.imread ("/home/pradeep/Downloads/3862699-3/3862699-3_closed_iris_screenshot_2.PNG")
# img=img[:,:,1]

# c=pywt.wavedec2(img,'haar',mode="periodization",level=2)
# imgr=pywt.waverec2(c,'haar',mode="periodization")

# imgr=np.uint8(imgr)

# cA2=c[0]
# (cH1,cV1,cD1)=c[-1]
# (cH2,cV2,cD2)=c[-2]


import numpy as np

import pywt

import pywt.data

import matplotlib.image as mpimg

import matplotlib.pyplot as plt
import cv2




img=cv2.imread("/home/pradeep/Downloads/w256a.bmp")

img=img[:,:,1]



c=pywt.wavedec2(img,'coif5',mode="periodization",level=2)





#print(c)
# c=np.uint8(c)


imgr=pywt.waverec2(c,'coif5',mode="periodization")



imgr=np.uint8(imgr)



cA2=c[0]

(cH1,cV1,cD1)=c[-1]

(cH2,cV2,cD2)=c[-2]






cv2.imshow("ca2",cA2)


cv2.imshow("cV2",cV2)
# cv2.imshow("cD2",cD2)
#cv2.imshow("cH2",cH2)
# cv2.waitKey(0)
cv2.imshow("imgr",imgr)
cv2.waitKey(0) 

# arr,coeff_slices=pywt.coeffs_to_array(c)
# print(coeff_slices)

# cv2.imshow("test",arr)
# cv2.waitKey(0)



# import numpy as np

# import pywt

# import pywt.data

# import matplotlib.image as mpimg

# import matplotlib.pyplot as plt
# import cv2




# img=cv2.imread("/home/pradeep/Documents/FPI_honeywell/FPI-Skyharbor/Crops/all/defected/frame_0_defect.jpg")
# img=cv2.resize(img,(1600,800))
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img=img[:,:,1]

# coeffs=pywt.wavedecn(img,'haar',mode='symmetric',level=1)



# arr,coeff_slices=pywt.coeffs_to_array(coeffs)
# print(arr.shape)
# print(np.unique(arr))




# # arr=np.uint8(arr)
# # print(arr)

# arr[np.abs(arr)<300]=0
# # print(np.unique(arr))
# # print(arr)



# coeffs_from_array=pywt.array_to_coeffs(arr,coeff_slices,output_format="wavedecn")



# img_out=pywt.waverecn(coeffs_from_array,'haar',mode="symmetric")
# print(np.unique(img_out))
# img_out[np.abs(img_out)<230]=0
# cv2.imwrite("img.png",img_out)
# cv2.imshow("test",img_out)
# cv2.waitKey(0)





# c=pywt.wavedec2(img,'db1',mode="periodization",level=2)
# print(c)
# # print(len(c[]))
# # c=np.uint8(c)
# # print(c.shape)
# imgr=pywt.waverec2(c,'db1',mode="periodization")
#
#
#
# imgr=np.uint8(imgr)
#
#
#
# cA2=c[0]
#
# (cH1,cV1,cD1)=c[-1]
#
# (cH2,cV2,cD2)=c[-2]
#
#
#
#
#
#
# cv2.imwrite("ca2.png",cA2)
#
#
# cv2.imwrite("cV2.png",cV2)
# cv2.imwrite("cD2.png",cD2)
# cv2.imwrite("cH2.png",cH2)
# arr,coeff_slices=pywt.coeffs_to_array(c)