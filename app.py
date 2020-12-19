import streamlit as st
import torch
from transformers import pipeline

st.sidebar.title("© Harvinder Power")
st.sidebar.header("Text Generation")

x = "And what about you...?"

def textInput(x):
    dummy_text = x
    user_input = st.text_area("Text:", value=dummy_text)
    if st.button("Generate Text"):
        generateText(user_input)

def generateText(gen):
        gpt2 = pipeline('text-generation')
        x = gpt2(gen)[0]["generated_text"]
        x
        textInput(x)

textInput(x)