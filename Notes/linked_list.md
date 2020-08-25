# Linked-List 链表

## 1. 基础知识

### 1.1 链表的基本结构

链表通过一个个节点组成,每个节点否包含任意的实例数据和一或两个用来指向上一个或下一个节点位置的指针。
链表保持着数据之间的逻辑顺序，其存储空间不必按照顺序存储。

链表中最简单的一种是单向链表，如图所示：

![Singly Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/408px-Singly-linked-list.svg.png)


单向链表的每个节点包含两个域，左半部分称为值域，用来存放用户数据；
右半部分称为指针域，用来存放指向下一个节点的指针。单向链表止咳向一个方向遍历。

在最后一个节点会保存一个特殊的结束标记，其指针域为None。
另外在一个固定的head节点保存指向第一个节点的指针。
一般查找一个节点的时候需要从第一各级欸点开始依次访问下一个节点，直到访问到需要的位置。

### 1.2 链表的定义

仿**LeetCode**官方`ListNode`定义如下：

[参考leetcode用户**boywithacoin_cn**代码](https://leetcode-cn.com/problems/add-two-numbers/solution/python3ti-jie-fang-leetcodeguan-fang-lei-listnoded/)

```python
class ListNode():
    def __init__(self, val):
        if isinstance(val,int):
            self.val = val
            self.next = None
    
        elif isinstance(val,list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next
```

### 1.3 顺序打印或逆序打印

通过递归依次打印链表的每一个元素：
```python
def printBackward(listnode):
    if listnode == None:return
    printBackward(listnode.next)
    print(listnode.val) #调换以上两句的顺序即可完成顺序打印
```

> 维基百科 https://zh.wikipedia.org/wiki/链表 \
> python数据结构之链表 https://blog.csdn.net/qq_39422642/article/details/78988976