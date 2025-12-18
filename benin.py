# English to Edo (Benin) Dictionary
# Simple version - Type English words to get Edo translations

# Dictionary with 20 common English-Edo word pairs
english_to_edo = {
    "hello": "Kóyo",
    "goodbye": "Ókhian",
    "thank you": "Ób'ówie",
    "please": "Má sé",
    "sorry": "Miẹ rẹ",
    "water": "Amẹ",
    "food": "Emwẹn",
    "house": "Ówá",
    "child": "Ómó",
    "man": "Ókpọsọ",
    "woman": "Ókpọlọ",
    "father": "Dáda",
    "mother": "Néné",
    "friend": "Óre",

    "day": "Ọdẹ",
    "night": "Ótẹ",
    "sun": "Ógẹ",
    "moon": "Ókpá",
    "star": "Ọtọlọkẹ",
    "earth": "Ayé"
}

def main():
    """Main function to run the dictionary program"""
    print("=" * 50)
    print("ENGLISH TO EDO (BENIN) DICTIONARY")
    print("=" * 50)
    print("Type any English word to see its Edo translation")
    print("Type 'list' to see all available words")
    print("Type 'quit' to exit the program")
    print("=" * 50)

    
    while True:
        # Get user input
        user_input = input("\nEnter English word: ").lower().strip()
        
        # Check if user wants to quit
        if user_input == 'quit' or user_input == 'exit':
            print("Ókhian! (Goodbye!)")
            break
        
        # Check if user wants to see all words
        if user_input == 'list':
            print("\nAll available words:")
            print("-" * 30)
            for english_word in sorted(english_to_edo.keys()):
                print(f"{english_word:15} → {english_to_edo[english_word]}")
            continue

        
        # Search for the word in dictionary
        if user_input in english_to_edo:
            edo_translation = english_to_edo[user_input]
            print(f"\n✓ '{user_input}' in Edo is: '{edo_translation}'")
            
            # Show pronunciation for common words
            pronunciations = {
                "Kóyo": "KOH-yoh",
                "Ókhian": "OH-khee-ahn",
                "Ób'ówie": "OH-boh-WEE-eh",
                "Má sé": "MAH say",
                "Miẹ rẹ": "mee-EH reh"
            }
            if edo_translation in pronunciations:
                print(f"  Pronunciation: {pronunciations[edo_translation]}")
        else:

            print(f"\n✗ '{user_input}' not found in dictionary.")
            
            # Suggest similar words
            suggestions = []
            for word in english_to_edo:
                if user_input in word or word.startswith(user_input[:3]):
                    suggestions.append(word)
            
            if suggestions:
                print("Did you mean:")
                for suggestion in suggestions[:3]:  # Show only top 3 suggestions
                    print(f"  • {suggestion}")

# Run the program
if __name__ == "__main__":
    main()
