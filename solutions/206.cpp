// LeetCode Problem 206: Reverse Linked List
// Difficulty: Easy
// URL: https://leetcode.com/problems/reverse-linked-list/

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