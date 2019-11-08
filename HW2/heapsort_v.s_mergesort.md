# Heapsort 和 Mergesort 的比較
> ✅表示勝出，沒寫表示持平

| Heapsort | Mergesort |
|:-------- |:--------- |
|1. 時間複雜度: all case - $O(nlogn)$。<br>2. 空間：最少$O(1)$✅<br>3. 較不穩定：不同狀況中數列的相對位置會被改變 |1. 時間複雜度: all case - $O(nlogn)$。<br>2. 空間：最少$O(n)$<br>3.較穩定：相較於Heap，不同的狀況中數列的相對位置不會被改變✅|

# Strengths and Weakness of heap sort
- Strengths:
    1. 快：時間複雜度最快最慢只有 $O(nlogn)$。
    2. 節省空間：你只需要一個陣列
    3. 簡潔：短短程式碼就可以實現排序
- Weakness:
    1. 不穩定：可能會改變原本數列中相對的排序（[維基百科說穩定的算法不會出現這種事🤯](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95#%E4%B8%8D%E7%A9%A9%E5%AE%9A%E7%9A%84%E6%8E%92%E5%BA%8F)）
    
# Strengths and Weakness of the merge sort
- Strengths:
    1. 快：時間複雜度最快與最慢都只需 $O(nlogn)$。
    2. 穩定：相較於Heap，不同的狀況中數列的相對位置不會被改變
- Weakness:
    1. 某些情況下比quick sort慢
    2. 某些情況下所需的空間比heap sort多
