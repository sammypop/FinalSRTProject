import re
import tkinter as tk
from tkinter import ttk, messagebox

class EmailExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Extractor")
        self.root.geometry("400x400")

        self.emails = []

        self.notebook = ttk.Notebook(self.root)
        self.browse_tab = ttk.Frame(self.notebook)
        self.message_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.browse_tab, text="Browse")
        self.notebook.add(self.message_tab, text="Message")
        self.notebook.pack(expand=True, fill="both")

        # Browse tab content
        self.email_listbox = tk.Listbox(self.browse_tab, font=("Arial", 10))
        self.email_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Message tab content
        self.text_input = tk.Text(self.message_tab, font=("Arial", 12), height=10)
        self.text_input.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 0))

        # Buttons
        self.button_frame = tk.Frame(self.message_tab)
        self.button_frame.pack(pady=10)

        self.extract_btn = tk.Button(self.button_frame, text="EXTRACT", command=self.extract_emails, bg="#0033cc", fg="white", width=10)
        self.extract_btn.grid(row=0, column=0, padx=10)

        self.cancel_btn = tk.Button(self.button_frame, text="CANCEL", command=self.clear_input, width=10)
        self.cancel_btn.grid(row=0, column=1, padx=10)

    def extract_emails(self):
        message = self.text_input.get("1.0", tk.END)
        emails_found = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", message)

        if emails_found:
            self.email_listbox.delete(0, tk.END)
            self.emails = emails_found
            for email in self.emails:
                self.email_listbox.insert(tk.END, email)
            self.notebook.select(self.browse_tab)
        else:
            messagebox.showinfo("No Emails Found", "No valid email addresses were found in the message.")

    def clear_input(self):
        self.text_input.delete("1.0", tk.END)
        self.email_listbox.delete(0, tk.END)
        self.emails.clear()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EmailExtractorApp(root)
    root.mainloop()
