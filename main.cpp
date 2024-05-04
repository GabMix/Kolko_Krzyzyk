#include <iostream>

using namespace std;

#define COLS 3
#define ROWS 3

void drawBoard(char board[COLS][ROWS]) 
{ 
    cout << "-------------\n"; 
    for (int i = 0; i < COLS; i++) 
    { 
        cout << "| "; 
        for (int j = 0; j < ROWS; j++) 
        { 
            cout << board[i][j] << " | "; 
        } 
        cout << "\n-------------\n"; 
    } 
} 

int main()
{
    char board[COLS][ROWS] = { { ' ', ' ', ' ' }, 
                         { ' ', ' ', ' ' }, 
                         { ' ', ' ', ' ' } }; 
    drawBoard(board);
}
