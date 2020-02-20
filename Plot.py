import matplotlib.pyplot as plt
import matplotlib
from SciDAVis2Python import func_ale


def draw (x_data, y_data, func, title, name_file, popt,fig_size = [16,9]):
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
    plt.figure(figsize = fig_size)
    plt.plot(x_data, y_data, 'k.', label='data')
    plt.plot(x_data, func(x_data, *popt), 'r-',
             label='fit:\n wn_x=%5.3f\n, wn_y=%5.3f\n, Eta_x=%5.3f\n, Eta_y=%5.3f\n, k_x=%5.3f\n, \
             Eta_y=%5.3f' % tuple(popt), linewidth = 3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.savefig(name_file, dpi = 300)
    plt.close()
