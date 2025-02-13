import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Importing a pre-trained model from hugging face
chatbot = pipeline("text-generation", model="distilgpt2")

# Define healthcare-specific response
def healthcare_chatbot(user_input):
    # Rule based response
    if "symptom" in user_input:
        return "If your symptoms persist, please consult doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule appointment with the doctor?"
    elif "dosage" in user_input:
        return "It is necessary to take medicines as per the doctor's prescription. If you are not clear about the dosage please contact your doctor."
    elif "pain" in user_input:
        return "Using painkillers to relieve from pain is not suggested as they cause side effects. If you feel much pain consult your doctor."
    elif "stomachpain" in user_input:
        return "Stomach pain can have various reasons like indigestion,gas,etc.\n 1.TAKE REST:Sit or lie down in a comfortable position to relax your abdominal muscles\n2.WARM COMPRESS:Place a heating pad or warm cloth on your stomach to ease the pain\n3.STAY HYDRATED:Sip on warm water herbal tea or clear fluids to stay hydrated and soothe your stomach"
    elif "headache" in user_input:
        return "Headache can be caused by various factors such as stress,dehydration,lack of sleep,etc..\nHere are few suggestions to help you:\n1.DRINK WATER:Dehydration is a common cause to the headache,so try sipping water./n2.TAKE A BREAK:Rest your eyes and mind\n3.APPLY A COOL COMPRESS:Place a cold cloth or an ice pack on your forehead or on back of your neck\n4.MASSAGE:Gently massage your temples,neck or the area wher you feel pain"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor."
    else:
        # Response by pre-trained model
        response = chatbot(user_input, max_length = 300, num_return_sequences=1)
        return response[0]['generated_text']

# Streamlit web app interface
def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")

    # Display chatbot response
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
