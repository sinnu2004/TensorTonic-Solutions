import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    n = len(x)
    for i in range(n):
        if x[i] < 0.0 :
            x[i] = alpha * float(x[i])
    return x 