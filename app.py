import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import easyocr
from PIL import Image
from PIL import ImageDraw


st.title('IDENTIFY THE TEXT FROM AN IMAGE')
image_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])

try:


    def load_image(image_file):
        img = Image.open(image_file)
        return img

    st.image(load_image(image_file), caption = 'UPLOADED IMAGE')



    images = load_image(image_file)

    reader = easyocr.Reader(['en'])

    output = reader.readtext(np.array(images), contrast_ths=0.07, adjust_contrast=0.9, add_margin=0.3, width_ths=0.9, decoder='beamsearch')

    def draw_boxes(image):
        draw = ImageDraw.Draw(image)
        for bound in output:
            p0, p1, p2, p3 = bound[0]
            draw.line([*p0,*p1,*p2,*p3,*p0], fill='red', width=8)
        return image
    st.image(draw_boxes(images), caption = 'TEXT-BOXES')


    final = [text[-2] for text in output]
    st.write('Extracted Texts: ', final)

except:
    pass



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: visible;}
            footer {visibility: hidden;}
            footer:after {
	            content:'Made by Nilavo Boral'; 
	            visibility: visible;
	            display: block;
	            position: relative;
	            #background-color: red;
	            padding: 5px;
	            top: 2px;
                color: tomato;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)