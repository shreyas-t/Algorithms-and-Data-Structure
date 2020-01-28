# Problem: Find Min Number of Coins needed to make a change with infinite supply of coins

def findMin(V, deno):
    n = len(deno)

    i = n-1
    while  i >= 0:
        while V >= deno[i]: 
            V -= deno[i]
            print(deno[i],end= ' ')

        i -= 1
    print()

if __name__ == '__main__': 
    n = 93
    deno = [1, 2, 5, 10, 20, 50, 100, 500, 1000] 
    print("Following is minimal number of change for", n, ": ", end = "") 
    findMin(n, deno) 
    