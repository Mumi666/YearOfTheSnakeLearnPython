def is_subsequence(a, b):
    # 将序列b转换成迭代器
    # 利用了迭代器只能向前移动，确保元素的顺序性
    b = iter(b)

    #all() 确保所有元素都满足条件
    # for i in a 遍历a中的每个元素
    # i in b 用 a 中的每一个元素 去迭代器b中比较
    return all(i in b for i in a)

def is_subsequence_verbose(a, b):
    b_iterator = iter(b)
    for char in a:
        found = False
        for b_char in b_iterator:
            if char == b_char:
                found = True
                break
        if not found:
            return False
    return True

print(is_subsequence('abc', 'ahbgdc'))
print(is_subsequence('axc', 'ahbgdc'))
print(is_subsequence('bac', 'ahbgdc'))

print(is_subsequence_verbose('abc', 'ahbgdc'))
print(is_subsequence_verbose('axc', 'ahbgdc'))
print(is_subsequence_verbose('bac', 'ahbgdc'))