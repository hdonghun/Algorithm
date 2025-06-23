# 전체학생수, 방 안에 들어갈 수 있는 학생 수
# 성별0/1 , 학년(6학년까지)

n,k = map(int, input().split())

student = []
result = 0

for i in range(n):
    s,y = map(int,input().split())
    ## [(1,6), (0,1)] 이런식으로 담고 싶어서
    student.append((s,y))
    
    
from collections import defaultdict
count = defaultdict(int)
# (1,6)이나 (0,2) 같은 조합별로 학생 수를 세겠다는 뜻입니다.
# count는 defaultdict(int)이기 때문에, 해당 키가 처음 나와도 자동으로 0으로 초기화되고, 그 후 +1이 됩니다.

for s, y in student:
    count[(s,y)] += 1 # 조합 마다, 카운트하기 편하게!!
    
for (s,y), c in count.items(): # 여기서 c는 (성별 s, 학년 y) 조합에 해당하는 학생 수, 즉 그 방에 배정해야 할 인원 수입니다.

# count = {
#    (1, 6): 2,
#    (0, 2): 1
#   }
    result += (c+k-1)//k
print(result)

    


