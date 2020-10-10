import streamlit as st
import os
import PIL
import cv2


def write():
  st.set_option('deprecation.showfileUploaderEncoding', False)
  st.title("Fracture Tooth Detection By A.Adithya Sherwood IX-E")
  st.subheader('Disclaimer: Please check with your local specialized dentist, if you are in doubt please try atleast twice.')
  uploaded_file = st.file_uploader("Choose an image", type="jpg")

  if uploaded_file is not None:
      image = PIL.Image.open(uploaded_file)
      image = image.resize((416,416))
      image.save('./Test.jpg')
      st.image(image, caption='Uploaded Image.', use_column_width=True)
      st.write("")
      os.system("python detect.py --weights weights/best.pt --img 416 --conf 0.5 --source ./Test.jpg")
      image_pred = PIL.Image.open('./inference/output/Test.jpg')
      st.image(image_pred, caption='Predictions.', use_column_width=True)