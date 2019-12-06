# author: 汶穗
# period: 19.11.23 - 19.12.06

from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
                
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity

    def encode(self, key):
        key_before_hash = MD5.new()
        key_before_hash.update(key.encode('utf-8'))
        hexi_key_before_hash = key_before_hash.hexdigest()
        int_key_before_hash = int(key_before_hash.hexdigest(), 16)
        return int_key_before_hash
    
    def hash_function(self, int_key_before_hash):
        return int_key_before_hash % self.capacity
    
    def traversal_to_last(self, head):
        if head:
            cur = head
            if cur.next != None:
                cur = cur.next
        return cur
        
    def add(self, key):
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        
        find_drawer = self.data[drawer_index]
        
        if find_drawer == None:
            head_node = ListNode(int_key_before_hash)
            self.data[drawer_index] = head_node
        else:
            new_node = ListNode(int_key_before_hash)
            self.traversal_to_last(self.data[drawer_index]).next = new_node

    
    def find_val(self, head, int_key_before_hash):
        if head == None:
            return False
        
        if head.val == int_key_before_hash:
            return True
        else:
            cur = head.next
            self.find_val(cur, int_key_before_hash)
        return False
            
    def contains(self, key):
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        
        head = self.data[drawer_index]
        true_or_false = self.find_val(head, int_key_before_hash)
        return true_or_false
    
    def find_target(self, head, int_key_before_hash):
        if head:
            prev = head
            cur = head.next
            if cur:
                while cur.val != int_key_before_hash and cur.next!= None:
                    cur = cur.next
                    prev = prev.next
                if cur.val == int_key_before_hash:
                    return prev
        return False
    
    def edit_list(self, head, int_key_before_hash):
        if self.find_target(head, int_key_before_hash) == False:
            pass
        else:
            self.find_target(head, int_key_before_hash).next = self.find_target(head, int_key_before_hash).next.next
            self.edit_list(head, int_key_before_hash)
    
    def remove(self, key):
        int_key_before_hash = self.encode(key)
        drawer_index = self.hash_function(int_key_before_hash)
        
        head = self.data[drawer_index]
        self.edit_list(head, int_key_before_hash)
        if head.val == int_key_before_hash:
            self.data[drawer_index] = head.next

## Reference
# - [Data Structures and Algorithms Bootcamp:Binary Trees / by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/9512548#overview)
# - [目錄：演算法與資料結構](http://alrightchiu.github.io/SecondRound/mu-lu-yan-suan-fa-yu-zi-liao-jie-gou.html)
# - [Hash Table：Intro(簡介)](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html)
# - [Hash Table：Chaining](http://alrightchiu.github.io/SecondRound/hash-tablechaining.html)
# - [白話的 Hash Table 簡介](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)
# - [Hash Table From Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
# - [加密和雜湊有什麼不一樣？](https://blog.m157q.tw/posts/2017/12/25/differences-between-encryption-and-hashing/)
# - [如何區分加密、壓縮、編碼](https://blog.m157q.tw/posts/2017/12/23/differences-between-encryption-compression-and-encoding/)
# - [從刪除 linked-list node 看程式設計的品味](https://medium.com/fcamels-notes/%E5%BE%9E%E5%88%AA%E9%99%A4-linked-list-node-%E7%9C%8B%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E7%9A%84%E5%93%81%E5%91%B3-b597cc5af785)
