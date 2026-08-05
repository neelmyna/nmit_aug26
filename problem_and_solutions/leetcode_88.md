```
i = last valid element in nums1
j = last index in nums2
k = last index of nums1 (n+m-1)

While i >= 0 and j >= 0
    If nums1[i] > nums2[j]
        nums1[k] = nums1[i]
        i--
    Else
        nums1[k] = nums2[j]
        j--
    k--
While j >= 0
    Copy remaining elements
Return nums1
```
