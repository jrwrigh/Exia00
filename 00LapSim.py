# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 21:55:08 2016

@author: jrwrigh
"""

from Track import *
from Car import *
from Tire import *




        
corner1=Corner(7,19)
tire=Tire(1.2)
tiger19=Car(204,-1.204,0.567,0.608)

print tiger19

print corner1.V_max(tiger19,tire)
print corner1.time(tiger19,tire)

