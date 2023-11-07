vacation=int(input())
language=int(input())
math=int(input())
max_language=int(input())
max_math=int(input())

if language%max_language==0:
    l_done=language//max_language
else:
    l_done=language//max_language+1

if math%max_math==0:
    m_done=math//max_math
else:
    m_done=math//max_math+1

max_d=max(l_done,m_done)
print(vacation-max_d)