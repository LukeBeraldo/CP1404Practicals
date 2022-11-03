"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

word_to_counter = {}
new_text = input("Text: ")
words = new_text.split()
print(words)
for word in words:
    try:
        word_to_counter[word] += 1
    except KeyError:
        word_to_counter[word] = 1

words = list(word_to_counter.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_counter[word]}")
