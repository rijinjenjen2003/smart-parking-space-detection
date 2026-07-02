import streamlit as st
import cv2
import pickle
import numpy as np

st.title("Smart Parking Space Detection")

uploaded_file = st.file_uploader("Upload Parking Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    with open("position.pkl", "rb") as file:
        positions = pickle.load(file)

    free = 0

    for pos in positions:

        x,y=pos
        slot=image[y:y+180,x:x+100]
        gray=cv2.cvtColor(slot,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(gray,(3,3),1)
        _,threshold=cv2.threshold(blur,80,255,cv2.THRESH_BINARY)
        kernal=np.ones((3,3),np.uint8)
        dilate=cv2.dilate(threshold,kernal,iterations=2)
        white=cv2.countNonZero(dilate)
        print("White Pixels:", white)
        if white>100:
            color=(0,0,255)
        else:
            color=(0,255,0)
        free+=1
        cv2.rectangle(
        image,
        (x,y),
        (x+100,y+180),
        color,
        2
    )
    total = len(positions)

    cv2.putText(
        image,
        f"Free: {free}/{total}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )
    st.image(
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
        caption="Parking Detection Result"
    )