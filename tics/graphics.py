import numpy as np
import pandas as pd
import os, sys

from scipy.linalg import norm

from  . system_of_units import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


from typing import Tuple, List


def set_fonts(ax, fontsize=20):
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(fontsize)
