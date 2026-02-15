theBoard = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}

def printBoard(board):
    print(board['1']+'|'+board['2']+'|'+board['3'])
    print("-+-+-")
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print("-+-+-")
    print(board['7']+'|'+board['8']+'|'+board['9'])
turn = 'x'
theBoard['5'] = turn
printBoard(theBoard)
for i in range(9):
    data1 = input()
    theBoard[data1] = 'o'
    if data1=='2':
        theBoard['7'] = 'x'
        printBoard(theBoard)
        data2 = input()
        theBoard[data2] = 'o'
        if data2=='3':
            theBoard['1'] = 'x'
            printBoard(theBoard)
            data3 = input()
            theBoard[data3] = 'o'
            if data3=='4':
                theBoard['9'] = 'x'
                printBoard(theBoard)
                break
            elif data3=='9':
                theBoard['4'] = 'x'
                printBoard(theBoard)
                break
    
    if data1=='6':
        theBoard['7'] = 'x'
        printBoard(theBoard)
        data2 = input()
        theBoard[data2] = 'o'
        if data2=='3':
            theBoard['9'] = 'x'
            printBoard(theBoard)
            data3 = input()
            theBoard[data3] = 'o'
            if data3=='1':
                theBoard['8'] = 'x'
                printBoard(theBoard)
                break
            elif data3=='8':
                theBoard['1'] = 'x'
                printBoard(theBoard)
                break

    if data1=='4':
        theBoard['3'] = 'x'
        printBoard(theBoard)
        data2 = input()
        theBoard[data2] = 'o'
        if data2=='7':
            theBoard['1'] = 'x'
            printBoard(theBoard)
            data3 = input()
            theBoard[data3] = 'o'
            if data3=='9':
                theBoard['2'] = 'x'
                printBoard(theBoard)
                break
            elif data3=='2':
                theBoard['9'] = 'x'
                printBoard(theBoard)
                break

    if data1=='8':
        theBoard['1'] = 'x'
        printBoard(theBoard)
        data2 = input()
        theBoard[data2] = 'o'
        if data2=='9':
            theBoard['7'] = 'x'
            printBoard(theBoard)
            data3 = input()
            theBoard[data3] = 'o'
            if data3=='4':
                theBoard['3'] = 'x'
                printBoard(theBoard)
                break
            elif data3=='3':
                theBoard['4'] = 'x'
                printBoard(theBoard)
                break
    
    if data1=='1':
        theBoard['4'] = 'x'
        printBoard(theBoard)
        data2 = input()
        theBoard[data2] = 'o'
        if data2=='6':
            theBoard['3'] = 'x'
            printBoard(theBoard)
            data3 = input()
            theBoard[data3] = 'o'
            if data3=='7':
                theBoard['8'] = 'x'
                printBoard(theBoard)
                data4 = input()
                theBoard[data4] = 'o'
                if data4=='2':
                    theBoard['9'] = 'x'
                    printBoard(theBoard)
                    break

    if data1=='3':
        theBoard['6'] = 'x'
        printBoard(theBoard)
        data2 = input()
        theBoard[data2] = 'o'
        if data2=='4':
            theBoard['2'] = 'x'
            printBoard(theBoard)
            data3 = input()
            theBoard[data3] = 'o'
            if data3=='8':
                theBoard['9'] = 'x'
                printBoard(theBoard)
                data4 = input()
                theBoard[data4] = 'o'
                if data4=='1':
                    theBoard['7'] = 'x'
                    printBoard(theBoard)
                    break

    if data1=='7':
        theBoard['8'] = 'x'
        printBoard(theBoard)
        data2 = input()
        theBoard[data2] = 'o'
        if data2=='2':
            theBoard['4'] = 'x'
            printBoard(theBoard)
            data3 = input()
            theBoard[data3] = 'o'
            if data3=='6':
                theBoard['9'] = 'x'
                printBoard(theBoard)
                data4 = input()
                theBoard[data4] = 'o'
                if data4=='1':
                    theBoard['3'] = 'x'
                    printBoard(theBoard)
                    break

    if data1=='9':
        theBoard['8'] = 'x'
        printBoard(theBoard)
        data2 = input()
        theBoard[data2] = 'o'
        if data2=='2':
            theBoard['6'] = 'x'
            printBoard(theBoard)
            data3 = input()
            theBoard[data3] = 'o'
            if data3=='4':
                theBoard['7'] = 'x'
                printBoard(theBoard)
                data4 = input()
                theBoard[data4] = 'o'
                if data4=='3':
                    theBoard['1'] = 'x'
                    printBoard(theBoard)
                    break
    
print("computer wins")