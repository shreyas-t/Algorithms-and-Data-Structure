MAX_CHARS = 26

def kUniques(s, k):
    count = [0]*MAX_CHARS
    n = len(s)
    u = 0

    max_start = 0
    max_end = 1

    start = 0
    end = 0
    window = set()

    for i in range(n):

        window.add(s[i])
        count[ord(s[i])- ord('a')] +=1
        end += 1
       
        while len(window)>k:
            start += 1
           
            count[ord(s[start])- ord('a')] -=1
            
            if(count[ord(s[start])- ord('a')]==0):
                window.remove(s[start])
        
        if max_end-max_start < end-start:
            max_start = start
            max_end = end
        
    
    print("Max substring is : " + s[max_start:max_end]  +" with length " + str(max_end-max_start) )

s = "aabacbebebe"
k = 3
kUniques(s, k) 