from typing import List

class HashingConcepts:
    def __init__(self):
        self.hashed = [0] * 26

    # In python me can get the ascii values using ord() function 
    def asciiP(c: str ):
        return ord(c)


    # So lets hash a string

    def hashAString(self, s: str):
        # first we convert to lower case 
        lower = s.lower()
        
        for i in range(0, len(lower), 1):
            # index value nikalne ke liye ascii ko apan 'a' se minus krenge kyuki lower a = 97 so 97-97= 0
            #  a apna first index pr jayega
            index = ord(lower[i]) - ord('a') #or 97
            # print(index)
            self.hashed[index] += 1
    
    def getHashedCharCount(self, s:str):
        index = ord(s.lower()) - ord('a')
        val = self.hashed[index]
        return val
    



def countFrequencies(nums: List[int]):
    o = {}

    for i in range(0, len(nums), 1):
        if(nums[i] in o):
            v = o.get(nums[i])
            u = v + 1
            o.update({nums[i]: u})
        else:
            o[nums[i]] = 1
    
    a = []
    for k,v in o.items():
         a.append([k,v])
    return a

def maxFrequencies(nums: List[int]):
    o = {}

    for i in range(0, len(nums), 1):
        if(nums[i] in o):
            v = o.get(nums[i])
            u = v + 1
            o.update({nums[i]: u})
        else:
            o[nums[i]] = 1
    
    a = 0
    c = 0
    for k,v in o.items():
         if v > c:
            c = v
            a = k
    return a




if __name__ == '__main__':
    # print(asciiP('a'))
    # a = HashingConcepts()
    # a.hashAString('aabbaaacccc')
    # c = a.getHashedCharCount('a')
    # print(c)
    feq = maxFrequencies([1,2,1,2,4,5,12,6,2,1,1])
    print(feq)

