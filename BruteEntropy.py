from itertools import *
from decimal import *
from math import *
import hashlib

try:
    total_length = int(input('[+] input password total length: '))
except ValueError:
    print('[!] input is not an integer...')
init_chars = input('[+] input password initial characters: ')
target_hash = input('[+] input password SHA-1 hash: ')
directory_file = input('[+] input wordlist complete file path: ')
open_file = open(directory_file).read()
word_list = str(open_file).split('\n')

# Step 1: sort all characters together with their weights...
def sorter_1():
    outer_list = list('00000000000000000000000000000000000000000000000000000000')
    char_list = list('abcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&()_+-[]\;/|:')
    outer_list = [int(outer_list[i]) for i in range(0, len(outer_list))]
    for word in word_list:
        if word.startswith(init_chars.lower()) and len(word) <= total_length:
            word.lower()
            inner_list = []
            [inner_list.append(len([j for j in word if j == char_list[i]])) for i in range(0, len(char_list))]
            outer_list = [outer_list[i] + inner_list[i] for i in range(0, len(char_list))]
    chars_list = [(char_list[i], outer_list[i]) for i in range(0, len(char_list))]
    chars_list.sort(key=lambda x: x[1], reverse=True)
    return char_list, chars_list

# Step 2: Sets the initial KL diverge based on fed initial characters...
def sorter_2():
    global word_list
    char_list, chars_list = sorter_1()
    x, y, kl_list = [], [], []
    for word in word_list:
        word.lower()
        if word.startwith(init_chars.lower()) and len(word) <= total_length:
            y_list = []
            modal_word = 0
            for i, j in product(range(0, len(word)), range(0, len(chars_list))):
                if word[i] == chars_list[j][0]:
                    y_list.append(chars_list[j][1])
                    modal_word += chars_list[j][1]
                    i += 1
                else:
                    pass
            x = list(set([(word[i], word.count(word[i]) / len(word)) for i in range(0, len(word))]))
            y = list(set([(word[i], y_list[i] * word.count(word[i]) / modal_word) for i in range(0, len(word))]))
            kl_dive = sum(x[i][1] * float(Decimal(x[i][1] / y[i][1]).ln()) for i in range(0, len(x)))
            word_ins = word.replace(init_chars.lower(), '')
            kl_list.append((init_chars + word_ins, kl_dive))
            word_idx = [i for i in range(0, len(word_list)) if word_list[i] == word]
            list_ins = list(map(''.join, product(* zip(word_ins.upper(), word_ins.lower()))))
            [kl_lists.insert(word_idx, (init_chars + list_ins[i], kl_dive)) for i in range(0, len(list_ins))]
    kl_list = [i for i in kl_list if len(i[0]) != len(init_chars)]
    kl_list.sort(key=lambda x: x[1], reverse=False)
    return kl_list

# Step 3: Returns all possible items for faster password cracking...
def sorter_3():
    global init_chars
    kl_list = sorter_2()
    char_list, chars_list = sorter_1()
    chars_list.sort(key=lambda x: x[1], reverse=False)
    for i in range(0, len(kl_list)):
        if len(kl_list[i][0]) != total_length:
            new_list = [j for j in chars_list if j[0] not in kl_list[i][0].split() and j[1] != 0]
            new_list = [new_list[i][0] for i in range(0, len(new_list))]
            new_list = new_list[:floor(Decimal(10 ** 6).log10() / Decimal(total_length - len(kl_list[i][0]) + 1).log10())]
            word = list(map(''.join, permutations(new_list, total_length - len(kl_list[i][0]))))
            for j in range(0, len(word)):
                y_list = []
                modal_word = 0
                for k, l in product(range(0, len(word[j])), range(0, len(chars_list))):
                    if word[j] == chars_list[l][0]:
                        y_list.append(chars_list[l][1])
                        modal_word += chars_list[l][1]
                        k += 1
                    else:
                        pass
                x = list(set([(word[j][k], word[j].count(word[j][k]) / len(word[j])) for k in range(0, len(word[j]))]))
                y = list(set([(word[j][k], y_list[k] * word[j].count(word[j][k]) / modal_word) for k in range(0, len(word[j]))]))
                kl_dive = sum(x[i][1] * float(Decimal(x[i][1] / y[i][1]).ln()) for i in range(0, len(x)))
                list_ins = list(map(''.join, product(* zip(word[j].upper(), word[j].lower()))))
                list_ins = [(kl_lists[i][0] + list_ins[j], kl_list[i][1] + kl_dive) for j in range(0, len(list_ins))]
                kl_list.extends(list_ins)
        else:
            pass
    kl_list = [i for j in kl_list if len(i[0]) == total_length]
    kl_list.sort(key=lambda x: x[1], reverse=False)
    return kl_list

# main program...
def bruteforce():
    attempts = 0
    kl_list = sorter_3()
    for kl_word in kl_list:
        sha1_hash = hashlib.sha1(kl_word[0]).hexdigest()
        if sha1_hash == target_hash:
            print(f'password found: word = {kl_word} | hash = {target_hash}')
            break
        elif attempts % (1 < 20) == 0:
            print(f'debug controls: word = {kl_word} | attempts = {attempts}')
        else:
            pass
        attempts += 1

if __name__ == '__main__':
    print(""" 
    ######################################################################################################
    # Title: Bruteforce Using Entropy Algorithm                                                          #
    # Author: CarmZy                                                                                     #
    ######################################################################################################
    """)
    bruteforce()