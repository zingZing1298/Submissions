def threeSumClosest(self, arr, k):
        min_diff = 99999999999999
        arr.sort()
        result = 0
        n = len(arr)
        for i in range(n-2):
            p1,p2 = i+1,n-1
            while(p1 < p2):
                sum1 = arr[i] + arr[p1] + arr[p2]
                diff = abs(k-sum1)
    
                if diff ==0:
                    return sum1
                
                if diff < min_diff:
                    min_diff = diff
                    result = sum1
                
                if sum1 <= k:
                    p1+=1
                else:
                    p2 -= 1
        return result