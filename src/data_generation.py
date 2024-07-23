import numpy as np
import pandas as pd

def classify_residues(residue):
    if residue < 33.33:
        return 0  # Bajo
    elif residue < 66.66:
        return 1  # Medio
    else:
        return 2  # Alto

def generate_random_data(num_samples):
    residues = np.random.uniform(0, 100, num_samples)  # Cantidad de residuos en %
    data = {
        'residuos': residues,
        'dia_semana': np.random.choice(range(1, 8), num_samples),  # Día de la semana (1-7)
        'hora': np.random.choice(range(0, 24), num_samples),  # Hora del día (0-23)
        'temperatura': np.random.uniform(15, 35, num_samples),  # Temperatura en grados Celsius
        'latitud': np.random.uniform(-0.5, 0.5, num_samples) + -0.4667,  # Latitud aproximada de Francisco de Orellana
        'longitud': np.random.uniform(-0.5, 0.5, num_samples) + -76.9867,  # Longitud aproximada de Francisco de Orellana
        'nivel_residuos': [classify_residues(r) for r in residues]  # Nivel de residuos
    }
    return pd.DataFrame(data)
