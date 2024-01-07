import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("لعبة التخمين")
        self.master.geometry("300x200")  # حجم النافذة

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # تخصيص الألوان
        self.bg_color = "#f0f0f0"  # لون خلفية النافذة
        self.label_color = "#333333"  # لون نص العنوان
        self.button_color = "#4caf50"  # لون زر التخمين
        self.entry_color = "#ffffff"  # لون مربع الإدخال

        # إعداد تخصيصات الواجهة
        self.master.config(bg=self.bg_color)

        self.label = tk.Label(master, text="لقد اخترت رقماً بين 1 و 100. هل يمكنك تخمينه؟", fg=self.label_color, bg=self.bg_color)
        self.label.pack()

        self.entry = tk.Entry(master, bg=self.entry_color)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="تخمين", command=self.make_guess, bg=self.button_color, fg="white")
        self.guess_button.pack()

    def make_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess == self.secret_number:
                messagebox.showinfo("تهانينا!", f"لقد قمت بتخمين الرقم في {self.attempts} محاولة.")
                self.master.destroy()
            elif guess < self.secret_number:
                messagebox.showinfo("أقل من المطلوب", "منخفض جداً. حاول مرة أخرى.")
            else:
                messagebox.showinfo("أعلى من المطلوب", "مرتفع جداً. حاول مرة أخرى.")
        except ValueError:
            messagebox.showerror("خطأ", "الرجاء إدخال عدد صحيح صالح.")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()