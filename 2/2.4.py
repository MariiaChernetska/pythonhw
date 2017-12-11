english_latin = {
   'apple': ['malum', 'pomum', 'popula'],
   'fruit': ['baca', 'bacca', 'popum'],
   'punishment': ['malum', 'multa']
}
#result dictionary
latin_english = dict()

#forming result dictionary using values from original as keys 
#and keys as values
for key in english_latin:
    for values in english_latin[key]:
        latin_english[values] = key

print(latin_english)
word = input("Enter word ") 
print("translation ", latin_english[word])

