class TreeNode:
    '''Tree Node'''
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    '''Binary Tree'''
    def __init__(self):
        self.root = None

    def insert(self, key):
        '''
        Втавляє новий вузол у дерево.
        Якщо дерево порожнє, новий вузол стає коренєм.
        Інакше, викликає допоміжну функцію для рекурсивного вставлення.
        '''
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        '''Допоміжна функція для рекурсивного вставлення нового вузла.'''
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def find_max(self):
        '''Знаходить і повертає найбільше значення у дереві.'''
        if self.root is None:
            return None
        return self._find_max(self.root)

    def _find_max(self, node):
        '''
        Допоміжна функція для знаходження найбільшого значення.
        Проходить по правим дочірнім вузлам до кінця дерева.
        '''
        current = node
        while current.right is not None:
            current = current.right
        return current.val

    def find_min(self):
        '''Знаходить і повертає найменше значення у дереві.'''
        if self.root is None:
            return None
        return self._find_min(self.root)

    def _find_min(self, node):
        '''
        Допоміжна функція для знаходження найменшого значення.
        Проходить по лівим дочірнім вузлам до кінця дерева.
        '''
        current = node
        while current.left is not None:
            current = current.left
        return current.val
    
    def sum_values(self):
        '''Обчислює і повертає суму всіх значень у дереві.'''
        return self._sum_values(self.root)

    def _sum_values(self, node):
        '''Допоміжна рекурсивна функція для обчислення суми значень у дереві.'''
        if node is None:
            return 0
        return node.val + self._sum_values(node.left) + self._sum_values(node.right)


# Приклад використання
bst = BinaryTree()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(5)
bst.insert(15)
bst.insert(25)
bst.insert(35)

print("Найбільше значення у дереві:", bst.find_max())
print("Найменше значення у дереві:", bst.find_min())
print("Сума всіх значень у дереві:", bst.sum_values())
