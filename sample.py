import tkinter as tk
from tkinter import messagebox


# Logic Functions
def generate_stacks(n, fake_stack_index):
    stacks = []
    for i in range(n):
        if i == fake_stack_index:
            stacks.append([11] * n)
        else:
            stacks.append([10] * n)
    return stacks


def brute_force_find_fake_stack(stacks):
    for i, stack in enumerate(stacks):
        weight = sum(stack)
        if weight != len(stack) * 10:
            return i + 1  # 1-based indexing
    return -1


def optimal_find_fake_stack(stacks):
    total_weight = 0
    n = len(stacks)
    for i in range(n):
        total_weight += stacks[i][0] * (i + 1)

    expected_weight = 10 * (n * (n + 1)) // 2
    diff = total_weight - expected_weight

    return diff  # This directly gives the fake stack number


# GUI Code
class FakeCoinDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fake Coin Detector")

        self.stacks = []
        self.n = 0
        self.fake_index = -1

        # Title
        title_label = tk.Label(root, text="Fake Coin Detector", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # Inputs
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Number of Stacks (n):").grid(row=0, column=0, padx=5, pady=5)
        self.n_entry = tk.Entry(input_frame, width=10)
        self.n_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Fake Stack Index (1 to n):").grid(row=1, column=0, padx=5, pady=5)
        self.fake_index_entry = tk.Entry(input_frame, width=10)
        self.fake_index_entry.grid(row=1, column=1)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Generate Stacks", command=self.generate_stacks_gui).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Brute Force Detect", command=self.run_brute_force).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Optimal Detect", command=self.run_optimal).grid(row=0, column=2, padx=10)

        # Output
        self.output_text = tk.Text(root, height=10, width=60, font=("Courier", 10))
        self.output_text.pack(pady=10)

    def generate_stacks_gui(self):
        try:
            self.n = int(self.n_entry.get())
            self.fake_index = int(self.fake_index_entry.get()) - 1

            if self.n <= 0:
                raise ValueError("Number of stacks must be positive.")
            if not (0 <= self.fake_index < self.n):
                raise ValueError("Fake stack index out of range.")

            self.stacks = generate_stacks(self.n, self.fake_index)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"✅ Stacks generated with {self.n} stacks.\n")
            self.output_text.insert(tk.END, f"💡 Fake Stack: {self.fake_index + 1}\n")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def run_brute_force(self):
        if not self.stacks:
            messagebox.showwarning("Warning", "Please generate stacks first.")
            return
        result = brute_force_find_fake_stack(self.stacks)
        self.output_text.insert(tk.END, f"\n🔎 Brute Force Result: Stack {result}\n")

    def run_optimal(self):
        if not self.stacks:
            messagebox.showwarning("Warning", "Please generate stacks first.")
            return
        result = optimal_find_fake_stack(self.stacks)
        self.output_text.insert(tk.END, f"\n⚡ Optimal Result: Stack {result}\n")


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FakeCoinDetectorApp(root)
    root.mainloop()
