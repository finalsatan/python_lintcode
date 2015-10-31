class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(n):
        # write your code here
        if(n<0):
            return 0
        else:
            resultList = [1];
            for i in range(n):
                temp = 0
                for i in range(len(resultList)):
                    temp += resultList[i]*resultList[len(resultList)-1-i]
                resultList.append(temp)
            return resultList[n]

if __name__ == "__main__":
    
    for i in range(10):
        print( i, Solution.numTrees(i) )
