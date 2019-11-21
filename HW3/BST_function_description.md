# HW3: BST新增/刪除/查詢/修改功能說明
陳汶穗｜巨資四B｜04113020

初始想法
- `insert()`新增: 新增節點，讓所有節點依照二元搜尋樹的規則排列好。
- `delete()`刪除: 刪除指定的節點，並讓剩下的節點依照二元搜尋樹的規則排列好。
- `search()`查詢: 搜尋某個節點的值
- `modify()`修改: 把所有具有相同值得節點改成另一個值，並讓更新後的所有節點依照二元搜尋樹的規則排列好。

## 一、新增
`insert()`
```python
def insert(self, root, val):

        # 如果root沒有東西，把新insert()的val當成root    
        if root == None:
            new_node = TreeNode(val)
            root = new_node
            return root

        # 若root有東西，建立一個新的Node
        new_node = TreeNode(val)
        
        # 如果新節點的值小於等於目前root節點的值，而且該節點左邊子節點的值是None(沒有左節點)，那麼把新節點放到左子節點
        if new_node.val <= root.val:
            if root.left == None:
                root.left = new_node
                return root.left
            # 如果左節點已經有值了，繼續把該左節點當成root重新比大小，直到遇到None的子節點就安插新的節點進去
            else:
                self.insert(root.left, new_node.val)
        
        # 如果新節點的值大於目前root節點的值，而且該節點右邊子節點的值是None(沒有右節點)，那麼把新節點放到右子節點
        if new_node.val > root.val:
            if root.right == None:
                root.right = new_node
                return root.right
            # 如果右節點已經有值了，繼續把該右節點當成root重新比大小，直到遇到None的子節點就安插新的節點進去
            else:
                self.insert(root.right, new_node.val)
```

## 二、刪除
`delete()`
- 分成三種情況來刪除節點:無子節點/恰有一子節點/有兩節點
    
```python
    #檢查節點是否有子節點的函式，沒有回傳True
    def is_no_child(self, node):
        if node.left == None and node.right == None:
            print('no child')
            return True
        else:
            return False
    
    #檢查節點是否剛好有一個子節點的函式，剛好一個回傳True
    def is_a_child(self, node):
        if (node.left == None) and node.right:
            print('left(X), right(O)')
            return True
        if node.left and (node.right == None):
            print('left(O), right(X)')
            return True
        else:
            return False
    
    #檢查節點是否剛好有兩個子節點的函式，剛好兩個回傳True
    def is_two_children(self, node):
        if node.left and node.right:
            print('left(O), right(O)')
            return True 
        else:
            return False
    
    #尋找右分支最小值的函式：若是兩個子節點的情況，需要找右邊分支的最小值來代替要刪除的值，才能保證樹的組成正確
    def root_right_min_val(self, root):
        if root:
            count = 1
            cur_root = root
            if cur_root.right and count <=1:
                cur_root = root.right
                count+=1
                self.root_right_min_val(cur_root.left)
            while cur_root.left:
                cur_root = root.left
        return cur_root
    
    #刪除功能的main function
    def delete(self, root, target):
        # 1. 如果BST沒有節點可以刪除，直接回傳None
        if root == None:
            return None
                
        # 2. 比大小找節點
        # 如果目標值大於root，繼續往右邊找
        if target > root.val:
            self.search(root.right, target)
        
        # 如果目標值大於root，繼續往左邊找
        elif target < root.val:
            self.search(root.left, target)
        
        # 3. Case 1: 無節點
        # 如果整個tree就只有root一個元素的話，直接把該元素改成None
        if self.is_no_child(root) == True:
            root = None
        
        # 4. Case 2: 恰一節點
        # 如果root有某一邊有子節點，用該節點取代原本的root，這樣原本的root就消失了，然後繼續往下檢查看有沒有符合target的元素
        elif self.is_a_child(root) == True:
            if root.left:
                root = root.left
                self.delete(root, target)
            if root.right:
                root = root.right
                self.delete(root, target)

        # 5. Case 3: 恰兩節點
        # 如果root兩邊都有子節點，先找到在root右子樹中最小的值，用該值取代root，刪除該值原本的節點後，再檢查新的節點是不是target
        elif self.is_two_children(root) == True:
            root.val = self.root_right_min_val(root).val
            root.right = self.delete(self.root_right_min_val(root), target)
                
        return root
```

## 三、查詢
`search()`

```python
    def search(self, root, target):
        #當root的值=target，回傳該root
        if root.val == target:
            print('search root:', root.val)
            return root
        
        #當target < root的值，繼續往左邊找，直到找到等於的就回傳
        if target < root.val:
            self.search(root.left, target)
        
        #當target > root的值，繼續往左邊找，直到找到等於的就回傳
        if target > root.val:
            print('target > root.val')
            print(root.right.val)
            self.search(root.right, target)
```

## 四、修改
`modify()`

```python
    def modify(self, root, target, new_val):
        # 當root存在時，如果root==target值，直接把該root改成新的值
        if root:
            if root.val == target:
                root.val = new_val
        
        # 當root的左邊子節點存在，繼續找直到找到target值，回到第一個函式修改值
        if root.left:
            self.modify(root.left, target, new_val)
        
        # 當root的右邊子節點存在，繼續找直到找到target值，回到第一個函式修改值
        if root.right:
            self.modify(root.right, target, new_val)
            
        return root
```

## Reference
[Data Structures and Algorithms Bootcamp:Binary Trees / by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/9520088?start=195#content)


```python

```
