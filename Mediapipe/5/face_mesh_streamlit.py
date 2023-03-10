import cv2
import streamlit as st
import mediapipe as mp
import cv2 as cv
import numpy as np
import tempfile
import time
from PIL import Image



# Basic App Scaffolding
st.title('Face Mesh App using Streamlit')

## Add Sidebar and Main Window style
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 350px
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 350px
        margin-left: -350px
    }
    </style>
    """,
    unsafe_allow_html=True,
)

## Create Sidebar
st.sidebar.title('FaceMesh Sidebar')
st.sidebar.subheader('Parameter')




# Resize Images to fit Container
@st.cache()
# Get Image Dimensions
def image_resize(image, width=None, height=None, inter=cv.INTER_AREA):

    dim = None
    # grab the image size
    (h,w) = image.shape[:2]

    if width is None and height is None:
        return image
    
    if width is None:
        r = width/float(w)
        dim = (int(w*r),height)
    
    else:
        r = width/float(w)
        dim = width, int(h*r)

    # Resize image
    resized = cv.resize(image,dim,interpolation=inter)

    return resized





max_faces = st.sidebar.number_input('Maximum Number of Faces', value=5, min_value=1)
st.sidebar.markdown('---')
detection_confidence = st.sidebar.slider('Min Detection Confidence', min_value=0.0,max_value=1.0,value=0.5)
tracking_confidence = st.sidebar.slider('Min Tracking Confidence', min_value=0.0,max_value=1.0,value=0.5)
st.sidebar.markdown('---')

stframe = st.empty()

video = cv.VideoCapture(0)


width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
fps_input = int(video.get(cv.CAP_PROP_FPS))
fps = 0
i = 0

drawing_spec = mp.solutions.drawing_utils.DrawingSpec(thickness=2, circle_radius=1)

kpil, kpil2, kpil3 = st.columns(3)

with kpil:
    st.markdown('**Frame Rate**')
    kpil_text = st.markdown('0')

with kpil2:
    st.markdown('**Detected Faces**')
    kpil2_text = st.markdown('0')

with kpil3:
    st.markdown('**Image Resolution**')
    kpil3_text = st.markdown('0')

st.markdown('<hr/>', unsafe_allow_html=True)


## Face Mesh
with mp.solutions.face_mesh.FaceMesh(
    max_num_faces=max_faces,
    min_detection_confidence=detection_confidence,
    min_tracking_confidence=tracking_confidence

) as face_mesh:

        prevTime = 0

        while video.isOpened():
            i +=1
            ret, frame = video.read()
            if not ret:
                continue

            results = face_mesh.process(frame)
            frame.flags.writeable = True

            face_count = 0
            if results.multi_face_landmarks:

                #Face Landmark Drawing
                for face_landmarks in results.multi_face_landmarks:
                    face_count += 1

                    mp.solutions.drawing_utils.draw_landmarks(
                        image=frame,
                        landmark_list=face_landmarks,
                        connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
                        landmark_drawing_spec=drawing_spec,
                        connection_drawing_spec=drawing_spec
                    )

            # FPS Counter
            currTime = time.time()
            fps = 1/(currTime - prevTime)
            prevTime = currTime

            # Dashboard
            kpil_text.write(f"<h1 style='text-align: center; color:red;'>{int(fps)}</h1>", unsafe_allow_html=True)
            kpil2_text.write(f"<h1 style='text-align: center; color:red;'>{face_count}</h1>", unsafe_allow_html=True)
            kpil3_text.write(f"<h1 style='text-align: center; color:red;'>{width*height}</h1>",
                                unsafe_allow_html=True)

            frame = cv.resize(frame,(0,0), fx=0.8, fy=0.8)
            frame = image_resize(image=frame, width=640)
            stframe.image(frame,channels='BGR', use_column_width=True)

