import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    y = np.asarray(y)
    if y.size == 0 :
        return 0.0
    _ , counts = np.unique(y,return_counts=True)
    probs = counts / counts.sum()
    probs = probs[probs > 0]
    return float(- np.sum(probs * np.log2(probs)))