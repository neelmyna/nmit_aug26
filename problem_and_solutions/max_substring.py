s = input('Enter the input string: ')

seen = set()
left = 0
maximum_length = 0
current_length = 0
right = 0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    # maximum_length += 1
    current_length = right - left + 1
    maximum_length = max(maximum_length, current_length)
print(maximum_length)