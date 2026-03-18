# Vowel Counter
word = input("enter a word: ")
vowel_count = 0
for char in word:
    if char.lower() in "aeiou":
        vowel_count += 1
print(f"total number of vowels is {vowel_count}")