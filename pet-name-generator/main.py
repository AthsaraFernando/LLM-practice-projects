import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")

user_animal_type = st.sidebar.selectbox("what is your per?",('cat','dog','hamster'))

if user_animal_type=='cat':
    pet_color = st.sidebar.text_area(label="what is your cat's color?", max_chars=15)

if user_animal_type=='dog':
    pet_color = st.sidebar.text_area(label="what is your dog's color?", max_chars=15)

if user_animal_type=='hamster':
    pet_color = st.sidebar.text_area(label="what is your hamster's color?", max_chars=15)
    
if pet_color:
    response = lch.generate_pet_name(user_animal_type, pet_color)
    st.text(response['pet_name'])