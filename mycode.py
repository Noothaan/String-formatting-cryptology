import re

with open("mystory.txt") as f:
  story = f.read().lower()
  
all_letters = re.findall("[a-z]", story)

letters = {}
for letter in all_letters:
  if letter in letters:
    letters[letter] += 1
  else:
      letters[letter] = 1
      
print(letters)

alphabet = []
for letter in letters:
  alphabet.append(letter)
  
alphabet.sort ()

print("Letter/Frequency")
for letter in alphabet:
  frequency = letters[letter]
  bar = "="*(frequency // 10)
  print("{:>6}/{:}".format(letter, bar))
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  