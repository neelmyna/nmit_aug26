# S.No. 32

# LeetCode 232. Implement Queue using Stacks

**Difficulty:** Easy

**Category / Pattern**

* Queue
* Design

---

## Problem Description
```
Implement a **Queue (FIFO)** using only stacks.
Support:
* push()
* pop()
* peek()
* empty()
```
---

## Observation
```
Two stacks can reverse the order of elements.
This produces FIFO behavior.
```
---

## Solution Idea
```
Maintain two stacks.
* Input Stack
* Output Stack
Move elements only when Output Stack becomes empty.
```
---

## Algorithm
```
1. Push into Input Stack.
2. Before pop/peek:
   * If Output Stack is empty,
     move all elements from Input Stack.
3. Pop/Peek from Output Stack.
```
---

## Pseudocode

```text
instk = empty()
outstk = empty()
Push(x)
    instk.push(x)
Pop()
    if outstk.empty()
        while NOT instk.empty()
            outstk.push(instk.pop())
    return outstk.pop()
Peek()
    if outstk.empty()
        while NOT instk.empty()
            outstk.push(instk.pop())
    return outstk.top()
Empty()
    return instk.empty() AND outstk.empty()
```

---

## Dry Run

Push

```text
1
2
3
```

Input Stack

```text
3
2
1
```

Pop

↓

Move all

↓

Output Stack

```text
1
2
3
```

Pop

↓

```text
1
```

---

## Time Complexity

| Operation | Complexity     |
| --------- | -------------- |
| Push      | O(1)           |
| Pop       | Amortized O(1) |
| Peek      | Amortized O(1) |
| Empty     | O(1)           |

---

## Space Complexity

```text
O(n)
```

---

## Key Learning Points
```
* Two stacks simulate queue behavior.
* Elements are transferred only when needed.
* Amortized analysis is important.
```
---

## Pattern Used
```
* Queue
* Stack
* Design
```
---

## Related Problems

* LC 225 Implement Stack using Queues
* LC 155 Min Stack
* LC 622 Design Circular Queue

# Implementation
This pseudocode is the classic algorithm for implementing a Queue using two Stacks (LeetCode 232: Implement Queue using Stacks).

Here is the translation into Java, C++, and Python.

### Java

```java
import java.util.Stack;

class MyQueue {
    private Stack<Integer> instk;
    private Stack<Integer> outstk;
    public MyQueue() {
        instk = new Stack<>();
        outstk = new Stack<>();
    }    
    public void push(int x) {
        instk.push(x);
    }    
    public int pop() {
        if (outstk.isEmpty()) {
            while (!instk.isEmpty()) {
                outstk.push(instk.pop());
            }
        }
        return outstk.pop();
    }    
    public int peek() {
        if (outstk.isEmpty()) {
            while (!instk.isEmpty()) {
                outstk.push(instk.pop());
            }
        }
        return outstk.peek(); // peek() gets the top element in Java
    }    
    public boolean empty() {
        return instk.isEmpty() && outstk.isEmpty();
    }
}

```

### C++

*Note: In C++, popping from a `std::stack` does not return the value, so we must access it using `.top()` before calling `.pop()`.*

```cpp
#include <stack>

class MyQueue {
private:
    std::stack<int> instk;
    std::stack<int> outstk;
public:
    MyQueue() {
    }    
    void push(int x) {
        instk.push(x);
    }    
    int pop() {
        if (outstk.empty()) {
            while (!instk.empty()) {
                outstk.push(instk.top());
                instk.pop();
            }
        }
        int val = outstk.top();
        outstk.pop();
        return val;
    }    
    int peek() {
        if (outstk.empty()) {
            while (!instk.empty()) {
                outstk.push(instk.top());
                instk.pop();
            }
        }
        return outstk.top();
    }    
    bool empty() {
        return instk.empty() && outstk.empty();
    }
};

```

### Python 3

*Note: In Python, standard lists are used as stacks using `.append()` for push and `.pop()` for pop.*

```python
class MyQueue:
    def __init__(self):
        self.instk = []
        self.outstk = []
    def push(self, x: int) -> None:
        self.instk.append(x)
    def pop(self) -> int:
        if not self.outstk:
            while self.instk:
                self.outstk.append(self.instk.pop())
        return self.outstk.pop()
    def peek(self) -> int:
        if not self.outstk:
            while self.instk:
                self.outstk.append(self.instk.pop())
        return self.outstk[-1] # [-1] gets the top element without removing it
    def empty(self) -> bool:
        return len(self.instk) == 0 and len(self.outstk) == 0
```