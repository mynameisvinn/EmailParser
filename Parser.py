import codecs
import numpy as np
from spacy.en import English

def read_email(fname):
    """Read email as unicode."""
    with codecs.open(fname, encoding='utf-8') as email:
        text = email.read().encode('utf-8')
    return text

def strip(msg):
    return msg.strip().split('\n')

def generate_text(sentences, threshold, pos_parser, fname):
    """
    For each line, determine if line is signature block.

    If prob(signature block) is less than the defined threshold, write
    line to file.

    Parameters
    ----------
    sentence : str
        Represents line in email block.
    threshold: float
        Lower thresholds will result in more false positives.
    POS_parser: obj
        Spacy English object used to tag parts-of-speech. Will explore using
        other POS taggers like NLTK's.
    """
    with open(fname, "w") as new_file:
        for sentence in sentences:
            if _prob_block(sentence, pos_parser) < threshold:
                new_file.write(unicode(sentence, 'utf8'))
    return True

def _prob_block(sentence, pos_parser):
    """Calculate probability of email block.

    Parameters
    ----------
    sentence : str
        Line in email block.
    pos_parser : obj
        A POS tagger object. This version relies on Spacy's English POS-tagger.

    Returns
    -------
    probability(signature block | line)
    """
    try:
        sentence = unicode(sentence)
        parsed_data = pos_parser(sentence)
        for span in parsed_data.sents:
            sent = [parsed_data[i] for i in range(span.start, span.end)]
        non_verbs = np.sum([token.pos_ != 'VERB' for token in sent])
        total = len(sent)
        return float(non_verbs) / total
    except:
        return 0

if __name__ == '__main__':
    pass
