# tim so luong phan tu khac nhau (lon nhat) cua chuoi string con lai neu xoa di R phan tu lien ke.
def solution(input, r):
    chars_map = {}

    # Set char map
    for char in input:
        chars_map[char] = chars_map.get(char, 0) + 1

    print("chars_map ", chars_map)
    max_value = 0
    for i in range(0, len(input)):
        chars_map[input[i]] = chars_map[input[i]] - 1
        if chars_map[input[i]] <= 0:
            del chars_map[input[i]]
        if i == r - 1:
            max_value = len(chars_map)
        if i >= r:
            chars_map[input[i - r]] = chars_map.get(input[i - r], 0) + 1
            if len(chars_map) > max_value:
                max_value = len(chars_map)
    return max_value

# test string
#input = "212322"
#r = 3
#max_value = solution(input, r)
#print("Max value: ", max_value)
print("Max value: ", solution([2, 1, 2, 3, 2, 2], 3))
print("Max value: ", solution([2, 3, 1, 1, 2], 2))
print("Max value: ", solution([20, 10, 10, 10, 30, 20], 3))
print("Max value: ", solution([1, 100000, 1], 3))
    