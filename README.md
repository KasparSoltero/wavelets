Implementation of the discrete wavelet transform and associated processing functions.

Usage: import wavelets as wl:

wl.multires (Multiple-resolution analysis) repeatedly decomposes the approximate coefficients. Because the approximate coefficients represent the low frequency part of the signal,
each level analyses a lower frequency portion of the signal.

    [signal]──┬─>[cD1] ┄┄┄┄┄┄┄┄┄┄┄┄┄┄[cD1]        level 1
              └─>[cA1]──┬─>[cD2]┄┄┄┄┄[cD2]        level 2
                        └─>[cA2]──┬─>[cD3]        level 3
                                  └─>[cA3]

Each decomposition splits the signal into a higher and lower frequency component,
so the frequencies spanned by the final sets of coefficients e.g.:

    cD1: 1000 - 500 Hz
    cD2: 500 - 250 Hz
    cD3: 250 - 125 Hz
    cA3: 125 - 0 Hz

wl.inverseMultires reconstructs the original signal from the set of coefficients generated by multi-resolution analysis. In reverse to multi-resolution decomposition, it iteratively reconstructs each approximate coefficient array from the lower level

    [cD1]──────────────────────┬─>[signal]
    [cD2]────────────┬─>[cA1]──┘
    [cD3]──┬─>[cA2]──┘
    [cA3]──┘