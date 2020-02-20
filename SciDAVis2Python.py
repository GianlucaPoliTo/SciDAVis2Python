# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:03:21 2020

@author: Gianl
"""


import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import matplotlib
import argparse
import pandas as pd

matplotlib.rcParams.update({'font.size': 30})
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 22
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 25
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['figure.titlesize'] = 15
plt.ioff()

#Define the data to be fit with some noise:

def func_ale (x, wn_x, wn_y, eta_x, eta_y, k_x, k_y): 

    return np.sqrt(((1-(x/wn_x)**2)/(((1-(x/wn_x)**2)**2+eta_x**2)*k_x)+(-eta_y/(((1-(x/wn_y)**2)**2+eta_y**2)*k_y)))**2+((-eta_x/(((1-(x/wn_x)**2)**2+eta_x**2)*k_x))+(-(1-(x/wn_y)**2)/(((1-(x/wn_y)**2)**2+eta_y**2)*k_y)))**2)

def main(directory_p):
    element = os.listdir(directory_p)
    #DA COMPLETARE LA RICERCA DEI FILE CSV OCCHIO ALLA VARIABILE I IN SAVEFIG
    #IMPLEMENTARE ANCHE IL SETTAGGIO DEI PARAMETRI INIZIALI
    for i in element:
        if i.split(".")[1] == "csv":
            
            p0 = np.array([192, 190, 0.05, 0.03, 10, 11])
            wn_x = 194.339182788087
            wn_y = 195.688030521315
            Eta_x = 0.05
            Eta_y = 0.03
            K_x = 10
            K_y = 11
                        
            df = pd.read_excel(r"C:\Users\Gianl\Downloads\Telegram Desktop\Data.xls", encoding = "utf-8")  #colonne pari x colonne dispari y
            x_data = df["Frequenza 1"]
            y_data =df["Ampiezza 1"]
            
            x_data = x_data.dropna()
            y_data = y_data.dropna()
     
            plt.figure(figsize = [16,9])
            plt.plot(x_data, y_data, 'b.', label='data')
            popt, pcov = curve_fit(func_ale,x_data, y_data, p0 = p0, method='lm')
            
            plt.plot(x_data, func_ale(x_data, *popt), 'g-',
                     label='fit: wn_x=%5.3f, wn_y=%5.3f, Eta_x=%5.3f, Eta_y=%5.3f, k_x=%5.3f, \
                     Eta_y=%5.3f' % tuple(popt))
            
            plt.xlabel('x')
            plt.ylabel('y')
            plt.legend()
            plt.grid()
            plt.savefig(i.split["."][0]+"_"+"???"+"png", dpi = 300)
            plt.close()



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument ("-d", "--directory", help = "Directory of .csv file", required = True)
    args = parser.parse_args()
    directory_p = args.directory
    main(directory_p)