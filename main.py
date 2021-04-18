import time
start_whole = time.monotonic()
# Whole program timings
lst = []
first_list = input('Enter list using whitespace: ').split()
for element in first_list:
    lst.append(int(element))
num = int(input('Enter a number: '))
lst.sort()
# The list and a number are ready for the program


def iterations(list_input, number):
    left = 0
    middle = len(list_input) // 2
    right = len(list_input) - 1
    # boundaries

    while list_input[middle] != number and left <= right:
        if number > list_input[middle]:
            left = middle + 1
        else:
            right = middle - 1
        middle = (left + right) // 2

    if left > right:
        return 'None'
    else:
        return 'Index of a number is: ' + str(middle)


start = time.monotonic()
# Time at the beginning (iterations)
print('\nResult of iteration program:\n', iterations(lst, num), sep='')
result = time.monotonic() - start
# end of iteration part

# Recursive part


def recursive(list_input, number):
    '''Binary recursive method of finding num in the list'''
    try:
        try:
            mid = len(list_input) // 2
            if number == list_input[mid]:
                return mid
            if number > list_input[mid]:
                return recursive(list_input[mid+1:], number) + (mid + 1)
            else:
                return recursive(list_input[:mid], number)
        except IndexError:
            return None
    except TypeError:
        return None


# RESULTS
print("Time to do the iteration part is: {:>.10f}".format(result) + " sec.\n")
print('Result of recursive program:')
start_rec = time.monotonic()
# Time at the beginning (Recursive)
if str(recursive(lst, num)).isdigit():
    print('Index of a number is: ', recursive(lst, num))
else:
    print(recursive(lst, num))
result_rec = time.monotonic() - start_rec
print("Time to do the recursive part is: {:>.10f}".format(result_rec) + " sec.")
result_whole = time.monotonic() - start_whole
print("\nTime to do the whole program is: {:>.10f}".format(result_rec) + " sec.")
