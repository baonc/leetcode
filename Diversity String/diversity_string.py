def solution(n):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x','y', 'z']

    index = 0
    number_of_appears = 0
    i = 26
    while i > 0:
        if (n / i).is_integer():
            index = i
            number_of_appears = n / i
            break
        i  = i - 1
    result = ''
    print("Number of appears: ", number_of_appears)
    for j in range(int(number_of_appears)):
        for k in range(index):
            result = result + alphabet[k]
    return result

print("solution: ", solution(100))


