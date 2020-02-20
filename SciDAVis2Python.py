# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:03:21 2020

@author: Gianl
"""


from scipy.optimize import curve_fit
import numpy as np
import matplotlib
import argparse
import pandas as pd
from Plot import plot
import os
import random
#Define the data to be fit with some noise:

def func_ale (x, wn_x, wn_y, eta_x, eta_y, k_x, k_y):
    #la funzione è ok
    return np.sqrt(((1-(x/wn_x)**2)/(((1-(x/wn_x)**2)**2+eta_x**2)*k_x)+(-eta_y/(((1-(x/wn_y)**2)**2+eta_y**2)*k_y)))**2+((-eta_x/(((1-(x/wn_x)**2)**2+eta_x**2)*k_x))+(-(1-(x/wn_y)**2)/(((1-(x/wn_y)**2)**2+eta_y**2)*k_y)))**2)

def set_p0_rule(x_data, parameters,tolerance):
    #usare x_data per settarli
    wn_x = random.uniform(np.max(x_data) - tolerance/100*np.max(x_data), np.max(x_data) + tolerance/100*np.max(x_data))
    wn_y = wn_x
    #wn_y = random.uniform(np.max(y_data) - tolerance/100*np.max(y_data), np.max(y_data) + tolerance/100*np.max(y_data))
    Eta_x = parameters[0]
    Eta_y = parameters[1]
    K_x = parameters[2]
    K_y = parameters[3]
    return np.array([wn_x, wn_y, Eta_x, Eta_y, K_x, K_y])

def main(directory_p, parameters, tolerance):
    #%%
    element = os.listdir(directory_p) #guardo tutti gli elementi nella directory
    #DA COMPLETARE LA RICERCA DEI FILE CSV OCCHIO ALLA VARIABILE I IN SAVEFIG
    #IMPLEMENTARE ANCHE IL SETTAGGIO DEI PARAMETRI INIZIALI
    for i in element:
        if i.split(".")[1] == "xls": #seleziono il primo file .csv
            #FUNZIONA SOLO PRIMA COLONNA ORA
            #colonne pari x colonne dispari y
            df = pd.read_excel(r"{}/{}".format(directory_p,i), encoding = "utf-8", header = 0)
            column = df.columns

            x_data = df.filter(regex="Frequenza")
            y_data = df.filter(regex="Ampiezza")
            for x,y in zip(x_data, y_data):
                x = x.dropna()
                y = y.dropna()
                p0 = set_p0_rule(x, parameters, tolerance) #IMPOSTARE BENE!!
                popt, pcov = curve_fit(func_ale, x_data, y_data, p0, method='lm')
            #   plot (????) #libreria nostra!
            #i.split["."][0]+"_"+"???"+"png



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument ("-d", "--directory", help = "Directory of .csv file", required = True)
    parser.add_argument ("-p", "--parameters", nargs = 4 ,help = "values of: Eta_x, Eta_y, K_x, K_y", required = True)
    parser.add_argument ("-t", "--tolerance", help = "% tolerance for wn_x and wn_y", required = False, default = 5 )
    args = parser.parse_args()
    directory_p = args.directory
    main(directory_p, args.parameters, args.tolerance)
