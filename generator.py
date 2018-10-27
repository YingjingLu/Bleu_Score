import numpy as np 
from util import * 
import pickle
from vocab import VocabEntry 

def greedy_generator_single_sentence( sentence, vocab, secure_n_gram, replace_prob, replace_with_top, displacement_range, displacement_prob ):
    """
    Take in a single sentence and output the 
    """

def greedy_generator( in_file, out_file, vocab, secure_n_gram, replace_prob, replace_with_top, displacement_range, displacement_prob ):
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
    pass
    