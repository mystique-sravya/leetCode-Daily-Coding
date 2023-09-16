from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q  = deque()
        
        n = len(tickets)  
        # get length of tickets 
        for i in range(n):
            q.append(i) # add tickets indices to queue
            
        #initialize time to 0
        # As each person comes give one ticket and each person goes to back of queue
        t = 0 
        while(True):
            # get each index of ticket_count from front end of queue by popping it
            x = q.popleft()
            tickets[x]-= 1
            # for each index , ticket_count is reduced by 1 and time is increased by 1
            t += 1
            if ( x == k and tickets[k] == 0):
                return t
            # after reducing if the ticket_count is not 
            if tickets[x] > 0:
                q.append(x)
            
            
            
            
            