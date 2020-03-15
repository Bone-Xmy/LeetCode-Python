from collections import defaultdict

def test_dict():
    rows = [defaultdict(int) for i in range(9)]

    rows[0][1] += 1
    print("1 这个 key 的值为：" + str(rows[0][1]))
    rows[0][1] -= 1
    print("1 这个 key 的值为：" + str(rows[0][1]))

    print("1 是否在rows[0]中：" + str(1 in rows[0]))
    print(1 in rows[1])

if __name__ == "__main__":
    test_dict()
