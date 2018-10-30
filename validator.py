from util import read_corpus, compute_bleu_for_sentences

def validate_output_file( hypo_f, refer_f ):
    hypo_data = read_corpus( hypo_f, "src" )
    refer_data = read_corpus( refer_f, "tar" )
    return compute_bleu_for_sentences( refer_data, hypo_data )