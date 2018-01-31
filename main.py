'''
definition: Shannon entropy is the minimum number of bits per character required for encoding the file

'''

import sys
import os
import math
import numpy as np
import matplotlib.pyplot as plt


def read_file(file_name):
    f = open(file_name, 'rb')
    byte_seq = f.read()
    print(byte_seq)
    f.close()

    return byte_seq, len(byte_seq)


def get_frequency_list(byte_seq, file_size):
    result = list()
    for b in range(256):
        cnt = 0
        for byte in byte_seq:
            if byte == b:
                cnt += 1
        result.append(float(cnt)/file_size)

    return result


def get_shannon_entropy(prob_lists):
    ent = 0.0
    for prob in prob_lists:
        if prob > 0:
            ent += prob * math.log(prob, 2)

    return -ent


def draw_pyplot_graph(prob_lists):
    N = len(prob_lists)

    ind = np.arange(N)  # the x locations for the groups
    width = 1.00  # the width of the bars

    # fig = plt.figure()
    fig = plt.figure(figsize=(11, 5), dpi=100)
    ax = fig.add_subplot(111)
    rects1 = ax.bar(ind, prob_lists, width)
    ax.set_autoscalex_on(False)
    ax.set_xlim([0, 255])

    ax.set_ylabel('Frequency')
    ax.set_xlabel('Byte')
    ax.set_title('Frequency of Bytes 0 to 255')

    plt.show()

    pass


def run(file_name):
    byte_seq, file_size = read_file(file_name)
    print('file size: {}'.format(file_size))

    prob_lists = get_frequency_list(byte_seq, file_size)

    entropy = get_shannon_entropy(prob_lists)
    print('file entropy: {}'.format(entropy))
    print()
    print('--minimum possible file size--')
    print('at least {bit}bits, {byte}bytes'.format(bit=(entropy*file_size), byte=(entropy*file_size)/8))

    draw_pyplot_graph(prob_lists)

    pass


if __name__ == '__main__':
    target_file_name = os.path.normpath(os.path.abspath('./input.zip'))

    run(target_file_name)

    pass
