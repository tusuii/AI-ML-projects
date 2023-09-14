import streamlit as st
import time

st.sidebar.title("this is great sidebar")

st.title("This is heading for stramlit App")
st.header("This is heading from streamlit App")
st.subheader("This is streamlit subheader")
st.latex(r'''\[E=mc^2\]''')
st.caption("this is sample caption")
st.markdown("""
* this is markdown
                 
    - level 1
    - level 2
* this is another markdown pointer
""")
st.write("Hello world")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/The_GIMP_icon_-_gnome.svg/800px-The_GIMP_icon_-_gnome.svg.png")
checkbox = st.checkbox("I Am Agree")
button = st.button("click me")
if checkbox :
    st.write("you clicked on a checkbox")

if button:
    st.write(f"1 + 1 = {1+1}")

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['mercury','venus','earth','pluto','Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['1 good', '2', '3','4','5 Excellent'])
st.slider('Pick a number', 0,255)


st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.balloons()

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)

with st.spinner('Wait for it...'):
    time.sleep(3)


st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

import matplotlib.pyplot as plt
import numpy as np
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

