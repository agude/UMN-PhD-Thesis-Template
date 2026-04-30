import numpy as np
from bilby.core.prior import Constraint, Cosine, Sine, Uniform
from bilby.gw.prior import (
    UniformInComponentsChirpMass,
    UniformInComponentsMassRatio,
    UniformSourceFrame,
)

mass_1 = Constraint(name='mass_1', minimum=5, maximum=200)
mass_2 = Constraint(name='mass_2', minimum=5, maximum=200)
mass_ratio = UniformInComponentsMassRatio(
    name='mass_ratio',
    minimum=0.125,
    maximum=1,
)
chirp_mass = UniformInComponentsChirpMass(
    name='chirp_mass',
    minimum=15,
    maximum=200,
)
luminosity_distance = UniformSourceFrame(
    name='luminosity_distance',
    minimum=1e2,
    maximum=3.5e4,
)
dec = Cosine(name='dec')
ra = Uniform(name='ra', minimum=0, maximum=2 * np.pi, boundary='periodic')
theta_jn = Sine(name='theta_jn')
psi = Uniform(name='psi', minimum=0, maximum=np.pi, boundary='periodic')
phase = Uniform(name='phase', minimum=0, maximum=2 * np.pi, boundary='periodic')
a_1 = Uniform(name='a_1', minimum=0, maximum=0.99)
a_2 = Uniform(name='a_2', minimum=0, maximum=0.99)
tilt_1 = Sine(name='tilt_1')
tilt_2 = Sine(name='tilt_2')
phi_12 = Uniform(name='phi_12', minimum=0, maximum=2*np.pi, boundary='periodic')
phi_jl = Uniform(name='phi_jl', minimum=0, maximum=2*np.pi, boundary='periodic')
