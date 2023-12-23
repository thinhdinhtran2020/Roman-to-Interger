class Solution:
    def romanToInt(self, s):
        numList = []
        for i in s:
            if i == 'I':
                numList.append(1)
            if i == 'V':
                numList.append(5)
            if i == 'X':
                numList.append(10)
            if i == 'L':
                numList.append(50)
            if i == 'C':
                numList.append(100)
            if i == 'D':
                numList.append(500)
            if i == 'M':
                numList.append(1000)
        for i in range(len(numList)):
            if (i+1) == len(numList) or (i+1) > len(numList):
                return sum(numList)
            if numList[i] < numList[i+1]:
                numList[i] = numList[i+1] - numList[i]
                numList.remove(numList[i+1])
        return sum(numList)

def main():
    solution = Solution()
    print(solution.romanToInt('MCMXCIV'))
    
main()