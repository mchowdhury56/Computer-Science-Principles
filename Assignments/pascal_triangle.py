from cs115 import*

def pascal_helper(row):
    '''add adjacent terms in the pascal triangle together'''
    if row == []:   return []
    if len(row) == 1:   return []
    else:
        return [row[0]+row[1]]+pascal_helper(row[1:])
    

def pascal_row(n):
    '''returns the nth row's set of numbers in pascal's triangle'''
    if n == 0:  return [1]
    else:
        return [1]+pascal_helper(pascal_row(n-1))+[1]
    

def pascal_triangle(n):
    ''' generates pascal triangle list to the nth row'''
    if n == 0:  return [[1]]
    else: return pascal_triangle(n-1)+[pascal_row(n)]

def test_pascal_row ():
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(2) == [1,2,1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]
    
def test_pascal_triangle ():
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1],[1,1],[1,2,1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    
