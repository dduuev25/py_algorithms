# 快速排序，使用递归实现

def quick_sort(data):

    if len(data) >= 2:
        mid = data[len(data)//2]
        left = []
        right = []
        data.remove(mid)

        for x in data:
            if x > mid:
                right.append(x)
            else :
                left.append(x)
        return quick_sort(left) + [mid] +quick_sort(right)
    else:
        return data


if __name__ == "__main__":
    some_list = [4,6,31,3,6,7,8,4,77,3,3,222,2,2,34,5,6,7,88,5,5,4,33]
    print(quick_sort(some_list))