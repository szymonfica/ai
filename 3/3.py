import sys

def V(i,j):
    return 'V%d_%d' % (i,j)
    
def domains(Vs):
    return [ q + ' in 1..9' for q in Vs ]
    
def all_different(Qs):
    return 'all_distinct([' + ', '.join(Qs) + '])'
    
def get_column(j):
    return [V(i,j) for i in range(9)] 
            
def get_raw(i):
    return [V(i,j) for j in range(9)] 
                        
def horizontal():   
    return [all_different(get_raw(i)) for i in range(9)]

def vertical():
    return [all_different(get_column(j)) for j in range(9)]

def squares():
    small_square = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    big_square = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

    return [[all_different((V(i[0] + j[0], i[1] + j[1])) for j in small_square)][0] for i in big_square]

def print_constraints(Cs, indent, d):
    position = indent
    print (indent * ' ', end='')
    for c in Cs:
        print (c + ',', end=' ')
        position += len(c)
        if position > d:
            position = indent
            print ()
            print (indent * ' ', end='')

      
def sudoku(assigments):
    variables = [ V(i,j) for i in range(9) for j in range(9)]
    
    print (':- use_module(library(clpfd)).')
    print ('solve([' + ', '.join(variables) + ']) :- ')
    
    
    cs = domains(variables) + vertical() + horizontal() + squares() #TODO: too weak contraints, add something!
    for i,j,val in assigments:
        cs.append( '%s #= %d' % (V(i,j), val) )
    
    print_constraints(cs, 4, 70),
    print ()
    print ('    labeling([ff], [' +  ', '.join(variables) + ']).' )
    print ()
    print (':- solve(X), write(X), nl.')       

if __name__ == "__main__":
    input_file = open("zad3_input.txt", "r", encoding='utf8').readlines()
    output_file = open("zad3_output.txt", "w", encoding='utf8')
    
    orig_stdout = sys.stdout
    sys.stdout = output_file

    row = 0
    triples = []
    
    for x in input_file:
        x = x.strip()
        if len(x) == 9:
            for col in range(9):
                if x[col] != '.':
                    triples.append((row, col, int(x[col]))) 
            row += 1          
    sudoku(triples)

    sys.stdout = orig_stdout
    output_file.close()
    
    
"""
89.356.1.
3...1.49.
....2985.
9.7.6432.
.........
.6389.1.4
.3298....
.78.4....
.5.637.48

53..7....
6..195...
.98....6.
8...6...3
4..8.3..1
7...2...6
.6....28.
...419..5
....8..79

3.......1
4..386...
.....1.4.
6.924..3.
..3......
......719
........6
2.7...3..
"""