import numpy  as np
import pandas as pd

pd.options.display.precision = 2

from numpy.polynomial import Polynomial

import matplotlib.pyplot as plt

####################################################################################################

fname = 'Force_Sensor_Calibration_Data_Log_Corrected_Converted_R_elem[-R_elem_ref].txt'

M_unit = 'g'  # Unit of measurement of mass.

M_units_per_kg = 1e3

i = 0
M = 0

i_list = []
M_list = []
R_list = []

markers = []

with open(fname) as buffer:
    
    for line in [line[:-1] for line in buffer.readlines()]:
        
        if line[-len(M_unit):] == M_unit:
            
            i = i + 1/2
            M = float(line[:-len(M_unit)])
            
            markers.append(line)
            
        elif len(markers) % 2 == 0:
            
            R = float(line)
            
            i = round(i)
            
            R_list.append(R)
            M_list.append(M)
            i_list.append(i)

del i, M, R

####################################################################################################

df = pd.DataFrame({'i': i_list, 'M': M_list, 'R': R_list})

df_M = df.pivot_table(columns = 'i', values = 'M').transpose()

df_F = df_M / M_units_per_kg * 9.81;  df_F.columns = ['F']

def aggregate_R(df, aggfunc, name):
    
    df_R_ = df.pivot_table(columns = 'i', values = 'R', aggfunc = aggfunc).transpose()
    df_R_.columns = [name]
    
    return df_R_

def trendline(R_vals):
    
    return Polynomial.fit(np.arange(len(R_vals)), R_vals, 1, window = [0, len(R_vals)])

def drift(R_vals):
    
    slope = trendline(R_vals).coef[1]
    
    return slope

def drift_corrected_var(R_vals):

    return np.var(R_vals - trendline(R_vals)(R_vals) + np.mean(R_vals))

df_R_count       = aggregate_R( df, 'count'             , 'R_count'               )
df_R_mean        = aggregate_R( df, 'mean'              , 'R_mean'                )
df_R_var         = aggregate_R( df, 'var'               , 'R_var'                 )
df_R_drift       = aggregate_R( df,  drift              , 'Relative Drift Rate'   )
df_R_undrift_var = aggregate_R( df,  drift_corrected_var, 'Drift-Corrected R_var' )

#  M                      Mass of the applied load.
#  F                      Force calculated due to gravity acting on the mass.
#  R_count                The number of samples of sensor resistance values taken under the corresponding applied force.
#  R_mean                 The average resistance value.
#  R_var                  The statistical variance of resistance. A measure of sensor noise and noise from other sources.
#  Relative Drift Rate    A measure of sensor drift that may be compared within the same test setup.
#  Drift-Corrected R_var  The statistical variance of resistance after accounting for the relative drift rate.

####################################################################################################

if __name__ == '__main__':
    
    print('')
    print(df)
    print('')
    print(pd.concat([df_M, df_F, df_R_count, df_R_mean, df_R_var, df_R_drift], axis = 1))
    print('')
    
    plt.figure(tight_layout = True)
    
    plt.plot(R_list, drawstyle = 'steps-mid')
    
    plt.plot([df_R_mean.loc[i] for i in i_list], 'k', drawstyle = 'steps-mid')
    
    ylim = plt.ylim()
    
    partitions = np.argwhere(np.diff(i_list)) + 0.5
    
    plt.vlines(partitions, *ylim, 'k')
    
    plt.xlim(0, len(i_list))
    plt.ylim(ylim)
    
    plt.xlabel('\n Sample Number \n')
    plt.ylabel('\n Resistance R = R_elem[ − R_elem_ref] [Ω] \n')
    
    plt.title('\n  \n')
    
    plt.show()
    
    while True:
        pass
    
else:
    
    F = np.array(df_F     ).flatten()
    R = np.array(df_R_mean).flatten()
