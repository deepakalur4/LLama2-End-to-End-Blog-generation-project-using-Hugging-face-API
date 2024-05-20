import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub

from dotenv import load_dotenv
load_dotenv()
# Fucntion to get response from LLama 2 model
def get_Llama_response(input_text,no_words,blog_style):
    ## LLama 2 model
    llm_huggingface=HuggingFaceHub(repo_id="TheBloke/Llama-2-7B-Chat-GGML",model_kwargs={"temperature":0.6,"max_length":64})

    #Prompttemplate
    template='''
    Write a blog for the {blog_style} job profile for the topic {input_text} 
    within {no_words} words
    '''
    prompt=PromptTemplate(input_variables=["blog_style","input_text","no_words"],
    template=template
    )

    # Generate the response from LLAM2 model
    response=llm_huggingface(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response



st.set_page_config(page_title="Generate blogs",layout="centered",initial_sidebar_state="collapsed")
st.header("Generate Blogs")

input_text=st.text_input("Enter the blog topic")


# Creating 2 more columns for additional 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input("No of words")
with col2:
    blog_style=st.selectbox("writing the blog for: ",("Researchers","Data scientiests","Common people"),index=0)

submit=st.button("Generate")

## Final response

if submit:
    st.write(get_Llama_response(input_text,no_words,blog_style))
