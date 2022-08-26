import decimal
import re
import numpy as np
A = dict()
B = dict()
# X = [1,2,3,4,5]
# Y = ["a","b","c","d","e","f"]

# A = {"1":0.3,"2":0.5, "3":1,"4":0.7,"5":0.2 }
# B = {"a":0.3,"b":0.5, "c":0.8,"d":1 }

# ejercicio de ejemplo
X = [1, 2, 3]
Y = ["a", "b"]
A = {"1": 0.1, "2": 0.4, "3": 1}
B = {"a": 0.3, "b": 1}


def Ejercico1(A_set, B_set):
    print("###################################")
    print("# ejercicio 1                     #")
    print("###################################")
    A_len = len(A_set)
    B_len = len(B_set)

    GODEL_mat = np.array(
        [0]*A_len*B_len, dtype=np.dtype(decimal.Decimal)).reshape(A_len, B_len)
    LUKASIEWICZ_mat = np.array([0]*A_len*B_len).reshape(A_len, B_len)
    GOGUEN_mat = np.array([0]*A_len*B_len).reshape(A_len, B_len)

    for A_key, A_pos in zip(A_set, range(A_len)):
        for B_key, B_pos in zip(B_set, range(B_len)):
            GODEL_value = godel_op(A_set[A_key], B_set[B_key])
            LUKASIEWICZ_value = lukasiewicz_op(A_set[A_key], B_set[B_key])
            GOGUEN_value = goguen_op(A_set[A_key], B_set[B_key])

            GODEL_mat = set_value(GODEL_mat, A_pos, B_pos, GODEL_value)
            LUKASIEWICZ_mat = set_value(
                LUKASIEWICZ_mat, A_pos, B_pos, LUKASIEWICZ_value)
            GOGUEN_mat = set_value(GOGUEN_mat, A_pos, B_pos, GOGUEN_value)

            print("A_key = " + A_key + " A_Value = " + str(A_set[A_key]))
            print("B_key = " + B_key + " B_Value = " + str(B_set[B_key]))
            print("GODEL_value = " + str(GODEL_value))
            print("LUKASIEWICZ_value = " + str(LUKASIEWICZ_value))
            print("GOGUEN_value = " + str(GOGUEN_value))
            print("###################################")

    print("GODEL_mat")
    print(GODEL_mat)

    print("LUKASIEWICZ_mat")
    print(LUKASIEWICZ_mat)

    print("GOGUEN_mat")
    print(GOGUEN_mat)
    return GODEL_mat, LUKASIEWICZ_mat, GOGUEN_mat


def godel_op(a, b):
    if a <= b:
        return 1
    else:
        return b


def lukasiewicz_op(a, b):
    c = 1-a+b
    if 1 > c:
        return 1
    else:
        return c


def goguen_op(a, b):
    if a <= b:
        return 1
    else:
        return b/a


def set_value(mat, A_pos, B_pos, val):
    mat[A_pos][B_pos] = val
    return mat


def Ejercicio2(A, B, GODEL_mat, LUKASIEWICZ_mat, GOGUEN_mat):
    print("###################################")
    print("# ejercicio 2                     #")
    print("###################################")
    #A_P = {"1":0.5, "2":0.7, "3":0.9, "4":0.5, "5":0.4 }
    # ejercicio de ejemplo
    A_P = {"1": 0.5, "2": 1, "3": 0.9}

    A_P_mat = np.array(list(A_P.values()))

    R_GODEL_mat = max_op(A, B, GODEL_mat, A_P_mat)
    R_LUKASIEWICZ_mat = max_op(A, B, LUKASIEWICZ_mat, A_P_mat)
    R_GOGUEN_mat = max_op(A, B, GOGUEN_mat, A_P_mat)

    print("GODEL_mat")
    print(R_GODEL_mat)

    print("LUKASIEWICZ_mat")
    print(R_LUKASIEWICZ_mat)

    print("GOGUEN_mat")
    print(R_GOGUEN_mat)


def set_value2(mat, B_pos, val):
    mat[B_pos] = val
    return mat


def max_op(A_set, B_set, mat, arr):
    A_len = len(A_set)
    B_len = len(B_set)
    # assuming normalized arr as input data
    R_mat = np.array([0]*B_len, dtype=np.dtype(decimal.Decimal)).reshape(B_len)
    for B_pos in range(B_len):
        min_list = []
        for A_pos in range(A_len):
            # funcion T
            # porfavor pillar si esta bien (basado en el ejercicio de ejemplo)
            min_val = min(mat[A_pos][B_pos], arr[A_pos])

            min_list.append(min_val)
        R_mat = set_value2(R_mat, B_pos, max(min_list))
    return R_mat


########################
#       main           #
########################

GODEL_mat, LUKASIEWICZ_mat, GOGUEN_mat = Ejercico1(A, B)
Ejercicio2(A, B, GODEL_mat, LUKASIEWICZ_mat, GOGUEN_mat)
