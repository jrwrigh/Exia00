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

#print tiger19
#
#print corner1.V_max(tiger19,tire)
#print corner1.time(tiger19,tire)

"""Straight calculation Scratch"""

Tau=59 #N*m
v0=14

def accelbalance(t,car,tire,Tau,v0): #time,car,tire,Torque to tire,initial velocity
    alpha = car.massv / ( Tau * tire.radius )
    beta = ( 2*car.massv ) / ( car.cd * const.rhoair * car.frontarea )
    c = -( alpha * v0 + beta / v0 )    
    return ((( c - t )** 2 - 4 * alpha * beta )**0.5 - c + t ) / ( 2*alpha )

# (Tau=torque,alpha=alpha,beta=beta,v0=14)
#speed, err= sp.integrate.quad( accelbalance ,0,1, args=(tiger19 , tire , Tau , v0 ))
#print speed

def brakebalance(u,t,car,tire,v0):
    u1, u2=u
        #u1=x u2=x'
    beta=( 2*car.massv ) / ( car.cd * const.rhoair * car.frontarea )
    gamma=( 2*car.massv ) / ( tire.mu * car.cl * const.rhoair * car.frontarea )
    uprime=[u2 , -tire.mu * sp.constants.g - ( 1/gamma + 1/beta ) * u2**2]
    return uprime
  
#print sp.integrate.odeint(brakebalance,[0,14],np.linspace(0,2,100),args=(tiger19,tire,v0))

#Track must start and end with corner (can be same corner if continous track)
track1=Track()
track1.add_feature(Corner(10,25))
track1.add_feature(Straight(70))
track1.add_feature(Corner(10,25))
track1.add_feature(EndFeature)

def LapTimeCalc(Track,Car,Tire,tau):
    vlast=0.01
    dt=.001
    laptime=float(0)

    for i in range(Track.num_features()):
        print i
        feature = Track._features[i]        
        if isinstance(Track._features[i],EndFeature):
            next_feature=Track.features[0]            
        else:
            next_feature=Track._features[i+1]
               
        if isinstance(feature,Straight):
            v2=next_feature.V_max(Car,Tire) #Final speed on straight should equal max speed of next feature
            t=0 #time initialization
            speeds=[] #speeds list initialization
            speeds.append(vlast) #start speed on straight is last speed through
            count=0
            maxtime=feature.length/5 #maximum time spent on straight equal to length of straight divided by initial v
            deltadist=1
            accel_dist=0
            taccel=0
            while deltadist>0:
                speed, err = sp.integrate.quad( accelbalance ,0,dt, args=(Car , Tire , tau , speeds[count] ))
                speeds.append(speed)
                accel_dist += dt * ( speeds[count] + speeds[count+1] ) / 2
                taccel += dt
                
                    #TODO make time range change based on v1 of straight to end of straight
                tvalues = np.linspace( 0 , 5 ,  1000 )
                noftvalues = int(tvalues.shape[0])
                                #TODO replace sp.integrate.odeint with Crank Nicholson allow program to stop once v=v2
                brakedata = sp.integrate.odeint( brakebalance , [0,speeds[count+1]] , tvalues , args=( Car , Tire , speed))
                brakedata = np.array(brakedata)
                for i in range(0,noftvalues):
                    if brakedata[i,1] < v2:
                        brakedist = brakedata[i,1]
                        tbrake = (i+1) * dt / 10
                        break
                    else:
                        brakedist=0
                totdist = accel_dist + brakedist
                distances=[totdist,accel_dist,brakedist]
                print distances
                deltadist=feature.length-totdist
                #TODO add brake velocity data to speeds
#                print deltadist
                count += 1
            tstraight = taccel + tbrake
            laptime += tstraight

        elif isinstance(feature,Corner):
            velocity = feature.V_max( Car , Tire )
            length = feature.length
            tcorner = velocity * length
            laptime += tcorner

    
    return laptime
    
print LapTimeCalc(track1,tiger19,tire,Tau)

   