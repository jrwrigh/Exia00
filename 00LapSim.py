# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 21:55:08 2016

@author: jrwrigh
"""

from Track import *
from Car import *
from Tire import *
import Constants as const
import numpy as np
import scipy as sp




        
corner1=Corner(7,19)
tire=Tire(1.2,0.4826)
tiger19=Car(204,-1.204,0.567,0.608)

print tiger19

print corner1.V_max(tiger19,tire)
print corner1.time(tiger19,tire)

"""Straight calculation Scratch"""

Tau=59 #N*m
v0=14


def accelbalance(t,car,tire,Tau,v0): #time,car,tire,Torque to tire,initial velocity
    alpha=car.massv/(Tau*tire.radius)
    beta=(2*car.massv)/(car.cd*const.rhoair*car.frontarea)
    c=-(alpha*v0+beta/v0)    
    return (((c-t)**2-4*alpha*beta)**0.5-c+t)/(2*alpha)
    

# (Tau=torque,alpha=alpha,beta=beta,v0=14)
print sp.integrate.quad(accelbalance,0,1,args=(tiger19,tire,Tau,v0))


def brakebalance(u,t,car,tire,v0):
    u1, u2=u
        #u1=x u2=x'
    beta=(2*car.massv)/(car.cd*const.rhoair*car.frontarea)
    gamma=(2*car.massv)/(car.cl*const.rhoair*car.frontarea)
    uprime=[u2 , -tire.mu * sp.constants.g - ( 1/gamma + 1/beta ) * u2]
    return uprime
    
    
print sp.integrate.odeint(brakebalance,[0,14],np.linspace(0,2,100),args=(tiger19,tire,v0))