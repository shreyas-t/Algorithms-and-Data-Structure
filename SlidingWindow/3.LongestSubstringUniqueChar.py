# https://www.techiedelight.com/find-longest-substring-given-string-containing-distinct-characters/

CHAR_SIZE = 256

def containsUnique(count):
    for i in range(CHAR_SIZE):
        if(count[i]>1):
            return False
    return True

def longestSubString(str):

    n = len(str)
    count = [0]*CHAR_SIZE

    start = 0
    end = 0

    max_start = 0
    max_end = 0

    for i in range(n):

        count[ord(str[i])] += 1
        end += 1
        print(str[start:end], containsUnique(count))
        print(str[start:end])

        while(not containsUnique(count)):
            
            count[ord(str[start])] -= 1
            start +=1
        
        if(end-start > max_end-max_start):
            max_start = start
            max_end = end
    
    return str[max_start:max_end]




str = "abbcdafeegh"
print(longestSubString(str))