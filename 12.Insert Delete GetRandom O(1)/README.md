<div align='center'>
<h1><a href='https://leetcode.com/problems/insert-delete-getrandom-o1/description/'><strong>12) Insert Delete GetRandom O(1)</strong></a></h1>
</div>

Вообще не выкупил в чем тут задача.

Создадим список и словарь, они в совокупности и будут нашим рандомизированным множеством. Самый простой метод - **getRandom**(), импортируем встроенную библиотеку **random**, используем функцию **choice**, которая возвращает случайный элемент из последовательности, в качестве аргумента передадим наш список.

Теперь **insert**(**val**), для этого реализуем вспомогательный метод **search**(**val**), который будет возвращать **True**, если **val** является ключом нашего словаря. С помощью **search** мы определяем есть ли элемент **val** в нашем множестве, если есть, то возвращаем **False**, вставлять ничего не нужно, если нет, то добавляем его в список, при этом записывая в словарь его индекс(элемент выступает в качестве ключа). И возвращаем **True**.

**remove**(**val**), аналогично если данного элемента нет в множестве, то мы возвращаем **False** и ничего не делаем, для этого используем ранее реализованный метод **search**(**val**), далее из словаря получаем индекс элемента, который нужно удалить.

Теперь прикольный прикол - мы меняем местами последний элемент списка с тем, который хотим удалить. Затем, чтобы удалить наш элемент нужно просто убрать последний элемент из списка с помощью **pop**(). Такой алгоритм действий гарантирует сверхбыстрое удаление, потому что удаление из середины списка более дорогостоющая операция, чем удаление из конца списка. Теперь нам остается удалить наш элемент из словаря и вернуть **True**.

Так как мы используем список и словарь, то время, затраченное на вставку элемента, будет равно **O**(**1**), время, затраченное на удаление, - **O**(**N**) (Так как мы используем список, если бы был массив то мы получили бы **O**(**1**)), **getRandom**() - скорее всего **O**(**N**), так как реализация **random**.**choice**() неизвестна, то предполагаем наихудший случай.

## Код:
```python
import random


class RandomizedSet:
    def __init__(self):
        self.lst = []
        self.idx_map = {}

    def search(self, val):
        return val in self.idx_map

    def insert(self, val):
        if self.search(val):
            return False

        self.lst.append(val)
        self.idx_map[val] = len(self.lst) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False

        idx = self.idx_map[val]
        self.lst[idx] = self.lst[-1]
        self.idx_map[self.lst[-1]] = idx
        self.lst.pop()
        del self.idx_map[val]
        return True

    def getRandom(self):
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


if __name__ == "__main__":
    obj = RandomizedSet()
    param_1 = obj.insert(2)
    param_2 = obj.insert(3)

    param_4 = obj.getRandom()
    print(param_1, param_2, param_4)

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/11.H-Index'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/13.Product%20of%20Array%20Except%20Self'>следующая задача ➡️</a></h3></div>