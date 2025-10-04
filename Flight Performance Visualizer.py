"""
- Lift vs Speed
- Parasite / Induced / Total Drag vs Speed
- Thrust Required vs Thrust Available
- Rate of Climb vs Speed
"""

import numpy as np
import matplotlib.pyplot as plt
W_N      = 5000# Weight [N]
S_m2     = 18# Wing area [m^2]
CD0      = 0.025# Zero-lift drag coefficient
AR       = 7# Aspect ratio
e        = 0.8# Oswald efficiency factor
h_m      = 0# Altitude [m]
T_max_N  = 1800# Max thrust available [N]
g        = 9.81

V = np.linspace(20, 120, 200)# Speeds from 20 to 120 m/s
# ISA Density Function
def isa_density(h):
    T0 = 288.15
    p0 = 101325
    R = 287.058
    L = -0.0065
    if h < 0: h = 0
    if h <= 11000:
        T = T0 + L*h
        p = p0 * (T/T0)**(-g/(R*L))
        rho = p / (R*T)
    else:
        T = T0 + L*11000
        p = p0 * (T/T0)**(-g/(R*L))
        rho = p / (R*T)
    return rho

rho = isa_density(h_m)
k = 1 / (np.pi * AR * e)
# Calculations
CL = 2*W_N / (rho * V**2 * S_m2)
CD = CD0 + k * CL**2
q = 0.5 * rho * V**2

Lift = q * S_m2 * CL
Parasite = q * S_m2 * CD0
Induced = q * S_m2 * (CD - CD0)
TotalDrag = Parasite + Induced
ThrustRequired = TotalDrag
ThrustAvailable = np.ones_like(V) * T_max_N
RateOfClimb = (ThrustAvailable - TotalDrag) * V / W_N
# Plots
plt.figure()
plt.plot(V, Lift, label="Lift")
plt.axhline(W_N, color='r', linestyle='--', label="Weight")
plt.xlabel("Speed (m/s)")
plt.ylabel("Lift (N)")
plt.title("Lift vs Speed")
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(V, Parasite, label="Parasite Drag")
plt.plot(V, Induced, label="Induced Drag")
plt.plot(V, TotalDrag, label="Total Drag")
plt.xlabel("Speed (m/s)")
plt.ylabel("Drag (N)")
plt.title("Drag vs Speed")
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(V, ThrustRequired, label="Thrust Required")
plt.plot(V, ThrustAvailable, label="Thrust Available")
plt.xlabel("Speed (m/s)")
plt.ylabel("Thrust (N)")
plt.title("Thrust Required vs Thrust Available")
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(V, RateOfClimb, label="Rate of Climb")
plt.axhline(0, color='r', linestyle='--',label="Speed")
plt.xlabel("Speed (m/s)")
plt.ylabel("Rate of Climb (m/s)")
plt.title("Rate of Climb vs Speed")
plt.grid(True)
plt.legend()

plt.show()

