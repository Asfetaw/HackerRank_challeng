#Day 18: Queues and Stacks
import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.mylist_stack=[]
        self.mylist_queue=[]
    def pushCharacter(self,ch):
        self.mylist_stack.append(ch)
    def enqueueCharacter(self,ch):
        self.mylist_queue.append(ch)
    def popCharacter(self):
        return self.mylist_stack.pop()
    def dequeueCharacter(self):
        d=self.mylist_queue[0]
        del self.mylist_queue[0]
        return d


# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
