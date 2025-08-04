# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 12:08:10 2025

@author: hp
"""

'''1) Write a program to check if a number is a strong or not'''

import math

def is_strong_number(number):
    original = number
    sum_of_factorials = 0

    while number > 0:
        digit = number % 10
        sum_of_factorials += math.factorial(digit)
        number //= 10

    return sum_of_factorials == original

# Take input from user
try:
    user_input = int(input("Enter a number to check if it's a strong number: "))
    if is_strong_number(user_input):
        print(f"{user_input} is a strong number.")
    else:
        print(f"{user_input} is not a strong number.")
except ValueError:
    print("Please enter a valid integer.")

# Test cases
print("\nRunning test cases:")
test_numbers = [1, 2, 145, 40585, 123, 0]
for num in test_numbers:
    result = "Strong" if is_strong_number(num) else "Not Strong"
    print(f"{num}: {result}")



#2) 2.	Find the First Non-Repeating Character in a String

#3.	Count Pairs with a Given Sum in a List
def count_pairs_with_sum(nums, target_sum):
    count = 0
    seen = {}

    for num in nums:
        complement = target_sum - num
        if complement in seen:
            count += seen[complement]
        seen[num] = seen.get(num, 0) + 1

    return count

# Take input from user
try:
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, user_input.strip().split()))
    target = int(input("Enter the target sum: "))

    result = count_pairs_with_sum(numbers, target)
    print(f"Number of pairs with sum {target}: {result}")

except ValueError:
    print("Please enter valid integers only.")

# Test Cases
print("\nRunning test cases:")
test_cases = [
    ([1, 5, 7, -1, 5], 6),        # Output: 3 (1+5, 7+(-1), 1+5 again)
    ([1, 1, 1, 1], 2),            # Output: 6 (4C2 = 6 pairs)
    ([10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1], 11),  # Output: 9
    ([1, 2, 3, 4, 5], 9),         # Output: 1 (4+5)
    ([0, -1, 2, -3, 1], -2),      # Output: 1 (-3 + 1)
    ([], 4),                      # Output: 0
    ([3], 3),                     # Output: 0
]

for nums, target in test_cases:
    res = count_pairs_with_sum(nums, target)
    print(f"List: {nums}, Target Sum: {target} -> Pairs Count: {res}")


# 4.	Move All Zeros to the End of a List

def move_zeros_to_end(arr):
    non_zero_index = 0

    # First pass: move all non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1

    # Second pass: fill the remaining positions with zeros
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0

    return arr

# Take input from user
try:
    user_input = input("Enter list elements separated by spaces: ")
    user_list = list(map(int, user_input.strip().split()))

    result = move_zeros_to_end(user_list.copy())
    print("List after moving zeros to end:", result)
except ValueError:
    print("Please enter valid integers.")



for case in test_cases:
    output = move_zeros_to_end(case.copy())
    print(f"Input: {case} → Output: {output}")
    
##5.	Check if a String is a Palindrome (Ignoring Case and Spaces)
## Palindrome numbers are the numbers which is same if we reversed them
# example 141 = 141
def is_palindrome(s):
  """
  Checks if a given string is a palindrome, ignoring case and spaces.

  Args:
    s: The input string.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  # Step 1: Remove spaces and convert to lowercase
  # This makes the comparison case-insensitive and ignores spacing.
  processed_s = "".join(filter(str.isalnum, s)).lower()

  # Step 2: Compare the processed string with its reverse
  # A string is a palindrome if it reads the same forwards and backwards.
  return processed_s == processed_s[::-1]

# --- Test Cases ---

# Example 1: Basic palindrome
string1 = input("enter a string to check it is palindrome or not: ")
print(f"'{string1}' is a palindrome: {is_palindrome(string1)}")

##6.	Fibonacci Series up to N Terms (Using Recursion and Memoization)

# Dictionary to store memoized results
memo = {}

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # If result is already computed, return it
    if n in memo:
        return memo[n]

    # Recursively compute and store in memo
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

# Function to print Fibonacci series up to N terms
def print_fibonacci_series(n_terms):
    print(f"Fibonacci series up to {n_terms} terms:")
    for i in range(n_terms):
        print(fibonacci(i), end=' ')
    print()

# Taking user input
n = int(input("Enter the number of terms: "))
print_fibonacci_series(n)

##7.	Check If Two Strings are Anagrams

from collections import Counter

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return Counter(str1) == Counter(str2)

# Take input from the user
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if are_anagrams(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

#8.	Find the Missing Number in a List of N Natural Numbers
def find_missing_number(nums):
    n = len(nums) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Input from user
nums = list(map(int, input("Enter numbers separated by space: ").split()))
missing = find_missing_number(nums)
print("The missing number is:", missing)

#9.	Find All Duplicates in a List Without Using Set
def find_duplicates(nums):
    duplicates = []
    count_dict = {}

    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num in count_dict:
        if count_dict[num] > 1:
            duplicates.append(num)

    return duplicates

# Input from user
nums = list(map(int, input("Enter list elements separated by space: ").split()))
dups = find_duplicates(nums)

if dups:
    print("Duplicates found:", dups)
else:
    print("No duplicates found.")


## count the numberof decreasing sequences and max_length
input1 = [11,3,1,4,7,8,12,2,3,7]
def count_decreasing_sequences(input1):

    input2 = len(input1)

    count_sequences = 0 # Number of decreasing sequences
    max_length = 0 #longest sequence length
    current_length = 1 #Start with 1 (every number is its own sequence)

    for i in range(1, input2): # start form second element
       if input1[i] < input1[i-1]: #if its decreasing
          current_length +=1 #increase sequence length
       else:
           if current_length > 1: #if we had a decreasing sequence
              count_sequences +=1 #count the sequence
              max_length = max(max_length, current_length) #update
              current_length=1 #reset for new sequence
    if current_length > 1:
      count_sequences +=1
      max_length = max(max_length, current_length)
    return count_sequences, max_length

print(count_decreasing_sequences(input1))


##### 
def find_odd_sequences(input1):
    sequences = []
    current_sequence = []

    for num in input1:
        if num % 2 != 0:  # If the number is odd
            current_sequence.append(num)
        else:
            if current_sequence:  # If we were building a sequence
                sequences.append(current_sequence)
                current_sequence = []

    # Handle any sequence left at the end
    if current_sequence:
        sequences.append(current_sequence)

    return sequences

# Test input
input1 = [11,3,1,4,7,8,12,2,3,7]

# Get and print odd sequences
odd_sequences = find_odd_sequences(input1)
print("Odd number sequences:")
for seq in odd_sequences:
    print(seq)


# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 10:11:45 2025

@author: user
"""

#Check if a Number is a Strong Number
'''
What is a Strong Number?
A Strong Number is a number whose sum of the factorials 
of its digits equals the number itself.

Examples:

145 → 1! + 4! + 5! = 1 + 24 + 120 = 145 
2 → 2! = 2 
123 → 1! + 2! + 3! = 1 + 2 + 6 = 9 

'''
def is_strong_number(num):
    def factorial(n):
        return 1 if n == 0 else n * factorial(n - 1)
        '''
        Defines a recursive factorial function:
        If n is 0 → return 1 (since 0! = 1)
        Else → return n * factorial(n - 1)
       So: factorial(5) = 5 × 4 × 3 × 2 × 1 = 120
       factorial(0) = 1
         
     '''
    return num == sum(factorial(int(d)) for d in str(num))
'''
Converts the number into a string → str(num)
for d in "145":  # Loop runs 3 times
    d = '1'  → then d = '4'  → then d = '5'
For example, 145 becomes "1", "4", "5"
Converts each digit d back to an integer → int(d)
Calculates the factorial of each digit → factorial(int(d))
Sums them all → sum(...)
Compares the sum to the original number → return num == sum(...)

'''
# Example
print(is_strong_number(145))  # True

is_strong_number(145) 
is_strong_number(2) 
is_strong_number(123) 

#Find the First Non-Repeating Character in a String
def first_unique_char(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None
'''
Check If Character is Unique
if s.count(ch) == 1:
For the current character ch, it counts how many times 
it appears in the string using s.count(ch).
If it appears only once, it's considered unique.

'''
# Example
print(first_unique_char("engineering"))  # r

first_unique_char("leetcode")    # 'l' is the first unique character
first_unique_char("aabbcddex")  # 'c' is the first unique character
first_unique_char("aabb")       # All characters repeat
first_unique_char("x")           # Single character, so it's unique

first_unique_char("aAbBcCdD")    # 'a' is different from 'A', so 'a' is unique
first_unique_char("AaBbCcDd")    # Each appears once, return the first one
##########################

#Count Pairs with a Given Sum in a List
'''
A unique pair refers to a distinct combination of two numbers 
that add up to a given target without considering order or repeated values.
lst = [1, 5, 7, -1, 5]
target = 6
Now let’s find all pairs that sum to 6:
(1, 5)
(1, 5) ← duplicate in values
(7, -1)


count = 0: To keep track of the number of valid pairs.
seen = set(): A set to keep numbers we’ve already seen while iterating through the list.

a + b == target
a == target - num
The seen set is used to remember the numbers you've already visited 
in the list — so that for each new number, 
you can check if there's a previously seen number that forms a valid pair with it.


Step	num	target - num	What's in seen before?	Is target - num in seen?	Action Taken	count
1	     1	6 - 1 = 5	     {}	                     No	Just add 1 to seen	0
2	     4	6 - 4 = 2	     {1}	                 No	Just add 4 to seen	0
3	     5	6 - 5 = 1	    {1, 4}	                 Yes → (1, 5) is a pair	Count += 1, add 5 to seen	1
4	     3	6 - 3 = 3	{1, 4, 5}	                 No	Just add 3 to seen	1
5	     2	6 - 2 = 4	{1, 3, 4, 5}	             Yes → (2, 4) is a pair	Count += 1, add 2 to seen	2


'''
def count_pairs(lst, target):
    count = 0
    seen = set()
    for num in lst:
        if target - num in seen:
            count += 1
        seen.add(num)
    return count

# Example
print(count_pairs([1, 5, 7, -1, 5], 6))  # 3
#############################
#Move All Zeros to the End of a List
'''
Step 1: Filter out non-zero elements
non_zero = [x for x in lst if x != 0]
#This list comprehension creates a new list containing only the elements that are not zero.
lst = [0, 1, 0, 3, 12]
non_zero = [1, 3, 12]
#Step 2: Calculate how many zeros were removed
[len(lst) - len(non_zero)]
In our example:
len(lst) = 5
len(non_zero) = 3
So we need 2 zeros at the end
Step 3: Concatenate non-zeros and zeros
return non_zero + [0] * (len(lst) - len(non_zero))
[0] * 2 → creates [0, 0]
Then adds this to [1, 3, 12]
[1, 3, 12, 0, 0]


'''
def move_zeros(lst):
    non_zero = [x for x in lst if x != 0]
    return non_zero + [0] * (len(lst) - len(non_zero))

# Example
print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
###############################
#Check if a String is a Palindrome (Ignoring Case and Spaces)
def is_palindrome(s):
    s = ''.join(s.lower().split())
    return s == s[::-1]

# Example
print(is_palindrome("A man a plan a canal Panama"))  # True
###################################
#Fibonacci Series up to N Terms (Using Recursion and Memoization)
'''
What is the Fibonacci sequence?
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Each number is the sum of the two previous numbers:
  a, b = b, a + b  
We’re doing:
Add current number a to the result.
Then shift the pair forward:
a becomes b (next Fibonacci number)
b becomes a + b (the one after that)

'''
def fibonacci_series(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci_series(10))

##########################
#Check If Two Strings are Anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example
print(are_anagrams("listen", "silent"))  # True
#####################
#Find the Missing Number in a List of N Natural Numbers
def find_missing_number(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)

# Example
print(find_missing_number([1, 2, 4, 6, 3, 7, 8]))  # 5
#########################
#Find All Duplicates in a List Without Using Set
def find_duplicates(lst):
    duplicates = []
    seen = {}
    for item in lst:
        if item in seen:
            if seen[item] == 1:
                duplicates.append(item)
            seen[item] += 1
        else:
            seen[item] = 1
    return duplicates

####
#input1 = [3, 1, 5, 2, 4, 6, 7, 9, 11, 8, 10, 12, 13 , 15, 17, 19]
#nput1 = [1, 3, 5, 2, 7, 9, 11, 4, 13, 15, 17]
#input1= [2, 4, 6, 7, 9, 11]
#input1= []
input1= [1, 3, 5, 2 ,4]
def sum_of_odd(input1):
    current_length=0
    current_sum=0
    max_length=0
    longest_sum=[]
    for num in input1:
        if num%2!=0:
            current_length+=1
            current_sum+=num
        else:
            if current_length>max_length:
                max_length=current_length
                longest_sum=[current_sum]
            elif current_length==max_length:
                longest_sum.append(current_sum)
                current_length=0
                current_sum=0
    if current_length>max_length:
        max_length=current_length
        longest_sum=[current_sum]
    else:
        current_length==max_length
        longest_sum.append(current_sum)
    print(sum(longest_sum) if longest_sum else -1)
sum_of_odd(input1)




###
'''Example - If the given number is 58109, the sum of power of digits ==
(5 raised to the power of 8) + (8 raised to the power)
= 390625 + 64 + 2 + 1 + 0+ 1= 390693

Alex contacts you to help him write a program for finding sum of power digits.
write the logic in the given function sumOfPowerOfDigits
where,
input1 represents the given number.
The function is expected to return
the "sum fo powers of  digits" of input1 '''

def sumOfPowerOfDigits(input1):
    # Convert the number to a string
    num_str = str(input1)

    total_sum = 0

    for i in range(len(num_str)):
        base = int(num_str[i])  # corrected typo here

        # The base is the current digit in the number.
        # Example: If the num_str = "58109"

        if i + 1 < len(num_str):
            exponent = int(num_str[i + 1])
        else:
            exponent = 0  # If last digit, raise to power 0 (anything^0 = 1)

        total_sum += base ** exponent

    return total_sum

# Test cases
test_number = 582109
print(sumOfPowerOfDigits(test_number))

input1 = 98
print(sumOfPowerOfDigits(input1))



'''
How to attempt?
Sum of Sums of Digits in cyclic Order: Alex has been asked by

If the given number is 582109, the sum of Sums of Digits will be 
= (5+8+2+1+0+9)+(8+2+1+0+9) + (2+ 1 + 0)
= 25 + 20 + 12 + 10 + 9 + 9 =085
'''
def sumOfSumsOfDigits(input1):
     num_str = str(input1)
     total_sum = 0
     
     for i in range(len(num_str)):
         digits = num_str[i:]
         digit_sum = sum(int(digit) for digit in digits)
         total_sum += digit_sum
    
     return total_sum 
#input1 = 582109
input1= 111
print(sumOfSumsOfDigits(input1)) 

################
'''
Identify possible words: Detective Bakshi , while solving a case, stunmbled upon
a leeter that had many words where one character was missing, i.e., one character in the words
 was replaced by an underscore. For example, "Fi_er". He also found thin
 strips of paper which had a group of words separated by colons.
 For example:
"Fever:filer:Filter:Fixer:fiber:fibre:tailor:offer".

He could figure out that hte word whose one character was missing
was one of the possible words from the thin strips of paper.
Detective Bakshi has approached you ( a computer programmer)
asking for help in identifying the possible words for each incomplete word.

You are expected to write a funtion to identify the set of possible words
The function identifyPossiblewords takes two strings as input where:

input1 contains the incomplete word.
input2 is the string containing a set of words separated by colons.
The function is expected to find all the possible words from input2
that can replace the incomplete word input1
and return the result in the format suggested below.

Example 1-
input1="Fi_er"
input2="Fever:filer:Filter:Fixer:fiber:tailor:offer"
output string should be returned as "FILER:FIXER:FIBER"
'''
def identifyPossibleWords(input1, input2):
    
    words=input2.split(":")
    
    valid_words= []
    
    input1=input1.strip()
    words = [word.strip() for word in words]
    
    for word in words:
        if len(word) != len(input1):
            continue
        #If the word length doesn't match the pattern length, skip it.
        is_match=True # Assume it's a match
        for c1,c2, in zip(input1,word):
            if c1 == "_":
                continue
            if c1.lower() != c2.lower():
                is_match=False
                break
            #For each character pair from input1 and word
            #do the following:
            #If the pattern character c1 is an underscore (_),
            #skip comparison (wildcard)
            #Otherwise, compare characters
            #(case-insensitive using .lower()).
            #If any character doesn't match, it's not valid word.
        if is_match:
            valid_words.append(word.upper())
    
    return ":".join(valid_words)
#Test case

input1 = "Fi_er"
input2 = "Fever:filer:Filter:Fixer:fiber:fibre:tailor:offer"

output = identifyPossibleWords(input1 , input2)
print(f"Expected: FILER:FIXER:FIBER, Got: {output}")


# Test case 2
input1 = "_____"
input2 = "apple:ample:angle:alier:alert:abcde:banana"

output = identifyPossibleWords(input1, input2)
print(output)


#Test case 3

input1 = "Te_t"
input2= "test:TExt:TeSt:tent:tEsting"

output= identifyPossibleWords(input1, input2)
print(output)

#Test case 4
 
input1 = "W_rd"
input2 = "card:hard:wardrobe"
output = identifyPossibleWords(input1, input2)
print(output)


#############
'''
Encoding three strings
Anand was assigned the task of coming up with
an encoding mechanism for any given three strings.
He has come with the following plan.

Step1: Splitting Each String into Three Parts
Given three input strings, break each string
into three parts: Front, Middle , and End.

Rules of Splitting:
If the string length is a multiple of 3,
divide it into equal three parts.
If the string length is not a multiple of 3:
If one extra character is present, assign it to the middle part.
If two extra characters are present, assign
one extra character each to the front and end parts.
Example Splitting:

For Input1 = "John" (Length = 4, i.e., 3+1)

Front = "J"
Middle = "oh" (gets the extra character)
End = "n"
For Input2= "Johny" (Length = 4,i.e., 3+1)

front = "Jan"
Middle = "ard"
End = "han"
Step 2: Concatenation of Parts
After Splitting, concatenate the corresponding parts from all

output1= Front1+Front2+Front3
Output2= Middle1 + Middle2 + Middle3
Output3 = End1 +End2 +End3
using the example:
    
'''
s1 = "John"
s2 = "Johny"
s3 ="Janardhan"
lst = [s1, s2, s3]
char_list= [list(word)for word in lst]
for char in char_list:
    n= len(char)
 
first_parts
    
    if n%3 ==1p:
        first = char[:1]
        middle = char[1:n-1]
        end = char[n-1:]
    
    elif n%3 ==2 :
        first = char[:2]
        middle = char[2:n-2]
        end= char[n-2:]
    
    else:
        first = char[:3]
        middle = char[3:6]
        end= char[6:9]
        
    print(f"First:{''.john(first))},
          Middle:{''.join(middle)},End:{''.join(end)}")
        
    
    
    
    
    
    
    
    
    
    
    
    































































     

     
     
     
     
      
        
        
        
        
        
        
        
        
        
        
        












