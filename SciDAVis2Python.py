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



#Define the data to be fit with some noise:

def func_ale (x, wn_x, wn_y, eta_x, eta_y, k_x, k_y):
    #la funzione è ok
    return np.sqrt(((1-(x/wn_x)**2)/(((1-(x/wn_x)**2)**2+eta_x**2)*k_x)+(-eta_y/(((1-(x/wn_y)**2)**2+eta_y**2)*k_y)))**2+((-eta_x/(((1-(x/wn_x)**2)**2+eta_x**2)*k_x))+(-(1-(x/wn_y)**2)/(((1-(x/wn_y)**2)**2+eta_y**2)*k_y)))**2)

def set_p0_rule(x_data, y_data):
    #usare x_data per settarli
    wn_x = 194.339182788087
    wn_y = 195.688030521315
    Eta_x = 0.05
    Eta_y = 0.03
    K_x = 10
    K_y = 11
    return np.array([wn_x, wn_y, Eta_x, Eta_y, K_x, K_y])

def main(directory_p):
    element = os.listdir(directory_p) #guardo tutti gli elementi nella directory
    #DA COMPLETARE LA RICERCA DEI FILE CSV OCCHIO ALLA VARIABILE I IN SAVEFIG
    #IMPLEMENTARE ANCHE IL SETTAGGIO DEI PARAMETRI INIZIALI
    for i in element:
        if i.split(".")[1] == "csv": #seleziono il primo file .csv
            p0 = set_p0_rule #IMPOSTARE BENE!!

            #FUNZIONA SOLO PRIMA COLONNA ORA
            df = pd.read_excel(r"C:\Users\Gianl\Downloads\Telegram Desktop\Data.xls", encoding = "utf-8")  #colonne pari x colonne dispari y
            column = df.column
            
            x_data = df["Frequenza 1"]
            y_data =df["Ampiezza 1"]

            x_data = x_data.dropna()
            y_data = y_data.dropna()
            popt, pcov = curve_fit(func_ale,x_data, y_data, p0 = p0, method='lm')

            #i.split["."][0]+"_"+"???"+"png



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument ("-d", "--directory", help = "Directory of .csv file", required = True)
    args = parser.parse_args()
    directory_p = args.directory
    main(directory_p)
