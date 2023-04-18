import tkinter as tk

def show_tree():
    with open('tree.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()

    # contar número de líneas y caracteres por línea
    num_lines = len(content)
    max_line_len = max([len(line) for line in content])


    root = tk.Tk()
    text_widget = tk.Text(root, width=max_line_len, height=num_lines)
    text_widget.pack()


    text_widget.insert('end', ''.join(content))


    root.mainloop()
