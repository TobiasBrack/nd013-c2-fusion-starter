import numpy as np



def kalman_filter(x, P, u, F, H, R, I, measurements):
    for n in range(len(measurements)):
        pass # TODO
        # measurement update
        Z = np.matrix([[measurements[n]]])
        y = Z - (H * x)
        S = H * P * np.transpose(H) + R
        K = P * np.transpose(H) * np.linalg.inv(S)
        x = x + (K * y)
        P = (I - (K * H)) * P

        # prediction
        x = (F * x) + u
        P = F * P * np.transpose(F)
        
        
    return x,P

measurements = [1, 2, 3]

x = np.matrix([[0.], [0.]]) # initial state (location and velocity)
P = np.matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = np.matrix([[0.], [0.]]) # external motion
F = np.matrix([[1., 1.], [0, 1.]]) # next state function
H = np.matrix([[1., 0.]]) # measurement function
R = np.matrix([[1.]]) # measurement uncertainty
I = np.matrix([[1., 0.], [0., 1.]]) # identity matrix

print(kalman_filter(x, P, u, F, H, R, I, measurements))