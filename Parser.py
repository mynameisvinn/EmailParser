from spacy.en import English
import numpy as np
import codecs

def read_email(fname):
    """Read email as unicode."""
    f = codecs.open(fname, encoding='utf-8')
    text = f.read()
    msg = text.encode('utf-8')
    return msg

def strip(msg):
    """Remove new lines."""
    return msg.strip().split('\n')

def prob_block(multiSentence, parser):
    """Calculate probability of email block."""
    try:
        multiSentence = unicode(multiSentence)
        parsedData = parser(multiSentence)
        for span in parsedData.sents:
            sent = [parsedData[i] for i in range(span.start, span.end)]
        non_verbs = np.sum([token.pos_ != 'VERB' for token in sent])
        total = len(sent)
        return float(non_verbs) / total
    except:
        return 0