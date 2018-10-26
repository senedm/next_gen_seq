#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sened
email - deenesmaark@gmail.com

"""

def load_txt_data(root_path,file_name):

    '''This function opens the unknown seqence from .txt format and the checks it'''

    import os
    
    data = os.path.join(root_path, file_name)
    total_file = []

    #loads the whole txt file to one list
    #every element of the list is one row

    with open(data) as infile:
        for line in infile:
            total_file.append(line)

    #whatever can go wrong, will go wrong
    total_file = [x.upper() for x in total_file]

    bases = ['A','C','G','T','U']
    # [A, C, G, T] - bases of DNA
    # [A, C, G, U] - bases of RNA

    message = True
    #it checks are it contains wrong characters
    for i in range(len(total_file)):
        for j in range(len(total_file[i])-1):
            if total_file[i][j] not in bases:
                print('It is not a base: '+total_file[i][j] +', in the position: '+ str(i)+'-' + str(j))
                message = False

    total_file = ''.join(total_file)

    if message is True:
        print('No wrong characters in the file!')

    #overwrite the old file
    final_file = open(data,'w') 

    final_file.write(str(total_file))

    final_file.close()
    
    return total_file

def count_the_bases(sequence):
    
    """It counts the bases of the sequence and the non-correct
    characters e.g. numbers or any non-base character """
    
    A,C,G,T,U = 0, 0, 0, 0, 0
    errors = 0
    
    for i in range(len(sequence)):
    
        if sequence[i] == 'A':
            A = A + 1
        elif sequence[i] == 'C':
            C = C + 1
        elif sequence[i] == 'G':
            G = G+1
        elif sequence[i] == 'T':
            T = T+1
        elif sequence[i] == 'U':
            U = U+1
        else:
            errors = errors + 1
            
    print('ERRORS:' + str(errors))
    print('Adenine:' + str(A))
    print('Cytosine:' + str(C))
    print('Guanine:' + str(G))
    print('Thymine:' + str(T))
    print('Uracil:' + str(U))
    
    if U == 0:
    
        print()
        print('It was probably a DNA')
   
    else:
        
        print()
        print('It was probably a RNA')
    
    return errors,A,C,G,T,U

def DNA_to_RNA(DNA):
    
    """ It replaces every Uracil to Thymine """
    
    RNA = []
    
    for i in range(len(DNA)):
    
        if DNA[i] == 'U':
            RNA.append['T']
        else:
            RNA.append(DNA[i])
            
    RNA = ''.join(RNA) #stick it
    
    return RNA

def reverse_complement(seq,base_type):
    
    """It calculates the complementer of the seqence
    base_tye can be RNA or DNA"""
    
    DNA = {
        'A':'T',
        'C':'G',
        'G':'C',
        'T':'A',
    }
    
    RNA = {
        'A':'U',
        'C':'G',
        'G':'C',
        'U':'A',
    }
    
    if base_type.upper() == 'DNA':
            
        complementer = [DNA[seq[i]] for i in range(len(seq))]

    
    elif base_type.upper() == 'RNA':
        
        
        complementer = [RNA[seq[i]] for i in range(len(seq))]
    
    else:
        
        print()
        print('''ERROR: WRONG FORMAT of base_type! It must be 'DNA' or 'RNA'!''')
                
    complementer = ''.join(complementer)
        
    return complementer

def find_pattern(seq, pattern):
    
    matched_lines = [line for line in seq.split('\n') if str(pattern[0]) in line]
    
    return matched_lines

root_path = "/home/sened/Dokumentumok/Omixon_entry_questions"
file_name = 'unknow_seq1.txt'

test1 = load_txt_data(root_path,file_name)
print(count_the_bases(test1))
print()
print(DNA_to_RNA(test1))
print()
print(reverse_complement(test1,'DNA'))



''' ___________Pattern search with repeats_____________ '''

'''DRY ;)'''
    

seq_path = "/home/sened/Dokumentumok/Omixon_entry_questions"
seq_name = 'where_r.txt'

pattern_path = "/home/sened/Dokumentumok/Omixon_entry_questions/Patterns"
pattern_name = 'pattern_test1.txt'
    
seq = load_txt_data(seq_path, seq_name)
pattern = load_txt_data(pattern_path, pattern_name)

print(find_pattern(seq,pattern))




