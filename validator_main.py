import argparse
from validator import *

def parse_arguments():
    # Command-line flags are defined here.
    parser = argparse.ArgumentParser()
    parser.add_argument('--ref-file', dest='ref_file',
                        type=str, default="",
                        help="reference file path")
    parser.add_argument('--hypo-file', dest='hypo_file', type=str,
                        default="", help="hypo file path")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()

    bleu_score = validate_output_file( args.hypo_file, args.ref_file )

    print( "Bleu Score: {}".format( bleu_score ) )