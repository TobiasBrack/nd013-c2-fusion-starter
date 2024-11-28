# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np
import sympy as sp

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        pass

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############
        dt = params.dt
        F = np.identity(params.dim_state)
        dim = params.dim_state//2
        DT = dt*np.identity(dim)
        F[0:dim,dim:params.dim_state] = DT
        return F

        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############   
   
        # Define the symbols
        t, q_symbolic, dt_symbolic = sp.symbols('t q Δt')
        dim = params.dim_state//2

        # define F(t)
        F = sp.zeros(params.dim_state)
        for i in range(params.dim_state):
            F[i, i] = 1
        for i in range(dim):
            F[i, dim + i] = t

        # define q
        Qq = sp.zeros(params.dim_state)
        for i in range(dim):
            Qq[dim+i,dim+i] = q_symbolic

        # integrate
        integrand = F @ Qq @ F.T
        Q = sp.integrate(integrand, (t, 0, dt_symbolic))

        # substitute values
        subs_dict = {dt_symbolic: params.dt, q_symbolic: params.q}  # Substitute t=2, q=5
        Q = np.matrix(Q.subs(subs_dict), dtype='float64')
        return Q


        
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############
        F = self.F()
        P = track.P
        x = F*track.x # state prediction
        P = F*P*F.transpose() + self.Q() # covariance prediction
        track.set_x(x)
        track.set_P(P)
        
        
        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############

        H = meas.sensor.get_H(track.x) # measurement matrix
        P = track.P
        x = track.x
        K = P*H.transpose()*np.linalg.inv(self.S(track,meas,H)) # Kalman gain
        x = x + K*self.gamma(track, meas) # state update
        I = np.identity(params.dim_state)
        P = (I - K*H) * P # covariance update
        track.set_x(x)
        track.set_P(P)    
        
        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############
        Hx = meas.sensor.get_hx(track.x)
        gamma = meas.z - Hx
        return gamma
        
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############
        S = H*track.P*H.transpose() + meas.R
        #S = np.array(S, dtype='float64')
        return S
        
        ############
        # END student code
        ############ 