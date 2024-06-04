def solution(num_list):
    odd_num =""
    even_num=""
    for num in num_list:
        if num %2 !=0:
            odd_num+="".join(str(num))
        else:
            even_num+="".join(str(num))
    return int(odd_num)+int(even_num)