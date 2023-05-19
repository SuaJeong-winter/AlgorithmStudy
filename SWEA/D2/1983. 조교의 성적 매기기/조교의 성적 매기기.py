T = int(input())
grades = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']  #등급

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n,k=map(int,input().split())
    score_list = []
    for _ in range(n):
        mid,final,hws = map(int, input().split()) #중간 기말 과제 점수 입력값 받기 
        total=(mid*0.35)+(final*0.45)+(hws*0.20)
        score_list.append(total)          
        #여기까지는 풀었다
      #k번 학생의 점수 - k번째 학생의 인덱스를 구한다 
    k_score = score_list[k-1]
    #정렬
    score_list.sort(reverse=True)  #점수가 높->낮은 순으로 정렬
    div=n//10  #평점별 들어가는 학생 수
    final_k_score = score_list.index(k_score)//div
    
    print(f'#{test_case} {grades[final_k_score]}')

    # ///////////////////////////////////////////////////////////////////////////////////
