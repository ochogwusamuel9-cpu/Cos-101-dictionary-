def english_to_yoruba_dictionary():
    """
    A simple English to Yoruba dictionary with 20 words.
    Allows users to look up translations.
    """
    
    # Dictionary of 20 English words and their Yoruba translations
    english_yoruba_dict = {
        "hello": "bawo",
        "goodbye": "o dabọ",
        "thank you": "o ṣeun",
        "please": "jọwọ",
        "yes": "bẹẹni",

        "no": "bẹẹkọ",
        "water": "omi",
        "food": "ounjẹ",
        "house": "ilé",
        "family": "idile",
        "friend": "ọrẹ",
        "love": "ifẹ",
        "child": "ọmọ",
        "man": "ọkunrin",
        "woman": "obirin",
        "sun": "oorun",
        "moon": "osupá",
        "star": "irawo",
        "tree": "igi",
        "book": "iwe"
    }
    
    print("=" * 50)
    print("ENGLISH TO YORUBA DICTIONARY")
    print("=" * 50)

    print(f"This dictionary contains {len(english_yoruba_dict)} words.")
    print("\nAvailable English words:")
    
    # Display available words in a neat format
    words = list(english_yoruba_dict.keys())
    for i in range(0, len(words), 5):
        print(", ".join(words[i:i+5]))
    
    print("\n" + "-" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Look up a word")
        print("2. Show all words in the dictionary")
        print("3. Add a new word to the dictionary")
        print("4. Exit")
        

        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            # Look up a word
            word = input("Enter an English word to translate: ").strip().lower()
            
            if word in english_yoruba_dict:
                print(f"\n✓ '{word}' in Yoruba is: '{english_yoruba_dict[word]}'")
            else:
                print(f"\n✗ '{word}' is not in the dictionary.")
                # Suggest similar words if available
                similar_words = [w for w in words if word in w or w.startswith(word[:3])]
                if similar_words:
                    print(f"Did you mean: {', '.join(similar_words)}?")
        
        elif choice == "2":
            # Display all words in the dictionary
            print("\n" + "=" * 50)
            print("FULL ENGLISH-YORUBA DICTIONARY")
            print("=" * 50)
            for english, yoruba in sorted(english_yoruba_dict.items()):
                print(f"{english:15} → {yoruba}")
        
        elif choice == "3":
            # Add a new word to the dictionary
            print("\nAdd a new word to the dictionary:")
            new_english = input("Enter English word: ").strip().lower()
            
            if new_english in english_yoruba_dict:

                print(f"'{new_english}' is already in the dictionary.")
                overwrite = input("Do you want to update its translation? (yes/no): ").strip().lower()
                if overwrite != 'yes':
                    continue
            
            new_yoruba = input("Enter Yoruba translation: ").strip()
            english_yoruba_dict[new_english] = new_yoruba
            print(f"✓ '{new_english}' has been added/updated in the dictionary.")
        
        elif choice == "4":
            # Exit the program
            print("\nO dabọ! (Goodbye!)")
            print("Thank you for using the English-Yoruba Dictionary.")
            break

        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")


# Run the dictionary program
if __name__ == "__main__":

    english_to_yoruba_dictionary()