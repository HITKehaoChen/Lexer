class DFA:
    # 初始化DFA
    def __init__(self, S, s0, F, move):
        self.S = S  # 状态集(list)
        self.s0 = s0  # 初态(lsit)
        self.F = F  # 终态(list)
        self.move = move  # 状态转移函数（套成傻逼了已经）

    # 判断是否接受x
    def isAccept(self, x):
        print('判断是否接受输入的字符串x')
        for ch in x:
            flag = False
            for i in self.s0:
                for j in range(len(move[i])):
                    if ch in list(move[i].keys())[j]:
                        self.s0 = list(move[i].values())[j]
                        flag = True
            if(flag == False):
                print("False")
                return flag

                # else:
                #     print("False")
                #     return False

        if len(set(self.s0).intersection(set(self.F))) != 0:
            print("True")
            return True
        else:
            print("False")
        return False




# DFA用法
if __name__ == '__main__':
    digitlist = [chr(i) for i in range(48, 58)]
    digit = tuple(digitlist)
    Alphabetalist = [chr(i) for i in range(65, 91)]
    alphabetalist = [chr(i) for i in range(97, 123)]
    alphabeta = Alphabetalist + alphabetalist
    alphabeta = tuple(alphabeta)

    # S = [0, 1, 2, 3]
    S = [0,1,2,3,4,5,6]

    # s0 = [0]
    s0 = [0]

    # F = [3]
    F = [1,3,6]

    # move = [{('a',): [1], ('b',): [0]}, {('a',): [1], ('b',): [2]}, {('a',): [1], ('b',): [3]}, {('a',): [1], ('b',): [0]}]
    move = [{digit: [1, 3, 6]}, {digit: (1, 3, 6), ('.',): [2], ('E', 'e'): [4, 5]}, {digit: [3, 6]},
            {digit: [3, 6], ('E', 'e'): [4, 5]}, {digit: [6], ('+', '-'): [5]}, {digit: [6]}, {digit: [6]}]



    D = DFA(S, s0, F, move)

    x = "123.5."
    D.isAccept(x)
