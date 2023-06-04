import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfFileReader, PdfFileWriter,PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import pickle

#sidebar contents

with st.sidebar:
    st.title('VK pdf LLM chat APP')
    st.markdown('''
    ## About:

    Main resource of the app is used to build:

    - [streamlit](https://streamlit.io/)
    - [Langchain](https://docs.langchain.com/docs/)
    - [OpenAI](https://openai.com/)
    
    ''')

    add_vertical_space(4)
    st.write('All about pdf based chatbot, created by VK')

def main():
    st.header("Chat with your pdf file")

    #upload a your pdf file
    pdf = st.file_uploader("Upload your PDF", type='pdf')
    st.write(pdf.name)

    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        text = ""
        for page in pdf_reader.pages:
            text+= page.extract_text()

        #langchain_textspliter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len
        )

        chunks = text_splitter.split_text(text=text)

        #embedding (Openai methods) 
        embeddings = OpenAIEmbeddings()

        #Store the chunks part in db (vector)
        vectorstore = FAISS.from_texts(chunks,embedding=embeddings)

        #store pdf name
        store_name = pdf.name[:-4]
        with open(f"{store_name}.pkl","wb") as f:
            pickle.dump(vectorstore,f)

            
        #st.write(chunks)

if __name__=="__main__":
    main()