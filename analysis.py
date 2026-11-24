
import numpy as np
from scipy.signal import resample_poly
from math import gcd

def calculate_distortion(original, converted,
                         original_rate, target_rate):

    common = gcd(original_rate, target_rate)

    # Convert back to the original sampling rate
    reconstructed = resample_poly(
        converted,
        target_rate // common,
        original_rate // common,
        axis=0
    )
