function pawn(x, y, color, board) {
    let possibility = new Array(3)

    if (color == "white") {
        possibility[0] = {'x' : x-1, 'y' : y}

        if (board[x-1][y-1] != "" && board[x-1][y+1].color == "black") possibility[1] = {'x' : x-1, 'y' : y-1}
        else possibility[1] = {'x' : -1, 'y' : -1}

        if (board[x-1][y+1] != "" && board[x-1][y+1].color == "black") possibility[1] = {'x' : x-1, 'y' : y+1}
        else possibility[1] = {'x' : -1, 'y' : -1}
    }

    else { 
        possibility[0] = {'x' : x+1, 'y' : y}

        if (board[x+1][y-1] != "" && board[x-1][y+1].color == "white") possibility[1] = {'x' : x+1, 'y' : y-1}
        else possibility[1] = {'x' : -1, 'y' : -1}

        if (board[x+1][y+1] != "" && board[x-1][y+1].color == "white") possibility[1] = {'x' : x+1, 'y' : y+1}
        else possibility[1] = {'x' : -1, 'y' : -1}
    }
    
    return possibility
}

function rook(x, y, color, board) {
    let possibility = new Array(16)

    let x1 = x;
    let y1 = y;

    if (color == "white") {
    }

    else {}
}

