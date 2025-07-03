import tkinter as tk
from tkinter import messagebox, filedialog
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Button, Progressbar
from pytube import YouTube
import threading
import yt_dlp
import os

# Initialize the main application window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("800x450")
root.resizable(False, False)

# Initialize the style
style = Style(theme='flatly')

# Foldder path StringVar
folder_path = tk.StringVar(value=os.getcwd())


def browse_folder():
    path = filedialog.askdirectory()
    if path:
        folder_path.set(path)
        messagebox.showinfo("Folder Selected", f"Download folder set to: {path}")


def on_progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes', 0)
        downloaded_bytes = d.get('downloaded_bytes', 0)
        if total_bytes > 0:
            progress["maximum"] = total_bytes
            progress["value"] = downloaded_bytes
            status_label.config(text=f"Downloading... {int(downloaded_bytes / total_bytes * 100)}%")
    elif d['status'] == 'finished':
        status_label.config(text="✅ Download completed!")
        progress["value"] = 0


def download_video():
    url = url_entry.get()
    path = folder_path.get()

    if not url.startswith("https://") and not url.startswith("http://"):
        messagebox.showerror("Invalid URL", "Please enter a valid YouTube video URL.")
        return

    if not os.path.exists(path):
        messagebox.showerror("Invalid Folder", "Please select a valid download folder.")
        return

    status_label.config(text="Fetching video info...")
    progress["value"] = 0

    def run():
        try:
            ydl_opts = {
                'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
                'progress_hooks': [on_progress_hook],
                'quiet': True,
                'no_warnings': True,
                'format': 'mp4',  # or 'best[ext=mp4]/best' to force single format
                'merge_output_format': None  # <-- this skips merging
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            messagebox.showerror("Download Error", f"An error occurred: {e}")
            status_label.config(text="❌ Download failed.")

    threading.Thread(target=run).start()


# Create UI elements
tk.Label(root, text="Youtube Downloader", font=("Helvetica", 18, "bold")).pack(pady=10)

url_entry = Entry(root, font="Helvetica 12", width=55)
url_entry.insert(0, "https://www.youtube.com/")
url_entry.pack(pady=5)

folder_frame = tk.Frame(root)
folder_frame.pack(pady=5)

folder_entry = Entry(folder_frame, textvariable=folder_path, font=("Helvetica", 10), width=40)
folder_entry.pack(side="left", padx=5)

browse_btn = Button(folder_frame, text="Browse", bootstyle="secondary", command=browse_folder)
browse_btn.pack(side="left", padx=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

download_btn = Button(button_frame, text="Download", bootstyle="primary", command=download_video)
download_btn.pack(side="left", padx=10)

cancel_btn = Button(button_frame, text="Cancel", bootstyle="light", command=root.destroy)
cancel_btn.pack(side="left", padx=10)

progress = Progressbar(root, length=450, mode="determinate")
progress.pack(pady=10)

status_label = tk.Label(root, text="", font=("Helvetica", 10), fg="green")
status_label.pack()

# Start GUI
root.mainloop()