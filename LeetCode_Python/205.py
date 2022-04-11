#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 00:47:42 2022

@author: hakyungsung
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_map = dict()
        idx_s = 0
        converted_s = ""
        
        for c in s:
            if c not in s_map:
                s_map[c] = idx_s
                idx_s += 1
            converted_s += str(s_map[c]) + " "
            
        t_map = dict()
        idx_t = 0
        converted_t = ""
        
        for c in t:
            if c not in t_map:
                t_map[c] = idx_t
                idx_t += 1
            converted_t += str(t_map[c]) + " "
            
        return converted_s == converted_t

s1, t1 = "egg", "add"
s2, t2 = "foo", "bar"
s3, t3 = "paper", "title"
s4, t4 = "abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck"

sol = Solution()
print(sol.isIsomorphic(s1, t1))
print(sol.isIsomorphic(s2, t2))
print(sol.isIsomorphic(s3, t3))
print(sol.isIsomorphic(s4, t4))