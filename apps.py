import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json


class CommoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Commo POST → DRF")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.configure("Title.TLabel", font=("Arial", 16, "bold"))

        ttk.Label(root, text="Отправка данных устройства", style="Title.TLabel").pack(pady=15)

        # --- Device ID ---
        dev_frame = ttk.LabelFrame(root, text="Device ID", padding=10)
        dev_frame.pack(fill="x", padx=20, pady=5)
        self.device_var = tk.StringVar(value="device_001")
        ttk.Entry(dev_frame, textvariable=self.device_var, width=50).pack()

        # --- Data ---
        data_frame = ttk.LabelFrame(root, text="Data", padding=10)
        data_frame.pack(fill="x", padx=20, pady=5)
        self.data_var = tk.StringVar(value="36.6")
        ttk.Entry(data_frame, textvariable=self.data_var, width=50).pack()

        # --- URL ---
        url_frame = ttk.LabelFrame(root, text="URL", padding=10)
        url_frame.pack(fill="x", padx=20, pady=5)
        self.url_var = tk.StringVar(value="http://localhost:8000/api/api/messages/")
        ttk.Entry(url_frame, textvariable=self.url_var, width=50).pack()

        # --- Кнопка ---
        self.send_btn = ttk.Button(root, text="Отправить POST", command=self.send_post)
        self.send_btn.pack(pady=10)

        # --- Ответ ---
        log_frame = ttk.LabelFrame(root, text="Ответ сервера", padding=10)
        log_frame.pack(fill="both", expand=True, padx=20, pady=(5, 15))

        self.log_text = tk.Text(log_frame, height=6, wrap="word")
        scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        self.log_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def send_post(self):
        self.send_btn.config(state="disabled")
        self.log_text.delete("1.0", tk.END)

        try:
            device_id = self.device_var.get().strip()
            data_raw = self.data_var.get().strip()

            if not device_id:
                raise ValueError("Заполните Device ID!")
            if not data_raw:
                raise ValueError("Заполните Data!")

            payload = {"device_id": device_id, "data": data_raw}

            response = requests.post(
                self.url_var.get(),
                json=payload,
                timeout=10,
                headers={"Content-Type": "application/json"},
            )

            self.log_text.insert("1.0", f"Код: {response.status_code}\n\n")
            try:
                self.log_text.insert("end", json.dumps(response.json(), indent=2, ensure_ascii=False))
            except Exception:
                self.log_text.insert("end", response.text)

            if response.status_code in [200, 201]:
                messagebox.showinfo("Успех", f"Сохранено!")

        except requests.exceptions.ConnectionError:
            self.log_text.insert("1.0", "Сервер не отвечает!")
            messagebox.showerror("Ошибка", "Нет соединения.\nЗапустите: python manage.py runserver")
        except requests.exceptions.Timeout:
            self.log_text.insert("1.0", "Таймаут!")
            messagebox.showerror("Ошибка", "Сервер не ответил вовремя")
        except Exception as e:
            self.log_text.insert("1.0", str(e))
            messagebox.showerror("Ошибка", str(e))
        finally:
            self.send_btn.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = CommoApp(root)
    root.mainloop()
