@date: 2026-04-24
@problem: 509. Fibonacci Number
@leetcode: https://leetcode.com/problems/fibonacci-number/
@difficulty: Easy
@tags: math, dynamic-programming
@language: C++

class Solution {
public:
    int fib(int n) {
        if(n==0 || n==1){
            return n;
        }
        return fib(n-1)+fib(n-2);
        
    }
};