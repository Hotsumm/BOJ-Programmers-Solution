def solution(n):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 2
    if n < 2 :
        answer = dp[n-1]
        return answer

    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2] 
        
    answer = dp[n-1]%1234567
    return answer
