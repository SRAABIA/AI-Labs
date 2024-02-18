'''
- Take a user input (a sentence), tokenize it, make pairs of the consecutive 2 words.
- Apply a next word prediction, and take another input from user (another sentence), based on the last word in second sentence,
  predict what should be the next word w.r.t the value learned out of Sentence 1.
- Keeping in mind, a word may repeat in the sentence.

'''
import nltk
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk import ngrams,bigrams

text = input('Enter your first sentence: ')
text = text.lower()
text = text.replace('.','')
text = text.replace(',','')
word_tokenized = word_tokenize(text)
print('\n',word_tokenized)

pairs = list(bigrams(word_tokenized))
print("\nBigrams Pairs:", pairs)

freq = FreqDist(pairs)

# for i in range(3):
#     ngram_1[i+1] = list(ngrams(word_tokenized, i+1))[-1]
# print(freq)

text2 = input('\nEnter your second sentence: ')
text2 = text2.lower()
word2_tokenized = word_tokenize(text2)
last_word = word2_tokenized[-1]

# print(last_word)

predicword = []

for word in pairs:
  if last_word == word[0]:
    # predicword.append(word[1])
    predicword.append(word)

if not predicword:
  print('\nNo suggestions')

for pair in predicword:
    frequency = freq[pair]
    print(f"\nFrequency of {pair} = {frequency}")

def freqn(x):
  return freq[x];

best_pair = max(predicword, key = freqn )

print('\n\nYour next word might be: ', best_pair[1])

# References:
# 1. YouTube: Python NLTK Playlist https://www.youtube.com/playlist?list=PLS1QulWo1RIZDws-_0Bfw5FZFmQJWtMl1
# 2. Medium Article: Language Modeling With NLTK https://medium.com/swlh/language-modelling-with-nltk-20eac7e70853#1799
# 3. YouTube: What are Bigrams and Trigrams (Topic Modeling and Python for DH 01.03) https://www.youtube.com/watch?v=GBQFelgzjKQ
# &  stackoverflow.