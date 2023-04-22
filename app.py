import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.write('Hello, World!')
    user_input = st.text_input("Enter your message", "")
    st.sidebar.text_input("Your message", value=user_input, key="message", max_chars=None, type="default", help=None)
    st.write("Chat history goes here...")

if __name__ == '__main__':
    main()