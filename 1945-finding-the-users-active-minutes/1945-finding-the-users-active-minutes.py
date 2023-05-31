class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        #Initial thoughts
        #answer will be of len(k), whose element value is the number of users with 
        #that element's UAM 


        #Data Structure might look something like a hashTable where
        #{userNumber:(actions)}
        #userNumber is logs[i] = [IDi]
        #actions is a SET (unique list) logs[i] = [timei] (done)

        #Answer will be based on hashTable (UAM)
        #Look through hashTable (0, 1) == 2 users and count the UAM, aka
        #UAM == len(hashTable.values())
        #Be careful the 0th/1st counting indexing

        hashTable = {}

        for log in logs:
            if log[0] not in hashTable:
                someSet = {log[1]}
                hashTable[log[0]] = someSet
            else:
                hashTable[log[0]].add(log[1])

        print(hashTable)

        answer = {}
        for i in range(k):
            answer[i] = 0


        for user in hashTable:
            indexToAdd = len(hashTable[user]) - 1
            answer[indexToAdd] += 1
        

        return list(answer.values())




                