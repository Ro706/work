a_String=str(input(""))
lowercase = a_String.lower()
vowel_counts = {}
for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_counts[vowel] = count
counts = vowel_counts.values()
total_vowels = sum(counts)
print(total_vowels)
print("made by ro404")
  
