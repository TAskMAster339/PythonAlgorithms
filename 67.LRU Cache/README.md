# [**67) LRU Cache**](https://leetcode.com/problems/lru-cache/description/)

## **Условие:**

Необходимо реализовать структуру данных, реализующую **Least** **Recently** **Used** (**LRU**) **cache**.

Нужно создать **LRUCache** класс с конструктором **LRUCache**(**int** **capacity**), методами **int** **get**(**int** **key**), который возвращает значение по ключу **key**, если оно есть, иначе -**1**, **void** **put**(**int** **key**, **int** **value**), который добавляет или изменяет значение по ключу **key**.

Если количество ключей превышает емкость **capacity**, то самый неиспользуемый ключ и его значение удаляются. Сложность методов должна быть **O**(**1**)

## **Идея:**

**O**(**1**) при записи и чтении говорит о Хэш-таблице. Осталось придумать структуру для построения очереди ключей.

## **Реализация:**

Для нашей задачи идеально подходит очередь с приоритетами, но её сложность **O**(**logN**), что сильно замедлит наш алгоритм. Поэтому нужно придумать собственную структуру данных, которая за **O**(**1**), будет менять последовательность элементов. Для этого хорошо подойдет двусвязный список.

Создадим два узла **oldest** и **latest**, они будут заглушками. **oldest** - это тот, узел, следующий за которым нужно будет удалять в случае переполнения памяти кэша. А **latest** - это тот, который будет де факто началом очереди.

Для начала реализуем два метода. **remove**(**node**) и **insert**(**node**). Первый удаляет узел из очереди за константное время. (просто меняем ссылки). Второй метод вставляет узел в начало очереди. (опять за **O**(**1**), так как просто меняем ссылки)

Теперь при получение объекта из кэша, мы проверяем, есть ли он в хэш-таблице, если есть возвращаем, при этом передвинув его узел из очереди в  её начало. (Сначала делаем **remove**, потом **insert**)

При добавлении в кэш, мы создаем узел **Node**(**key**, **value**) и добавляем его в очередь. (Если он уже был в хэш-таблице, нужно не забыть вынуть его из очереди). И если емкость нашего кэша превышена, то мы берем узел, следующий за **oldest**, это как раз и будет самый неиспользуемый объект. Его мы удаляем из хэш-таблицы и очереди



## **Оценка:**

Так как мы используем хэш-таблицу и нашу очередь, операции в которых выполняются за **O**(**1**), то и сложность всех методов будет **O**(**1**) по времени. По памяти мы затратим **O**(**N**), где **N** - емкость **capacity** нашего кэша

## Код:
```python
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node: Node) -> None:
        prev, next = self.latest.prev, self.latest
        next.prev = node
        prev.next = node
        node.next = next
        node.prev = prev


if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # cache is {1=1}
    lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    print(lRUCache.get(1))  # return 1
    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))  # returns -1 (not found)
    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1))  # return -1 (not found)
    print(lRUCache.get(3))  # return 3
    print(lRUCache.get(4))  # return 4

```

