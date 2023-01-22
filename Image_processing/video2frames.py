# Program To Read video
# and Extract Frames
import cv2
from multiprocessing import Pool

import os

similarFolderName = 0
# Function to extract frames


def FrameCapture(path):

    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1
    success, image = vidObj.read()
    folderName = path.split('/')[-1][:-4]
    path = f"/home/pradeep/Documents/FPI_honeywell/FPI-Skyharbor/Frames/{folderName}"

    os.mkdir(path)

    saveFrameCount = 0

    while success:
        success, image = vidObj.read()
        if count % 30 == 0:
            # vidObj object calls read
            # function extract frames

            # Saves the frames with frame-count
<<<<<<< Updated upstream
=======
            frameDir = f"{writeDir}/Frame{saveFrameCount}"
            if not os.path.exists(frameDir):
                os.mkdir(frameDir)
            frameName = f"{videoName}_Frame{saveFrameCount}.jpg"

            framePath = f"{frameDir}/{frameName}"
            cv2.imwrite(framePath, image)

            frame2patch(framePath)
            cv2.imwrite(f"{writeDir}/{videoName}_Frame{saveFrameCount}.jpg", image)
>>>>>>> Stashed changes

            cv2.imwrite(
                f"/home/pradeep/Documents/FPI_honeywell/FPI-Skyharbor/Frames/{folderName}/frame_{saveFrameCount}.jpg", image)
            saveFrameCount += 1
            print(saveFrameCount)

        count = count + 1


# Driver Code
if __name__ == '__main__':

    pass
    # Calling the function
<<<<<<< Updated upstream
    videos = ["/home/pradeep/Downloads/3826138-3/220610130844_HONEYWELL_(1).WMV", "/home/pradeep/Downloads/3827320-5/220628122630_HONEYWELL_(1).WMV",
              "/home/pradeep/Downloads/3862699-3/220610100928_HONEYWELL_(1).WMV"]
    # for i in range(len(videos)):
    # 	FrameCapture(i)
=======
    videos = [
        "/home/pradeep/Documents/FPI-honeywell/FPI-Skyharbor/Videos/3035118-6/3035118-6/3035118-6_Vid_3.WMV"]
>>>>>>> Stashed changes

    pool = Pool(processes=8)
    pool.map(FrameCapture, videos)

    pool.close()
    print("success")
