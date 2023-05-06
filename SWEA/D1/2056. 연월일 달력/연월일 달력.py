T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    monthlista=[1,3,5,7,8,10,12]
    monthlistb=[4,6,9,11]
    monthlistc= [2]
    ymd = input()
    year=int(ymd[0:4])
    month=int(ymd[4:6])
    date=int(ymd[6:])
    if month in monthlistc and 1<=date<=28:
            print(f"#{test_case} {str(year).zfill(4)}/{str(month).zfill(2)}/{str(date).zfill(2)}")
    elif month in monthlista and 1<=date <=31:
            print(f"#{test_case} {str(year).zfill(4)}/{str(month).zfill(2)}/{str(date).zfill(2)}")
    elif month in monthlistb and 1<=date <=30:
            print(f"#{test_case} {str(year).zfill(4)}/{str(month).zfill(2)}/{str(date).zfill(2)}")
    else:
            print(f"#{test_case} -1")

            
    # ///////////////////////////////////////////////////////////////////////////////////

