import time

# sudoku = [
#     5, 6, 0, 1, 0, 0, 0, 0, 0,
#     8, 0, 0, 3, 4, 0, 0, 0, 7,
#     0, 0, 4, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 9, 0, 1, 0, 4, 8,
#     0, 0, 0, 4, 0, 0, 9, 0, 3,
#     0, 1, 0, 0, 0, 0, 5, 0, 0,
#     0, 5, 0, 0, 0, 0, 3, 0, 0,
#     0, 0, 0, 0, 3, 0, 0, 8, 0,
#     2, 0, 8, 5, 6, 0, 0, 0, 0,
# ]


def input_sudoku():
    """输入数独的函数，返回一个列表，存储了9个元素，
    每个元素是9个数字的字符串，用来代表数独"""
    str_sudo = []
    sudoku = []
    print("请输入数独,每行9个数字，空的格为0，回车换行：")
    for i in range(0, 9):
        str_sudo.append(input())
    for i in range(0, 9):
        for j in range(0, 9):
            num = int(str(str_sudo[i])[j])
            sudoku.append(num)
    return sudoku


def print_sudoku(sudo_name):
    """使输出数独易于阅读"""
    for i in range(0, 9):
        if i % 3 == 0:
            print(" -------------------------")
        for j in range(0, 9):
            if j % 3 == 0:
                print(" |", end='')
            print("%2s" % sudo_name[i*9+j], end='')
        print(" |")
    print(" -------------------------")
    
def check(sudo_name, n, num):
    """检查第n个数字的横、竖和小方格子能不能填num，
    能填则返回True，否则返回False"""
    x = int(n / 9)
    y = int(n % 9)
    # 所在行和列
    x_sqr = int(x/3)*3
    y_sqr = int(y/3)*3
    # 所在小方格第一个数字的行和列
    for i in range(0, 9):
        if sudo_name[x*9+i] == num:
            return False
        if sudo_name[i*9+y] == num:
            return False
    for i in range(0, 3):
        for j in range(0, 3):
            location = (x_sqr+i)*9+y_sqr+j
            if sudo_name[location] == num:
                return False
    return True

def sum_sudoku(sudo_name):
    """统计数独已经填了多少个格子"""
    m = 0
    for n in range(0, 81):
        if sudo_name[n] != 0:
            m = m+1
    return m


def solve_print(sudo_name, n):
    if n == 81:
        print("运算结果为： ")
        print_sudoku(sudo_name)
        return
    if sudo_name[n] != 0:
        solve_print(sudo_name, n+1)
    else:
        for i in range(1, 10):
            if check(sudo_name, n, i):
                sudo_name[n] = i
                solve_print(sudo_name, n + 1)
            sudo_name[n] = 0
            

def run():
    sudoku = input_sudoku()
    print(" 输入的数独为： ")
    print_sudoku(sudoku)
    start_time = time.time()
    solve_print(sudoku, 0)
    stop_time = time.time()
    func_time = stop_time - start_time
    print(" 运算用时：%s s" % func_time)


if __name__ == '__main__':
    run()