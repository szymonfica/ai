import sys

def B(i, j):
    return 'B_%d_%d' % (i, j)

def domains(Bs):
    return [b + ' in 0..1' for b in Bs]

def cols_threes(R, C):
    res = []
    for i in range(1, R-1):
        for j in range(C):
            res.append(B(i - 1, j) + " + 2 * " + B(i, j) + " + 3 * " + B(i + 1, j) + " #\= 2")
    return res

def rows_threes(R, C):
    res = []
    for i in range(R):
        for j in range(1, C-1):
            res.append(B(i, j-1) + " + 2 * " + B(i, j) + " + 3 * " + B(i, j+1) + " #\= 2")
    return res

def square(R, C):
    res, forbidden = [], [6, 7, 9, 11, 13, 14]
    for i in range(R - 1):
        for j in range(C - 1):
            for f in forbidden:
                res.append(B(i, j) + " + 2 * " + B(i, j + 1) + " + 4 * " + B(i + 1, j) + " + 8 * " + B(i + 1, j + 1) + " #\= " + str(f))
    return res

def cols_sums(R, C):
    res = []
    for j in range(C):
        s = ""
        for i in range(R):
            s += B(i, j)
            if i != R - 1:
                s += " + "
        s += " #= " + str(cols[j])
        res.append(s)
    return res

def rows_sums(R, C):
    res = []
    for i in range(R):
        s = ""
        for j in range(C):
            s += B(i, j)
            if j != C - 1:
                s += " + "
        s += " #= " + str(rows[i])
        res.append(s)
    return res

def set_known(known):
    res = []
    for i, j, k in known:
        res.append( '%s #= %d' % (B(i,j), k) )
    return res

def print_constraints(Cs, indent, d):
    position = indent
    print(indent * ' ', end="")
    for c in Cs:
        print(c + ', ', end="")
        position += len(c)
        if position > d:
            position = indent
            print('')
            print(indent * ' ', end="")

def storms(rows, cols, assigments):
    print(':- use_module(library(clpfd)).')

    R = len(rows)
    C = len(cols)

    variables = [B(i,j) for i in range(R) for j in range(C)]

    bs = domains(variables) + cols_threes(R, C) + rows_threes(R, C) + square(R, C) + cols_sums(R, C) + rows_sums(R, C) + set_known(assigments)

    print('solve([' + ', '.join(variables) + ']) :- ')
    print_constraints(bs, 4, 70)
    print('    labeling([ff], [' +  ', '.join(variables) + ']).')
    print()
    print(":- tell('prolog_result.txt'), solve(X), write(X), nl, told.")


txt = open('zad4_input.txt').readlines()

rows = (list(map(int, txt[0].split())))
cols = (list(map(int, txt[1].split())))
triples = []

for i in range(2, len(txt)):
    if txt[i].strip():
        triples.append(list(map(int, txt[i].split())))

output_file = open("zad4_output.txt", "w", encoding='utf8')
orig_stdout = sys.stdout
sys.stdout = output_file
storms(rows, cols, triples)
sys.stdout = orig_stdout
output_file.close()