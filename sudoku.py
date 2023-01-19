import random


board = [[None]*9]*9

board_answer = [ [0]*9 for i in range(9)]


def generate_puzzle():
    
    def check_box(row,col, num):

        #print("This function ran and looped 9 times")
        og_loc_row = row % 3
        og_loc_col = col % 3
        
        #goal is to make loc be the top left corner no matter the original loc

        match og_loc_row:
            case 0:
                loc_row = row
            case 1:
                loc_row = row - 1
            case 2:
                loc_row = row - 2

        match og_loc_col:
            case 0:
                loc_col = col
            case 1:
                loc_col = col - 1
            case 2:
                loc_col = col - 2

        #loc should now be the top left corner of the box
        #run the logic as normal 

        for x in range(9):
            match x:
                case 0:
                    spot = board_answer[loc_row][loc_col]
                case 1:
                    spot = board_answer[loc_row][loc_col+1]
                case 2:
                    spot = board_answer[loc_row][loc_col+2]
                case 3:
                    spot = board_answer[loc_row+1][loc_col]
                case 4:
                    spot = board_answer[loc_row+1][loc_col+1]
                case 5:
                    spot = board_answer[loc_row+1][loc_col+2]
                case 6:
                    spot = board_answer[loc_row+2][loc_col]
                case 7:
                    spot = board_answer[loc_row+2][loc_col+1]
                case 8:
                    spot = board_answer[loc_row+2][loc_col+2]
            #print("num = " + str(num))
            #print("spot = " + str(spot) + "spot loc is ")
            #print("row -- " + str(row))
            #print("col -- " + str(col))

            #print()
            
            if spot == num:
                #print("This is false")
                return False
        #print("this is true")
        return True
        



    def check_row(row, col, num):
        if num in board_answer[row]:
            return False
        return True

    
    def check_col(row, col, num):
        for i in range(len(board_answer)):
            #print("num  == " + str(num))
            #print("spot num --" + str(board_answer[i][col]))
            if board_answer[i][col] == 0:
                break
            elif num == board_answer[i][col]:
                return False
        return True
            
        

    def random_int():
        return random.randint(1,9)

    def generate_num(row, col):
        check_BOX = False
        check_ROW = False
        check_COL = False
        
        while not check_BOX or not check_ROW or not check_COL:
            num = random_int()
            check_BOX = check_box(row,col,num)
            check_ROW = check_row(row,col,num)
            check_COL = check_col(row,col,num)
        return num
        #print("num = " + str(num))
        #print("check_BOX " + str(check_BOX) + "    check_ROW    " + str(check_ROW) + "    check_COL    " + str(check_COL))
        '''if check_BOX and check_ROW and check_COL:
           # print("||||||||||||||||||||||||||||||")
            return num
        return generate_num(row, col)'''







    def generate_board():
        for row in range(len(board_answer)):
            for col in range(len(board_answer[row])):
                board_answer[row][col] = generate_num(row,col)
                #print_board()
            #print(row)
                

    generate_board()








                
def print_board():
    for row in range(len(board_answer)):
        if row % 3 == 0:
            for i in range(9):
                print("-", end=" ")
            print()
        for col in range(len(board_answer[row])):
            if col % 3 == 0:
                print("|", end=" ")
            print(board_answer[row][col], end=" ")
        print()
    print()
            
            





#def check_input(row, col, num):

generate_puzzle()
print_board()