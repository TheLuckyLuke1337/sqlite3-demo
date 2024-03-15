from astropy.constants import sigma_sb
import numpy as np
print(sigma_sb.value, sigma_sb.unit)


def diameter(luminosity, temperature):

    return 2*np.sqrt(luminosity / (4 * np.pi * sigma_sb.value * temperature**4))
