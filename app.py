import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "If your symptoms persist, please consult doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule appointment with the doctor?"
    elif "dosage" in user_input:
        return "It is necessary to take medicines as per the doctor's prescription. If you are not clear about the dosage please contact your doctor."
    elif "pain" in user_input:
        return "Using painkillers to relieve from pain is not suggested as they cause side effects. If you feel much pain consult your doctor."
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor."
    else:
        response = chatbot(user_input, max_length = 100, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User: ",user_input)
            with st.spinner("Processing your query, Please wait...."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ",response)
        else:
            st.write("Please enter a message to get a response")

if __name__ == "__main__":
    main()