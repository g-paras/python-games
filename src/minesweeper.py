import random

def GenerateMineSweeperMap(n, k):
    arr = [[0 for row in range(n)] for column in range(n)]
    for num in range(k):
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        arr[y][x] = 'X'
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1
        if (x >=1 and x <= n-1) and (y >= 0 and y <= n-1):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1
        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1
 
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 
        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1
        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1
    return arr
def GeneratePlayerMap(n):
    arr = [['-' for row in range(n)] for column in range(n)]
    return arr
def DisplayMap(map):
    for row in map:
        print(" ".join(str(cell) for cell in row))
        print("")
def CheckWon(map):
    for row in map:
        for cell in row:
            if cell == '-':
                return False
    return True
def CheckContinueGame(score):
    print("Score: ", score)
    isContinue = input("Do you want to try again? (y/n) :")
    if isContinue == 'n':
        return False
    return True
def main():
    GameStatus = True
    while GameStatus:
        difficulty = input("Select your difficulty (1, 2, 3):")
        if difficulty.lower() == '1':
            n = 5
            k = 3
        elif difficulty.lower() == '2':
            n = 6
            k = 8
        else:
            n = 8
            k = 20
 
        minesweeper_map = GenerateMineSweeperMap(n, k)
        player_map = GeneratePlayerMap(n)
        score = 0
        while True:
            if CheckWon(player_map) == False:
                print("Which cell do you want to open : eg. 1,1 upto 5,5\n")
                ans=input()
                x=int(ans.split(",")[0])-1
                y=int(ans.split(",")[0])-1
                if (minesweeper_map[y][x] == 'X'):
                    print("Game Over :(")
                    DisplayMap(minesweeper_map)
                    GameStatus = CheckContinueGame(score)
                    break
                else:
                    player_map[y][x] = minesweeper_map[y][x]
                    DisplayMap(player_map)
                    score += 1
 
            else:
                DisplayMap(player_map)
                print("You Won!!")
                GameStatus = CheckContinueGame(score)
                break

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('\nEnd of Game.')
