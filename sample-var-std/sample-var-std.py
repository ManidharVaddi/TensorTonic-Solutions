import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with  and .
    """
    # Write code here
    dict = {}
    s2 = 0
    avg = sum(x)/len(x)
    for i in range(len(x)):
        s2 += ((x[i] - avg) ** 2)
    var = s2/(len(x) - 1)
    sd = var ** 0.5
        
    dict['variance'] = var
    dict['standard_deviation'] = sd

    return dict