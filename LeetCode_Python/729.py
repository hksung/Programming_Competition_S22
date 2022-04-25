#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:24:57 2022

@author: hakyungsung
"""

#leetcode_729: My Calendar1

class MyCalendar:

    def __init__(self):
        self.book_state=[]

    def book(self, start: int, end: int) -> bool:

        if len(self.book_state) ==0:
            self.book_state.append([start, end]) #new iput
            return True
        
        else:
            for state in self.book_state:
                if start>= state[1] or end <= state[0]: #fits to the condition
                    continue
                else:
                    return False
            self.book_state.append([start, end])
            
            return True

