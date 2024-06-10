from typing import List


class TrieNode:
    
    def __init__(self, value:str) -> None:
        self.value = value
        self.children:List[TrieNode] = [None] * 26
        self.isWorld = False
    



class Trie:
    def __init__(self) -> None:
        self.root = TrieNode('\0')


    def insert(self, value)->None:
        curr:TrieNode = self.root
        for i in value:
            if(curr.children[ord(i) - ord('a')] == None):
                curr.children[ord(i) - ord('a')] = TrieNode(i) 
            curr = curr.children[ord(i) - ord('a')]
        
        curr.isWorld = True 

    def __getNode(self, key:str)->TrieNode|None:
        curr:TrieNode = self.root

        for i in key:
            if(curr.children[ord(i) - ord('a')] == None):
                return None 
            curr = curr.children[ord(i)- ord('a')]
        
        return curr
    
    def delete(self, key)->None:
        node: TrieNode = self.__getNode(key)
        node.isWorld = False

        print(f"{key} has been successfully deleted")

    def search(self, key:str)->None:
        node:TrieNode = self.__getNode(key)
        return node != None and node.isWorld 

    def startsWith(self, prefix:str)->None:
        return self.__getNode(prefix) != None
