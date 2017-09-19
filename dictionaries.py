#1
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
print(phonebook_dict['Elizabeth'])
phonebook_dict["Kareem"] = ["938-489-1234"]
del phonebook_dict["Alice"]
phonebook_dict["Bob"] = ['968-345-2345']
print(phonebook_dict)

#########################################################################
#########################################################################

#2 Nested Dicts.
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
print(ramit['email'])
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][1]['interests'][1])

#########################################################################
#########################################################################

#3 Letter Summary
ask = raw_input("Whats your favorite word? ")
def letter_histogram(word):
    char_count = {}
    for char in word:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count
print(letter_histogram(ask))

#########################################################################
#########################################################################

#4 Word Summary
#For this problem you can see that we took the sentence and had all the words placed in a list so that we could count words instead of characters. The split divider for this case was space hence the use of ().
some_words = raw_input("Say a sentence. ")
def word_histogram(sentence):
    word_count = {}
    word_list = sentence.split(" ")
    for words in word_list:
        if words not in word_count:
            word_count[words] = 1
        else:
            word_count[words] += 1
    return word_count
print(word_histogram(some_words.lower()))
