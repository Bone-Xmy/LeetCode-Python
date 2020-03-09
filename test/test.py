class Solution():
    def hello(self):
        a = "hualala"
        print(a)
        for i in range(5):
            print(i)

        print('===========')
        b = [1,1,1]
        del b[0]
        b[5] = 2
        self.foo(b)

    def foo(self, l):
        for i in l:
            print(i)

Solution().hello()
