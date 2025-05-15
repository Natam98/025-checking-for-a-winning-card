from random import sample, randint

def create_bingo_card()-> dict[str, list[int]]: 

    bingo_colums: str = "BINGO"
    bingo_card: dict[str, list[int]] = {}

    start_range: int = 1
    for colums in bingo_colums:
        bingo_card[colums]=sample(range(start_range, start_range+15), 5)
        start_range+=15
    
    return bingo_card


def display_bingo_card(bingo_card: dict[str, list[int]]) -> None:
    
    print("B    I    N    G    O")
    print("-"*23)
    for row in range(5):
        for column in bingo_card:
            print(f"{bingo_card[column][row]:<5}", end="")
        print()


def is_a_winning_bingo_card(bingo_card: dict[str, list[int]]) -> bool: 
    
    # Check for a winning row: five zeros in a horizontal line
    for index_row in range(5):
        if all(bingo_card[column][index_row] == 0 for column in bingo_card):
            return True

    
    # Check for a winning column: five zeros in a vertical line
    for column in bingo_card:
        if all(number == 0 for number in bingo_card[column]):
            return True
        
           
    # Check for a winning primary diagonal: five zeros from top-left to bottom-right

    if all(bingo_card[column][index_row] == 0 for index_row, column in enumerate(bingo_card)):
        return True
    

    # Check for a winning secondary diagonal: five zeros from top-right to bottom-left

    if all(bingo_card[column][4-index_row] == 0 for index_row, column in enumerate(bingo_card)):
        return True
    
    return False


def main():
    random_bingo_card: dict[str, list[int]] = {}
    random_bingo_card=create_bingo_card()

    print("Randomly generated Bingo card:")
    display_bingo_card(random_bingo_card)
    print()


    # Force a winning condition by setting an entire row to 0, select the third row (index 2)
    card_horizontal_win: dict[str, list[int]] = {}
    INDEX_WINNING_ROW: int = 2    
                   
    for column in random_bingo_card:
        new_column:list[int]
        new_column=random_bingo_card[column].copy()
        
        new_column[INDEX_WINNING_ROW]=0
    
        card_horizontal_win[column]=new_column
        
       
    # Force a winning condition by setting an entire column to 0, select the 'G' column
    card_vertical_win: dict[str, list[int]] = {}
    WINNING_COLUMN: str = "G"
    
    for column in random_bingo_card:
        new_column: list[int]
        new_column=random_bingo_card[column].copy()
        
        if column==WINNING_COLUMN:
            for index in range(len(new_column)):
                new_column[index]=0
        
        card_vertical_win[column]=new_column
    
              
    # Force a winning condition by setting the main diagonal to 0s (from top-left to bottom-right)
    card_diagonal_win: dict[str, list[int]] = {}
    index_row: int = 0
    
    for column in random_bingo_card:
        new_column:list[int]
        new_column=random_bingo_card[column].copy()
        
        new_column[index_row]=0
    
        card_diagonal_win[column]=new_column

        index_row+=1
   
            
    # Create a Bingo card with some marked numbers (0s) but no complete row, column, or diagonal
    no_winning_card: dict[str, list[int]] = {}
    index_row: int = randint(0, 4)
    
    for column in random_bingo_card:
        new_column:list[int]
        new_column=random_bingo_card[column].copy()
        
        new_column[index_row]=0
    
        no_winning_card[column]=new_column

        index_row=randint(0, 4)


    bingo_cards: list[tuple[str, dict[str, list[int]]]] = [
        
    ("Horizontal winning card", card_horizontal_win),
    ("Vertical winning card", card_vertical_win),
    ("Diagonal winning card", card_diagonal_win),
    ("No winning card with partial marks", no_winning_card)
    ]

    bingo_win_case: str
    bingo_card: dict[str, list[int]]
    
    for bingo_win_case, bingo_card in bingo_cards:
        print(f"{bingo_win_case}:")
        
        display_bingo_card(bingo_card)
        
        if is_a_winning_bingo_card(bingo_card):
            
            print("This card is a winner!\n")
        else:
            print("This card is not a winner!\n")


if __name__=="__main__":
    main()