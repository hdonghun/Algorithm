submit = [int(input()) for _ in range(28)]
all_students = list(range(1, 31))  

remaining = [i for i in all_students if i not in submit] 

print(min(remaining))
print(max(remaining))
