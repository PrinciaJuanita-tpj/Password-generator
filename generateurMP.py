import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    n = random.randint(8, 50)
    caractere = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caractere) for _ in range(n))
    entry_password.delete(0, tk.END)  # Effacer l'ancien mot de passe
    entry_password.insert(0, password)  # Afficher le nouveau

# Fenêtre principale
root = tk.Tk()
root.title("Passwords generator")
root.geometry("400x250")  # Définir la taille de la fenêtre
root.configure(bg="#2C3E50")  # Changer la couleur de fond


# Label titre
label_title = tk.Label(root, text="Password", font=("Arial", 14, "bold"), bg="#2C3E50", fg="white")
label_title.pack(pady=20)

# Champ d'affichage du mot de passe
entry_password = ttk.Entry(root, width=40, font=("Arial", 12))
entry_password.pack(pady=10, ipady=6)

# Bouton pour générer le mot de passe
button_generate = tk.Button(root, text="Generate", command=generate_password)
button_generate.pack(pady=5)

# Lancer l'application
root.mainloop()
