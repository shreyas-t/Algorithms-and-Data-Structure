def get_product_of_all_other(arr):

    if len(arr) < 2:
        raise ValueError("Getting the product of numbers at other indices requires at least 2 numbers")

    product_of_all_other = [None]*len(arr)

    product_so_far = 1
    for i in range(len(arr)):
        product_of_all_other[i] = product_so_far
        product_so_far *= arr[i]

    product_so_far = 1
    for i in range(len(arr)-1, -1, -1):
        product_of_all_other[i] *= product_so_far
        product_so_far *= arr[i]

    for i in range(len(arr)):
        print(product_of_all_other[i],end=' ')


arr = [10, 4, 1, 6, 2]

for i in range(len(arr)):
        print(arr[i],end=' ')
print()

get_product_of_all_other(arr)