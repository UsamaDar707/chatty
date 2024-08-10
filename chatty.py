import streamlit as st
import google.generativeai as genai

# Initialize generative AI with your API key
key = "AIzaSyC7zYuESCXYAiFcu4LVwYLrey2tNppZbG0"
genai.configure(api_key=key)

# Initialize the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to generate response from user input
def generate_response(input_text):
    # Generate content using the model
    model_response = model.generate_content(input_text)
    return model_response.text

# Streamlit app
def main():
    st.title("ARONA Chat-BOT")
    st.write("Powered  by: PGC Sialkot")

    # Store the user input in Streamlit session state
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    
    # Function to handle input and generate response
    def on_enter():
        if st.session_state.user_input:
            # Generate and display the response
            response = generate_response(st.session_state.user_input)
            st.session_state.response = response

    # Input field for user prompt with on_change trigger
    st.text_input("Enter your Prompt:", key="user_input", on_change=on_enter)

    # Display the generated response if available
    if "response" in st.session_state:
        st.write("ARONA  Response:")
        st.write(st.session_state.response)

if __name__ == "__main__":
    main()
