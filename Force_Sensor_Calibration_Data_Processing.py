from Force_Sensor_Calibration_Data_Preparation import F, R

import numpy as np

# from sklearn.pipeline      import make_pipeline
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model  import LinearRegression
# 
# from copy import copy

# from scipy.optimize import curve_fit

from numpy.polynomial import Polynomial

import matplotlib.pyplot as plt

####################################################################################################

# polynomial_order = 2
# 
# linear_regressor = LinearRegression()
# 
# pipeline = make_pipeline(PolynomialFeatures(polynomial_order), linear_regressor)
# pipeline.fit(R.reshape(-1, 1), F.reshape(-1, 1))

# def predictor(x, p_0, p_1, p_2):
#     
#     y = p_0 + p_1 * x + p_2 * x**2
#     
#     return y
# 
# p, _ = curve_fit(predictor, R, F)

polynomial_order = 2

best_fit_curve = Polynomial.fit(R, F, polynomial_order)

####################################################################################################

S_max = best_fit_curve.deriv()(min(best_fit_curve.roots()))
S_min = best_fit_curve.deriv()(max(R))

print('')
print(f'Minimum assumed sensitivity: {S_max} N/Ω')
print(f'Maximum assumed sensitivity: {S_min} N/Ω')

####################################################################################################

# coefs    = copy(linear_regressor.coef_[0])
# coefs[0] = copy(linear_regressor.intercept_[0])

# coefs = p

coefs = best_fit_curve.coef

print('')
print('You may copy this into your microcontroller C/C++/Arduino code for your calibration curve fit:')
print('')

template = ''.join(open('Force_Sensor_Calibration_Code_Template.txt').readlines())

print(template.replace('[R_min]', f'{min(best_fit_curve.roots())}') \
              .replace('[R_max]', f'{max(R)}') \
              .replace('[Polynomial_Eqn]', 'F = ' + ' + '.join([f'{coef} * pow(R, {degree})' for degree, coef in enumerate(coefs)])))
print('')

####################################################################################################

plt.figure(tight_layout = True)

plt.plot(R, F, '.', label = 'Calibration Data Points')

x_vals = np.linspace(min(best_fit_curve.roots()), max(R), 100)
y_vals = best_fit_curve(x_vals)  # predictor(x_vals, *p)  # pipeline.predict(x_vals.reshape(-1, 1))

plt.plot(x_vals, y_vals, 'k', label = 'Calibration Curve Fit')

plt.legend()

plt.xlabel('\n Resistance R = R_elem − R_elem_ref [Ω] \n')
plt.ylabel('\n Force F [N] \n')

plt.title('\n Force Sensor Calibration \n')

plt.show()

while True:
    pass
