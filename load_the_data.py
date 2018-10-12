#this function opens the unknown seqence from .txt format and the checks it

import os
import numpy as np

root_path = "/home/sened/Dokumentumok/Omixon_entry_questions"
file_name = 'test2.txt'

def load_the_data(root_path, file_name):
    
    data = os.path.join(root_path, file_name)
    check = []

    RNA = ['A','C','G','U']
    DNA = ['A','C','G','T']


    with open(data) as infile:
        for line in infile:
            check.append(line)

    if '\n' in check:
        print('WARNING: The analysis writing could interrupted, it contains new rows')


    for i in range(len(check[0])-1):
        if check[0][i] in RNA or check[0][i] in DNA:
            continue
        else:
            print('')
            print('ERROR: ' + check[0][i] + ' is NOT a base ' + '#' + str(i))
            print('')
            
    return check

test1 = load_the_data(root_path, file_name)
