input = "abcdef"
def reverse_string(input):
    stacks = []

    for char in input:
        stacks.append(char)
        
    while(len(stacks) > 0):
        print(stacks.pop())

reverse_string(input)