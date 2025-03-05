import random
import tkinter as tk
from tkinter import messagebox, simpledialog

class MafiaGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Multiplayer Mafia Game")
        self.players = []
        self.player_roles = {}
        self.mafia = []
        self.detective = ""
        self.doctor = ""
        self.narrator = ""
        self.create_intro_screen()
    
    def create_intro_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="Welcome to the Multiplayer Mafia Game!", font=("Arial", 14)).pack()
        tk.Label(self.master, text="Enter player names (comma-separated):").pack()
        
        self.entry = tk.Entry(self.master)
        self.entry.pack()
        tk.Button(self.master, text="Start Game", command=self.start_game).pack()
    
    def start_game(self):
        self.players = [p.strip() for p in self.entry.get().split(',') if p.strip()]
        if len(self.players) < 4:
            messagebox.showerror("Error", "At least 4 players are required!")
            return
        
        self.assign_roles()
        self.create_game_screen()
    
    def assign_roles(self):
        roles = ["Mafia", "Detective", "Doctor", "Narrator"] + ["Villager"] * (len(self.players) - 4)
        random.shuffle(roles)
        self.player_roles = dict(zip(self.players, roles))
        
        self.mafia = [player for player, role in self.player_roles.items() if role == "Mafia"]
        self.detective = [player for player, role in self.player_roles.items() if role == "Detective"][0]
        self.doctor = [player for player, role in self.player_roles.items() if role == "Doctor"][0]
        self.narrator = [player for player, role in self.player_roles.items() if role == "Narrator"][0]
    
    def create_game_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="Roles have been assigned. Let the game begin!", font=("Arial", 14)).pack()
        self.btn_action = tk.Button(self.master, text="Eliminate a Player", command=self.eliminate_player)
        self.btn_action.pack()
    
    def eliminate_player(self):
        target = simpledialog.askstring("Elimination", "Who do you want to eliminate?")
        if target in self.players:
            self.players.remove(target)
            messagebox.showinfo("Elimination", f"{target} has been eliminated!")
            self.check_win_condition()
        else:
            messagebox.showwarning("Invalid", "That player does not exist!")
    
    def check_win_condition(self):
        if not self.mafia:
            messagebox.showinfo("Game Over", "The Villagers win!")
            self.master.quit()
        elif len(self.mafia) >= len(self.players) - len(self.mafia):
            messagebox.showinfo("Game Over", "The Mafia wins!")
            self.master.quit()
    
    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = MafiaGame(root)
    root.mainloop()
