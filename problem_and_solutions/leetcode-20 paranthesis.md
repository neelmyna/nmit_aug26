# S.No. 6

# LeetCode 20. Valid Parentheses

**Difficulty:** Easy

**Category / Pattern:** Stack

---

## Problem Description
```
Given a string containing only ( ) { } [ ]
determine whether the brackets are valid.
A string is valid if:
    * Every opening bracket has a matching closing bracket.
    * Brackets close in the correct order.
```
---

## Example
``` 
1. Input: s = "()"
   Output: true
2. Input: s = "()[]{}"
   Output: true
3. Input: s = "(]"
   Output: false
```

---

## Observation
```
The last opening bracket must be closed first.
This is exactly the behavior of a **Stack (LIFO)**.
```
---

## Solution Idea
```
Whenever an opening bracket appears, push it onto the stack.
Whenever a closing bracket appears, check whether it matches the top element.
If not, return false.
```
---

## Algorithm
```
1. Create an empty stack.
2. Scan every character.
3. Opening bracket → Push.
4. Closing bracket → Compare with stack top.
5. If mismatch, return false.
6. At the end, stack should be empty.
```
---

## Pseudocode

```
stk = empty()
For each ch
    If '(' '[' '{'
        stk.push(ch)
    Else
        If stack.empty()
            Return false
        top = stk.pop()
        If top == '(' and ch != ')' or
           top == '[' and ch != ']'
           top == '{' and ch != '}'
            return false
Return stack.empty()
```

---

## Dry Run

```
s = "([{}])"
tok action              stack
(   push                (           
[   push                ([
{   push                ([{
}   match, pop          ([
]   match, pop          (
)   match, pop          empty
stop
return true
```

---

##  Complexity

```
Time = O(n)
Space = O(n)
```

---

## Key Learning Points
```
* Stack follows LIFO.
* Opening brackets are pushed.
* Closing brackets remove matching openings.
```
---

## Pattern Used

**Stack**

---

## Related Problems

* LC 155 Min Stack
* LC 225 Implement Stack
* LC 232 Implement Queue

# Implementation
Here is the translation of your pseudocode into Java, C++, and Python.

### Java

```java
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();        
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stk.push(ch);
            } else {
                if (stk.isEmpty()) {
                    return false;
                }
                char top = stk.pop();
                if ((top == '(' && ch != ')') ||
                    (top == '[' && ch != ']') ||
                    (top == '{' && ch != '}')) {
                    return false;
                }
            }
        }        
        return stk.isEmpty();
    }
}

```

### C++

```cpp
#include <stack>
#include <string>

class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> stk;        
        for (char ch : s) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stk.push(ch);
            } else {
                if (stk.empty()) {
                    return false;
                }
                char top = stk.top();
                stk.pop();
                
                if ((top == '(' && ch != ')') ||
                    (top == '[' && ch != ']') ||
                    (top == '{' && ch != '}')) {
                    return false;
                }
            }
        }        
        return stk.empty();
    }
};

```

### Python 3

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        
        for ch in s:
            if ch in "([{":
                stk.append(ch)
            else:
                if not stk:
                    return False
                
                top = stk.pop()
                if (top == '(' and ch != ')') or \
                   (top == '[' and ch != ']') or \
                   (top == '{' and ch != '}'):
                    return False
                    
        return len(stk) == 0

```