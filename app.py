import streamlit as st
import cv2
import numpy as np
from PIL import Image
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh= mp.solutions.face_mesh
model_face_mesh = mp_face_mesh.FaceMesh()

st.title("OpenCv Operations")
st.subheader("Image Operations")
st.write("This program is written to perform various operation on OpenCv")

add_select_sidebar = st.sidebar.selectbox("What operation would you like to perform? ",
                                          ("About","Gray Scale", "Blue", "Green", "Red", "Meshing"))
if add_select_sidebar == "About":
    st.write("This application is a demo for streamlit")
elif add_select_sidebar == "Gray Scale":
    image_file_path = st.sidebar.file_uploader("Upload file")
    if image_file_path is not None:
        image = np.array(Image.open(image_file_path))
        st.sidebar.image(image)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        st.image(gray_image)
elif add_select_sidebar == "Blue":
    image_file_path = st.sidebar.file_uploader("Upload Image")
    if image_file_path is not None:
        image = np.array(Image.open(image_file_path))
        st.sidebar.image(image)
        zeros = np.zeros(image.shape[:2], dtype = "uint8")
        r, g, b = cv2.split(image)
        blue_image = cv2.merge([zeros, zeros, b])
        st.image(blue_image)
elif add_select_sidebar == "Green":
    image_file_path = st.sidebar.file_uploader("Upload Image")
    if image_file_path is not None:
        image = np.array(Image.open(image_file_path))
        st.sidebar.image(image)
        zeros = np.zeros(image.shape[:2], dtype = "uint8")
        r, g, b = cv2.split(image)
        green_image = cv2.merge([zeros, g, zeros])
        st.image(green_image)
elif add_select_sidebar == "Red":
    image_file_path = st.sidebar.file_uploader("Upload Image")
    if image_file_path is not None:
        image = np.array(Image.open(image_file_path))
        st.sidebar.image(image)
        zeros = np.zeros(image.shape[:2], dtype = "uint8")
        r, g, b = cv2.split(image)
        red_image = cv2.merge([r, zeros, zeros])
        st.image(red_image)
elif add_select_sidebar == "Meshing":
    image_file_path = st.sidebar.file_uploader("Upload file")
    if image_file_path is not None:
        image = np.array(Image.open(image_file_path))
        st.sidebar.image(image)
        results = model_face_mesh.process(image)
        for landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(image, landmarks)
            st.image(image)




