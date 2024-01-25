def solution(input):
    result = input[1::]
    for i in range(len(input)):
        new_string = input[0:i:] + input[i+1::]
        if new_string < result:
            result = new_string
    return result

print("Solution: ", solution("aaaaaa"))