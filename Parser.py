import numpy as np
from spacy.lang.en import English
import spacy

def convert(fname, threshold=.9):
    pos_tagger = English()  # part-of-speech tagger
    original_email = _read_email(fname)
    sentences = _corpus2sentences(original_email)  # convert to sentences

    # iterate through sentence, write to a new file if not signature block
    fn = fname.split(".")
    new_fname = fn[0] + "_clean." + fn[1]
    _generate_text(sentences, new_fname)

def _read_email(fname):
    with open(fname, 'r') as email:
        text = email.read()
    return text

def _corpus2sentences(corpus):
    """split corpus into a list of sentences.
    """
    return corpus.strip().split('\n')

def _generate_text(sentences, fname, threshold=0.9):
    """iterate through sentences. if the sentence is not a signature block, 
    write to file.

    if probability(signature block) > threshold, then it is a signature block.

    Parameters
    ----------
    sentence : str
        Represents line in email block.
    POS_parser: obj
        Spacy English object used to tag parts-of-speech. Will explore using
        other POS taggers like NLTK's.
    fname : str
        Represents fname of new corpus, excluding signature block.
    threshold: float
        Lower thresholds will result in more false positives.
    """
    tagger = spacy.load('en_core_web_sm')

    with open(fname, "w") as new_file:
        for sentence in sentences:
            if _prob_block(sentence, tagger) < threshold:
                new_file.write(sentence)

def _prob_block(sentence, pos_tagger):
    """Calculate probability that a sentence is an email block.
    
    https://spacy.io/usage/linguistic-features

    Parameters
    ----------
    sentence : str
        Line in email block.

    Returns
    -------
    probability(signature block | line)
    """
    
    doc = pos_tagger(sentence)
    verb_count = np.sum([token.pos_ != "VERB" for token in doc])
    return float(verb_count) / len(doc)