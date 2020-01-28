def spiralPrint(top, bottom, left, right, m):

    if left > right:
        return

    for i in range(left, right+1):
        print(m[top][i],end=' ')

    top += 1

    if top > bottom:
        return

    for i in range(top, bottom+1):
        print(m[i][right],end=' ')

    
    right -= 1

    if left > right:
        return

    for i in range(right, left-1, -1):
        print(m[bottom][i],end=' ')

    bottom -= 1

    if top > bottom:
        return

    for i in range(bottom, top-1, -1):
        print(m[i][left],end=' ')

    left += 1

    spiralPrint(top, bottom, left, right, m)
        

a = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18] ] 
        
R = 3; C = 6
spiralPrint(0 , R-1, 0,  C-1, a) 