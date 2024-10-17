def count_word_frequencies(sentence):
    words_list = sentence.lower().split()
    word_frequency_dict = {}
    for word in words_list:
        if word in word_frequency_dict:

            word_frequency_dict[word] += 1
        else:

            word_frequency_dict[word] = 1

    return word_frequency_dict


user_sentence = input("Enter a sentence: ")

word_frequencies = count_word_frequencies(user_sentence)

print("Word frequencies:", word_frequencies)