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
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Lift vs Speed
axs[0, 0].plot(V, Lift, label="Lift")
axs[0, 0].axhline(W_N, color='r', linestyle='--', label="Weight")
axs[0, 0].set_xlabel("Speed (m/s)")
axs[0, 0].set_ylabel("Lift (N)")
axs[0, 0].set_title("Lift vs Speed")
axs[0, 0].grid(True)
axs[0, 0].legend()

# Drag vs Speed
axs[0, 1].plot(V, Parasite, label="Parasite Drag")
axs[0, 1].plot(V, Induced, label="Induced Drag")
axs[0, 1].plot(V, TotalDrag, label="Total Drag")
axs[0, 1].set_xlabel("Speed (m/s)")
axs[0, 1].set_ylabel("Drag (N)")
axs[0, 1].set_title("Drag vs Speed")
axs[0, 1].grid(True)
axs[0, 1].legend()

# Thrust Required vs Available
axs[1, 0].plot(V, ThrustRequired, label="Thrust Required")
axs[1, 0].plot(V, ThrustAvailable, label="Thrust Available")
axs[1, 0].set_xlabel("Speed (m/s)")
axs[1, 0].set_ylabel("Thrust (N)")
axs[1, 0].set_title("Thrust Required vs Thrust Available")
axs[1, 0].grid(True)
axs[1, 0].legend()

# Rate of Climb vs Speed
axs[1, 1].plot(V, RateOfClimb, label="Rate of Climb")
axs[1, 1].axhline(0, color='r', linestyle='--', label="Level Flight (RoC = 0)")
axs[1, 1].set_xlabel("Speed (m/s)")
axs[1, 1].set_ylabel("Rate of Climb (m/s)")
axs[1, 1].set_title("Rate of Climb vs Speed")
axs[1, 1].grid(True)
axs[1, 1].legend()

plt.tight_layout()

plt.show()



