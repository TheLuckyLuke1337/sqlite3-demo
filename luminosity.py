from numpy import pi as π
import astropy.units as u


def luminosity(flux, distance):
    result = []
    fluxes = list(flux)
    distances = list(distance)
    for flux, distance in zip(fluxes, distances):
        distance = 2 * (distance * u.pc).to(u.R_sun)
        result.append(4 * π * (flux * u.M_bol).to(u.W) * distance**2)
    return result
