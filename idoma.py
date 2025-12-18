# Enhanced English-Idoma Dictionary

english_to_idoma = {
    "hello": "Ndewo",
    "goodbye": "Odogwu", 
    "thank you": "Daalu",
    "please": "Biko",
    "sorry": "Ndo",
    "water": "Mmanu",
    "food": "Nri",
    "house": "Ulo",
    "child": "Nwata",
    "man": "Nwoke",
    "woman": "Nwanyi",
    "father": "Nna",
    "mother": "Nne",
    "friend": "Enyi",
    "day": "Ubochi",
    "night": "Anyasi",
    "sun": "Anwu",
    "moon": "Onwa",

    "star": "Kpakpando",
    "earth": "Uwa"
}

def main():
    print("=" * 40)
    print("    ENGLISH - IDOMA DICTIONARY")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Search for English word")
        print("2. View all words")
        print("3. Test your knowledge")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ")
        
        if choice == "1":

            word = input("\nEnter English word: ").lower().strip()
            if word in english_to_idoma:
                print(f"\nTranslation: {english_to_idoma[word]}")
            else:
                print(f"Word '{word}' not found.")
                # Find close matches
                matches = [w for w in english_to_idoma if w.startswith(word[:3])]
                if matches:
                    print("Did you mean:")
                    for match in matches[:3]:
                        print(f"  - {match}")
        
        elif choice == "2":
            print("\n" + "=" * 30)
            print("ENGLISH".ljust(15) + "IDOMA")
            print("=" * 30)
            for eng, idoma in sorted(english_to_idoma.items()):
                print(f"{eng.ljust(15)} {idoma}")
        
        elif choice == "3":
            # Simple quiz game
            import random
            print("\n=== IDOMA QUIZ ===")
            print("Translate these words to Idoma:")
            
            score = 0
            words = list(english_to_idoma.items())
            random.shuffle(words)
            
            for eng, idoma in words[:5]:  # Test on 5 random words
                answer = input(f"\nWhat is '{eng}' in Idoma? ").strip()
                if answer.lower() == idoma.lower():

                    print("✓ Correct!")
                    score += 1
                else:
                    print(f"✗ Wrong. The correct answer is: {idoma}")
            
            print(f"\nYour score: {score}/5")
        
        elif choice == "4":
            print("\nOdogwu! Daalu for using the dictionary!")
            break 
        
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
