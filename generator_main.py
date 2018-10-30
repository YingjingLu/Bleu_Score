import argparse
import os
from generator import *
import pickle
from util import *
from validator import *

def parse_arguments():
    # Command-line flags are defined here.
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', dest='mode',
                        type=str, default="greedy",
                        help="whether greedy or beam mode ")
    parser.add_argument('--in-file', dest='in_file',
                        type=str, default="",
                        help="input file")
    parser.add_argument('--out-file', dest='out_file', type=str,
                        default="", help="output file path")
    parser.add_argument('--vocab', dest='vocab', type=str,
                        default="", help="vocab path")
    parser.add_argument('--n-gram', dest='n_gram', type=int,
                        default=4, help="Max n gram to keep")
    parser.add_argument('--replace-top', dest='replace_top', type=int,
                        default=100, help="Top # word for replacement")
    parser.add_argument('--insert-top', dest='insert_top', type=int,
                        default=100, help="Top # word for insertment")
    parser.add_argument('--displacement-range', dest='displacement_range', type=int,
                        default=4, help="most displacement can take place")
    parser.add_argument('--replace-prob', dest='replace_prob', type=float,
                        default=0.3, help="replacement probability")
    parser.add_argument('--insert-prob', dest='insert_prob', type=float,
                        default=0.3, help="insert probability")
    parser.add_argument('--displacement-prob', dest='displacement_prob', type=float,
                        default=0.3, help="displacement probability")

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    displacement_range = [ 1, args.displacement_range ]
    vocab = pickle.load( open( args.vocab, "rb" ) )

    if args.mode == "greedy":
        greedy_generator( args.in_file, args.out_file, vocab, args.n_gram, 
                          args.replace_prob, args.replace_top, args.insert_prob, args.insert_top,
                        displacement_range, args.displacement_prob )
        bleu_score = validate_output_file( args.out_file, args.in_file )
        print("Bleu Score: {}".format( bleu_score )  )