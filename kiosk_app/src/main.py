import tkinter as tk
from tkinter import messagebox

class KioskApp:
    def __init__(self, master):
        self.master = master
        master.title("파이썬 키오스크 앱")
        master.geometry("800x600")

        self.label = tk.Label(master, text="환영합니다! 메뉴를 선택해주세요.", font=("Arial", 24))
        self.label.pack(pady=50)

        self.order_button = tk.Button(master, text="주문하기", command=self.place_order, font=("Arial", 18), width=15, height=2)
        self.order_button.pack(pady=20)

        self.exit_button = tk.Button(master, text="종료", command=master.quit, font=("Arial", 18), width=15, height=2)
        self.exit_button.pack(pady=10)

    def place_order(self):
        messagebox.showinfo("주문", "주문 기능을 여기에 구현할 예정입니다!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KioskApp(root)
    root.mainloop()
