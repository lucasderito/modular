import os
import matplotlib.pyplot as plt
from pandas import Series

def _ensure_dir(path: str):
    "Crea directorio padre si no existe."
    os.makedirs(os.path.dirname(path), exist_ok=True)

def plot_incidents_by_month(df, output_path: str):
    """
    Grafica la frecuencia de incidentes por mes (usando df['date']).
    Guarda el PNG en output_path.
    """
    _ensure_dir(output_path)
    counts = df['date'].dt.month.value_counts().sort_index()
    fig, ax = plt.subplots()
    counts.plot(kind='bar', ax=ax)
    ax.set_title('Incidentes por mes (basado en date)')
    ax.set_xlabel('Mes')
    ax.set_ylabel('Cantidad')
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)

def plot_cause_route(counts: Series, cause: str, output_path: str):
    """
    Recibe una Series de conteos por ruta (índices = rutas, valores = conteos)
    y grafica un bar chart, guardándolo en output_path.
    """
    _ensure_dir(output_path)
    fig, ax = plt.subplots()
    counts.plot(kind='bar', ax=ax)
    ax.set_title(f'Rutas (cause="{cause}")')
    ax.set_xlabel('Ruta')
    ax.set_ylabel('Cantidad de incidentes')
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)

