import tkinter as tk
from tkinter import filedialog, messagebox
import re
from tkinter import ttk
import os


class EmailExtractorApp:
    def __init__(self, initial):
        self.root = initial
        self.root.title("Email Extractor")
        self.root.geometry("300x250")

        # Time label (placeholder)
        self.time_label = tk.Label(initial, text="12:47", font=("Arial", 10))
        self.time_label.pack(pady=5)

        # Title
        self.title_label = tk.Label(initial, text="Email Extractor", font=("Arial", 14, "bold"))
        self.title_label.pack(pady=10)

        # Browse button
        self.browse_button = ttk.Button(initial, text="Browse", command=self.browse_folder)
        self.browse_button.pack(pady=5)

        # Message label
        self.message_label = tk.Label(initial, text="Message")
        self.message_label.pack(pady=5)

        # Text entry
        self.text_entry = tk.Text(initial, height=5, width=30)
        self.text_entry.pack(pady=5)

        # Button frame
        self.button_frame = tk.Frame(initial)
        self.button_frame.pack(pady=10)

        # Extract button
        self.extract_button = ttk.Button(self.button_frame, text="EXTRACT", command=self.extract_emails)
        self.extract_button.pack(side=tk.LEFT, padx=5)

        # Cancel button
        self.cancel_button = ttk.Button(self.button_frame, text="CANCEL", command=self.root.destroy)
        self.cancel_button.pack(side=tk.LEFT, padx=5)

        # Variables
        self.output_folder = ""

    def browse_folder(self):
        self.output_folder = filedialog.askdirectory()
        if self.output_folder:
            self.message_label.config(text=f"Output folder: {os.path.basename(self.output_folder)}")

    def extract_emails(self):
        text = self.text_entry.get("1.0", tk.END)
        if not text.strip():
            messagebox.showwarning("Warning", "Please enter some text to extract emails from.")
            return

        if not self.output_folder:
            messagebox.showwarning("Warning", "Please select an output folder first.")
            return

        # Extract emails using regex
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)

        if not emails:
            messagebox.showinfo("Info", "No email addresses found in the text.")
            return

        # Save to file
        output_file = os.path.join(self.output_folder, "extracted_emails.pdf")
        try:
            with open(output_file, 'w') as f:
                f.write("\n".join(emails))
            messagebox.showinfo("Success", f"{len(emails)} email(s) extracted and saved to:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save emails: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmailExtractorApp(initial=root)
    root.mainloop()