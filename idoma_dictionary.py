# pip install streamlit

import streamlit as st

english_to_idoma = {
    "hello": "alekwu",
    "goodbye": "uno",
    "thank you": "onya",
    "please": "mo",
    "sorry": "maa",
    "water": "ama",
    "food": "uwu",
    "house": "oga",
    "child": "oma",
    "man": "omaja",
    "woman": "omakwu",
    "father": "ada",
    "mother": "ene",
    "friend": "ocha",
    "day": "efe",
    "night": "ochichi",
    "sun": "efe",
    "moon": "Ogwo",
    "star": "igaga",
    "earth": "ala"
}

def main():
    st.title("English - Idoma Dictionary")

    # Sidebar for options (optional, but good practice)
    option = st.sidebar.selectbox("Choose an action:", ["Translate", "About"])

    if option == "Translate":
        st.header("Translate English to Idoma")
        english_word = st.text_input("Enter the English word:")

        if english_word:
            english_word = english_word.lower()
            if english_word in english_to_idoma:
                idoma_word = english_to_idoma[english_word]
                st.success(f"The Idoma translation of '{english_word}' is '{idoma_word}'")
            else:
                st.error(f"'{english_word}' is not found in the dictionary.")

    elif option == "About":
        st.header("About this Dictionary")
        st.write("This is a simple English-Idoma dictionary built with Streamlit.")
        st.write("It currently contains a limited vocabulary, but you can extend it by modifying the `english_to_idoma` dictionary in the code.")


if __name__ == "__main__":
    main()
# streamlit run dataviz_idoma.py 
