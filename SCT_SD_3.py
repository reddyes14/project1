import tkinter as tk
from tkinter import messagebox

entries = []

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def read_grid():
    board = []
    for r in range(9):
        row = []
        for c in range(9):
            value = entries[r][c].get()
            if value.strip() == "":
                row.append(0)
            elif value.isdigit() and 1 <= int(value) <= 9:
                row.append(int(value))
            else:
                raise ValueError(f"Invalid entry at row {r+1}, col {c+1}")
        board.append(row)
    return board


def solve_puzzle():
    try:
        board = read_grid()
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        return

    if solve(board):
        for r in range(9):
            for c in range(9):
                entries[r][c].delete(0, tk.END)
                entries[r][c].insert(0, str(board[r][c]))
    else:
        messagebox.showinfo("No Solution", "This puzzle has no solution.")


def clear_grid():
    for r in range(9):
        for c in range(9):
            entries[r][c].delete(0, tk.END)


BG_COLOR = "#1e2a38"
BOX_LIGHT = "#f4f4f4"
BOX_SHADE = "#cfe8ef"
TEXT_COLOR = "#1e2a38"

root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("400x500")
root.configure(bg=BG_COLOR)

title = tk.Label(root, text="Sudoku Solver", font=("Arial", 16, "bold"),
                  bg=BG_COLOR, fg="#ffffff")
title.pack(pady=10)

grid_frame = tk.Frame(root, bg=BG_COLOR)
grid_frame.pack()

for r in range(9):
    row_entries = []
    for c in range(9):
        box_id = (r // 3) + (c // 3)
        cell_color = BOX_SHADE if box_id % 2 == 0 else BOX_LIGHT

        e = tk.Entry(grid_frame, width=2, font=("Arial", 14), justify="center",
                      bg=cell_color, fg=TEXT_COLOR, relief="flat",
                      highlightthickness=1, highlightbackground="#888888")
        e.grid(row=r, column=c, padx=(3 if c % 3 == 0 else 1),
               pady=(3 if r % 3 == 0 else 1))
        row_entries.append(e)
    entries.append(row_entries)

button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=15)

solve_button = tk.Button(button_frame, text="Solve", command=solve_puzzle, width=10,
                          bg="#2a9d8f", fg="white", font=("Arial", 10, "bold"),
                          relief="flat", cursor="hand2")
solve_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_grid, width=10,
                          bg="#e76f51", fg="white", font=("Arial", 10, "bold"),
                          relief="flat", cursor="hand2")
clear_button.grid(row=0, column=1, padx=5)

note = tk.Label(root, text="Leave empty cells blank. Enter numbers 1-9 for known values.",
                 wraplength=350, font=("Arial", 9), bg=BG_COLOR, fg="#cccccc")
note.pack(pady=5)

root.mainloop()
