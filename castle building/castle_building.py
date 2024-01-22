def solution(a, n):
    number_of_castle = 0

    start_index = 0
    end_index = 0
    for i in range(n):
        # Check end
        if i == n - 1:
            if start_index != 0:
                number_of_castle = number_of_castle + 1
        if a[i] == a[end_index]:
            end_index = i
            print("end index: ", end_index)
        if a[i] > a[end_index]:
            # check is a valley?
            if start_index == 0:
                number_of_castle = number_of_castle + 1
            elif a[start_index - 1] > a[start_index]:
                number_of_castle = number_of_castle + 1
            start_index = i
            end_index = i
        if a[i] < a[end_index]:
            # check is a hill?
            if start_index == 0:
                number_of_castle = number_of_castle + 1
            elif a[start_index - 1] < a[start_index]:
                number_of_castle = number_of_castle + 1
            start_index = i
            end_index = i
    return number_of_castle

print("Number of castle: ", solution([2,2,3,4,3,3,2,2,1,1,2,5], 12))



