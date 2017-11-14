import random

def read_words_from_file():
    try:
        input_file = open("dictionary_computer_short.txt")
        words      = []
        a_line     = input_file.readline()

        while a_line:
            words.append(a_line.rstrip())
            a_line = input_file.readline()

        return words
    
    except FileNotFoundError:
        print()
        print("FILE NOT FOUND")
        print()

def choose_random_word(word_list):
    '''
    Choose a random word from the list and transform it into a list
    of characters.
    '''

    word_chars  = []
    list_len    = len(word_list)
    rand_num    = random.randint(0, (list_len - 1))
    random_word = word_list[rand_num]
    # random_word = random.choice(word_list)

    for char in random_word:
        word_chars.append(char)
        
    return word_chars

def mask_random_word(random_word):
    masked_list = []

    for char in random_word:
        masked_list.append("_")

    return masked_list

def contains_dashes(masked_word):
    for char in masked_word:
        if char == "_":
            return True
        else:
            return False

def replace_dash_with_letter(word, masked_word, player_input):
    new_word = masked_word

    for char in word:
        if char == player_input:
            new_word[word.index(char)] = player_input
        
    return new_word


def play_game():
    num_of_misses = 0
    words         = read_words_from_file()
    random_word   = choose_random_word(words)
    masked_word   = mask_random_word(random_word)

    # print_final   = ""
    # print_mask    = " "

    print(random_word)

    while contains_dashes(masked_word) and num_of_misses < 6:
        # print(num_of_misses)

        print(masked_word)
        
        player_input = input("Type in a letter (a - z): ")
        
        if player_input in random_word:
            print(player_input + " is in the random_word")
            masked_word = replace_dash_with_letter(random_word, masked_word, player_input)
            print()
            
        else:
            print("'" + player_input + "'" + " is incorrect!")
            num_of_misses += 1
        


# play_game()

# print(words)
# print(random_word)
# print(masked_word)
# print(contains_dashes(test_mask))
word = "batman"
masked_word = mask_random_word(word)
print(masked_word)
print(replace_dash_with_letter(word, masked_word, "b"))
print(replace_dash_with_letter(word, masked_word, "a"))
