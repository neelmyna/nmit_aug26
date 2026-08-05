from collections import Counter

def check_if_anagram1(s, t) -> bool:
    return sorted(s) == sorted(t)

def check_if_anagram2(s, t) -> bool:
    result = Counter(s) == Counter(t)
    return result

def check_if_anagram2(s, t) -> bool:
    

s = 'listen'
t = 'silent'

print(check_if_anagram2(s,t))
