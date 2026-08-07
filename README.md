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
stk = empty() # take a empty list(Stack)
For each char in in InputString do:
If char is '(' or '[' or '{' then:
stk.push(ch)
Else # Thechar is mostly a closing bracket
If stack.empty() # so you have more closing brackets than opening
Return false # Hence return false
top = stk.pop() # if the char is matching pair
If top == '(' and ch != ')' # IF the opening and closing brackets are different
top == '[' and ch != ']'
top == '{' and ch != '}'
return false
Return stack.empty() # If the Stack still has characters in it (which is the extra opening brackets), return false. If the Stack is empty then everything has gone fine! Hence return true.

---

LeetCode #232

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

---

## 2 Lists Converge or Not!

if head1 == None or head2 == None:"
return False

ptrA = head1 #Point to 1st list
ptr2 = head2 #Point to 2nd list

while ptrA != ptr2:
if ptrA == None: #if list1 exhausts
ptrA = head2
else:
ptrA = ptrA.next
if ptrB == None: #if list2 exhausts
ptrB = head1
else:
ptrB = ptrB.next
return ptrA

# When loop breaks, either ptrA and ptrB point to the node of conversion, else both are None

create list1()
create list2()
check_if_converge()

---

def converges(head1, head2) -> bool:
    p1 = head1
    p2 = head2
    if head1 == None or head2 == None:
        return False
    while p1.next != None or p2.next != None:
        if p1.next != None:
            p1 = p1.next
        if p2.next != None:
            p2 = p2.next
    
    if p1 == p2:
        return True
    return False

def converges(head1, head2) -> bool:
    p1 = head1
    p2 = head2

    list_nodes = set()
    # add all nodes of list1 to set
    while p1 != None:
        list_nodes.add(p1)
        p1 = p1.next
    
    while p2 != None:
        if list_nodes has p2:
            return True
    return False

i = -1
i -= -1
print(i)

result = 1 ** 2 ** 3 ** 3
print(result)

num = 25
while num <= 50:
    print(num)
    num += 7
else:
    print(10)

s1 = 'bengaluru'
s2 = 'ooru'
print(s1.index(s2, 1))
print(s1.find(s2, 0, 20))

s1 = 'bengaluru'
s2 = 'ooru'
try
    print(s1.index(s2, 1))
    print(s1.find(s2, 0, 20))
except exception as e:
    print(e)
except ValueError as ve:
    print(e)
print('Afterwards')