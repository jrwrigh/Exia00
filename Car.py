# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 18:46:56 2016

@author: jrwrigh
"""

class Car(object):
    def __init__(self,massv,cl,cd,frontarea):
        self.massv=massv
        self.cl=cl
        self.cd=cd
        self.frontarea=frontarea
     
    def __str__(self):
        return "Vehicle Mass:............ %s \nCoefficient of Lift:.... %s \nCoefficienct of Drag:.... %s \nFrontal Area:............ %s" % (self.massv,self.cl,self.cd, self.frontarea)
    