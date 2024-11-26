def update(mu,s2,mu_meas,s2_meas):
    mu_new = 1/(s2 + s2_meas) * (mu*s2_meas + mu_meas*s2)
    s2_new = 1/(1/s2 + 1/s2_meas)
    return mu_new, s2_new

def predict(mu1,var1,mu2,var2):
    mu_new = mu1 + mu2
    var_new = var1 + var2
    return mu_new, var_new


# Test Kalman Code
measurements = [5,6,7,8,10]
motion = [1,1,2,1,1]
s2_meas = 4
s2_motion = 2
mu = 0
s2 = 0.000000001

for n in range(len(measurements)):
    # motion update
    [mu,s2] = update(mu, s2,measurements[n],s2_meas)
    print(f"update: mu = {mu:.5f}, s2 = {s2:.5f}")
    # prediction
    [mu,s2] = predict(mu,s2,motion[n],s2_motion)
    print(f"prediction: mu = {mu:.5f}, s2 = {s2:.5f}")



