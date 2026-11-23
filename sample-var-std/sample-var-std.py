import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x)
    n = len(x)
    variance = float((1 / (n-1)) * np.sum((x - np.mean(x))**2))
    sd = float(np.sqrt(variance))
    dic = {
        "variance" : variance,
        "standard_deviation" : sd
    }
    return dic