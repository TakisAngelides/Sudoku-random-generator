import numpy as np
import random as r

def get_box_indices():
    rows_indices = {}
    columns_indices = {}
    for i in range(9):
        rows_indices[i] = [i * 9 + j for j in range(9)]
    for j in range(9):
        columns_indices[j] = [j + 9 * k for k in range(9)]
    return rows_indices, columns_indices

def get_lattice_dictionaries(lattice_2D):
    lattice = np.reshape(np.array(lattice_2D), 81)
    rows_dictionary = {}
    columns_dictionary = {}
    for i in range(9):
        rows_dictionary[i] = [lattice[i*9+j] for j in range(9)]
    for j in range(9):
        columns_dictionary[j] = [lattice[j+9*k] for k in range(9)]
    return rows_dictionary, columns_dictionary

def get_box_neighbours(lattice_2D):
    box_dictionary = {}
    rows_dictionary, columns_dictionary = get_lattice_dictionaries(lattice_2D)
    row_indices, column_indices = get_box_indices()
    box1, box2, box3, box4, box5, box6, box7, box8, box9  = [], [], [], [], [], [], [], [], []
    box1_idx, box2_idx, box3_idx, box4_idx, \
    box5_idx, box6_idx, box7_idx, box8_idx, box9_idx = [], [], [], [], [], [], [], [], []

    for i in range(3):
        box1.append(rows_dictionary[i][0:3])
        box1_idx.append(row_indices[i][0:3])
        box2.append(rows_dictionary[i][3:6])
        box2_idx.append(row_indices[i][3:6])
        box3.append(rows_dictionary[i][6:9])
        box3_idx.append(row_indices[i][6:9])
    for i in range(3, 6):
        box4.append(rows_dictionary[i][0:3])
        box4_idx.append(row_indices[i][0:3])
        box5.append(rows_dictionary[i][3:6])
        box5_idx.append(row_indices[i][3:6])
        box6.append(rows_dictionary[i][6:9])
        box6_idx.append(row_indices[i][6:9])
    for i in range(6, 9):
        box7.append(rows_dictionary[i][0:3])
        box7_idx.append(row_indices[i][0:3])
        box8.append(rows_dictionary[i][3:6])
        box8_idx.append(row_indices[i][3:6])
        box9.append(rows_dictionary[i][6:9])
        box9_idx.append(row_indices[i][6:9])
    for idx in np.reshape(np.array(box1_idx),9):
        box_dictionary[idx] = np.reshape(np.array(box1),9)
    for idx in np.reshape(np.array(box2_idx),9):
        box_dictionary[idx] = np.reshape(np.array(box2),9)
    for idx in np.reshape(np.array(box3_idx),9):
        box_dictionary[idx] = np.reshape(np.array(box3),9)
    for idx in np.reshape(np.array(box4_idx),9):
        box_dictionary[idx] = np.reshape(np.array(box4),9)
    for idx in np.reshape(np.array(box5_idx),9):
        box_dictionary[idx] = np.reshape(np.array(box5),9)
    for idx in np.reshape(np.array(box6_idx),9):
        box_dictionary[idx] = np.reshape(np.array(box6),9)
    for idx in np.reshape(np.array(box7_idx),9):
        box_dictionary[idx] = np.reshape(np.array(box7),9)
    for idx in np.reshape(np.array(box8_idx),9):
        box_dictionary[idx] = np.reshape(np.array(box8),9)
    for idx in np.reshape(np.array(box9_idx),9):
        box_dictionary[idx] = np.reshape(np.array(box9),9)
    return box_dictionary

def create_valid_sudoku():

    sudoku_lattice = [[0] * 9 for _ in range(9)]
    rows_dictionary, columns_dictionary = get_lattice_dictionaries(sudoku_lattice)
    box_dictionary = get_box_neighbours(sudoku_lattice)
    flag = False
    for i in range(len(sudoku_lattice)):

        if flag:
            break

        for j in range(len(sudoku_lattice[0])):

            if flag:
                break

            if i == 8 and j == 8:
                sudoku_lattice[i][j] = 45 - np.sum(np.array(rows_dictionary[i]))
                flag = True

            nums = [z+1 for z in range(9)]

            for k in range(10):

                if k == 9:
                    flag = True
                    break

                num = r.sample(nums, 1)[0]
                idx = i*9 + j
                if num in rows_dictionary[i] or num in columns_dictionary[j] or num in box_dictionary[idx]:
                    nums.remove(num)
                    continue

                else:
                    rows_dictionary[i][j] = num
                    columns_dictionary[j][i] = num
                    sudoku_lattice[i][j] = num
                    box_dictionary = get_box_neighbours(sudoku_lattice)
                    break
    return sudoku_lattice

for _ in range(3):

    sudoku = create_valid_sudoku()

    while 0 in np.reshape(np.array(sudoku), 81):
        sudoku = create_valid_sudoku()

    print(np.array(sudoku))
    print('---------------------')
