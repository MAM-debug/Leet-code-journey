// LeetCode Problem 509: Fibonacci Number
// Difficulty: Easy
// URL: https://leetcode.com/problems/fibonacci-number/

class Solution {
public:
    int fib(int n) {
        if(n==0 || n==1){
            return n;
        }
        return fib(n-1)+fib(n-2);
        
    }
};