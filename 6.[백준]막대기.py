def solution(sticks):
    answer = sticks[len(sticks)-1]
    count  = 1
    for i in range(len(sticks)-2 , -1 , -1):
        if sticks[i] > answer :
            count = count +1
            answer = sticks[i]
        
    return count


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(solution(arr))