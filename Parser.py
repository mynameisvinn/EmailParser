import codecs
import numpy as np
from spacy.en import English

def read_email(fname):
    """Read email as unicode."""
    with codecs.open(fname, encoding='utf-8') as f:
        text = f.read().encode('utf-8')
    return text

def strip(msg):
    return msg.strip().split('\n')

def generate_text(msg, threshold, POS_parser, fname):
    """
    For each line, determine if line is signature block. 

    If prob(signature block) is less than the defined threshold, write
    line to file.

    Parameters
    ----------
    msg : str
        Represents line in email block.
    threshold: float
        Lower thresholds will result in more false positives.
    POS_parser: obj
        Spacy English object used to tag parts-of-speech. Will explore using
        other POS taggers like NLTK's.
    """
    with open(fname, "w") as f:
        for m in msg:
            if _prob_block(m, POS_parser) < threshold:
                f.write(unicode(m, 'utf8'))
    print "complete"
    return True

def _prob_block(multiSentence, POS_parser):
    """Calculate probability of email block.

    Parameters
    ----------
    multiSentence : str
        Line in email block.
    POS_parser : obj
        A POS tagger object. This version relies on Spacy's English POS-tagger.

    Returns
    -------
    probability(signature block | line)
    """
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