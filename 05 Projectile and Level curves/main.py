import tkinter as tk


WINDOW_BG = "#b7eeee"
TEXT = "#111111"


def launch_simulation(root):
    """Close the launcher and open the projectile-motion dashboard."""
    root.destroy()

    import matplotlib.pyplot as plt
    import plotting

    plt.show()


def main():
    root = tk.Tk()
    root.title("Projectile Motion")
    root.geometry("560x360")
    root.configure(bg=WINDOW_BG)
    root.resizable(False, False)

    frame = tk.Frame(root, bg=WINDOW_BG)
    frame.pack(expand=True, fill="both", padx=40, pady=35)

    tk.Label(
        frame,
        text="PROJECTILE MOTION",
        font=("Segoe UI", 22, "bold"),
        fg=TEXT,
        bg=WINDOW_BG,
    ).pack(pady=(20, 8))

    tk.Label(
        frame,
        text="A computational exploration of projectile motion",
        font=("Segoe UI", 10),
        fg=TEXT,
        bg=WINDOW_BG,
    ).pack(pady=(0, 30))

    tk.Button(
        frame,
        text="Launch Simulation",
        command=lambda: launch_simulation(root),
        font=("Segoe UI", 11, "bold"),
        width=20,
        padx=10,
        pady=8,
        cursor="hand2",
    ).pack(pady=8)

    tk.Button(
        frame,
        text="Exit",
        command=root.destroy,
        font=("Segoe UI", 10),
        width=20,
        padx=10,
        pady=6,
        cursor="hand2",
    ).pack(pady=4)

    tk.Label(
        frame,
        text="Numerical analysis • Energy • Momentum • Contour maps",
        font=("Segoe UI", 8),
        fg=TEXT,
        bg=WINDOW_BG,
    ).pack(side="bottom", pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
