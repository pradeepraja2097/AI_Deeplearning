import cv2
import glob
filenames=glob.glob("/home/pradeep/Pictures/test/*.png")
for i in filenames:
    a=i.split("/")[-1]

    img=cv2.imread(i)
    b=cv2.resize(img,(1600,256))
    cv2.imwrite(a,b)






