
def word_count(sentence):
    words_qty = {}
    sentence = sentence.lower()
    import re
    sentence = re.sub('[\W|_+]', ' ', sentence)
    sentence = sentence.split()
    for word in sentence:
        words_qty[word] = count_word_in_sentence(word, sentence)
    return words_qty

def count_word_in_sentence(word, sentece):
    contador = 0
    for word_sentece in sentece:
        if word == word_sentece:
            contador = contador + 1
    return  contador

