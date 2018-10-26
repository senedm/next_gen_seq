#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sened
email - deenesmaark@gmail.com

"""

def FASTQ_reader(rooth_path, file_name):
    
    import os

    data = os.path.join(root_path, file_name)
    total_file = []

    #loads the whole txt file to one list
    #every element of the list is one row

    with open(data) as infile:
        for line in infile:
            total_file.append(line)

    #slice and dice

    SEQ_ID = total_file[0::4]
    sequences = total_file[1::4]
    identifier = total_file[2::4]
    quality = total_file[3::4]

    #whatever can go wrong, will go wrong
    sequences = [x.upper() for x in sequences]

    #keep it simple: at first check the bases

    bases = ['A','C','G','T','U']
    # [A, C, G, T] - bases of DNA
    # [A, C, G, U] - bases of RNA
    
    #TODO: write preproc and catenate to class

    #what we gather along the way is what makes us...
    unique = list(set(sequences))

    print('File contains: '+ str(len(sequences)-len(unique))\
    + ' duplicate(s)'+ ' and ' + str(len(unique))+' unique value(s)')

    no_of_reads = len(sequences)

    no_of_read_pairs = 2*no_of_reads

    print('Number of read-pairs: ' + str(no_of_read_pairs))
        
    return SEQ_ID,sequences,identifier,quality

root_path = "/home/sened/Dokumentumok/Omixon_entry_questions/3."
file_name = 'DRR015565_1.fastq'

SEQ_ID,sequences,identifier,quality = FASTQ_reader(root_path, file_name)
