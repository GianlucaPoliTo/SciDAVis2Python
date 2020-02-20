import matplotlib.pyplot as plt
import matplotlib

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

def plot(x_data, y_data, func, title , name_file, fig_size = [16,9]):
    plt.figure(figsize = fig_size)
    plt.plot(x_data, y_data, 'b.', label='data')
    plt.plot(x_data, func_ale(x_data, *popt), 'g-',
             label='fit: wn_x=%5.3f, wn_y=%5.3f, Eta_x=%5.3f, Eta_y=%5.3f, k_x=%5.3f, \
             Eta_y=%5.3f' % tuple(popt))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.savefig(name_file, dpi = 300)
    plt.close()
