# Gamma-burst impact calculator
#===========================
# These variables are the main parameters of the gamma-burst
L = 3                       # Distance, in parsec
E = 20000000                # Burst energy, in joules * 10^(45)
WL = 0.02                   # Peak wavelenght, in nanometers
DELTA_WL = 0.002           # The wavelength range to perform calculations in, in nanometers
t = 5                       # Duration of the gamma-burst, in seconds
#===========================
# These variables are the main simulation parameters, it is not advised to change them unless you need to make them more specific
R = 20000                   # The radius for black body-related calculations, in meters
M = 10                      # The mass of the simulation satellite, in kg
S = 1                       # The surface area of the satellite receiving the energy from the gamma-burst, in m^2
W_CRIT = 53450              # The critical energy-to-weight ratio to have a crucial impact on the satellite, in J/kg
#===========================
# Performing the calculations
from scipy import constants as con
from decimal import Decimal, localcontext
from math import e as euler

with localcontext() as ctx:
    ctx.prec = 100  # 100 digits precision
    T = Decimal(0)
    T = Decimal(Decimal(Decimal(E)*Decimal(Decimal(10)**Decimal(45))/Decimal(t)/(Decimal(4)*Decimal(con.pi)*Decimal(con.sigma)*Decimal(R**2)))**Decimal(1/4)) # Black Body temperature
    B_l = Decimal(DELTA_WL)*Decimal(con.nano) * Decimal(Decimal(2)*Decimal(con.Planck)*Decimal(Decimal(con.c)**Decimal(2)))/Decimal(Decimal(Decimal(WL)*Decimal(con.nano))**Decimal(5)) * Decimal(1)/Decimal(Decimal(Decimal(euler)**Decimal(Decimal(Decimal(con.Planck)*Decimal(con.c))/Decimal(Decimal(WL)*Decimal(con.nano)*Decimal(con.k)*Decimal(T))))-Decimal(1))
    W = Decimal(B_l) * Decimal(R)**Decimal(2) / Decimal(Decimal(Decimal(L)*Decimal(con.parsec))**Decimal(2)) * Decimal(S)/Decimal(M) * Decimal(t)
    i = float(W/W_CRIT) # Safety coefficient
if i < 0.5:
    print("The gamma-burst you're analyzing is an S-category burst (Safe), with Safety coefficient of " + str(round(i, 6)))
elif i >= 0.5 and i < 1:
    print("The gamma-burst you're analyzing is an A-category burst (Average Danger), with Safety coefficient of " + str(round(i, 6)))
elif i > 1:
    print("The gamma-burst you're analyzing is a D-category burst (Dangerous), with Safety coefficient of " + str(round(i, 6)))