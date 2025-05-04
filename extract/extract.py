import pandas as pd

def extract_data(filepath: str) -> pd.DataFrame:
    """
    Lee el dataset de missing-migrants desde un CSV y devuelve un DataFrame.
    """
    df = pd.read_csv(filepath, low_memory=False)
    return df
