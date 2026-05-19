import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ----------------------------
# TOP ACTIONS FRANÇAISES
# ----------------------------
stocks = {
    "LVMH": "MC.PA",
    "TotalEnergies": "TTE.PA",
    "BNP Paribas": "BNP.PA",
    "Airbus": "AIR.PA",
    "Sanofi": "SAN.PA",
    "L'Oréal": "OR.PA",
    "Schneider Electric": "SU.PA",
    "AXA": "CS.PA",
    "Danone": "BN.PA",
    "Safran": "SAF.PA"
}

# ----------------------------
# COLLECT ALL DATA
# ----------------------------
def fetch_all_data(selected_keys):
    all_data = []

    for name in selected_keys:
        symbol = stocks[name]
        stock = yf.Ticker(symbol)
        info = stock.info

        if "regularMarketPrice" in info:
            all_data.append({
                "Company": name,
                "Symbol": symbol,
                "Price": info.get("regularMarketPrice"),
                "Open": info.get("open"),
                "High": info.get("dayHigh"),
                "Low": info.get("dayLow"),
                "Volume": info.get("volume"),
                "MarketCap": info.get("marketCap"),
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    return pd.DataFrame(all_data)


# ----------------------------
# DISPLAY DATA
# ----------------------------
def get_data():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select at least one stock")
        return

    selected_names = [list(stocks.keys())[i] for i in selected]

    df = fetch_all_data(selected_names)

    if df.empty:
        messagebox.showerror("Error", "No data found")
        return

    root.df = df

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, df.to_string())

    export_btn.config(state=tk.NORMAL)
    graph_btn.config(state=tk.NORMAL)


# ----------------------------
# EXPORT EXCEL
# ----------------------------
def export_excel():
    file = filedialog.asksaveasfilename(defaultextension=".xlsx")

    if file:
        root.df.to_excel(file, index=False)
        messagebox.showinfo("Success", "Excel exported")


# ----------------------------
# GRAPH FUNCTION (IMPORTANT)
# ----------------------------
def show_graph():
    df = root.df

    plt.figure(figsize=(10,6))
    plt.bar(df["Company"], df["Price"])

    plt.title("Stock Price Comparison")
    plt.xlabel("Companies")
    plt.ylabel("Price (€)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


# ----------------------------
# UI
# ----------------------------
root = tk.Tk()
root.title("Stock Market Analyzer PRO")
root.geometry("750x650")

title = tk.Label(root, text="📊 Stock Market Analyzer PRO", font=("Arial", 18))
title.pack(pady=10)

# MULTI SELECT LISTBOX
label = tk.Label(root, text="Select stocks (multi-select):")
label.pack()

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
listbox.pack()

for stock in stocks.keys():
    listbox.insert(tk.END, stock)

# BUTTONS
tk.Button(root, text="Fetch Data", command=get_data).pack(pady=5)

export_btn = tk.Button(root, text="Export Excel", command=export_excel, state=tk.DISABLED)
export_btn.pack(pady=5)

graph_btn = tk.Button(root, text="Show Graph", command=show_graph, state=tk.DISABLED)
graph_btn.pack(pady=5)

# OUTPUT
result_text = tk.Text(root, height=15)
result_text.pack(pady=10)

root.mainloop()