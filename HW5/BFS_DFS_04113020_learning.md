# HW5: BFS & DFS 流程圖、程式碼學習歷程、兩者原理與比較
陳汶穗｜巨資四B｜04113020  
Period: 2019.12.06 - 2019.12.20

# Graph
> BFS (Breadth First Search) & DFS (Depth First Search) 是Graph資料結構下基本搜尋的方法，所以先提及Graph的概念，再帶到BFS & DFS走訪本身的原理。

- 演算法中的「圖(Graph)」是一種用來表達資料關係的架構，由點(vertex)和邊(edge)組成，如下面兩張圖：
![](https://i.imgur.com/BbtOXyX.png)  
圖一-- [Graph from Wikipedia](https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)  
![](https://i.imgur.com/iibdz5n.png)  
圖二-- [Graph by Chiu CC](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)  
其中圖一表示了數值資料間的樹狀關係，圖二表示文字資料間的先後關係(以某大學的CS必修課程為例，此圖表達了修課的順序關係)

## Graph的定義
- def: $G(V+E)$，意指點與線的集合
- V: Vertices，意指點的集合
- E: Edges，意指線的集合

## Graph的Edge的分類
- 有向: 圖之間的邊有方向性，由一邊指向另一邊．或是有雙向的箭頭，如原本的圖二
- 無向: 圖之間的邊沒有方向性，如原本的圖一
    
## 描述Graph的方式
> 共有三種：Edge lists邊表, Adjacency Matrix相鄰/伴隨矩陣, Adjacency List相鄰串列

### Edge lists | 邊表
- def：把所有點之前的邊用一個一個的list表示，組成一個邊表。比如說上面的圖一用Edge lists來表示就是[[1,2],[1,3],[1,4],[2,5],[2,6],[5,9],[5,10],[4,7],[4,8],[7,11],[7,12]]。
- 優點：是個易於理解的資料結構
- 缺點：不易搜尋，想要快速找到一個點連接的線就最差的情況需要$O(n)$才能找到，而其他兩種表達Graph方式就可以解決這個問題。

### Adjacency Matrix | 相鄰/伴隨矩陣
- def：由所有的點組成的二維矩陣，用數字表達兩點有無邊連接，或表達邊的權重。若圖的邊是無權重的，相鄰矩陣中會把兩個點在有邊的連結的情況標記成1，若兩點間沒有邊連結則標記成0。
- 優點：查找快速，快速找到矩陣中的某兩點就可以快速地知道這兩點間有沒有一個線。
- 缺點：耗費儲存空間。

### Adjacency List | 相鄰串列: 
- def：這裡列舉兩種實現方式，一是類似上次實作hash table使用的結構，先用一個list(或array)把所有節點存起來，每個節點後面再用linked-list結構把與該點相連結的點連起來；另一種實現方式(這次作業中使用的方式)先新增節點建立成dict中的key，key後面的value以list型態存放資料。
- 優點：查找快速、可以快速找到點的鄰點
- 缺點：較難判斷邊是否存在、在complete graph的情況下較Adjacency Matrix更耗費空間。
> complete graph: n個節點有n-1條邊的圖形就是complete graph。

## Graph的用途範例
- build social network: 建立社群網路的基礎演算法就是graph的概念。
- path finding: 尋找最短路徑，如Google/Apple在地圖尋找路徑的演算法基礎也是graph。
- find nearest neighbor: 遊戲公司供玩家尋找最鄰近玩家，或提供低延遲的遊戲體驗的算法基礎也是graph。
- map worldwide map: Google如何連結各個不同的網站背後的想法也是使用到graph。
- recommendation: Spotify的推薦系統也使用到graph的概念。

## 補充
Adjacency Matrix和Adjacency List兩個概念對比就如下圖－－
![](https://i.imgur.com/2MD0S6L.png)- [Graph by Chiu CC](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)

※更多關於Graph的資料可以參考[Graph: Intro(簡介) by Chiu CC](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)或[Graph演算法筆記](http://www.csie.ntnu.edu.tw/~u91029/Graph.html#2)，這兩篇把Graph相關的概念圖文並茂地解釋的非常清楚。

# BFS 原理
BFS (Breadth First Search) | 廣度優先搜尋法: 意即從起點開始，以資料層級的廣度為優先下去搜尋的走訪方法。

## 從樹狀圖理解BFS
![](https://i.imgur.com/RaT65F9.gif)- [BFS from Wikipedia](https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)
以上面這個樹狀圖為例，從`a`為起點開始走訪，走訪到下一層級`b`的時候，不是繼續先往`b`下面的`d`,`e`走，而是從`b`同層級的`c`先走，沒了再往下一層繼續走，這樣以同個層級展開搜尋的方式就是廣度優先搜尋法。

## 從Graph理解BFS
![](https://i.imgur.com/sXxP9ot.png)- [Graph by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/10206538#overview)
BFS通常使用Queue的方式來存放欲走訪的節點。以上圖為例，若從0為起點以BFS方式走訪，整個流程會是：
- 因為起點0還沒走訪過，**標註**0為**visited**後把0**放入Queue**
- 從Queue中**dequeue**拿出元素0**放入**Path。因為Queue儲存的方式是先進先出(FIFO, First In First Out)，所以剛剛先進去的0先被取出。
- 接下來找尋0的鄰點是否有還沒visit的，若有，**標註**該元素為**visited**後把該元素**放入Queue**；若無，直接**dequeue**下一個元素重複以上的步驟。此例中這步驟0有鄰點1,6,3還沒visit，因此把1,6,3放入Queue，又因為點之間的順序並不影響我們描述一個Graph，所以放入Queue的元素不需要排序。
- 從Queue中**dequeue**拿出目前裡面最先放入的元素1**放入**Path。
- 找尋1的鄰點是否有還沒visit的，若有，**標註**該元素為**visited**後把該元素**放入Queue**。此處再把4,5放入Queue。
重複以上步驟後，我們可以得出BFS走訪的結果是Path，且所有點被標黃表示visited，如下圖：
![](https://i.imgur.com/pvQN1JA.png)- [Graph by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/10206538#overview)

因此我們可以濃縮出BFS所需執行的幾個步驟：
1. 從起點開始，先標註visited，後放入Queue
2. 從Queue中dequeue一個元素，檢查該元素是否有鄰點可以放入Queue。  
    (1)有鄰點放入Queue: 先標註該點visited，後放入Queue接著重複執行步驟2  
    (2)無鄰點放入Queue: 直接重複執行步驟2
3. 直到所有點遍歷就是成功以BFS走訪完畢。

## BFS的特性
- 空間複雜度: $O(V)$，V(Vertices)是節點的數量，因為所有節點都要被儲存所以複雜度為$O(V)$。
- 時間複雜度: $O(V+E)$，E(Edges)是邊的數量，最差情況需要遍歷每個點所以時間複雜度是$O(V+E)$。
- 完全性: 不論圖形大小和種類為何，只要目標存在BFS一定可以找到該目標，除非該目標不存在於圖中。
- 缺點: 當圖無限大的時候會有無限迴圈不會停止搜尋，儲存空間的要求也會非常大。(耗空間的算法)

# DFS 原理
DFS (Depth First Search) | 深度優先搜尋法: 意即從起點開始，以資料層級的深度為優先下去搜尋的走訪方法。

## 從樹狀圖理解DFS
![](https://i.imgur.com/GDC2zHa.gif)- [DFS from Wikimedia commons](https://commons.wikimedia.org/wiki/File:Depth-First-Search.gif)
以上面這個樹狀圖為例，從`1`為起點開始走訪，接著到數字`2`所在的第二層，接著是往`2`下面的`3`繼續往下走訪，走到最深之後才回到上面層級的點繼續往下遍歷，這樣在同個支線以深度展開搜尋的方式就是深度優先搜尋法。

![](https://i.imgur.com/bRymp3k.png)- [Graph by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/10206752#overview)
DFS通常使用Stack的方式來存放欲走訪的節點。以上圖為例，若從0為起點以DFS方式走訪，整個流程會是：
- 因為起點0還沒走訪過，**標註**0為**visited**後把0**push**到**Stack**裡面。
- 從Stack中**pop**拿出元素0**放入**Path。因為Stack儲存的方式是後進先出(LIFO, Last In First Out)，剛剛只進去一個的0當然同時是最後一個所以被取出。
- 接下來找尋0的鄰點是否有還沒visit的，若有，**標註**該元素為**visited**後把該元素**放入Stack**；若無，直接**pop**下一個元素重複以上的步驟。此例中這步驟0有鄰點1,6,3還沒visit，因此把1,6,3放入Stack，又因為點之間的順序並不影響我們描述一個Graph，所以放入Stack的元素一樣不需要排序。
- 從Stack中**pop**拿出目前裡面最後放入的元素3**放入**Path。
- 找尋3的鄰點是否有還沒visit的，若有，**標註**該元素為**visited**後把該元素**放入Stack**。此處再把5放入Stack。
重複以上步驟後，我們可以得出DFS走訪的結果顯示在Path，且所有點被標黃表示visited，如下圖：
![](https://i.imgur.com/uw8lTcd.png)

因此我們可以濃縮出DFS所需執行的幾個步驟：
1. 從起點開始，先標註visited，後放入Stack
2. 從Stack尾端pop一個元素，檢查該元素是否有鄰點可以放入Stack。  
    (1)有鄰點放入Stack: 先標註該點visited，後放入Stack接著重複執行步驟2  
    (2)無鄰點放入Stack: 直接重複執行步驟2
3. 直到所有點遍歷就是成功以DFS走訪完畢。

## DFS的特性
- 空間複雜度: $O(V)$，V(Vertices)是節點的數量，因為所有節點都要被儲存所以複雜度為$O(V)$，跟BFS一樣。
- 時間複雜度: $O(V+E)$，E(Edges)是邊的數量，最差情況需要遍歷每個點所以時間複雜度是$O(V+E)$，也跟BFS一樣。

# BFS v.s DFS

|比較項目| BFS | DFS |
|:-----|:-----|:-----|
|原理|以廣度為優先的搜尋法|以深度為優先的搜尋法|
|空間複雜度|𝑂(𝑉)|𝑂(𝑉)|
|時間複雜度|𝑂(𝑉+𝐸)|𝑂(𝑉+𝐸)|
|儲存方式|Queue: FIFO，先進先出|Stack: LIFO，後進先出|

# 流程圖
![](https://i.imgur.com/s7JvSyT.jpg)

# 作業格式
```python
# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
 ```
 ## 測試結果範例
 ```python
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.BFS(2))
print(g.DFS(2))
 ```

範例圖:
![](https://i.imgur.com/551OSo6.png)

# BFS 程式碼


```python
from collections import defaultdict 

class Graph:
    
    def __init__(self):  
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def check_adjacency_node(self, s, queue, bfs_traversal):
        adjacency_list = g.graph[s]
        len_of_adja_list = len(g.graph[s])
        for i in adjacency_list:
            print(queue, bfs_traversal)
            if i not in queue and i not in bfs_traversal:
                print(i)
                queue.append(i)
    
    def BFS(self, s):
        bfs_traversal = []
        queue = []
        
        if g.graph[s] == []:
            print("None")
            return []
        
        if s not in queue and s not in bfs_traversal:
            queue.append(s)
            print('queue after queue.append(s):', queue)
            
            bfs_traversal.append(queue[0])
            queue.pop(0)
            print('queue after queue.pop(0):', queue)
            
            cur_node = bfs_traversal[0]
            print('cur_node', cur_node)
            self.check_adjacency_node(cur_node, queue, bfs_traversal)
            print(queue, bfs_traversal)
        
        return bfs_traversal
        
#     def DFS(self, s):
#         """
#         :type s: int
#         :rtype: list
#         """

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print('-------------graph_test-------------')
print(g.graph)
print('g.graph[1]:', g.graph[2])
print('g.graph[44]:', g.graph[44])
print('--------------------------')

print(g.BFS(2))
# print(g.DFS(2))
```

    -------------graph_test-------------
    defaultdict(<class 'list'>, {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]})
    g.graph[1]: [0, 3]
    g.graph[44]: []
    --------------------------
    queue after queue.append(s): [2]
    queue after queue.pop(0): []
    cur_node 2
    [] [2]
    0
    [0] [2]
    3
    [0, 3] [2]
    [2]
    

👆發現走訪有誤，修正邏輯


```python
from collections import defaultdict 

class Graph:
    
    def __init__(self):  
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def check_adjacency_node(self, s, queue, bfs_traversal):
        adjacency_list = g.graph[s]
        len_of_adja_list = len(g.graph[s])
        for i in adjacency_list:
            print('-------------check_adjacency_node-------------')
            print(queue, bfs_traversal, adjacency_list)
            if i not in queue and i not in bfs_traversal:
                print(i)
                queue.append(i)
                print('--------------------------')
        return queue
    
    def BFS(self, s):
        bfs_traversal = []
        queue = []
        
        if g.graph[s] == []:
            print("None")
            return []
        
        if s not in queue and s not in bfs_traversal:
            queue.append(s)
            print('queue after queue.append(s):', queue)
            
            bfs_traversal.append(queue[0])
            queue.pop(0)
            print('queue after queue.pop(0):', queue)
            print('bfs after add:', bfs_traversal)
            
            cur_node = bfs_traversal[0]
            print('cur_node', cur_node)
            
            queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
            print('result(queue, bfs_traversal):', queue, bfs_traversal)
        
        return bfs_traversal
        
#     def DFS(self, s):
#         """
#         :type s: int
#         :rtype: list
#         """

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print('-------------graph_test-------------')
print(g.graph)
print('g.graph[1]:', g.graph[2])
print('g.graph[44]:', g.graph[44])
print('--------------------------')

print(g.BFS(2))

# print(g.DFS(2))
```

    -------------graph_test-------------
    defaultdict(<class 'list'>, {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]})
    g.graph[1]: [0, 3]
    g.graph[44]: []
    --------------------------
    queue after queue.append(s): [2]
    queue after queue.pop(0): []
    bfs after add: [2]
    cur_node 2
    -------------check_adjacency_node-------------
    [] [2] [0, 3]
    0
    --------------------------
    -------------check_adjacency_node-------------
    [0] [2] [0, 3]
    3
    --------------------------
    result(queue, bfs_traversal): [0, 3] [2]
    [2]
    

👆發現少寫return把值存起來所以導致走訪結果錯誤，現在修正了！繼續寫  
(return真的是我的初學者硬傷)


```python
from collections import defaultdict 

class Graph:
    
    def __init__(self):  
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def check_adjacency_node(self, s, queue, bfs_traversal):
        adjacency_list = g.graph[s]
        len_of_adja_list = len(g.graph[s])
        for i in adjacency_list:
            print('-------------check_adjacency_node-------------')
            print(queue, bfs_traversal, adjacency_list)
            if i not in queue and i not in bfs_traversal:
                print(i)
                queue.append(i)
                print('--------------------------')
        return queue
    
    def bfs_recursive(self, s, queue, bfs_traversal):
        if s not in bfs_traversal:
            if s not in queue:
                queue.append(s)
                print('queue after queue.append(s):', queue)

                bfs_traversal.append(queue[0])
                queue.pop(0)
                print('queue after queue.pop(0):', queue)
                print('bfs after add:', bfs_traversal)

                cur_node = bfs_traversal[0]
                print('cur_node', cur_node)

                queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
                print('result(queue, bfs_traversal):', queue, bfs_traversal)
            
            else:
                bfs_traversal.append(queue[0])
                cur_node = queue[0]
                queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
                queue.pop(0)
                print('queue after queue.pop(0):', queue)
                print('bfs after add:', bfs_traversal)
                  
        return s, queue, bfs_traversal
    
    def BFS(self, s):
        bfs_traversal = []
        queue = []
        
        if g.graph[s] == []:
            print("None")
            return []
        
        s, queue, bfs_traversal = self.bfs_recursive(s, queue, bfs_traversal)
        print(s, queue, bfs_traversal)

        while queue != []:
            for num in queue:
                self.bfs_recursive(num, queue, bfs_traversal)
                
        return bfs_traversal
        
#     def DFS(self, s):
#         """
#         :type s: int
#         :rtype: list
#         """

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print('-------------graph_test-------------')
print(g.graph)
print('g.graph[1]:', g.graph[2])
print('g.graph[44]:', g.graph[44])
print('--------------------------')

print(g.BFS(2))

# print(g.DFS(2))
```

    -------------graph_test-------------
    defaultdict(<class 'list'>, {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]})
    g.graph[1]: [0, 3]
    g.graph[44]: []
    --------------------------
    queue after queue.append(s): [2]
    queue after queue.pop(0): []
    bfs after add: [2]
    cur_node 2
    -------------check_adjacency_node-------------
    [] [2] [0, 3]
    0
    --------------------------
    -------------check_adjacency_node-------------
    [0] [2] [0, 3]
    3
    --------------------------
    result(queue, bfs_traversal): [0, 3] [2]
    2 [0, 3] [2]
    -------------check_adjacency_node-------------
    [0, 3] [2, 0] [1, 2]
    1
    --------------------------
    -------------check_adjacency_node-------------
    [0, 3, 1] [2, 0] [1, 2]
    queue after queue.pop(0): [3, 1]
    bfs after add: [2, 0]
    -------------check_adjacency_node-------------
    [3, 1] [2, 0, 3] [3]
    queue after queue.pop(0): [1]
    bfs after add: [2, 0, 3]
    -------------check_adjacency_node-------------
    [1] [2, 0, 3, 1] [2]
    queue after queue.pop(0): []
    bfs after add: [2, 0, 3, 1]
    [2, 0, 3, 1]
    

👆成功寫出測資，用其他圖測試


```python
from collections import defaultdict 

class Graph:
    
    def __init__(self):  
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def check_adjacency_node(self, s, queue, bfs_traversal):
        adjacency_list = g.graph[s]
        len_of_adja_list = len(g.graph[s])
        for i in adjacency_list:
            print('-------------check_adjacency_node-------------')
            print(queue, bfs_traversal, adjacency_list)
            if i not in queue and i not in bfs_traversal:
                print(i)
                queue.append(i)
                print('--------------------------')
        return queue
    
    def bfs_recursive(self, s, queue, bfs_traversal):
        if s not in bfs_traversal:
            if s not in queue:
                queue.append(s)
                print('queue after queue.append(s):', queue)

                bfs_traversal.append(queue[0])
                queue.pop(0)
                print('queue after queue.pop(0):', queue)
                print('bfs after add:', bfs_traversal)

                cur_node = bfs_traversal[0]
                print('cur_node', cur_node)

                queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
                print('result(queue, bfs_traversal):', queue, bfs_traversal)
            
            else:
                bfs_traversal.append(queue[0])
                cur_node = queue[0]
                queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
                queue.pop(0)
                print('queue after queue.pop(0):', queue)
                print('bfs after add:', bfs_traversal)
                  
        return s, queue, bfs_traversal
    
    def BFS(self, s):
        bfs_traversal = []
        queue = []
        
        if g.graph[s] == []:
            print("None")
            return []
        
        s, queue, bfs_traversal = self.bfs_recursive(s, queue, bfs_traversal)
        print(s, queue, bfs_traversal)

        while queue != []:
            for num in queue:
                self.bfs_recursive(num, queue, bfs_traversal)
                
        return bfs_traversal
        
#     def DFS(self, s):
#         """
#         :type s: int
#         :rtype: list
#         """

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 0)
g.addEdge(3, 4)
g.addEdge(3, 6)
g.addEdge(4, 5)
print('-------------graph_test-------------')
print(g.graph)
print('g.graph[1]:', g.graph[2])
print('g.graph[44]:', g.graph[44])
print('--------------------------')

print(g.BFS(3))

# print(g.DFS(2))
```

    -------------graph_test-------------
    defaultdict(<class 'list'>, {0: [1, 2, 3], 1: [3], 2: [3, 4], 3: [0, 4, 6], 4: [5]})
    g.graph[1]: [3, 4]
    g.graph[44]: []
    --------------------------
    queue after queue.append(s): [3]
    queue after queue.pop(0): []
    bfs after add: [3]
    cur_node 3
    -------------check_adjacency_node-------------
    [] [3] [0, 4, 6]
    0
    --------------------------
    -------------check_adjacency_node-------------
    [0] [3] [0, 4, 6]
    4
    --------------------------
    -------------check_adjacency_node-------------
    [0, 4] [3] [0, 4, 6]
    6
    --------------------------
    result(queue, bfs_traversal): [0, 4, 6] [3]
    3 [0, 4, 6] [3]
    -------------check_adjacency_node-------------
    [0, 4, 6] [3, 0] [1, 2, 3]
    1
    --------------------------
    -------------check_adjacency_node-------------
    [0, 4, 6, 1] [3, 0] [1, 2, 3]
    2
    --------------------------
    -------------check_adjacency_node-------------
    [0, 4, 6, 1, 2] [3, 0] [1, 2, 3]
    queue after queue.pop(0): [4, 6, 1, 2]
    bfs after add: [3, 0]
    -------------check_adjacency_node-------------
    [4, 6, 1, 2] [3, 0, 4] [5]
    5
    --------------------------
    queue after queue.pop(0): [6, 1, 2, 5]
    bfs after add: [3, 0, 4]
    queue after queue.pop(0): [1, 2, 5]
    bfs after add: [3, 0, 4, 6]
    -------------check_adjacency_node-------------
    [1, 2, 5] [3, 0, 4, 6, 1] [3]
    queue after queue.pop(0): [2, 5]
    bfs after add: [3, 0, 4, 6, 1]
    -------------check_adjacency_node-------------
    [2, 5] [3, 0, 4, 6, 1, 2] [3, 4]
    -------------check_adjacency_node-------------
    [2, 5] [3, 0, 4, 6, 1, 2] [3, 4]
    queue after queue.pop(0): [5]
    bfs after add: [3, 0, 4, 6, 1, 2]
    queue after queue.pop(0): []
    bfs after add: [3, 0, 4, 6, 1, 2, 5]
    [3, 0, 4, 6, 1, 2, 5]
    

🌞成功，來寫DFS

# DFS 程式碼


```python
from collections import defaultdict 

class Graph:
    
    def __init__(self):  
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def check_adjacency_node(self, s, queue, bfs_traversal):
        adjacency_list = g.graph[s]
        len_of_adja_list = len(g.graph[s])
        for i in adjacency_list:
            print('-------------check_adjacency_node-------------')
            print(queue, bfs_traversal, adjacency_list)
            if i not in queue and i not in bfs_traversal:
                print(i)
                queue.append(i)
                print('--------------------------')
        return queue
    
    def bfs_recursive(self, s, queue, bfs_traversal):
        if s not in bfs_traversal:
            if s not in queue:
                queue.append(s)
                print('queue after queue.append(s):', queue)

                bfs_traversal.append(queue[0])
                queue.pop(0)
                print('queue after queue.pop(0):', queue)
                print('bfs after add:', bfs_traversal)

                cur_node = bfs_traversal[0]
                print('cur_node', cur_node)

                queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
                print('result(queue, bfs_traversal):', queue, bfs_traversal)
            
            else:
                bfs_traversal.append(queue[0])
                cur_node = queue[0]
                queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
                queue.pop(0)
                print('queue after queue.pop(0):', queue)
                print('bfs after add:', bfs_traversal)
                  
        return s, queue, bfs_traversal
    
    def BFS(self, s):
        bfs_traversal = []
        queue = []
        
        if g.graph[s] == []:
            print("None")
            return []
        
        s, queue, bfs_traversal = self.bfs_recursive(s, queue, bfs_traversal)
        print(s, queue, bfs_traversal)

        while queue != []:
            for num in queue:
                self.bfs_recursive(num, queue, bfs_traversal)
                
        return bfs_traversal
    
    def pop(self, stack):
        if stack != []:
            stack.pop()
            return stack
    
    def add_adjacency(self, num, stack):
        adjacency_list = g.graph[num]
        for n in adjacency_list:
            if n not in stack:
                stack.append(n)
        return stack
        
    def DFS(self, s):
        dfs_traversal = []
        stack = []
        
        if g.graph[s] == []:
            print("None")
            return []

        stack.append(s)
        
        while stack != []:
            last_num = stack.pop() #記得這時候已經把最後一個數值從stack中pop出來
            if last_num not in dfs_traversal:
                dfs_traversal.append(last_num)        
                stack = self.add_adjacency(last_num, stack)
                    
        return dfs_traversal
                
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print('-------------graph_test-------------')
print(g.graph)
print('g.graph[1]:', g.graph[2])
print('g.graph[44]:', g.graph[44])
print('--------------------------')

# print(g.BFS(2))
print(g.DFS(2))
```

    -------------graph_test-------------
    defaultdict(<class 'list'>, {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]})
    g.graph[1]: [0, 3]
    g.graph[44]: []
    --------------------------
    [2, 3, 0, 1]
    

👆成功!繼續嘗試其他圖  
前面寫BFS已經了解recursive的流程以及知道篩選走訪的條件，所以寫DFS時就順暢很多，也精簡了許多不必要的條件，開心。


```python
from collections import defaultdict 

class Graph:
    
    def __init__(self):  
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def check_adjacency_node(self, s, queue, bfs_traversal):
        adjacency_list = g.graph[s]
        len_of_adja_list = len(g.graph[s])
        for i in adjacency_list:
            print('-------------check_adjacency_node-------------')
            print(queue, bfs_traversal, adjacency_list)
            if i not in queue and i not in bfs_traversal:
                print(i)
                queue.append(i)
                print('--------------------------')
        return queue
    
    def bfs_recursive(self, s, queue, bfs_traversal):
        if s not in bfs_traversal:
            if s not in queue:
                queue.append(s)
                print('queue after queue.append(s):', queue)

                bfs_traversal.append(queue[0])
                queue.pop(0)
                print('queue after queue.pop(0):', queue)
                print('bfs after add:', bfs_traversal)

                cur_node = bfs_traversal[0]
                print('cur_node', cur_node)

                queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
                print('result(queue, bfs_traversal):', queue, bfs_traversal)
            
            else:
                bfs_traversal.append(queue[0])
                cur_node = queue[0]
                queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
                queue.pop(0)
                print('queue after queue.pop(0):', queue)
                print('bfs after add:', bfs_traversal)
                  
        return s, queue, bfs_traversal
    
    def BFS(self, s):
        bfs_traversal = []
        queue = []
        
        if g.graph[s] == []:
            print("None")
            return []
        
        s, queue, bfs_traversal = self.bfs_recursive(s, queue, bfs_traversal)
        print(s, queue, bfs_traversal)

        while queue != []:
            for num in queue:
                self.bfs_recursive(num, queue, bfs_traversal)
                
        return bfs_traversal
    
    def pop(self, stack):
        if stack != []:
            stack.pop()
            return stack
    
    def add_adjacency(self, num, stack):
        adjacency_list = g.graph[num]
        for n in adjacency_list:
            if n not in stack:
                stack.append(n)
        return stack
        
    def DFS(self, s):
        dfs_traversal = []
        stack = []
        
        if g.graph[s] == []:
            print("None")
            return []

        stack.append(s)
        
        while stack != []:
            last_num = stack.pop() #記得這時候已經把最後一個數值從stack中pop出來
            if last_num not in dfs_traversal:
                dfs_traversal.append(last_num)        
                stack = self.add_adjacency(last_num, stack)
                    
        return dfs_traversal
                
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 0)
g.addEdge(3, 4)
g.addEdge(3, 6)
g.addEdge(4, 5)
print('-------------graph_test-------------')
print(g.graph)
print('g.graph[1]:', g.graph[2])
print('g.graph[44]:', g.graph[44])
print('--------------------------')

# print(g.BFS(2))
print(g.DFS(3))
```

    -------------graph_test-------------
    defaultdict(<class 'list'>, {0: [1, 2, 3], 1: [3], 2: [3, 4], 3: [0, 4, 6], 4: [5]})
    g.graph[1]: [3, 4]
    g.graph[44]: []
    --------------------------
    [3, 6, 4, 5, 0, 2, 1]
    

🌞完成!修成繳交作業的版本
# 作業繳交版本


```python
from collections import defaultdict 

class Graph:
    
    def __init__(self):  
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def check_adjacency_node(self, s, queue, bfs_traversal):
        adjacency_list = g.graph[s]
        len_of_adja_list = len(g.graph[s])
        for i in adjacency_list:
            if i not in queue and i not in bfs_traversal:
                queue.append(i)
        return queue
    
    def bfs_recursive(self, s, queue, bfs_traversal):
        if s not in bfs_traversal:
            if s not in queue:
                queue.append(s)

                bfs_traversal.append(queue[0])
                queue.pop(0)

                cur_node = bfs_traversal[0]

                queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
            
            else:
                bfs_traversal.append(queue[0])
                cur_node = queue[0]
                queue = self.check_adjacency_node(cur_node, queue, bfs_traversal)
                queue.pop(0)
                  
        return s, queue, bfs_traversal
    
    def BFS(self, s):
        bfs_traversal = []
        queue = []
        
        if g.graph[s] == []:
            return []
        
        s, queue, bfs_traversal = self.bfs_recursive(s, queue, bfs_traversal)

        while queue != []:
            for num in queue:
                self.bfs_recursive(num, queue, bfs_traversal)
                
        return bfs_traversal
    
    def add_adjacency(self, num, stack):
        adjacency_list = g.graph[num]
        for n in adjacency_list:
            if n not in stack:
                stack.append(n)
        return stack
        
    def DFS(self, s):
        dfs_traversal = []
        stack = []
        
        if g.graph[s] == []:
            return []

        stack.append(s)
        
        while stack != []:
            last_num = stack.pop() #記得這時候已經把最後一個數值從stack中pop出來
            if last_num not in dfs_traversal:
                dfs_traversal.append(last_num)        
                stack = self.add_adjacency(last_num, stack)
                    
        return dfs_traversal

    
# Reference
# - [佇列(Queue)](https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Queues/queue.html)
# - [堆疊(Stack)](https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Queues/stack.html)
# - [Graph演算法筆記](http://www.csie.ntnu.edu.tw/~u91029/Graph.html#2)
# - [Graph: Intro(簡介)](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)
# - [廣度優先搜尋Wikipedia](https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)
# - [基礎資料結構(4)---圖形結構](http://marklin-blog.logdown.com/posts/1535607-underlying-data-structure-3-the-graphic-structure)
# - [廣度優先搜尋法(Breadth-First Search)](https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Graphs/breadth-first_search.html)
# - [Data Structures and Algorithms Bootcamp:Binary Trees / by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/10206538#overview)
```

# Reference
- [佇列(Queue)](https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Queues/queue.html)
- [堆疊(Stack)](https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Queues/stack.html)
- [Graph演算法筆記](http://www.csie.ntnu.edu.tw/~u91029/Graph.html#2)
- [Graph: Intro(簡介)](http://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)
- [廣度優先搜尋Wikipedia](https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)
- [基礎資料結構(4)---圖形結構](http://marklin-blog.logdown.com/posts/1535607-underlying-data-structure-3-the-graphic-structure)
- [廣度優先搜尋法(Breadth-First Search)](https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Graphs/breadth-first_search.html)
- [Data Structures and Algorithms Bootcamp:Binary Trees / by Jonathan Rasmusson / Former Spotify Engineer](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp/learn/lecture/10206538#overview)


```python

```
