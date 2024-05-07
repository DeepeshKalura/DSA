#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
from typing import List

class TrieNode:
    
    def __init__(self, value:str) -> None:
        self.value = value
        self.children:List[TrieNode] = [None] * 26
        self.isWorld = False


class Solution:

    def __init__(self) -> None:
        self.root  = TrieNode('/0')
    

    def insert(self, value)->None:
        curr:TrieNode = self.root
        for i in value:
            if(curr.children[ord(i) - ord('a')] == None):
                curr.children[ord(i) - ord('a')] = TrieNode(i) 
            curr = curr.children[ord(i) - ord('a')]
        
        curr.isWorld = True 
    
        
    def __searchPrefix(self, word:str)->str:
        curr:TrieNode = self.root
        prefix = ""
        for i in word:
            prefix+=i
            if(curr.children[ord(i) - ord('a')] == None):
                return word
            curr = curr.children[ord(i)- ord('a')]
            if(curr.isWorld):
                return prefix
        
        return word
        
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ss = sentence.split(" ")
        result:List[str] = []
        for i in dictionary:
            self.insert(i)
        

        for i in ss:
            result.append(self.__searchPrefix(i))

        return " ".join(result)
               



# @lc code=end


dictionary = ["a", "aa", "aaa", "aaaa"]

sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"

print(Solution().replaceWords(dictionary, sentence))