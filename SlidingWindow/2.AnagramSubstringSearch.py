# https://www.techiedelight.com/find-substrings-string-permutation-given-string/

MAX_CHAR = 256

def compare(arr1, arr2):
    for i in range(MAX_CHAR):
        if arr1[i] != arr2[i]:
            return False
    return True

def searchAnagram(pat, txt):

    m = len(pat)
    n = len(txt)

    if m>n:
        print("The length of the anagram substring to search is greater than the text string")
        return 

    count_pat = [0]*MAX_CHAR
    count_text = [0]*MAX_CHAR

    for i in range(m):
        count_pat[ord(pat[i])] +=1
        count_text[ord(txt[i])] +=1
    
    
    
    for i in range(m,n):
        if compare(count_text, count_pat):
            print(txt[i-m])
        count_text[ord(txt[i])] += 1
        count_text[ord(txt[i-m])]-=1

    if compare(count_pat, count_text):
        print("Found at Index "+str(n-m))


txt = "BACDGABCDA"
pat = "ABCD"       
searchAnagram(pat, txt)    