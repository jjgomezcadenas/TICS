import numpy as np
import pandas as pd
from pandas import DataFrame
from typing import Tuple, List
from typing import TypeVar
from typing import Union

Range = TypeVar('Range', Tuple[float, float], int)

def get_class_name(cls):
    name = f"{type(cls)}"
    return name.split(".")[-1].split(">")[0][0:-1]
