"""
Conway's Game of Life in Python
The program takes in a file named "life.txt" and world dimensions (20x10)
It then displays a specified number of generations (10)
The input file may contain any number of rows and columns
Live cells are represented as '*' and dead cells as '-'

Author: Iskender Akhmedov
CS-UY 1134 Data Structures and Algorithms
Professor: John Sterling
Teaching Assistant: Meredith Mante
Due Date: May 26, 2018
"""

import copy


def create_world_matrix(rows, columns):
    # creates a matrix filled with dead cells based on given dimensions
    world_matrix = []
    for i in range(rows):
        row = [0] * columns
        world_matrix.append(row)
    return world_matrix


def convert_file_into_matrix(filename):
    # extracts information from text file and returns a list with numerical information
    f = open(filename, 'r')
    cells_list = f.readlines()
    matrix = []
    for line in cells_list:  # creates a list of lists for initial world
        row = []
        line = line[:-1]  # removes new line character at the end
        for i in range(len(line)):      # fills the list based on text file's
            if line[i] == '*':
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def add_borders(matrix):
    # creates a new matrix based on existing matrix, but with added borders around
    rows = len(matrix)
    columns = len(matrix[0])
    border_matrix = []
    top_bottom = [0] * (columns+2)      # list to be attached to top&bottom of matrix
    border_matrix.append(top_bottom)
    for i in range(rows):
        row = [0]
        for j in range(columns):
            row.append(matrix[i][j])
        row.append(0)
        border_matrix.append(row)
    border_matrix.append(top_bottom)
    return border_matrix


def remove_borders(matrix):
    # removes the borders added in order to prepare for displaying
    matrix.pop()
    matrix.pop(0)
    for item in matrix:
        item.pop()
        item.pop(0)
    return matrix


def alive_around(matrix, row_index, column_index):
    # returns the number of live cells around a point within a matrix
    neighbors_alive = 0
    for row_around in range(-1, 2):     # count all 9 cells around index
        for column_around in range(-1, 2):
            if matrix[row_index+row_around][column_index+column_around] == 1:
                neighbors_alive += 1
    if matrix[row_index][column_index] == 1:
        # since the value of cell itself is also accounted, it needs to be removed
        neighbors_alive -= 1
    return neighbors_alive


def generation(matrix):
    # takes in a matrix of cells and outputs the next generation based on the rules
    matrix_static = copy.deepcopy(matrix)
    for row in range(1, len(matrix)-1):
        for column in range(1, len(matrix[i])-1):
            alive = alive_around(matrix_static, row, column)
            if alive == 3:
                matrix[row][column] = 1
            elif alive < 2 or alive > 3:
                matrix[row][column] = 0
    return matrix


def visualize_matrix(matrix):
    # creates a string and fills it with *'s and -'s based on matrix provided
    visualization = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                visualization += '*'
            else:
                visualization += '-'
        visualization += '\n'
    return visualization


def output_generations(matrix, generations):
    # creates an output string for number of generations based on initial matrix
    output = ''
    for i in range(generations+1):
        output += 'Generation ' + str(i) + ':\n'
        output += visualize_matrix(matrix)
        output += '='*32 + '\n'
        matrix = add_borders(matrix)
        matrix = generation(matrix)
        matrix = remove_borders(matrix)
    return output


if __name__ == '__main__':
    seed_matrix = convert_file_into_matrix('life.txt')
    world = create_world_matrix(10, 20)
    for i in range(len(seed_matrix)):
        for j in range(len(seed_matrix[i])):
            if i <= len(world) and j <= len(world[0]):
                # checks if the matrix is within boundaries of the world
                # ignores the values that are outside
                world[i][j] = seed_matrix[i][j]

    print(output_generations(world, 10))
