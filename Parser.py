import codecs
import numpy as np
from spacy.en import English

def read_email(fname):
    """Read email as unicode."""
    with codecs.open(fname, encoding='utf-8') as f:
        text = f.read()
    return text

def strip(msg):
    """Remove new lines."""
    return msg.strip().split('\n')

def generate_text(msg, threshold, POS_parser):
    """For each line, determine if line is signature block.

    Parameters
    ----------
    msg : str
        Represents line in email block.
    threshold: float
        Lower thresholds will result in more false positives.
    POS_parser: obj
        Spacy English object used to tag parts-of-speech.
    """
    for m in msg:
        if _prob_block(m, POS_parser) < threshold:
            print m
        else:
            pass

def _prob_block(multiSentence, POS_parser):
    """Calculate probability of email block."""
    try:
        multiSentence = unicode(multiSentence)
        parsedData = POS_parser(multiSentence)
        for span in parsedData.sents:
            sent = [parsedData[i] for i in range(span.start, span.end)]
        non_verbs = np.sum([token.pos_ != 'VERB' for token in sent])
        total = len(sent)
        return float(non_verbs) / total
    except:
        return 0