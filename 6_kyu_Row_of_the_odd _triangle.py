import numpy as np

def odd_row(n):
    return np.arange((n * n + (n - 1)) - (2 * n - 2), n * n + (n - 1) + 2, 2).tolist()
