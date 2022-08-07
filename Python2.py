#Создайте программу для игры в ""Крестики-нолики"".



board = list(range(1,10))

wins_coord = [[1,2,3], [1,4,7], [1,5,9], [2,5,8], [3,6,9], [3,5,7], [4,5,6], [7,8,9]]

def draw_board():
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3],'|',board[2+i*3],'|')

# draw_board()

def take_input(p):
    while True:
        value = int(input('куда поставить' + p + '?'))
        if value > 9 or value < 1:
            print('ошибочный ввод')
            continue
        if board[value-1] != value:
            print('эта ячейка уже занята')
            continue
        board[value-1] = p
        break

def check_win():
    for each in wins_coord:
        new = list(map(lambda x: x - 1, each))
        if board[new[0]] == board[new[1]] == board[new[2]]:
            return board[new[1]]
    return False    

count = 0
while True:
    draw_board()
    if count % 2 == 0:
        take_input('X')
    else:
        take_input('O')
    if count > 3:
        winner = check_win()
        if winner:
            draw_board()
            print('победил ' + winner)
            break
    count += 1
    if count > 8:
        print('ничья')
        break     








