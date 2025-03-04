// https://leetcode.com/problems/greatest-common-divisor-of-strings

#include <bits/stdc++.h>

using namespace std;

class Solution {
    /**
     * For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
     * (i.e., t is concatenated with itself one or more times).
     * 
     * Given two strings str1 and str2, return the largest string x such that x divides 
     * both str1 and str2.
     */
    private:
        int gcd(int a, int b) {
            while (b != 0) {
                int temp = b;
                b = a % b;
                a = temp;
            }
            return a;
        }
    
    public:
        string gcdOfStrings(string str1, string str2) {
            if (str1 + str2 != str2 + str1) {
                return "";
            }
    
            int a = str1.length();
            int b = str2.length();
            
            int k = gcd(a, b);
            return str1.substr(0, k);
        }
    };