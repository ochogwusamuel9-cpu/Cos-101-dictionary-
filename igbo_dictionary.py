import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Igbo Dictionary", page_icon="🇳🇬")

# --- DATA INITIALIZATION ---
# Using session_state allows the dictionary to persist during the browser session
if 'igbo_dict' not in st.session_state:
    st.session_state.igbo_dict = {
        "day": "ụbọchị", "night": "abali", "water": "mmiri",
        "fire": "ọkụ", "earth": "ụwa", "tree": "osisi",
        "sun": "anwụ", "moon": "ọnwa", "star": "kpakpando",
        "river": "osimiri", "stone": "nkume", "mountain": "ugwu",
        "goodbye": "ka o di", "thankyou": "daalu", "light": "ụlọ",
        "darkness": "ọchịchịrị", "sky": "eluigwe", "wind": "ikuku",
        "leaf": "akwụkwọ", "fruit": "mkpọka"
    }

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Dictionary Menu")
choice = st.sidebar.radio("Select an Option:", 
    ["Look up a word", "Show all words", "Add a new word", "Sentence Translator"])

# --- MAIN INTERFACE ---
st.title("🇳🇬 English to Igbo Dictionary")
st.write(f"This dictionary contains **{len(st.session_state.igbo_dict)}** words.")

# --- OPTION 1: LOOK UP A WORD ---
if choice == "Look up a word":
    st.header("🔍 Word Lookup")
    word = st.text_input("Enter an English word:").strip().lower()
    
    if word:
        if word in st.session_state.igbo_dict:
            translation = st.session_state.igbo_dict[word]
            st.success(f"**{word.capitalize()}** in Igbo is: **{translation}**")
        else:
            st.error(f"'{word}' is not in the dictionary.")
            # Suggestion logic
            suggestions = [w for w in st.session_state.igbo_dict.keys() if word in w]
            if suggestions:
                st.info(f"Did you mean: {', '.join(suggestions)}?")

# --- OPTION 2: SHOW ALL WORDS ---
elif choice == "Show all words":
    st.header("📚 Full Dictionary")
    # Convert to list of dicts for a clean Streamlit table
    full_list = [{"English": k, "Igbo": v} for k, v in sorted(st.session_state.igbo_dict.items())]
    st.table(full_list)

# --- OPTION 3: ADD A NEW WORD ---
elif choice == "Add a new word":
    st.header("➕ Add New Entry")
    new_eng = st.text_input("English Word:").strip().lower()
    new_igbo = st.text_input("Igbo Translation:").strip()
    
    if st.button("Save to Dictionary"):
        if new_eng and new_igbo:
            st.session_state.igbo_dict[new_eng] = new_igbo
            st.success(f"Successfully added: **{new_eng}** → **{new_igbo}**")
        else:
            st.warning("Please fill in both fields.")

# --- OPTION 4: SENTENCE TRANSLATOR ---
elif choice == "Sentence Translator":
    st.header("📝 Sentence Translator")
    st.caption("Translates English sentences word-by-word.")
    sentence = st.text_area("Enter English sentence:").strip().lower()
    
    if st.button("Translate Sentence"):
        if sentence:
            words_in_sentence = sentence.split()
            st.write("### Translation:")
            
            # Create a display loop
            for w in words_in_sentence:
                clean_w = w.strip(".,!?;:")
                if clean_w in st.session_state.igbo_dict:
                    st.write(f"**{w}**: {st.session_state.igbo_dict[clean_w]}")
                else:
                    st.write(f"**{w}**: _[Translation not found]_")
        else:
            st.warning("Please enter a sentence first.")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.button("Exit Session", on_click=lambda: st.write("Goodbye! Ka o di!"))