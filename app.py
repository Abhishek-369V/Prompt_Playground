from Backend import generate_prompt
import streamlit as st

st.set_page_config(
    page_title= "Prompt Playground"
)

st.title("Prompt Playground")
st.caption("Provide the specific details to understand about prompts and there responses!")

role = st.selectbox("Select Role:", ["Teacher","Interviewer","Technical Writer","Friendly Assistant"])
task = st.selectbox("Select Task:", ["Explain","Summarize","Generate","Rewrite"])
constraints = st.selectbox("Select Constraints:", ["Simple Language","Bullet Points","Examples","Professional Tone"])
length = st.selectbox("Select Output_length:", ["Short/precise","Medium","Detailed","Friendly Assistant",])
query = st.text_area("Enter your query here:")

if st.button("Generate"):
    if not role or not task or not constraints or not length or not query:
        st.warning("Plz provide the requirements above!")
    else:
        output = generate_prompt(role, task, constraints, length, query)
        st.subheader("Generated Prompt")
        Constructed_Prompt = st.write(f"You are acting as: {role}, task:{task}, user_request:{query}, rules/constraints:{constraints}, response_length:{length},Generate response.")
        st.subheader("AI Response")
        st.write(output)