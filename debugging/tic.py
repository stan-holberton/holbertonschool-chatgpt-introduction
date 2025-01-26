#!/usr/bin/python3

def print_board(board):
    """
    Affiche le plateau de jeu avec des séparateurs.
    """
    for idx, row in enumerate(board):
        print(" | ".join(row))
        if idx < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    """
    Vérifie si un joueur a gagné.
    """
    # Vérifie les lignes
    for row in board:
        if all(cell == row[0] and cell != " " for cell in row):
            return True

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Vérifie les diagonales
    if board[1][1] != " ":
        if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            return True

    return False

def is_board_full(board):
    """
    Vérifie si toutes les cases sont remplies.
    """
    return all(" " not in row for row in board)

def get_valid_input(prompt):
    """
    Demande à l'utilisateur une entrée valide entre 0 et 2.
    """
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 2:
                return value
            print("Erreur : veuillez entrer un nombre entre 0 et 2.")
        except ValueError:
            print("Erreur : entrée invalide, un nombre est attendu.")

def tic_tac_toe():
     """
    Fonction principale pour le jeu.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"C'est au tour du joueur {player}.")
        row = get_valid_input("Choisissez une ligne (0, 1 ou 2) : ")
        col = get_valid_input("Choisissez une colonne (0, 1 ou 2) : ")

        if board[row][col] == " ":
            board[row][col] = player

            if check_winner(board):
                print_board(board)
                print(f"Le joueur {player} a gagné ! Félicitations !")
                break

            if is_board_full(board):
                print_board(board)
                print("Match nul ! Le plateau est plein.")
                break

            # Alterner entre X et O
            player = "O" if player == "X" else "X"
        else:
            print("Cette case est déjà occupée, essayez un autre emplacement.")

tic_tac_toe()
