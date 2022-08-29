import numpy as np


# Datos del ejercicio
X = [1, 2, 3, 4, 5]
Y = ["a", "b", "c", "d", "e", "f"]
A = {"1": 0.3, "2": 0.5, "3": 1, "4": 0.7, "5": 0.2}
B = {"a": 0.3, "b": 0.5, "c": 0.8, "d": 1}

'''
# ejercicio de ejemplo
X = [1, 2, 3]
Y = ["a", "b"]
A = {"1": 0.1, "2": 0.4, "3": 1}
B = {"a": 0.3, "b": 1}
'''

np.set_printoptions(precision=3)

def Ejercico1(A_set, B_set):

    print("\n###################################")
    print("# Ejercicio 1                     #")
    print("###################################")

    print("\nDatos del ejercicio 1")
    print("A(x) = ", end='')
    buffer = ''
    for key, value in A_set.items():
        buffer = buffer + f'{value}/{key} + '
    print(buffer.rstrip('+ '))

    buffer = ''
    print("B(x) = ", end='')
    for key, value in B_set.items():
        buffer = buffer + f'{value}/{key} + '
    print(buffer.rstrip('+ '), '\n')

    A_len = len(A_set)
    B_len = len(B_set)

    GODEL_mat = np.array([0]*A_len*B_len, dtype=np.dtype(float)).reshape(A_len, B_len)
    LUKASIEWICZ_mat = np.array([0]*A_len*B_len, dtype=np.dtype(float)).reshape(A_len, B_len)
    GOGUEN_mat = np.array([0]*A_len*B_len, dtype=np.dtype(float)).reshape(A_len, B_len)

    for A_key, A_pos in zip(A_set, range(A_len)):
        for B_key, B_pos in zip(B_set, range(B_len)):
            GODEL_value = godel_op(A_set[A_key], B_set[B_key])
            LUKASIEWICZ_value = lukasiewicz_op(A_set[A_key], B_set[B_key])
            GOGUEN_value = goguen_op(A_set[A_key], B_set[B_key])

            GODEL_mat = set_value(GODEL_mat, A_pos, B_pos, GODEL_value)
            LUKASIEWICZ_mat = set_value(LUKASIEWICZ_mat, A_pos, B_pos, LUKASIEWICZ_value)
            GOGUEN_mat = set_value(GOGUEN_mat, A_pos, B_pos, GOGUEN_value)

    buffer = ''
    print('Resultados del ejercicio 1')
    print('Godel')
    print('R(x,y) = ', end='')
    for A_key, A_pos in zip(A_set, range(A_len)):
        for B_key, B_pos in zip(B_set, range(B_len)):
            buffer = buffer + f'{round(GODEL_mat[A_pos][B_pos])}/({A_key},{B_key}) + '
    print(buffer.rstrip('+ '))
    print("\nEn forma matricial:")
    print(GODEL_mat)

    buffer = ''
    print('\nLukasiewicz')
    print('R(x,y) = ', end='')
    for A_key, A_pos in zip(A_set, range(A_len)):
        for B_key, B_pos in zip(B_set, range(B_len)):
            buffer = buffer + f'{round(LUKASIEWICZ_mat[A_pos][B_pos], 2)}/({A_key},{B_key}) + '
    print(buffer.rstrip('+ '))
    print("\nEn forma matricial:")
    print(LUKASIEWICZ_mat)

    buffer = ''
    print('\nGoguen')
    print('R(x,y) = ', end='')
    for A_key, A_pos in zip(A_set, range(A_len)):
        for B_key, B_pos in zip(B_set, range(B_len)):
            buffer = buffer + f'{round(GOGUEN_mat[A_pos][B_pos],2)}/({A_key},{B_key}) + '
    print(buffer.rstrip('+ '))
    print("\nEn forma matricial:")
    print(GOGUEN_mat)

    return GODEL_mat, LUKASIEWICZ_mat, GOGUEN_mat


def godel_op(a, b):
    if a <= b:
        return 1
    else:
        return b


def lukasiewicz_op(a, b):
    return min(1, 1 - a + b)


def goguen_op(a, b):
    if a <= b:
        return 1
    else:
        return b/a


def degenerada_op(a, b):
    if a == 1:
        return b
    elif b == 1:
        return a
    else:
        return 0


def set_value(mat, A_pos, B_pos, val):
    mat[A_pos][B_pos] = val
    return mat


def Ejercicio2(A, B, GODEL_mat, LUKASIEWICZ_mat, GOGUEN_mat):
    print("\n\n###################################")
    print("# Ejercicio 2                     #")
    print("###################################")
    A_P = {"1": 0.5, "2": 0.7, "3": 0.9, "4": 0.5, "5": 0.4}
    # ejercicio de ejemplo
    # A_P = {"1": 0.5, "2": 1, "3": 0.9}

    print("\nDatos del ejercicio 2")
    print("A(x) = ", end='')
    buffer = ''
    for key, value in A_P.items():
        buffer = buffer + f'{value}/{key} + '
    print(buffer.rstrip('+ '), '\n')

    A_P_mat = np.array(list(A_P.values()))

    R_GODEL_mat = max_op_lukasiewicz(A, B, GODEL_mat, A_P_mat)
    R_LUKASIEWICZ_mat = max_op_lukasiewicz(A, B, LUKASIEWICZ_mat, A_P_mat)
    R_GOGUEN_mat = max_op_lukasiewicz(A, B, GOGUEN_mat, A_P_mat)

    buffer = ''
    print('Resultados del ejercicio 2\n')
    print('T-Norm: interseccion drastica\n')
    print('R(x,y) obtenido con Godel: ', end='')
    print("B'(y) = ", end='')
    for B_key, B_pos in zip(B, range(len(B))):
        buffer = buffer + f'{R_GODEL_mat[B_pos]}/{B_key} + '
    print(buffer.rstrip('+ '))

    buffer = ''
    print('R(x,y) obtenido con Lukasiwewicz: ', end='')
    print("B'(y) = ", end='')
    for B_key, B_pos in zip(B, range(len(B))):
        buffer = buffer + f'{R_LUKASIEWICZ_mat[B_pos]}/{B_key} + '
    print(buffer.rstrip('+ '))

    buffer = ''
    print('R(x,y) obtenido con Goguen: ', end='')
    print("B'(y) = ", end='')
    for B_key, B_pos in zip(B, range(len(B))):
        buffer = buffer + f'{R_GOGUEN_mat[B_pos]}/{B_key} + '
    print(buffer.rstrip('+ '), '\n')

    R_GODEL_mat = max_op_degenerada(A, B, GODEL_mat, A_P_mat)
    R_LUKASIEWICZ_mat = max_op_degenerada(A, B, LUKASIEWICZ_mat, A_P_mat)
    R_GOGUEN_mat = max_op_degenerada(A, B, GOGUEN_mat, A_P_mat)

    buffer = ''
    print('T-Norm: Diferencia limitada (Lukasiewicz)\n')
    print('R(x,y) obtenido con Godel: ', end='')
    print("B'(y) = ", end='')
    for B_key, B_pos in zip(B, range(len(B))):
        buffer = buffer + f'{R_GODEL_mat[B_pos]}/{B_key} + '
    print(buffer.rstrip('+ '))

    buffer = ''
    print('R(x,y) obtenido con Lukasiwewicz: ', end='')
    print("B'(y) = ", end='')
    for B_key, B_pos in zip(B, range(len(B))):
        buffer = buffer + f'{R_LUKASIEWICZ_mat[B_pos]}/{B_key} + '
    print(buffer.rstrip('+ '))

    buffer = ''
    print('R(x,y) obtenido con Goguen: ', end='')
    print("B'(y) = ", end='')
    for B_key, B_pos in zip(B, range(len(B))):
        buffer = buffer + f'{R_GOGUEN_mat[B_pos]}/{B_key} + '
    print(buffer.rstrip('+ '),)


def set_value2(mat, B_pos, val):
    mat[B_pos] = val
    return mat


def max_op_old(A_set, B_set, mat, arr):
    A_len = len(A_set)
    B_len = len(B_set)
    # assuming normalized arr as input data
    R_mat = np.array([0]*B_len, dtype=np.dtype(float)).reshape(B_len)
    for B_pos in range(B_len):
        min_list = []
        for A_pos in range(A_len):
            # funcion T
            # porfavor pillar si esta bien (basado en el ejercicio de ejemplo)
            min_val = min(mat[A_pos][B_pos], arr[A_pos])

            min_list.append(min_val)
        R_mat = set_value2(R_mat, B_pos, max(min_list))
    return R_mat


def max_op_lukasiewicz(A_set, B_set, mat, arr):
    A_len = len(A_set)
    B_len = len(B_set)
    # assuming normalized arr as input data
    R_mat = np.array([0]*B_len, dtype=np.dtype(float)).reshape(B_len)
    for B_pos in range(B_len):
        lukasiewicz_list = []
        for A_pos in range(A_len):
            lukasiewicz_val = lukasiewicz_op(mat[A_pos][B_pos], arr[A_pos])
            lukasiewicz_list.append(lukasiewicz_val)
        R_mat = set_value2(R_mat, B_pos, max(lukasiewicz_list))
    return R_mat


def max_op_degenerada(A_set, B_set, mat, arr):
    A_len = len(A_set)
    B_len = len(B_set)
    # assuming normalized arr as input data
    R_mat = np.array([0]*B_len, dtype=np.dtype(float)).reshape(B_len)
    for B_pos in range(B_len):
        degenerada_list = []
        for A_pos in range(A_len):
            degenerada_val = degenerada_op(mat[A_pos][B_pos], arr[A_pos])
            degenerada_list.append(degenerada_val)
        R_mat = set_value2(R_mat, B_pos, max(degenerada_list))
    return R_mat


########################
#         main         #
########################

def main():
    GODEL_mat, LUKASIEWICZ_mat, GOGUEN_mat = Ejercico1(A, B)
    Ejercicio2(A, B, GODEL_mat, LUKASIEWICZ_mat, GOGUEN_mat)


if __name__ == "__main__":
    main()
