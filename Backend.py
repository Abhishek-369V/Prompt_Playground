from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_prompt(role, task, constraints, length, query):
    prompt = f'''
                 You are acting as: 
                 {role}, 
                 task:{task}, 
                 user_request:{query}, 
                 rules/constraints:{constraints}, 
                 response_length:{length},
                 Generate response using the above template, 
                 Goal:Students should observe: Changing prompt -> Changing output.
              '''
    if not role or not task or not constraints or not length or not query:
        return f"Plz fill all the above details!..."
    try:   
        response = client.chat.completions.create(
            model = 'gpt-4o-mini',
            messages = [{"role": "user", "content": prompt}],
            temperature = 0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"
    