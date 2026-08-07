# nmit_aug26

## This repo is created for the infy specific interview placement training for MCA of NMIT Bengaluru

## STEPS TO SOLVE A PROBLEM

### 1. Understand The Problem

Know what exactly the I/P is/are. What is the O/P. And the relevant information.

### 2. Find the Solution

Find the solution Mathematically or using trial and error method or using some specific formula or algorithm.

### 3. Write the Algorithm

Build the solution using step by step procedure.
Each step Must be simple, atomic, unambigious and finite.

### 4. Write the Fake Code

Writing pesudocode is necessary because we can apply SRP. We can focus only on the solution without having to worry about the syntax.

### 5. Flowchart, Find Efficiency and Optimize

For the given solution, for a given sample I/P, the time taken or the space required may vary. Thus the I/P data might lead to arriving at the O/P faster or may be slower. Thus you definitely have at least 2 efficiencues namely, best and worst.

### 6. Code it!

Implement the solution in a specific language/syntax.

### 7. Development

Unit testing, documentation, good coding practices, naming standards....

i++;
j--;
a[i] = b[j];
b[j]--;
a[++i] = b[--j]--;

float numbers[20];

float numbers[] = new float[size];

### Why index starts from zero

numbers[2]
_(numbers + 2) //numbers which name of the array is address of 1st element, and "+ 2" means jump 2 elements further. Lastly, uanry _ is value at opetator. NOTE: This syntax is available to use only in C/C++ but this is how/what is implemented in all languages.

---

input_size = int(input("Enter sie of the Array: "))

diameters = list() # []
print(f'Enter diameters of {input_size} Oranges: ')
for i in range(input_size):
print(i)
i += 2

[10, 20]
number >= 10 and number <= 20
number > 9 and number < 21
(5, 35)
number > 5 and number < 35
[3, 60)

for(int i = 1; i < 11; i++)
for(int i = 1; i <= 10; i++)

---

## P-Element Problem:

```
Array Size: N
Read numbers[N]
Read X, Y  such that X+ Y = N

Solution:
Sort numbers
P = numbers[y] - numbers[y-1] - 1
print P as result
```

---
DAY3 FRIDAY 07-08-2026

LeetCode Problem #20

Read InputString
stk = empty()  # take a empty list(Stack)
For each char in in InputString do: 
    If char is '(' or  '[' or '{' then:
        stk.push(ch)
    Else # Thechar is mostly a closing bracket
        If stack.empty() # so you have more closing brackets than opening
            Return false  # Hence return false
        top = stk.pop() # if the char is matching pair
        If top == '(' and ch != ')' # IF the opening and closing brackets are different
           top == '[' and ch != ']'
           top == '{' and ch != '}'
            return false
Return stack.empty() # If the Stack still has characters in it (which is the extra opening brackets), return false. If the Stack is empty then everything has gone fine! Hence return true.
---