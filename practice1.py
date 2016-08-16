import nltk
from nltk.tokenize import sent_tokenize,word_tokenize

example_text = "Recently, I moved from my earlier role as an Evangelist to a different stage all together. It has been an exciting journey to move into different horizons and explore newly found mountains. Though there is no doubt that I miss my earlier role and my friends over there a lot but I think Life sometimes is all about moving and just letting go."

print(sent_tokenize(example_text))

print "Testing work tokenizing"

print(word_tokenize(example_text))