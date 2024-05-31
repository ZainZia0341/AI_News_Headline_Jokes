import streamlit as st
import App
import json
import os

# response_content = ""

st.set_page_config(page_title="AI Joke", layout="wide")

col1, col2, col3 = st.columns(3)

with col1:
        st.subheader("News Article Content")
        prompt_text = st.text_area("Enter News article here", height=350)
        process_button = st.button("Run", type="primary")

with col2:
        if process_button:
            with st.spinner("Running..."):
                st.session_state.response_content = App.get_llm_body(prompt_text=prompt_text)
                st.write(st.session_state.response_content)

response_content = st.session_state.response_content

with col3:
        review_text = st.text_area("Enter your feedback about the joke", height=200)
        review_button = st.button("Submit", type="primary")
        if review_button:
            with st.spinner("saving response"):
                if os.path.exists('responses.json'):
                    with open('responses.json', 'r') as file:
                        data = json.load(file)
                else:
                    data = []
                # Append the new prompt-response pair
                data.append({
                    "prompt": prompt_text,
                    "response": response_content,
                    "review": review_text
                })
                # Save the updated data back to the file
                with open('responses.json', 'w') as file:
                    json.dump(data, file)
                    st.success("Prompt, response and review saved locally in responses.json")