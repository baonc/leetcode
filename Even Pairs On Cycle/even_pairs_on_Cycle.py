def solution(a, n):
    segment_dict = {}

    # seperating segment of odd or even
    count = 0
    for i in range(len(a)):
        