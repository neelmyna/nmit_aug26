nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

n = 3 # len of nums2 
m = 3 # len of nums1

i = m-1
j = n-1
k = m+n-1

while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1

nums1[k-j:k+1] = nums2[:j+1]

print(nums1)