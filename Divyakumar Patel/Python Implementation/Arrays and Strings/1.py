# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def unique_char_additional_ds():
    sentence = "divya patel"
    char_set = set()
    char_list = []
    for i in sentence:
        if i != ' ':
            char_list.append(i)
            char_set.add(i)
    if len(char_list) != len(char_set):
        print("String does not have Unique Character !!")
    else:
        print("String characters are unique !!")


def unique_char_without_additional_ds():
    sentence = "#132"
    characters = ''.join(sorted(sentence))
    # print(characters)
    flag = 0
    for i in range(0, len(characters)-1):
        if characters[i] != ' ' and characters[i] == characters[i+1]:
            print("String does not have Unique Character !!")
            flag = 1
    if flag == 0:
        print("String characters are unique !!")


unique_char_without_additional_ds()
