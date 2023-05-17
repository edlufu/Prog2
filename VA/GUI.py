"""  VA

Student: Edvin Lundberg
Mail: edvin.lundberg@gmail.com
Reviewed by: Sven-Erik Ekström
Date reviewed: 16/05
"""

import tkinter as tk
from box import Box


class App:
    def __init__(self):
        # creates root window
        self.window = tk.Tk()
        self.window.title("Bouncy Balls Battle Royal")
        self.window.resizable(width=False, height=False)

        # creates entry panel
        W = 200

        panel = tk.Frame(
            self.window,
            width=W,
        )
        panel.pack(fill=tk.Y, side=tk.RIGHT)
        panel.columnconfigure(0, minsize=W)
        panel.rowconfigure([0, 1, 2, 3], minsize=60)

        # Creates title for entry panel
        title_frame = tk.Frame(panel, relief=tk.RIDGE, borderwidth=5)
        tk.Label(
            title_frame,
            text="CONTROLL PANEL",
            font=("Arial", 18, "bold"),
            background="white",
        ).pack()
        title_frame.grid(column=0, row=0)

        # Creates entry for quantity(n) and velocity(v)
        n_label = tk.Label(panel, text="Quantity:")
        default_n = tk.StringVar(value="60")
        self.n_entry = tk.Entry(panel, textvariable=default_n, width=5)

        n_label.grid(column=0, row=1, sticky="w", padx=40)
        self.n_entry.grid(column=0, row=1, sticky="e", padx=40)

        v_label = tk.Label(panel, text="Velocity:")
        default_v = tk.StringVar(value="10")
        self.v_entry = tk.Entry(panel, textvariable=default_v, width=5)

        v_label.grid(column=0, row=2, sticky="w", padx=40)
        self.v_entry.grid(column=0, row=2, sticky="e", padx=40)

        # creates buttons for start and stop of animation
        self.btn_start = tk.Button(
            panel, text="Start", relief=tk.RAISED, command=self.start
        )
        self.btn_start.grid(column=0, row=3, sticky="n")
        self.btn_stop = tk.Button(
            panel, text="Stop", relief=tk.RAISED, command=self.stop
        )
        self.btn_stop.grid(column=0, row=3, sticky="s")

        # creates button to exit application
        panel.rowconfigure([4], minsize=450)
        self.btn_exit = tk.Button(
            panel,
            text="Exit",
            relief=tk.RAISED,
            command=self.exit,
            foreground="red",
        )
        self.btn_exit.grid(column=0, row=4, sticky="s")

        # creates emptry box (canvas object)
        self.box = Box(self.window)

    def run_simulation(self):
        """Runs animation eventloop"""
        st = self.box

        if st.last_ball():
            # shows hidden winner message and runs special winner movement
            st.canvas.itemconfig(st.announcement, state=tk.NORMAL)
            st.victory_lap()
        else:
            st.move_all()

        # loops movement with mainloop @ about 24fps
        self.window.after(40, self.run_simulation)

    def start(self):
        """sets box and runs animation"""
        self.btn_start.config(state="disabled")

        n = int(self.n_entry.get())
        v = float(self.v_entry.get())
        self.box.set_box(n, v)

        self.window.after(0, self.run_simulation)

    def stop(self):
        """clears box and so also stops animation,
        resets start button"""
        self.box.clear_box()
        self.btn_start.config(state="normal")

    def exit(self):
        """Exits application"""
        self.window.destroy()


if __name__ == "__main__":
    app = App()
    app.window.mainloop()
