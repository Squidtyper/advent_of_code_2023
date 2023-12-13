
def clean_list(l):
    while "" in l:
        l.remove("")

def get_difference(numbers, matrix):
    dif = []
    for i in range(1, len(numbers), 1):
        dif.append(numbers[i] - numbers[i-1])
    matrix.append(dif)
    for item in dif:
        if item != 0:
            get_difference(dif, matrix)
            break
    return matrix

def front_predict(matrix):
    matrix[-1].insert(0, 0)
    for i in range(len(matrix) - 2, -1, -1):
        matrix[i].insert(0, matrix[i][0] - matrix[i + 1][0])
    return matrix



file = open("./input.txt", 'r')
content = file.read()
lines = content.split('\n')
l_numbers = []
for line in lines:
    nstr = line.split(' ')
    clean_list(nstr)
    numbers = []
    for item in nstr:
        numbers.append(int(item))
    l_numbers.append(numbers)
l_matrix = []
for i in range(len(l_numbers)):
    matrix = []
    matrix.append(l_numbers[i])
    l_matrix.append(get_difference(l_numbers[i], matrix))
for i in range(len(l_matrix)):
    l_matrix[i] = front_predict(l_matrix[i])
total = 0
for matrix in l_matrix:
    total = total + matrix[0][0]
print(total)