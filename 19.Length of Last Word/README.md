<div align='center'>
<h1><a href='https://leetcode.com/problems/length-of-last-word/description/'><strong>19) Length of Last Word</strong></a></h1>
</div>

## **Условие:**

Дана строка **s**, которая содержит слова и пробелы, необходимо вернуть длину последнего слова в строке. Под словом понимается, максимальная подстрока, состоящая только из непробельных символов.

## **Идея:**

Воспользоваться определением слова.

## **Реализация:**

Создадим переменную **count**, в которой будем считать длину слова. Затем пройдемся по символам слова в обратном порядке. Пропускаем все **i**-тые пробельные символы до тех пор, пока не найдем первый непробельный символ, это будет последний символ последнего слова. Затем каждый раз как только **i**-тый символ не пробел, мы инкрементируем **count**, до тех пор, пока не встретим пробельный символ, в этот момент выходим из цикла, используя **break**, потому что слово закончилось, а его длина записана в **count**. В конце просто его возвращаем.

Также в коде я использовал условие **count** == **0**, чтобы пропустить пробелы, правильно бы было создать булеву переменную и использовать её как флаг, но **count** == **0** полностью справляется с этой функцией, единственный минус - ухудшается читаемость кода.



## **Оценка:**

В наихудшем случае вся строка это одно слово, поэтому будет выполнен весь цикл. Поэтому верхняя граница по времени **O**(**N**), а по памяти **O**(**1**)

## Код:
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if count == 0 and s[i] == " ":
                continue
            if s[i] != " ":
                count += 1
            else:
                break
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
    print(s.lengthOfLastWord("luffy is still joyboy"))

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/18.Integer%20to%20Roman'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/20.Longest%20Common%20Prefix'>следующая задача ➡️</a></h3></div>