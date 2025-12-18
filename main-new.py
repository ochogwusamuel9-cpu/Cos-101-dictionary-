def english_to_igbo_dictionary():
    """
    A simple french to english dictionary with 20 words.
    Allows users to look up translations.
    """
    
    # Dictionary of 20 french words and their english translations
    english_igbo_dict = {
        "day": "ụbọchị", 
        "night": "abali", 
        "water": "mmiri",
        "fire": "ọkụ", 
        "earth": "ụwa",
        "tree": "osisi", 
        "sun": "anwụ",
        "moon": "ọnwa", 
        "star": "kpakpando",
        "river": "osimiri",
        "stone": "nkume",
        "mountain": "ugwu", 
        "goodbye": "ka o di", 
        "thankyou": "daalu",
        "light": "ụlọ",
        "darkness": "ọchịchịrị",
        "sky": "eluigwe",
        "wind": "ikuku",
        "leaf": "akwụkwọ",
        "fruit": "mkpọka",
        
    }
    
    print("=" * 50)
    print("ENGLISH TO IGBO DICTIONARY")
    print("=" * 50)
    print(f"This dictionary contains {len(english_igbo_dict)} words.")
    print("\nAvailable English words:")
    
    # Display available words in a neat format
    words = list(english_igbo_dict.keys())
    for i in range(0, len(words), 5):
        print(", ".join(words[i:i+5]))
    
    print("\n" + "-" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Look up a word")
        print("2. Show all words in the dictionary")
        print("3. Add a new word to the dictionary")
        print("4. Translate a sentence (word by word)")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            # Look up a word
            word = input("Enter an English word to translate: ").strip().lower()
            
            if word in english_igbo_dict:
                print(f"\n✓ '{word}' in igbo is: '{english_igbo_dict[word]}'")
            else:
                print(f"\n✗ '{word}' is not in the dictionary.")
                # Suggest similar words if available
                similar_words = [w for w in words if word in w or w.startswith(word[:3])]
                if similar_words:
                    print(f"Did you mean: {', '.join(similar_words)}?")
        
        elif choice == "2":
            # Display all words in the dictionary
            print("\n" + "=" * 50)
            print("FULL ENGLISH-IGBO DICTIONARY")
            print("=" * 50)
            for english, igbo in sorted(english_igbo_dict.items()):
                print(f"{english:15} → {igbo}")
        
        elif choice == "3":
            # Add a new word to the dictionary
            print("\nAdd a new word to the dictionary:")
            new_english = input("Enter english word: ").strip().lower()
            
            if new_english in english_igbo_dict:
                print(f"'{new_english}' is already in the dictionary.")
                overwrite = input("Do you want to update its translation? (yes/no): ").strip().lower()
                if overwrite != 'yes':
                    continue
            
            new_igbo = input("Enter igbo translation: ").strip()
            english_igbo_dict[new_english] = new_igbo
            print(f"✓ '{new_english}' has been added/updated in the dictionary.")
        
        elif choice == "4":
            # Translate a sentence word by word
            print("\nTranslate a sentence (word by word translation):")
            sentence = input("Enter an english sentence: ").strip().lower()
            
            if not sentence:
                print("No sentence entered.")
                continue
                
            words_in_sentence = sentence.split()
            print("\nTranslation:")
            
            for word in words_in_sentence:
                # Remove punctuation for better matching
                clean_word = word.strip(".,!?;:")
                if clean_word in english_igbo_dict:
                    print(f"{word}: {english_igbo_dict[clean_word]}")
                else:
                    print(f"{word}: [Translation not found]")
        
        elif choice == "5":
            # Exit the program
            print("\ngoodbye!(ka o di!)")
            print("thankyou(daalu! ) for using the french-igbo Dictionary.")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")


# Run the dictionary program
if __name__ == "__main__":
    english_to_igbo_dictionary()