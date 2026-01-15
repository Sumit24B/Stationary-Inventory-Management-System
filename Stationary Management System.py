import tkinter as tk
from tkinter import messagebox, Label
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

# ---------------- DATABASE ----------------
conn = sqlite3.connect("full_stationery_shop_v3.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    quantity INTEGER,
    selling_price REAL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    product_name TEXT,
    quantity INTEGER,
    total_price REAL
)
""")

# ---------- STATIONERY DATA SEEDING ----------
def seed_data():
    cur.execute("SELECT COUNT(*) FROM inventory")
    if cur.fetchone()[0] == 0:
        items = [
            ('Ballpoint Pen', 'Writing', 500, 10),
('Gel Pen', 'Writing', 400, 20),
('Fountain Pen', 'Writing', 80, 250),
('Rollerball Pen', 'Writing', 100, 120),
('Ink Cartridge', 'Writing', 200, 40),
('Ink Bottle', 'Writing', 80, 120),
('HB Pencil', 'Writing', 600, 5),
('Mechanical Pencil', 'Writing', 200, 40),
('Colored Pencils', 'Writing', 150, 120),
('Pencil Lead Refills', 'Writing', 300, 20),
('Highlighter', 'Writing', 150, 35),
('Permanent Marker', 'Writing', 120, 50),
('Whiteboard Marker', 'Writing', 120, 45),
('CD Marker', 'Writing', 80, 30),
('Sketch Pens Set', 'Writing', 90, 150),

# ================= ERASING & CORRECTION =================
('Rubber Eraser', 'Correction', 300, 5),
('Non-Dust Eraser', 'Correction', 200, 10),
('Art Gum Eraser', 'Correction', 100, 20),
('Pencil Sharpener', 'Correction', 250, 15),
('Correction Fluid', 'Correction', 120, 30),
('Correction Tape', 'Correction', 100, 40),

# ================= PAPER & NOTEBOOKS =================
('A4 Printer Paper', 'Paper', 80, 380),
('Legal Size Paper', 'Paper', 60, 420),
('Bond Paper', 'Paper', 70, 300),
('Colored A4 Sheets', 'Paper', 100, 180),
('Card Stock Sheets', 'Paper', 80, 220),
('Chart Paper', 'Paper', 200, 15),
('Drawing Sheets Pad', 'Paper', 120, 90),
('Graph Notebook', 'Paper', 150, 55),
('Single Line Notebook', 'Paper', 300, 40),
('Double Line Notebook', 'Paper', 250, 45),
('Spiral Notebook', 'Paper', 200, 70),
('Fancy Diary', 'Paper', 100, 180),
('Pocket Diary', 'Paper', 120, 90),
('Notepad', 'Paper', 200, 35),
('Sticky Notes', 'Paper', 300, 30),
('Chit Block', 'Paper', 150, 25),
('White Envelope', 'Paper', 400, 5),
('Brown Envelope', 'Paper', 300, 7),
('Ruled Register', 'Paper', 150, 150),
('Attendance Register', 'Paper', 100, 120),

# ================= ADHESIVES & FASTENERS =================
('Glue Stick', 'Adhesive', 200, 30),
('Gum Bottle', 'Adhesive', 150, 45),
('Fevi Quick', 'Adhesive', 120, 25),
('Cellophane Tape Small', 'Adhesive', 200, 20),
('Cellophane Tape Large', 'Adhesive', 150, 45),
('Brown Packaging Tape', 'Adhesive', 120, 55),
('Double Sided Tape', 'Adhesive', 100, 60),
('Masking Tape', 'Adhesive', 80, 65),
('Stapler Small', 'Fastener', 80, 90),
('Stapler Heavy Duty', 'Fastener', 40, 250),
('Staple Pins', 'Fastener', 250, 25),
('Staple Remover', 'Fastener', 100, 30),
('Paper Clips', 'Fastener', 300, 10),
('Binder Clips', 'Fastener', 150, 25),
('Push Pins', 'Fastener', 200, 15),
('Drawing Pins', 'Fastener', 180, 15),
('Safety Pins', 'Fastener', 300, 10),
('Rubber Bands Pack', 'Fastener', 200, 20),
('Paper Tags', 'Fastener', 120, 30),
('File Lace', 'Fastener', 100, 20),

# ================= DESK ACCESSORIES =================
('Scissors Small', 'Desk', 100, 40),
('Scissors Large', 'Desk', 80, 75),
('Paper Cutter', 'Desk', 50, 180),
('Tape Dispenser', 'Desk', 70, 90),
('Hole Puncher', 'Desk', 80, 110),
('Ruler 30cm', 'Desk', 300, 20),
('Pencil Box', 'Desk', 150, 60),
('Pen Holder', 'Desk', 120, 85),
('Desk Organizer', 'Desk', 80, 220),
('Paper Tray', 'Desk', 60, 180),
('Waste Paper Basket', 'Desk', 50, 250),
('Stamp Pad', 'Desk', 80, 60),
('Stamp Ink', 'Desk', 60, 45),
('Card Holder', 'Desk', 70, 90),
('Letter Opener', 'Desk', 40, 70),

# ================= FILING & STORAGE =================
('Plastic File Folder', 'Filing', 300, 15),
('Box File', 'Filing', 150, 85),
('Display File', 'Filing', 120, 120),
('Ring Binder', 'Filing', 100, 180),
('Clip File', 'Filing', 180, 50),
('Document Bag', 'Filing', 140, 65),
('Zip Lock Packet', 'Filing', 200, 20),
('File Separator', 'Filing', 120, 40),

# ================= ART & CRAFT =================
('Poster Paint Set', 'Art', 80, 180),
('Acrylic Paint Set', 'Art', 50, 550),
('Watercolor Paints', 'Art', 90, 180),
('Paint Brushes Set', 'Art', 120, 120),
('Wax Crayons', 'Art', 150, 90),
('Oil Pastels', 'Art', 100, 150),
('Origami Sheets', 'Art', 140, 60),
('Glitter Powder', 'Art', 120, 50),
('Moulding Clay', 'Art', 80, 100),
('Canvas Board', 'Art', 60, 220),

# ================= OTHER ESSENTIALS =================
('Basic Calculator', 'Electronics', 60, 250),
('Scientific Calculator', 'Electronics', 40, 1100),
('Geometry Box', 'Math', 120, 180),
('Whiteboard', 'Furniture', 30, 650),
('Board Duster', 'Furniture', 80, 45),
('AA Batteries Pack', 'Electronics', 120, 120),
('USB Flash Drive', 'Electronics', 60, 550),
('Mouse Pad', 'Electronics', 80, 150),
('ID Card Holder', 'Accessories', 120, 40),
('Lanyard', 'Accessories', 100, 30),
('Name Plate', 'Accessories', 50, 220)
]
        cur.executemany("INSERT INTO inventory (name, category, quantity, selling_price) VALUES (?, ?, ?, ?)", items)
        conn.commit()

seed_data()

# ---------------- LOGIN ----------------
def login():
    if username_entry.get() == "Group11" and password_entry.get() == "1111":
        login_window.destroy()
        open_inventory_app()
    else:
        messagebox.showerror("Login Failed", "Invalid Credentials")

login_window = tk.Tk()
login_window.title("Stationery Shop Login")
login_window.geometry("350x250")

tk.Label(login_window, text="Shop Inventory Manager", font=("Arial", 16, "bold")).pack(pady=15)
tk.Label(login_window, text="Username").pack()
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)
tk.Label(login_window, text="Password").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)
tk.Button(login_window, text="Login", width=15, command=login, bg="#2c3e50", fg="white").pack(pady=15)

# ---------------- MAIN APP ----------------
def open_inventory_app():
    root = tk.Tk()
    root.title("Advanced Stationery Management System")
    root.geometry("1150x800")

    # --- FUNCTIONS ---
    def view_products():
        listbox.delete(0, tk.END)
        search_term = search_entry.get().lower()
        cur.execute("SELECT * FROM inventory")
        for row in cur.fetchall():
            if search_term in row[1].lower() or search_term in row[2].lower():
                stock_status = " [!] REORDER" if row[3] < 10 else ""
                listbox.insert(tk.END, f"ID: {row[0]:<4} | {row[1]:<30} | {row[2]:<12} | Qty: {row[3]:<5} | Price: ₹{row[4]:<8} {stock_status}")

    def refresh_data():
        search_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        cat_entry.delete(0, tk.END)
        qty_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        sell_qty.delete(0, tk.END)
        view_products()
        messagebox.showinfo("Refresh", "Inventory List Updated")

    def add_product():
        try:
            cur.execute("INSERT INTO inventory (name, category, quantity, selling_price) VALUES (?, ?, ?, ?)",
                        (name_entry.get(), cat_entry.get(), int(qty_entry.get()), float(price_entry.get())))
            conn.commit()
            refresh_data()
        except:
            messagebox.showerror("Error", "Please fill all fields correctly.")

    def sell_product():
        selected = listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection", "Please select an item from the list.")
            return
        
        raw_text = listbox.get(selected[0])
        pid = raw_text.split("|")[0].replace("ID:", "").strip()
        
        try:
            qty_sold = int(sell_qty.get())
            cur.execute("SELECT name, quantity, selling_price FROM inventory WHERE id=?", (pid,))
            item = cur.fetchone()

            if qty_sold > item[1]:
                messagebox.showerror("Stock Error", f"Only {item[1]} units available.")
                return

            total = qty_sold * item[2]
            cur.execute("INSERT INTO sales (product_id, product_name, quantity, total_price) VALUES (?,?,?,?)",
                        (pid, item[0], qty_sold, total))
            cur.execute("UPDATE inventory SET quantity = quantity - ? WHERE id=?", (qty_sold, pid))
            conn.commit()
            view_products()
            messagebox.showinfo("Success", f"Sale Recorded!\nItem: {item[0]}\nTotal: ₹{total}")
        except:
            messagebox.showerror("Input Error", "Enter a valid quantity.")

    def open_dashboard():
        cur.execute("SELECT product_name, SUM(quantity) FROM sales GROUP BY product_name")
        data = cur.fetchall()
        if not data:
            messagebox.showinfo("Dashboard", "No sales data to display.")
            return
        
        names = [x[0] for x in data]
        units = [x[1] for x in data]

        plt.figure(figsize=(10, 6))
        plt.pie(units, labels=names, autopct='%1.1f%%', startangle=140, shadow=True)
        plt.title("Product Sales Distribution")
        plt.axis('equal')
        plt.show()

    def show_report():
        cur.execute("SELECT SUM(total_price), SUM(quantity) FROM sales")
        res = cur.fetchone()
        rev = res[0] if res[0] else 0
        units = res[1] if res[1] else 0
        messagebox.showinfo("Sales Report", f"STATIONERY SHOP SUMMARY\n\nTotal Revenue: ₹{rev}\nTotal Items Sold: {units}")

    # --- UI COMPONENTS ---
    tk.Label(root, text="Stationery Shop Hub", font=("Helvetica", 24, "bold"), fg="#2c3e50").pack(pady=10)

    # Search & Refresh Bar
    top_bar = tk.Frame(root)
    top_bar.pack(fill="x", padx=30, pady=5)
    tk.Label(top_bar, text="Search Item:", font=("Arial", 10)).pack(side="left")
    search_entry = tk.Entry(top_bar, width=35, font=("Arial", 11))
    search_entry.pack(side="left", padx=10)
    tk.Button(top_bar, text="🔍 Search", command=view_products, width=10).pack(side="left", padx=5)
    tk.Button(top_bar, text="🔄 Refresh", command=refresh_data, width=10, bg="#ecf0f1").pack(side="left", padx=5)

    # Input Form
    input_frame = tk.LabelFrame(root, text="Add New Inventory", padx=15, pady=15, font=("Arial", 10, "bold"))
    input_frame.pack(pady=15, padx=30, fill="x")
    
    tk.Label(input_frame, text="Product Name:").grid(row=0, column=0, sticky="e")
    name_entry = tk.Entry(input_frame, width=30)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Category:").grid(row=0, column=2, sticky="e")
    cat_entry = tk.Entry(input_frame, width=20)
    cat_entry.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(input_frame, text="Stock Qty:").grid(row=1, column=0, sticky="e")
    qty_entry = tk.Entry(input_frame, width=15)
    qty_entry.grid(row=1, column=1, sticky="w", padx=5)

    tk.Label(input_frame, text="Price (₹):").grid(row=1, column=2, sticky="e")
    price_entry = tk.Entry(input_frame, width=15)
    price_entry.grid(row=1, column=3, sticky="w", padx=5)

    tk.Button(input_frame, text="➕ Add to Stock", bg="#27ae60", fg="white", font=("Arial", 10, "bold"), command=add_product, width=15).grid(row=0, column=4, rowspan=2, padx=30)

    # Listbox
    list_frame = tk.Frame(root)
    list_frame.pack(pady=5, padx=30)
    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side="right", fill="y")
    listbox = tk.Listbox(list_frame, width=130, height=18, font=("Courier", 10), yscrollcommand=scrollbar.set)
    listbox.pack()
    scrollbar.config(command=listbox.yview)

    # Checkout & Analytics
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(pady=20, fill="x", padx=30)

    sell_box = tk.LabelFrame(bottom_frame, text="Checkout Counter", bg="#f39c12", padx=10, pady=10)
    sell_box.pack(side="left", fill="both", expand=True)
    tk.Label(sell_box, text="Qty to Sell:", bg="#f39c12", font=("Arial", 10, "bold")).pack(side="left", padx=10)
    sell_qty = tk.Entry(sell_box, width=10, font=("Arial", 12))
    sell_qty.pack(side="left", padx=5)
    tk.Button(sell_box, text="CONFIRM SALE", command=sell_product, bg="#e67e22", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=20)

    analysis_box = tk.LabelFrame(bottom_frame, text="Shop Analytics", padx=10, pady=10)
    analysis_box.pack(side="right", fill="both", expand=True, padx=(20, 0))
    tk.Button(analysis_box, text="📊 Sales Dashboard", command=open_dashboard, width=20, height=2).pack(side="left", padx=10)
    tk.Button(analysis_box, text="📄 Total Report", command=show_report, width=20, height=2, bg="#34495e", fg="white").pack(side="left", padx=10)

    view_products()
    root.mainloop()

login_window.mainloop()