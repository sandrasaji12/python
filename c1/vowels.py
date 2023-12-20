vowels=['a','e','i','o','u']
word=input("Enter a word:")
print("Vowels in the word are:")
s=[i for i in word if i in vowels]
print(s)
