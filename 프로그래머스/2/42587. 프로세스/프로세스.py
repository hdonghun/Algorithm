from collections import deque

def solution(priorities, location):
    queue = deque([(i, priority) for i, priority in enumerate(priorities)])
    count = 0

    while queue:
        current_process = queue.popleft()
        if any(current_process[1] < process[1] for process in queue):
            queue.append(current_process)
        else:
            count += 1
            if current_process[0] == location:
                return count