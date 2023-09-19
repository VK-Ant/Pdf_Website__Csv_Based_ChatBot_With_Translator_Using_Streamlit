# **PDF based ChatBot using OpenAI,LangChain (Streamlit)**

## **OBJECTIVE:**

1. The project's goal is to create a chatbot that can quickly summarise your books' contents.

## **Project Diagram**

![Product Roadmaps - Frame 2](https://github.com/VK-Ant/PDFBasedChatBot_Streamlit/assets/75832198/3d9761a6-be6f-4dec-8511-066f3e31f807)

![Product Roadmaps - Frame 3](https://github.com/VK-Ant/PDFBasedChatBot_Streamlit/assets/75832198/bea758e3-56d0-4e3e-b63f-84530c926b17)


## **STEPS TO FOLLOW IN THIS PROJECT:**

### **1. Git clone and change directory**

```bash
$ git clone https://github.com/VK-Ant/AttendanceSystem-JetsonAGX.git](https://github.com/VK-Ant/BookBasedChatBot_Streamlit
$ cd pdfchatbot_streamlit
```
Make sure the path is correct.

### **2. Install prerequisite library using requirement file**

```bash

$ pip3 install -r requirements.txt

```
Check that OpenAI,langchain,streamlit,PyPDF2, and datetime are installed on yourdevice (Packages).

### **3.Add your project folder to the.env folder you created (put your openai api key)**

'''bash
OPENAI_API_KEY = your openai api key
'''

### **4. Finally run the code**

```bash

$ bash run.sh

or

$ streamlit run VK_BookBasedChatbot.py

```
![Screenshot from 2023-06-04 18-26-26](https://github.com/VK-Ant/BookBasedChatBot_Streamlit/assets/75832198/a2b2303b-a0e0-4bbb-b167-86cc6e29a548)


### **5. if you want pdf based chatbot with translator try this code**


```bash

$ streamlit run translate.py

```


![Screenshot from 2023-09-19 14-33-37](https://github.com/VK-Ant/PDFBasedChatBot_Streamlit/assets/75832198/9d5f2dfb-8fde-47b6-964d-e89f022fd02e)


## **PROJECT DESCRIPTION:**

1. Install requirement file.

2. .Add your project folder to the.env folder you created (put your openai api).

3. Run the main file

4. Upload your pdf and summarize the main content of pdf

5. And the translate feature in the chatbot


### **THANK YOU & CREDIT**

1. https://youtu.be/RIWbalZ7sTo
2. Streamlit, Langchain, OpenAI community
3. googletrans (library)
4. venkatesan (My colleague)


## **🤗Happy learning🤗**
