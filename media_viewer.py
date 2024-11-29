import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2

class MediaViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Viewer")
        self.root.geometry("800x600")
        
        self.load_button = tk.Button(root, text="Vložit fotku", command=self.load_image)
        self.load_button.pack(pady=10)

        self.load_video_button = tk.Button(root, text="Vložit video", command=self.load_video)
        self.load_video_button.pack(pady=10)

        self.screensaver_button = tk.Button(root, text="Zapnout screensaver", command=self.start_screensaver)
        self.screensaver_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Vypnout", command=self.exit_app)
        self.exit_button.pack(pady=10)

        self.display_frame = tk.Label(root)
        self.display_frame.pack(expand=True, fill=tk.BOTH)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            try:
                img = Image.open(file_path)
                img = img.resize((800, 500), Image.ANTIALIAS)
                img_tk = ImageTk.PhotoImage(img)
                self.display_frame.config(image=img_tk)
                self.display_frame.image = img_tk
            except Exception as e:
                messagebox.showerror("Chyba", f"Nelze načíst fotku: {e}")
    
    def load_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")])
        if file_path:
            cap = cv2.VideoCapture(file_path)
            if not cap.isOpened():
                messagebox.showerror("Chyba", "Nelze načíst video.")
                return

            def play_video():
                ret, frame = cap.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = cv2.resize(frame, (800, 500))
                    img = ImageTk.PhotoImage(Image.fromarray(frame))
                    self.display_frame.config(image=img)
                    self.display_frame.image = img
                    self.root.after(33, play_video)
                else:
                    cap.release()
            
            play_video()

    def start_screensaver(self):
        messagebox.showinfo("Info", "Funkce zapnutí screensaveru zatím není implementována.")

    def exit_app(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MediaViewerApp(root)
    root.mainloop()
