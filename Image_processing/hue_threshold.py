
import cv2
import numpy as np
import pandas as pd
import glob
import os
from multiprocessing import Pool

root = os.getcwd() + "/Frames"


def rescale(frame, scale=0.4):
    width, height = int(scale * frame.shape[1]), int(scale * frame.shape[0])

    dimension = (width, height)

    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)


def patchify(img, x, y, w, h, filepath):

    coords = f"{x},_{y}"
    # find the centroid of contour
    x, y = x + (w//2), y + (h//2)

    # specify the width & height of the required crop sized image from the centroid
    w, h = 256, 256

    #print(f"received {x1},{y1}, {x2}, {y2}")
    if x < w:
        # left side case overflow
        x = w
    elif x > (img.shape[1] - w):
        # right side case overflow
        x = img.shape[1] - w - 1

    if y < h:
        # top case overflow
        y = h
    elif y > (img.shape[0] - h):
        # bottom case overflow
        y = img.shape[0] - h - 1
        #y1 -= (y2 - img.shape[0])

    # print()

    # save the rles into csv file

    #rows.append([i,f"{x1},{y1}, {x2}, {y2}", f"{x1},{y1}, {x1+512}, {y1+512}",time])
    # write_to_csv(rows)

    # save the crop
    # name=i.split("/")[-1]
    #fname = name.split(".")[0]
    cropped = img[y-h: y+h, x-w: x+w]
    cv2.imwrite(filepath, cropped)


lower = np.array([36, 25, 25], dtype="uint8")
higher = np.array([75, 255, 255], dtype="uint8")

# filenames=glob.glob("/home/pradeep/Documents/FPI_honeywell/FPI-Skyharbor/Frames/3071770-4_Vid_1/*.jpg")
# filename=sorted(filenames)


def ReadFrames(dir):

    files = os.listdir(f"{root}/{dir}")
    print(files)

    #os.mkdir(f"Crops/{dir}")
    #os.mkdir(f"AnnotatedFrames/{dir}")

    for i in files:
        img = cv2.imread(f"{root}/{dir}/{i}")

        folder = i[:-4]
        os.mkdir(f"Crops/{dir}/{folder}")

        # print("img_shape ", img.shape)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, higher)
        # slice the green
        imask = mask > 0
        green = np.zeros_like(img, np.uint8)
        green[imask] = img[imask]

        kernel = np.ones((3, 3), np.uint8)
        dilate = cv2.dilate(green, kernel)

        aa, bb, cc = cv2.split(dilate)
        bmask = np.zeros(img.shape[:2], dtype=np.uint8)

        (T, threshInv) = cv2.threshold(bb, 200, 255, cv2.THRESH_BINARY)

        selected_cnts = []
        contours0, hierarchy = cv2.findContours(
            threshInv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours0:
            area = cv2.contourArea(c)
            if (area >= 100 and area <= 1500):

                selected_cnts.append(c)

        cv2.drawContours(bmask, selected_cnts, -1, 255, -1)
        # cv2.drawContours(img,selected_cnts, -1,(0, 25,255), -1)

        #cv2.putText(img, str(area), (int(x), int(y)-20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255),2)

        # masked=cv2.bitwise_and(img,img,mask=aaa)
        # c=cv2.resize(bbb,(1600,800))
        # d=cv2.resize(aaa,(1600,800))

        # cv2.imshow("CONTOURED",c)
        # cv2.imshow("MASKED",d)
        masked = cv2.bitwise_and(img, img, mask=bmask)

        #cv2.imwrite(f"AnnotatedFrames/{dir}/{i}", masked)

        

        cv2.imshow("masked", rescale(masked))
        cv2.waitKey(0)


if __name__ == "__main__":

    #FrameDirs = os.listdir(root)
    # FrameDirs = ["220628123748_HONEYWELL_(1)", ]
    FrameDirs="/home/pradeep/Documents/FPI-honeywell/FPI-Skyharbor/Videos/3035118-6/3035118-6/3035118-6_3035118-6-Vid-3/Frames"
    print(FrameDirs)
    pool = Pool(processes=8)
    pool.map(ReadFrames, FrameDirs)
    pool.close()
    print("success")
