import tkinter as tk
from tkinter import ttk

# Sample data (replace this with real API data later)
crypto_data = [
    {"name": "Bitcoin", "market_cap": "$1.2T", "circulating": "19.7M BTC", "liquidity": "$30B", "total_supply": "21M BTC"},
    {"name": "Ethereum", "market_cap": "$480B", "circulating": "120.2M ETH", "liquidity": "$18B", "total_supply": "Unlimited"},
    {"name": "BNB", "market_cap": "$90B", "circulating": "153.8M BNB", "liquidity": "$2B", "total_supply": "200M BNB"},
]

# UI setup
root = tk.Tk()
root.title("Crypto Market Overview")
root.geometry("800x300")

# Title label
title = tk.Label(root, text="Cryptocurrency Market Info", font=("Helvetica", 18, "bold"))
title.pack(pady=10)

# Table setup
columns = ("name", "market_cap", "circulating", "liquidity", "total_supply")
tree = ttk.Treeview(root, columns=columns, show='headings')

# Define headings
tree.heading("name", text="Name")
tree.heading("market_cap", text="Market Cap")
tree.heading("circulating", text="Circulating Supply")
tree.heading("liquidity", text="Liquidity")
tree.heading("total_supply", text="Total Supply")

# Set column width
for col in columns:
    tree.column(col, width=150, anchor="center")

# Insert data into table
for crypto in crypto_data:
    tree.insert("", tk.END, values=(
        crypto["name"],
        crypto["market_cap"],
        crypto["circulating"],
        crypto["liquidity"],
        crypto["total_supply"]
    ))

tree.pack(padx=20, pady=10, expand=True, fill=tk.BOTH)

root.mainloop()
