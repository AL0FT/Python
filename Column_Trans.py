# Experimental Columnar Transposition Solver

import numpy

row_one = ["A","A","S","Y","G","M","I","A"]
row_two = ["H","Y","B","Y","M","T","O","H"]
row_thr = ["D","T","I","C","E","A","N","U"]
row_fou = ["O","T","E","W","O","N","E","E"]
row_fiv = ["N","H","L","H","U","T","F","C"]
row_six = ["N","H","I","T","E","I","D","T"]
row_sev = ["I","W","K","N","L","E","S","E"]
row_eig = ["E","S","N","A","T","K","N","S"]

matrix = list(zip(row_one, row_two, row_thr, row_fou, row_fiv, row_six, row_sev, row_eig))
print(matrix)
print("/n")
matrix_2 = numpy.array([["A","A","S","Y","G","M","I","A"],
                        ["H","Y","B","Y","M","T","O","H"],
                        ["D","T","I","C","E","A","N","U"],
                        ["O","T","E","W","O","N","E","E"],
                        ["N","H","L","H","U","T","F","C"],
                        ["N","H","I","T","E","I","D","T"],
                        ["I","W","K","N","L","E","S","E"],
                        ["E","S","N","A","T","K","N","S"]])
print(matrix_2)