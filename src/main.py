from models.population_models import (
    MalthusModel,
    DiscreteModel,
    LogisticModel,
    DelayedLogisticModel
)
from views.main_window import MainWindow


def main():
    models = [
        MalthusModel(),
        DiscreteModel(),
        LogisticModel(),
        DelayedLogisticModel()
    ]

    app = MainWindow(models)
    app.mainloop()


if __name__ == "__main__":
    main()