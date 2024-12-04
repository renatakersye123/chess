# Chessboard Placement and Capture Checker

## Description
This program simulates placing chess pieces on an 8x8 board and checks for possible captures. It allows users to add one chosen white piece and up to 16 or 16 black pieces to the board while ensuring valid moves. 
After all pieces are placed, the program calculates potential captures for white pawn or rook that was chosen in the first move that user had made.

## Table of Contents
1. [Usage](#usage)
2. [Known Issues or Limitations](#known-issues-or-limitations)
3. [Credits or Acknowledgments](#credits-or-acknowledgments)
4. [Challenges and issues](#challenges-and-issues)
5. [Fixes after peer review](#fixes-after-peer-review)

## Usage
1. **Setup**: 
   - Run the script using Python.
   - The board is initialized as an empty 8x8 grid.
   - Ender what is required in the input.
   

2. **Placing Pieces**: 
   - Enter the coordinates for white and black pieces using the format `piece a1` (e.g., `pawn c2`).
   - White has a single turn to place one piece. Black can place up to 16 pieces, or stop early by typing `done`.

3. **Piece Types**:
   - White: `pawn` (O) and `rook` (R).
   - Black: `pawn`, `rook`, `king`, `queen`, `bishop`, `knight` - are not differentiated figures in the board representation so they will all appear as X because they do not make any moves in this board game logic.

4. **Move Validation**:
   - The program checks that the input format is correct, the chosen position is within the board boundaries, and the position is unoccupied.

5. **Capture Checks**:
   - Once all pieces are placed, the program evaluates possible captures for white pieces:
     - **Pawns**: Can capture diagonally upward if a black piece is present.
     - **Rooks**: Can capture along rows or columns until blocked by another piece.

6. **Output**:
   - A visual representation of the board is displayed after every move.
   - Capture opportunities are printed with coordinates in chess notation (e.g., `b3`).

## Known Issues or Limitations
- The program does not currently validate complex chess rules (e.g., legal moves for all piece types).
- Pieces other than white pawns and rooks do not have capture logic implemented.

## Credits or Acknowledgments
- **Author**: Renata K.
- Matterial used from various contents such as stackoverflow, chat gpt, previous tasks I.E. suggested solution for tiktaktoe, consultations. 

## Challenges and issues
- Fixed after peer review

## Fixes after peer review
- Instead of numerous #comments adjusted to docstrings
- Due to the fact that calculations were redundant and repeated - minimised as peer was able to note which parts are overexagerated 
- Some functions also were repetitive - minimised as peer was able to note which parts are overexagerated 
- Found a way to sync both reversed board row identifyers and coordinate placement according to that logic
- Formatted the code with "black"
- Adjusted coordinate placement input