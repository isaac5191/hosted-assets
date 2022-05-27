# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(str1,str2):
    # [assignment] Add your code hereh
    str1=input("ENTER the first value:")
    str2=input("Enter the second value:")
    str1_anagrams = sorted(str1)
    str2_anagrams =  sorted(str2)
    if str1_anagrams == str2_anagrams :
       return True
    else:
       return False
   
print(find_anagrams ('str1','str2'))
