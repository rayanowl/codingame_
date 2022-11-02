pyg = 'ay'

original = raw_input('Enter a word: ')

while not original.isalpha():
    original = raw_input('It\'s not a string, try again ')
if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word[1:len(new_word)]
  print new_word
  
else:
  print 'empty'