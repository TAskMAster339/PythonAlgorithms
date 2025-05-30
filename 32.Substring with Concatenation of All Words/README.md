<div align='center'>
<h1><a href='https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/'><strong>32) Substring with Concatenation of All Words</strong></a></h1>
</div>

## **Условие:**

Дана строка **s** и массив строк **words**. Все строки в массиве **words** одной и той же длины. Конкатенированная строка - это строка, которая состоит из любой перестановки всех строк массива **words**.

Например, **words** = ["**ab**","**cd**","**ef**"], тогда "**abcdef**", "**abefcd**", ... являются конкатенированными строками.

Нужно вернуть массив индексов начала всех конкатенированных подстрок в строке **s**, порядок индексов не важен.

## **Идея:**

В условии не сказано, но при решении обнаружиться, что строки в **words** могут быть одинаковыми, что портит первоначальную идею с множеством. Для того, чтобы работать с **мультимножеcтвами** (там где элементы могут повторятся) необходимо воспользоваться хэш-таблицей.

## **Реализация:**

В начале, создадим переменную **word_len** = **len**(**words**[**0**]), которая будет хранить длину каждой строки из **words**. Создадим массив **answer**, который вернем в качестве ответа. Также нам понадобится хэш-таблица **etalon**, которая будет эталоном для предполагаемых конкатенированных подстрок. Ключом будет строка из **words**, а значением её частота в массиве.

Теперь с помощью двух циклов проверим все возможные комбинации конкатенированных строк, длинной **word_len**. Первый цикл будет определять отступ от начала строки **s**. (**0**, **1**, **2**, ..., **word_len** - **1**). Второй цикл будет уже шагать по словам в строке, с шагом в **word_len**. Таким незамысловатым образом, мы пройдем по всем возможным конкатенированным строкам.

Для их определения нам понадобиться еще одна хэш-таблица **winodw**, которая будет изменяться динамически, как только она окажется равна эталону, мы будем добавлять в массив с ответом индекс **start**, который аккуратно будет указывать на начало первого в конкатенированной строке слова.



## **Оценка:**

Оценка по времени будет **O**(**N**), так как если обозначить длину строки из **words** за **M**, то первый цикл пройдет **O**(**M**), второй же цикл пройдет **O**(**N** / **M**) (Шаг цикла равен **M**, поэтому количество итераций уменьшится в **M** раз). Так как циклы вложены получим **O**(**M** * **N** / **M**) = **O**(**N**). По памяти нам понадобиться **O**(**K**), где **K** - размер массива **words**. (По условию **1** <= **K** <= **5000**). Так как **K** много меньше **N**, то получим верхнюю границу по памяти равную **O**(**1**).

## Код:
```python
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        etalon = dict()
        answer = []

        for word in words:
            if word in etalon:
                etalon[word] += 1
            else:
                etalon[word] = 1

        for i in range(word_len):
            start = i
            count = 0
            window = dict()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j : j + word_len]
                if word not in words:
                    start = j + word_len
                    window.clear()
                    count = 0
                    continue

                count += 1

                if word in window:
                    window[word] += 1
                else:
                    window[word] = 1

                while window[word] > etalon[word]:
                    window[s[start : start + word_len]] -= 1
                    start += word_len
                    count -= 1

                if count == len(words):
                    answer.append(start)
        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(
        s.findSubstring(
            "wordgoodgoodgoodbestword",
            ["word", "good", "best", "word"],
        ),
    )
    print(s.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
    print(
        s.findSubstring(
            "wordgoodgoodgoodbestword",
            ["word", "good", "best", "good"],
        ),
    )
    print(
        s.findSubstring(
            "lingmindraboofooowingdingbarrwingmonkeypoundcake",
            ["fooo", "barr", "wing", "ding", "wing"],
        ),
    )

```

<div align='center'><h3><a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/31.Longest%20Substring%20Without%20Repeating%20Characters'>⬅️ предыдущая задача</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/README.md'>Все задачи</a>&nbsp;|&nbsp;<a href='https://github.com/TAskMAster339/PythonAlgorithms/tree/main/33.Minimum%20Window%20Substring'>следующая задача ➡️</a></h3></div>