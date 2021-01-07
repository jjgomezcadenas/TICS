import numpy as np
from   typing import Tuple, List
from numpy import sqrt

NN = np.nan

# Binning data

def bin_data_with_equal_bin_size(data     : List[np.array],
                                 bin_size : float)->List[np.array]:
    """
    Given a list of numpy arrays (or any sequence with max() and min())
    and a bin size (the same for all arrays) return arrays with the bin edges

    """
    BinData = []
    for x in data:
        nbins = int((x.max() - x.min()) / bin_size) + 1
        xbins = np.histogram_bin_edges(x, nbins)
        BinData.append(xbins)
    return BinData
