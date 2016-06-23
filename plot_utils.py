import constants
import matplotlib
import matplotlib.pyplot as plt
import itertools
import sys
import numpy as np
import os
plt.ion()

# probs = np.load('generation/dataset_10000_probs.npy')
# probs_jump = np.load('generation/dataset_10000_info_0.npy')
# probs_chord = np.load('generation/dataset_10000_info_1.npy')
# chosen = np.load('generation/dataset_10000_chosen.npy')
# chosen_map = np.eye(probs.shape[-1])[chosen]


def plot_generated(mat, name=""):
    f = plt.figure()
    f.canvas.set_window_title(name)
    plt.imshow(mat.T, origin="lower", interpolation="nearest", cmap='viridis')
    plt.colorbar()
    for y in range(0,36,12):
        plt.axhline(y + 1.5, color='c')
    for x in range(0,4*(constants.WHOLE//constants.RESOLUTION_SCALAR),(constants.QUARTER//constants.RESOLUTION_SCALAR)):
        plt.axvline(x-0.5, color='k')
    for x in range(0,4*(constants.WHOLE//constants.RESOLUTION_SCALAR),(constants.WHOLE//constants.RESOLUTION_SCALAR)):
        plt.axvline(x-0.5, color='c')
    plt.show()

def plot_all(folder, idx=0):
    probs = np.load(os.path.join(folder,'generated_probs.npy'))
    chosen_raw = np.load(os.path.join(folder,'generated_chosen.npy'))
    chosen = np.eye(probs.shape[-1])[chosen_raw]
    plot_generated(probs[idx], 'Probabilities')
    plot_generated(chosen[idx], 'Chosen')
    try:
        for i in itertools.count():
            probs_info = np.load(os.path.join(folder,'generated_info_{}.npy'.format(i)))
            plot_generated(probs_info[idx], 'Info {}'.format(i))
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    plot_all(sys.argv[1], int(sys.argv[2]))
    input("Press enter to close.")