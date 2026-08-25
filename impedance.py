#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:38:28 2026

@author: mikinakajima
"""


import numpy as np

# input parameter 
u_pH = 2864.0 #estimated shock particle shock velocity of MgO (Hugoniot)
rho0= 3560  #MgO initial density
gamma = 1.5# Gruneisen parameter for MgO 

u_int = 3500 # interface velocity (measurements)
K_S = 160e9 #bulk modules for MgO
rho0_LiF =  2640 #LiF density
###

# Hugoniot info for MgO
U_sH = 7049 + 1.24 * u_pH 
P_H = rho0 * U_sH * u_pH
rho_H = rho0 * U_sH/(U_sH - u_pH) 
T_H = 0.702 * (P_H*1e-9)**1.604 + 193.438


#Hugoniot info for LiF
U_LiF = 5144 + 1.355 * u_int
P_int = rho0_LiF * U_LiF * u_int


rho_int = rho_H * np.exp((P_int - P_H)/K_S) # density of MgO at the interface. rough estimate - needs a better model
T_int = T_H * (rho_int/rho_H) # temperature of MgO at the interface

# this calculates the interface particle velocity. Adjust u_pH until u_int_calc ~ u_int
u_int_calc = u_pH + 2.0/(gamma-1.0) *np.sqrt(gamma*P_H/rho_H)*(1-(P_int/P_H)**((gamma-1.0)/(2.0*gamma)))
print('calculated particle velocity (m/s) at the interface =', u_int, 'input particle velocity =', u_int_calc, 'interface temperature=', T_int, 'Hugoniot temperature=',T_H)