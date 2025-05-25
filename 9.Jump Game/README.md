<div align='center'>
<h1><a href='https://leetcode.com/problems/jump-game/description/'><strong>9) Jump Game</strong></a></h1>
</div>

Идея: заметим, что единственный случай, когда мы не можем дойти от начала до конца, это когда мы упираемся в непроходимый **0**.

Если список состоит из одного элемента, то мы возвращаем **True**. Создадим переменную **target**, с помощью которой будем проверять найденный нуль на проходимость, еще нам понадобится логическая переменная **zero_flag**, равная **True**, если нуль не проходим, иначе **False**.

Далее мы идем по списку, начиная с предпоследнего элемента, заканчивая первым. Если **nums**[**i**] оказался равным **0** и это первый встретившийся нам **0**, то мы поднимаем **zero_flag** и присваиваем **target** = **2**, так как чтобы пройти через этот нуль, нам нужно найти такое **nums**[**i**] >= **2**.

Теперь, когда мы нашли нуль, мы проверяем можно ли через него пройти, если можно, то устанавливаем **target** = **0** и опускаем флаг нуля, если нельзя, то увеличиваем **target** на **1**, так как следующие число будет на **1** дальше от этого нуля. Также тут мы наивно предполагаем, что рано или поздно может найтись такой элемент, который перешагнет этот нуль.

После цикла возвращаем **target** == **0**. Это выражение истинно, если в нашем массиве нет нулей, или все нули в нашем массиве проходимы. Если **target** != **0**, то есть такой нуль, который пройти не возможно, следовательно дойти от начала списка до конца не представляется возможным.

Сложность алгоритма **O**(**n**) по времени и **O**(**1**) по памяти.

## Код:
```python
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        target = 0
        zero_flag = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0 and not zero_flag:
                target = 2
                zero_flag = True
            elif target != 0:
                if nums[i] >= target:
                    target = 0
                    zero_flag = False
                else:
                    target += 1
        return target == 0


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
    print(s.canJump([3, 2, 1, 0, 4]))
    print(s.canJump([0, 2, 3]))
    print(s.canJump([2, 0, 1, 0, 1]))
    print(s.canJump([3, 0, 0, 0]))
    print(s.canJump([1, 0, 0, 1, 1, 2, 2, 0, 2, 2]))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/8.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/10.Jump%20Game%20II'>следующая задача ➡️</a></h3></div>