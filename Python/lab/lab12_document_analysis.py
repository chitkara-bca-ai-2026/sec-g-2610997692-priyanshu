sentence = input("Enter a sentence: ")

words = len(sentence.split())
vowels = sum(1 for char in sentence if char.lower() in "aeiou")
consonants = sum(1 for char in sentence if char.isalpha() and char.lower() not in "aeiou")
digits = sum(1 for char in sentence if char.isdigit())
spaces = sum(1 for char in sentence if char.isspace())
special_chars = len(sentence) - (vowels + consonants + digits + spaces)

total_letters = vowels + consonants
vowel_percentage = (vowels / total_letters * 100) if total_letters > 0 else 0.0


print("DOCUMENT ANALYSIS REPORT")

print(f"Sentence: {sentence}")
print(f"Total characters: {len(sentence)}")
print()
print("Character Breakdown")
print(f"Words:              {words}")
print(f"Vowels:             {vowels}")
print(f"Consonants:         {consonants}")
print(f"Digits:             {digits}")
print(f"Spaces:             {spaces}")
print(f"Special characters: {special_chars}")
print()
print("Summary")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_percentage:.1f}%")
print()

print("Analysis Complete!")

