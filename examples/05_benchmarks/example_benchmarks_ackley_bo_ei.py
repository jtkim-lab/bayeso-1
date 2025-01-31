# example_benchmarks_ackley_bo_ei
# author: Jungtaek Kim (jtkim@postech.ac.kr)
# last updated: April 28, 2020

import numpy as np
import os

from bayeso import bo
from bayeso_benchmarks import Ackley
from bayeso import wrappers
from bayeso.utils import utils_bo
from bayeso.utils import utils_plotting


STR_FUN_TARGET = 'ackley'
PATH_SAVE = '../figures/benchmarks/'
NUM_DIM = 3

obj_fun = Ackley(NUM_DIM)

def fun_target(X):
    return obj_fun.output(X)

def main():
    num_bo = 5
    num_iter = 10
    num_init = 5

    bounds = obj_fun.get_bounds()
    model_bo = bo.BO(bounds, debug=True)
    list_Y = []
    list_time = []
    for ind_bo in range(0, num_bo):
        print('BO Round', ind_bo + 1)
        X_final, Y_final, time_final, _, _ = wrappers.run_single_round(model_bo, fun_target, num_init, num_iter, str_initial_method_bo='gaussian', str_sampling_method_ao='gaussian', num_samples_ao=100, seed=42 * (ind_bo + 1))
        print(X_final)
        print(Y_final)
        print(time_final)
        list_Y.append(Y_final)
        list_time.append(time_final)

        bx_best, y_best = utils_bo.get_best_acquisition_by_history(X_final, Y_final)
        print(bx_best, y_best)

    arr_Y = np.array(list_Y)
    arr_Y = np.expand_dims(np.squeeze(arr_Y), axis=0)
    arr_time = np.array(list_time)
    arr_time = np.expand_dims(arr_time, axis=0)
    utils_plotting.plot_minimum_vs_iter(arr_Y, [STR_FUN_TARGET], num_init, True, path_save=PATH_SAVE, str_postfix=STR_FUN_TARGET)
    utils_plotting.plot_minimum_vs_time(arr_time, arr_Y, [STR_FUN_TARGET], num_init, True, path_save=PATH_SAVE, str_postfix=STR_FUN_TARGET)


if __name__ == '__main__':
    if not os.path.isdir(PATH_SAVE):
        os.makedirs(PATH_SAVE)
    main()
