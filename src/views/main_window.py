import customtkinter as ctk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class MainWindow(ctk.CTk):
    def __init__(self, models):
        super().__init__()
        self.models = models
        self.current_model = None
        self.parameter_entries = {}

        self.title("Modelos Poblacionales")
        self.geometry("1100x700")
        self.configure_layout()
        self.set_theme()

        self.create_widgets()
        self.update_model_options()

    def configure_layout(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    @staticmethod
    def set_theme():
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("dark-blue")

    def create_widgets(self):
        control_frame = ctk.CTkFrame(self, width=300, corner_radius=0)
        control_frame.grid(row=0, column=0, sticky="nsew")

        self.model_selector = ctk.CTkComboBox(
            control_frame,
            values=[],
            state="readonly",
            command=self.on_model_selected
        )
        self.model_selector.pack(pady=15, padx=20, fill="x")

        self.parameters_frame = ctk.CTkScrollableFrame(
            control_frame,
            height=400,
            label_text="Parámetros del Modelo"
        )
        self.parameters_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.btn_plot = ctk.CTkButton(
            control_frame,
            text="Generar Gráfico",
            command=self.on_plot
        )
        self.btn_plot.pack(pady=15, padx=20, fill="x")

        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.setup_initial_plot()

        self.canvas_frame = ctk.CTkFrame(self, corner_radius=0)
        self.canvas_frame.grid(row=0, column=1, sticky="nsew")

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=20)

    def setup_initial_plot(self):
        self.ax.set_title("Seleccione un modelo")
        self.ax.text(
            0.5, 0.5,
            "Seleccione un modelo y configure los parámetros",
            ha='center', va='center', fontsize=12
        )
        self.ax.axis('off')

    def update_model_options(self):
        model_names = [model.get_name() for model in self.models]
        self.model_selector.configure(values=model_names)
        if model_names:
            self.model_selector.set(model_names[0])
            self.on_model_selected()

    def on_model_selected(self, event=None):
        model_name = self.model_selector.get()
        self.current_model = next(m for m in self.models if m.get_name() == model_name)

        # Clean Parameters
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()
        self.parameter_entries.clear()

        # Create new input fields
        for param, default in self.current_model.get_parameters():
            self.create_parameter_input(param, default)

    def create_parameter_input(self, param, default):
        frame = ctk.CTkFrame(self.parameters_frame)
        frame.pack(fill="x", pady=3, padx=5)

        label = ctk.CTkLabel(frame, text=f"{param}:", width=120)
        label.pack(side="left", padx=(0, 10))

        entry = ctk.CTkEntry(frame)
        entry.insert(0, str(default))
        entry.pack(side="right", fill="x", expand=True)
        self.parameter_entries[param] = entry

    def get_parameters(self):
        params = {}
        for param, entry in self.parameter_entries.items():
            try:
                params[param] = float(entry.get())
            except ValueError:
                return None
        return params

    def on_plot(self):
        if not self.current_model:
            return

        params = self.get_parameters()
        if not self.current_model.validate_parameters(params):
            return

        self.generate_plot(params)



    def generate_plot(self, params):

        self.ax.clear()
        self.ax.grid(True, linestyle='--', alpha=0.7)

        if self.current_model.is_discrete():
            time_values = np.linspace(0, params['time'])
            p = self.current_model.calculate(params, time_values)
            self.plot_discrete(time_values, p)
        else:
            time_values = np.linspace(0, params['time'], 1000)
            p = self.current_model.calculate(params, time_values)
            self.plot_continuous(time_values, p)

        self.ax.set_title(self.current_model.get_name(), fontsize=14)
        self.ax.set_xlabel('Tiempo', fontsize=12)
        self.ax.set_ylabel('Población', fontsize=12)
        self.canvas.draw()

    def plot_continuous(self, time_values, p):
        self.ax.plot(time_values, p, linewidth=2.5)

    def plot_discrete(self, time_values, p):
        self.ax.scatter(time_values, p)