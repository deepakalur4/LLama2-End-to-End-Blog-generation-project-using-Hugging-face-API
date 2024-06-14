from langchain_community.llms import HuggingFaceHub,OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_model_response_for_blog(text,maximum_length,about):
    llm_model=HuggingFaceHub(repo_id="TheBloke/Llama-2-7B-Chat-GGML",model_kwargs={"max_length":maximum_length})
    prompting=PromptTemplate(input_variables=["maximum_length","about","text"],template=
                             f"Write a blog on {text} for a length of {maximum_length} and its for {about}"                           
                                                          )
    response=llm_model.predict(prompting.format(text=text, maximum_length=maximum_length, about=about))
    return response

# initialise streamlit app

st.set_page_config("Blog generation app")
st.header("Content-Type", "blog application")

input_text=st.text_input("Enter the blog topic")

col1,col2=st.columns([5,5])

with col1:
    about=st.selectbox("Bolg",("Data scientiest","normal people"),index=0)
with col2:
    maximum_length=st.text_input("maximum_length")


submit=st.button("Submit")

if submit:
    st.write(get_model_response_for_blog(text=input_text,about=about,maximum_length=maximum_length))

