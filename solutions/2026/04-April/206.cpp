@date: 2026-04-24
@problem: 206. Reverse Linked List
@leetcode: https://leetcode.com/problems/reverse-linked-list/
@difficulty: Easy
@tags: linked-list, recursion
@language: C++

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode*current=head;
        ListNode*prev=nullptr;
        ListNode*next=nullptr;
        while(current!=nullptr){
            next=current->next;
            current->next=prev;
            prev=current;
            current=next;
        }
        return prev;
    }
};