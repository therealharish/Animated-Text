from collections import deque
from typing import List, Dict

def findMinimumSum(a: List[int], k: int) -> int:
    n = len(a)
    dq = deque()
    mp = {}
    ans = -1
    sum = 0
    for i in range(k):
        dq.append(a[i])
        if a[i] in mp:
            mp[a[i]] += 1
        else:
            mp[a[i]] = 1
        sum += a[i]
    
    for i in range(k, n):
        if len(mp) == k:
            ans = max(ans, sum)
        temp = dq.popleft()
        sum -= temp
        
        if mp[temp] == 1:
            mp.pop(temp)
        else:
            mp[temp] -= 1
        
        dq.append(a[i])
        sum += a[i]
        if a[i] in mp:
            mp[a[i]] += 1
        else:
            mp[a[i]] = 1
        
    if len(mp) == k:
        ans = max(ans, sum)
    return ans

if __name__ == "__main__":
    n = int(input())
    v = list(map(int, input().split()))
    k = int(input())
    print(findMinimumSum(v,k))
