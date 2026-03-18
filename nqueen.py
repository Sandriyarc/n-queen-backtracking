import tkinter as tk
import time
import winsound  # hanya untuk Windows

N = 4
board = [[0]*N for _ in range(N)]

root = tk.Tk()
root.title("N-Queen Visualisasi")

# ===== JUDUL =====
title = tk.Label(root, text="Step-by-step Solving (Backtracking N-Queen)",
                 font=("Arial", 14, "bold"))
title.grid(row=0, column=0, columnspan=N+1, pady=10)

# ===== STATUS =====
status_label = tk.Label(root, text="Status: Idle", font=("Arial", 12))
status_label.grid(row=1, column=0, columnspan=N)

cells = [[None]*N for _ in range(N)]

# ===== PAPAN CATUR =====
for i in range(N):
    for j in range(N):
        color = "#EEE" if (i+j) % 2 == 0 else "#888"
        label = tk.Label(root, text="", width=4, height=2,
                         bg=color, fg="black",
                         borderwidth=1, relief="solid", font=("Arial", 16))
        label.grid(row=i+2, column=j)
        cells[i][j] = label

# ===== LOG BOX =====
log_box = tk.Text(root, height=12, width=40)
log_box.grid(row=2, column=N, rowspan=N)

def log(text):
    log_box.insert(tk.END, text + "\n")
    log_box.see(tk.END)
    root.update()

# ===== SOUND =====
def play_sound(freq=800, duration=100):
    try:
        winsound.Beep(freq, duration)
    except:
        pass  # biar ga error kalau bukan Windows

def update_board(highlight=None, color=None):
    for i in range(N):
        for j in range(N):
            base_color = "#EEE" if (i+j) % 2 == 0 else "#888"

            if board[i][j] == 1:
                cells[i][j].config(text="Q", bg="lightgreen")
            else:
                cells[i][j].config(text="", bg=base_color)

    if highlight:
        r, c = highlight
        cells[r][c].config(bg=color)

    root.update()
    time.sleep(0.3)

def is_safe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve(row):
    if row == N:
        log("✅ Solusi ditemukan!")
        play_sound(1200, 200)
        return True

    for col in range(N):
        log(f"➡️ Coba posisi ({row},{col})")
        play_sound(600, 100)
        update_board((row, col), "yellow")

        if is_safe(row, col):
            log("✔️ Aman → letakkan ratu")
            play_sound(1000, 150)
            board[row][col] = 1
            update_board()

            if solve(row + 1):
                return True

            log(f"❌ Backtrack dari ({row},{col})")
            play_sound(400, 150)
            board[row][col] = 0
            update_board((row, col), "red")
        else:
            log("❌ Tidak aman")
            play_sound(400, 150)
            update_board((row, col), "red")

    return False

def start():
    btn.config(state="disabled")
    status_label.config(text="Status: Running...")

    log("=== Mulai Backtracking ===")
    solve(0)

    status_label.config(text="Status: Done ✅")
    btn.config(state="normal")

# ===== BUTTON =====
btn = tk.Button(root, text="Start", command=start)
btn.grid(row=N+3, column=0, columnspan=N)

root.mainloop()