
from collections import defaultdict


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def tree_(beer_):
    dict_ = defaultdict(int)
    for char in beer_:
        dict_[char] += 1
    print(dict_)

    list_s = list(dict_.items())
    list_s.sort(key=lambda i: i[1])
    print(list_s)

    while len(list_s) > 1:

        value = list_s[0][1] + list_s[1][1]

        node = MyNode(left=list_s.pop(0)[0], right=list_s.pop(0)[0])

        for j, item in enumerate(list_s):
            if value > item[1]:
                continue
            else:
                list_s.insert(j, (node, value))
                break
        else:
            list_s.append((node, value))

    return list_s[0][0]


code_ = {}


def encode(tree, path=''):

    if not isinstance(tree, MyNode):
        code_[tree] = path
    else:
        encode(tree.left, path=f'{path}0')
        encode(tree.right, path=f'{path}1')


def main():
    beer_ = input("Введите данные:  ")
    # beer_ = 'beep boop beer!'
    encode(tree_(beer_))
    for i in beer_:
        print(code_[i], end=' ')


if __name__ == '__main__':
    main()

