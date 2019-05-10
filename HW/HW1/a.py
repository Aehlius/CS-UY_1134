def add_borders(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    border_matrix = []
    top_bottom = [0] * (columns+2)
    border_matrix.append(top_bottom)
    for i in range(rows):
        row = [0]
        for j in range(columns):
            row.append(matrix[i][j])
        row.append(0)
        border_matrix.append(row)
    border_matrix.append(top_bottom)
    return border_matrix

def create_world_matrix(rows, columns):
    world_matrix = []
    for j in range(rows):
        row = [0] * columns
        world_matrix.append(row)
    return world_matrix

def alive_around(matrix, i, j):
    count = 0
    for l in range(-1, 2):
        for k in range(-1, 2):
            if matrix[i+l][j+k] == 1:
                count += 1
    if matrix[i][j] == 1:
        count -= 1
    return count

def generation(matrix):
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            alive = alive_around(matrix, i, j)
            if alive == 3:
                matrix[i][j] = 1
            elif alive < 2 or alive > 3:
                matrix[i][j] = 0
    return matrix


def visualize_matrix(matrix):
    visualization = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                visualization += '*'
            else:
                visualization += '-'
        visualization += '\n'
    return visualization

world = create_world_matrix(10, 20)
print(world)


k = open('life.txt', 'r')
f = k.readlines()
matrix = []
for line in f:
    row = []
    line = line[:-1]      #removes new line character at the end
    for i in range(len(line)):
        if line[i] == '*':
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

print(matrix)
print(len(matrix))
print(len(matrix[1]))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i <= len(world) and j <= len(world[0]):  #checks if the matrix is within boundaries of the world
            world[i][j] = matrix[i][j]

print(world)
world = add_borders(world)
print(world)

print(visualize_matrix(world))


print((generation(world)))
print(visualize_matrix(generation(world)))