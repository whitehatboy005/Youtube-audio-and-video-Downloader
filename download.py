import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to handle video download using yt-dlp
def download_video():
    link = url_entry.get()
    if not link:
        messagebox.showerror("Error", "Please enter a YouTube link")
        return

    download_directory = directory_entry.get()
    if not download_directory:
        messagebox.showerror("Error", "Please select a download directory")
        return

    download_type = download_option.get()

    # yt-dlp options
    ydl_opts = {
        'outtmpl': f'{download_directory}/%(title)s.%(ext)s',  # Save as title.mp4 or title.mp3
        'noplaylist': True,  # Avoid downloading entire playlists
    }

    if download_type == "Audio":
        ydl_opts['format'] = 'bestaudio/best'  # Select best audio stream only
    else:  # Video
        ydl_opts['format'] = 'best'  # Select the best combined video and audio stream (combined format like .mp4)

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            status_label.config(text="Downloading...")
            root.update()

            # Download the video/audio
            ydl.download([link])

            status_label.config(text="Download completed!!")
            messagebox.showinfo("Success", f"Download completed! File saved to {download_directory}")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {str(e)}")
        status_label.config(text="Download failed.")

# Function to browse directory
def browse_directory():
    download_directory = filedialog.askdirectory()
    if download_directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, download_directory)

# Create the main window using tkinter
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and place the URL label and entry
url_label = tk.Label(root, text="YouTube URL:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the directory label and entry
directory_label = tk.Label(root, text="Download Directory:")
directory_label.grid(row=1, column=0, padx=10, pady=10)

directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the browse button
browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.grid(row=1, column=2, padx=10, pady=10)

# Create and place the download type dropdown
option_label = tk.Label(root, text="Download Type:")
option_label.grid(row=2, column=0, padx=10, pady=10)

download_option = tk.StringVar(root)
download_option.set("Video")  # Default to Video

option_menu = tk.OptionMenu(root, download_option, "Video", "Audio")
option_menu.grid(row=2, column=1, padx=10, pady=10)

# Create and place the download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.grid(row=3, column=1, padx=10, pady=10)

# Create and place the status label
status_label = tk.Label(root, text="", fg="blue")
status_label.grid(row=4, column=1, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
