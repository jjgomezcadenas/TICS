import numpy as np
from   typing import Tuple, List
from numpy import sqrt

NN = np.nan

def in_range(data, minval=-np.inf, maxval=np.inf):
    """
    Find values in range [minval, maxval).

    Parameters
    ---------
    data : np.ndarray
        Data set of arbitrary dimension.
    minval : int or float, optional
        Range minimum. Defaults to -inf.
    maxval : int or float, optional
        Range maximum. Defaults to +inf.

    Returns
    -------
    selection : np.ndarray
        Boolean array with the same dimension as the input. Contains True
        for those values of data in the input range and False for the others.
    """
    return (minval <= data) & (data < maxval)


def relative_error_ratio(a : float, sigma_a: float,
                         b :float, sigma_b : float) ->float:
    """
    Error of a/b

    """
    return sqrt((sigma_a / a)**2 + (sigma_b / b)**2)


def mean_and_std(x      : np.array,
                 range_ : Tuple[float, float])->Tuple[float, float]:
    """
    Computes mean and std for an array within a range:
    takes into account nans

    """

    mu = NN
    std = NN

    if np.count_nonzero(np.isnan(x)) == len(x):  # all elements are nan
        mu  = NN
        std  = NN
    elif np.count_nonzero(np.isnan(x)) > 0:
        mu = np.nanmean(x)
        std = np.nanstd(x)
    else:
        x = np.array(x)
        if len(x) > 0:
            y = x[in_range(x, *range_)]
            if len(y) == 0:
                print(f'warning, empty slice of x = {x} in range = {range_}')
                print(f'returning mean and std of x = {x}')
                y = x
            mu = np.mean(y)
            std = np.std(y)

    return mu, std


def gaussian_experiment(nevt : int = 1000,
                        mean : float  = 100,
                        std  : float  = 10)->np.array:

    Nevt  = int(nevt)
    e  = np.random.normal(mean, std, Nevt)
    return e


def gaussian_experiments(mexperiments : int   = 1000,
                         nsample      : int   = 1000,
                         mean         : float    = 1e+4,
                         std          : float    = 100)->List[np.array]:

    return [gaussian_experiment(nsample, mean, std) for i in range(mexperiments)]


def gaussian_experiments_variable_mean_and_std(mexperiments : int   = 1000,
            nsample      : int                  = 100,
            mean_range   : Tuple[float, float]  = (100, 1000),
            std_range    : Tuple[float, float]  = (1, 50))->List[np.array]:
    """
    Run mexperiments gaussina experiments each with nsample samples
    """
    Nevt   = mexperiments
    sample = nsample
    stds   = np.random.uniform(low=std_range[0],  high=std_range[1],
                                                  size=sample)
    means  = np.random.uniform(low=mean_range[0], high=mean_range[1],
                                                  size=sample)
    exps   = [gaussian_experiment(Nevt, mean,
                                        std) for mean in means for std in stds]
    return means, stds, exps


def smear_e(e : np.array, std : float)->np.array:
    """
    Gaussian smearing to array (e)
    """
    return np.array([np.random.normal(x, std) for x in e])


# Binning data

def bin_data_with_equal_bin_size(data     : List[np.array],
                                 bin_size : float)->List[np.array]:
    """
    Given a list of numpy arrays (or any sequence with max() and min())
    and a bin size (the same for all arrays) return arrays with the bin edges

    """
    BinData = []
    for x in data:
        nbins = int((x.max() - x.min()) / bin_size)
        assert nbins >= 1, "bin size must be at least same size that xmax-xmin"
        _, bin_edges = np.histogram(x, bins=nbins + 1)
        #xbins = np.linspace(x.min(), x.max(), nbins)
        BinData.append(bin_edges)
    return BinData
