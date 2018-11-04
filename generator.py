import numpy as np 
from util import * 
import pickle
from vocab import VocabEntry, tokenize
import random 

def greedy_generator_single_sentence( sentence, vocab, secure_n_gram, replace_prob, replace_with_top, insert_prob, insert_with_top, displacement_range, displacement_prob ):
    """
    Take in a single sentence and output the 
    """
    # convet to number array
    word_list = tokenize( sentence )
    idx_list = vocab.single_sentence2ids( word_list )
    length = len( idx_list )
    cur_length = 0
    idx_array = []

    replace_lst = np.arange( 1, replace_with_top )
    replace_p = np.linspace( replace_with_top, 1 , num = replace_with_top - 1 )
    replace_p = replace_p / np.sum( replace_p )
    
    insert_lst = np.arange( 1, insert_with_top )
    insert_p = np.linspace( insert_with_top, 1 , num = insert_with_top - 1 )
    insert_p = insert_p / np.sum( insert_p )
    # break sentences into n_grams with top n gram being secure_n_gram
    while cur_length < length:
        slice_length = random.randint( 1, secure_n_gram )
        idx_array.append( idx_list[ cur_length: cur_length + slice_length ] )
        cur_length += slice_length

    # randomly replace words in n_gram
    for l in range( len( idx_array ) ):
        for i in range( len( idx_array[ l ] ) ):
            if random.random() < replace_prob:
                idx_array[ l ][ i ] = np.random.choice( replace_lst, p = replace_p )
    
    # randomly insert n_gram in the sentence
    for l in range( len( idx_array ) ):
        if random.random() < insert_prob:
            insert_len = random.randint( 1, secure_n_gram )
            ins = []
            for _ in range( insert_len ):
                ins.append( np.random.choice( insert_lst, p = insert_p ) )
            idx_array[ l ] += ins 
    # randomly displace
    cur_len = 0
    ret = []
    while cur_len < len( idx_array ):
        displace_len = random.randint( 1, displacement_range )
        while( displace_len + cur_len > len( idx_array ) ):
            displace_len = random.randint( 1, displacement_range )
        add = idx_array[ cur_len: cur_len + displace_len ]
        if random.random() < displacement_prob:
            shuffle_idx = np.arange( displace_len, dtype = np.int )
            np.random.shuffle( shuffle_idx )
            add_new = []
            for i in shuffle_idx:
                add_new.append( add[ i ] )
            add = add_new
        cur_len += displace_len
        ret += add
    res = []
    for item in ret:
        res += item 
    return vocab.id2single_sentence( res )

def greedy_generator( in_file, out_file, vocab, secure_n_gram, replace_prob, replace_with_top,insert_prob, insert_with_top, displacement_range, displacement_prob ):
    """
    Replace a src sentence with random vocab, and displacement in certain probability
    Args:
        in_file: input file path 
        out_file: output file path 
        vocab: preprocessed vocab path 
        secure_n_gram: the max n gram feature to be preserved 
        replace_prob: the prob of a single work be replaced
        replace_with_top: replaced wordd with top frequent replace_with_top words in the vocab
        displacement_range: length n_gram words to shuffle order 
        displacement_prob: probability of a n_gram to be shuffled , this is not overlapping n_grams
    Returns:
        list of sentences 
    """
    in_f = open( in_file, "r", encoding = "utf-8" )
    out_f = open( out_file, "w" )

    line = in_f.readline()
    while line != "":
        res = greedy_generator_single_sentence( line, vocab, secure_n_gram, replace_prob,
                                                replace_with_top, insert_prob, insert_with_top,
                                                displacement_range, displacement_prob )
        out_f.write( res + "\n" )

        line = in_f.readline()
        # print( "done 1" )
    in_f.close()
    out_f.close()
    return 0


def naive_beam(  in_file, out_file, vocab, secure_n_gram, replace_prob, replace_with_top,
                 insert_prob, insert_with_top, displacement_range, displacement_prob, beam_size = 5 ):
    pass