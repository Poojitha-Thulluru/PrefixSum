def prefix_sum(array):
    prefix_sum_array = [array[0]]
    for index in range(1, len(array)):
        prefix_sum_array.append(prefix_sum_array[index - 1] + array[index])
    return prefix_sum_array


try:
    print("Enter array elements separated by space to get their prefix array : ")
    numbers = list(map(int, input().split()))
    print(prefix_sum(numbers))
except ValueError:
    print("Invalid input. Please Enter only integers with space")
