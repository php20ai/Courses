

# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    N=len(A)
    emp=[]
    for i in range(N):
        m=(i+K-1) % N
        emp.append(A[m])
    return emp


print(solution([3, 8, 9, 7, 6], 3 ))

#### solution to codility problem 2 #####

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# All comments shown below are from the applicant
# First, I notice a pattern when I see examples from task 1, i.e., when A=[3,8,9,7,6] and K=3, the "solution" function returns [9,7,6,3,8], here I notice that the value "3" in array A has index 0, and "3" in [9,7,6,3,8] has index 3, 8 in array A has index value 1 and 8 in [9,7,6,3,8] has index value 4, and so on, this also applies to all other examples in task 1. So I notice that get the out put of the function "solution" from its input array, we need to add K to each index in A, then take modulo N, where N is the length of array A, then the value at the original index i in A, now has index at K+i in the output array, so e.g.

# consider A=[3,8,,97,6,3,8] and K=3, in A "9" has index 0, so 0+K=0+3=3, and 3mod(5)=3, where 5 is length of array A, so "9" is now at index 3 in the output array []

def solution(A, K):
   N=len(A) # here N is the length of rray A
   emp=[] # here created an empty array
   for i in range(N): 
       emp.append(i)
    # The for loop above changes array emp, to an array of length N
   for j in range(N):
        m=(j+K) % N
        emp[m]=A[j]
   return emp