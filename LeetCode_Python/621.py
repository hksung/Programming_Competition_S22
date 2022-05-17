#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:42:05 2022

@author: hakyungsung
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = collections.Counter(tasks)
        result = 0
        while True:
            sub_count = n
            for i in tasks_count.most_common(n+1):
                if i[1] !=0:
                    sub_count -=1
                    result +=1
                    tasks_count[i[0]]-=1
                    
                    # ends function when nothing lefts
                
            if not any(tasks_count.values()):
                return result
            
            while sub_count >= 0:
                sub_count -=1
                result += 1