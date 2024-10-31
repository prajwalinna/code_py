from spellchecker import SpellChecker

class MySpellChecker:
    def __init__(self):
        self.spell = SpellChecker()

    def corrected_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)

            # Print correction if the word is different
            if corrected_word != word:
                print(f"correcting '{word}' to '{corrected_word}' ")
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)

        return ' '.join(corrected_words)

    def run(self):
        print("\n--Spell checker--")

        while True:
            text = input("Enter text to check (or 'q' to quit): ")
            if text.lower() == 'q':
                print("closing program......\nThank you")
                break
            corrected_text = self.corrected_text(text)
            print(f"Corrected Text: {corrected_text}")

if __name__ == "__main__":
    MySpellChecker().run()
