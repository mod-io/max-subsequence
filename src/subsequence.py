#!/usr/bin/env python3
import sys

#Implement max subsequence and optimal value
def max_subsequence():

    charVal = {} #changed list to dic for .get()
    stringA = ""
    stringB = ""

    with open("data/example1.in") as file:

        k = int(file.readline().strip())

        for i in range(k):
            line = file.readline().strip()  
            parts = line.split()            
            charVal[parts[0]] = int(parts[1])

        stringA = file.readline().strip()  
        stringB = file.readline().strip()   

    n, m = len(stringA), len(stringB)

    dp = [[0] * (m + 1) for row in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if stringA[i - 1] == stringB[j - 1]:
                val = charVal.get(stringA[i - 1], 0)   
                dp[i][j] = dp[i - 1][j - 1] + val

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    #traceback
    result = []
    i, j = n, m

    while i > 0 and j > 0:

        if stringA[i - 1] == stringB[j - 1]:
            result.append(stringA[i - 1])  
            i -= 1; j -= 1

        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    result.reverse()
    value, subseq = dp[n][m], ''.join(result)

    print(value)
    print(subseq)
    
    return value, subseq

#added method w/ dp logic to run tests
def hvlcs(stringA, stringB, charVal):

    n, m = len(stringA), len(stringB)
    dp = [[0] * (m + 1) for row in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if stringA[i - 1] == stringB[j - 1]:
                val = charVal.get(stringA[i - 1], 0)
                dp[i][j] = dp[i - 1][j - 1] + val

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = []
    i, j = n, m

    while i > 0 and j > 0:

        if stringA[i - 1] == stringB[j - 1]:
            result.append(stringA[i - 1])
            i -= 1; j -= 1

        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    result.reverse()
    return dp[n][m], ''.join(result)


if __name__ == "__main__":
    max_subsequence()