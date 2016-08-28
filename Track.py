# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 16:23:24 2016

@author: jrwrigh
"""
import scipy.optimize
import scipy.constants as spconst
import Constants as const
import numpy as np


class Track(object):
    def __init__(self):
        self._features=[]
    
    def add_feature(self,feature):
        self._features.append(feature)

    def num_features(self):
        return len(self._features) - 1
        
    def show_featuers(self):
        pass
    
class Corner(object):
    def __init__(self,radius,length):
        self.radius=radius
        self.length=length
   
    def V_max(self,car,tire):
#        def V_balance(V):
#            return np.absolute(((car.cl * car.frontarea * tire.mu * const.rhoair * .5) - (car.massv / 
#            self.radius) ) * V ** 2 + car.massv * spconst.g * tire.mu)
#        return scipy.optimize.minimize_scalar(V_balance).x
        return ((-car.massv*spconst.g*tire.mu)/((car.cl * car.frontarea * tire.mu * const.rhoair * .5) - (car.massv / 
            self.radius)))**0.5
    def time(self,car,tire):
        return self.V_max(car,tire)/self.length
        
class Straight(object):
    def __init__(self,length):
        self.length=length

class EndFeature(object):
    def __init__(self):
        pass
    