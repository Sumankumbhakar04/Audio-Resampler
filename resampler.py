
import numpy as np
from scipy.signal import resample_poly
from math import gcd

def resample_audio(audio, original_rate, target_rate):

    common = gcd(original_rate, target_rate)

    up = target_rate // common
    down = original_rate // common

    converted_audio = resample_poly(
        audio,
        up,
        down
    )

    return converted_audio
