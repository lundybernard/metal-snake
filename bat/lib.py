from typing import List, Dict

import numpy as np
from scipy.spatial.distance import cdist


def minimize_distance(features: List[Dict[str, bool]]) -> int:
    # convert features to list of Binary Lists
    bin_matrix = [
        [d[k] for d in features]
        for k, v in features[0].items()
    ]

    # perform a distance-transform on each list
    # ex: [1, 0, 0, 0, 1] => [0, 1, 2, 1, 0]
    distmap = np.array([distance_transform(L) for L in bin_matrix])
    '''
    [[0 1 1 0 1 2]
     [3 2 1 0 1 0]
     [0 0 1 1 0 1]]
    '''
    print(f'{distmap=}')
    print(f'{distmap.T=}')
    ret = distmap.T.sum(axis=1)
    print(f'{ret=}')
    ret = ret.argmin()
    print(f'{ret=}')
    return ret



def distance_transform(A: List[bool]) -> List[int]:
    A = np.array(A)
    print(f'{A=}')
    a = np.argwhere(A)
    na = np.argwhere(~A)

    m = np.zeros(A.shape, dtype=int)
    print(f'{m=}')
    m[tuple(na.T)] = cdist(a, na, 'cityblock').min(0, initial=len(A))
    print(f'{m=}')

    return m


def hello_world():
    return 'Hello World!'
