def solution(numbers):
    answer = ""
    num_dict = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7',
                "eight": '8', "nine": '9'}
    word = ""
    for i in range(0, len(numbers)):
        word += numbers[i]
        if word in num_dict:
            answer += num_dict[word]
            word = ""
    return int(answer)