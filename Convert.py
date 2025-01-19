import tkinter as tk
from tkinter import filedialog, messagebox
import os
from pdf2image import convert_from_path

class PDFtoJPEGConverter:
    def __init__(self, master):
        self.master = master
        master.title("PDF to JPEG Converter")
        
        # PDF file selection
        self.pdf_path = tk.StringVar()
        self.pdf_button = tk.Button(master, text="Select PDF", command=self.select_pdf)
        self.pdf_button.pack(pady=10)
        self.pdf_label = tk.Label(master, textvariable=self.pdf_path)
        self.pdf_label.pack()

        # Output folder selection
        self.output_path = tk.StringVar()
        self.output_button = tk.Button(master, text="Select Output Folder", command=self.select_output)
        self.output_button.pack(pady=10)
        self.output_label = tk.Label(master, textvariable=self.output_path)
        self.output_label.pack()

        # Convert button
        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.pack(pady=20)

        # Poppler path (adjust this path to match your Poppler installation)
        self.poppler_path = r"C:\Program Files\poppler-24.08.0\Library\bin"
        
         # Label with hyperlink at the bottom
        self.hyperlink_label = tk.Label(master, text="Developed by Cameron James", fg="blue", cursor="hand2")
        self.hyperlink_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)
        self.hyperlink_label.bind("<Button-1>", lambda e: self.callback("http://cameronjames.io"))

    def callback(self, url):
        import webbrowser
        webbrowser.open_new(url)

    def select_pdf(self):
        pdf = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf:
            self.pdf_path.set(pdf)

    def select_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_path.set(folder)

    def convert(self):
        if not self.pdf_path.get() or not self.output_path.get():
            messagebox.showerror("Error", "Please select both PDF file and output folder.")
            return
        
        try:
            # Convert PDF to images using the specified Poppler path
            images = convert_from_path(self.pdf_path.get(), dpi=300, output_folder=self.output_path.get(), poppler_path=self.poppler_path)
            
            # Naming and saving images
            pdf_name = os.path.splitext(os.path.basename(self.pdf_path.get()))[0]
            for i, image in enumerate(images):
                image_name = f"{pdf_name}_page_{i+1}.jpg"
                image_path = os.path.join(self.output_path.get(), image_name)
                image.save(image_path, 'JPEG')
            
            messagebox.showinfo("Success", f"Conversion completed! {len(images)} image(s) saved to {self.output_path.get()}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during conversion: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    app = PDFtoJPEGConverter(root)
    root.mainloop()