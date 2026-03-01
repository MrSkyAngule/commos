import tkinter as tk
import json

def update_json(*args):
    # Берем текст и упаковываем в словарь, затем в JSON-строку
    data = {"user_input": user_text.get()}
    json_string = json.dumps(data, ensure_ascii=False)
    print(f"Текущий JSON: {json_string}") # Для проверки в консоли

root = tk.Tk()
user_text = tk.StringVar()

# 'write' означает, что функция сработает при любой записи в переменную
user_text.trace_add("write", update_json)

entry = tk.Entry(root, textvariable=user_text)
entry.pack(pady=20)

root.mainloop()
