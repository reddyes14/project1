import tkinter as tk
from tkinter import ttk, messagebox
class TemperatureConverter:
    UNITS = ["Celsius", "Fahrenheit", "Kelvin"]

    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter | SkillCraft Software Development")
        self.root.geometry("420x320")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")
        self._build_widgets()
    def _build_widgets(self):
        title_label = tk.Label(
            self.root,
            text="🌡️  Temperature Converter",
            font=("Segoe UI", 16, "bold"),
            bg="#f0f4f8",
            fg="#1a1a2e",
        )
        title_label.pack(pady=(20, 10))

        subtitle_label = tk.Label(
            self.root,
            text="Convert between Celsius, Fahrenheit and Kelvin",
            font=("Segoe UI", 10),
            bg="#f0f4f8",
            fg="#555555",
        )
        subtitle_label.pack(pady=(0, 15))

        form_frame = tk.Frame(self.root, bg="#f0f4f8")
        form_frame.pack(pady=5)

        tk.Label(
            form_frame, text="Enter Value:", font=("Segoe UI", 10), bg="#f0f4f8"
        ).grid(row=0, column=0, sticky="w", padx=5, pady=8)

        self.value_entry = ttk.Entry(form_frame, width=18, font=("Segoe UI", 10))
        self.value_entry.grid(row=0, column=1, padx=5, pady=8)
        self.value_entry.focus()

        tk.Label(
            form_frame, text="From:", font=("Segoe UI", 10), bg="#f0f4f8"
        ).grid(row=1, column=0, sticky="w", padx=5, pady=8)

        self.from_unit = ttk.Combobox(
            form_frame, values=self.UNITS, state="readonly", width=16
        )
        self.from_unit.current(0)
        self.from_unit.grid(row=1, column=1, padx=5, pady=8)
        tk.Label(
            form_frame, text="To:", font=("Segoe UI", 10), bg="#f0f4f8"
        ).grid(row=2, column=0, sticky="w", padx=5, pady=8)

        self.to_unit = ttk.Combobox(
            form_frame, values=self.UNITS, state="readonly", width=16
        )
        self.to_unit.current(1)
        self.to_unit.grid(row=2, column=1, padx=5, pady=8)

        convert_btn = tk.Button(
            self.root,
            text="Convert",
            command=self.convert,
            bg="#4361ee",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=14,
            relief="flat",
            cursor="hand2",
        )
        convert_btn.pack(pady=15)

        self.result_label = tk.Label(
            self.root,
            text="Result will appear here",
            font=("Segoe UI", 12, "bold"),
            bg="#f0f4f8",
            fg="#2a9d8f",
        )
        self.result_label.pack(pady=10)
        self.root.bind("<Return>", lambda event: self.convert())
    @staticmethod
    def to_celsius(value, unit):
        """Convert any unit to Celsius (used as an intermediate step)."""
        if unit == "Celsius":
            return value
        elif unit == "Fahrenheit":
            return (value - 32) * 5 / 9
        elif unit == "Kelvin":
            return value - 273.15

    @staticmethod
    def from_celsius(value, unit):
        """Convert Celsius to the target unit."""
        if unit == "Celsius":
            return value
        elif unit == "Fahrenheit":
            return (value * 9 / 5) + 32
        elif unit == "Kelvin":
            return value + 273.15

    def convert(self):
        raw_value = self.value_entry.get().strip()
        from_u = self.from_unit.get()
        to_u = self.to_unit.get()

        if not raw_value:
            messagebox.showwarning("Input Error", "Please enter a temperature value.")
            return

        try:
            value = float(raw_value)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid numeric value.")
            return
        if from_u == "Kelvin" and value < 0:
            messagebox.showerror(
                "Invalid Temperature", "Kelvin values cannot be negative (below absolute zero)."
            )
            return

        celsius_value = self.to_celsius(value, from_u)

        if celsius_value < -273.15:
            messagebox.showerror(
                "Invalid Temperature", "This value is below absolute zero and is not physically valid."
            )
            return

        result = self.from_celsius(celsius_value, to_u)

        self.result_label.config(
            text=f"{value:g} °{self._symbol(from_u)}  =  {result:.2f} °{self._symbol(to_u)}"
        )

    @staticmethod
    def _symbol(unit):
        return {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"}[unit]


def main():
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()


if __name__ == "__main__":
    main()
