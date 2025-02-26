def print_board(board):
    """Fungsi untuk mencetak papan permainan."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Fungsi untuk memeriksa apakah pemain menang."""
    # Cek baris dan kolom
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    
    # Cek diagonal
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    """Fungsi untuk memeriksa apakah permainan seri."""
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    """Fungsi utama untuk permainan Tic-Tac-Toe."""
    # Inisialisasi papan
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Selamat datang di Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Ambil input pemain
        print(f"Pemain {players[current_player]}: Masukkan baris dan kolom (0-2) dipisahkan spasi.")
        try:
            row, col = map(int, input("Baris Kolom: ").split())
            if board[row][col] != " ":
                print("Kotak sudah terisi. Coba lagi.")
                continue
        except (ValueError, IndexError):
            print("Input tidak valid. Masukkan angka antara 0-2 untuk baris dan kolom.")
            continue

        # Perbarui papan
        board[row][col] = players[current_player]
        print_board(board)

        # Cek apakah ada pemenang
        if check_winner(board, players[current_player]):
            print(f"Selamat! Pemain {players[current_player]} menang!")
            break

        # Cek apakah seri
        if is_draw(board):
            print("Permainan seri!")
            break

        # Ganti pemain
        current_player = 1 - current_player


# Main
if __name__ == "__main__":
    tic_tac_toe()
