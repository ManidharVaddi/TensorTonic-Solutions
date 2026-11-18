from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    freq = Counter(x)
    hfrq = max(freq.values())
    modi = min(k for k,v in freq.items() if hfrq == v )
    x = np.array(x)
    avg = np.mean(x)
    meadi = np.median(x)

    dict = {}
    dict['mean'] = float(avg)
    dict['median'] = float(meadi)
    dict['mode'] = float(modi)
    
    return dict