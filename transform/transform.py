import pandas as pd

def transform_date(df: pd.DataFrame) -> pd.DataFrame:
    # Concatenar mes nombre + año y parsear:
    df['date'] = pd.to_datetime(
        df['Reported Month'] + ' ' + df['Incident year'].astype(str),
        format='%B %Y',  # %B reconoce nombres completos de mes en inglés
        errors='coerce'  # convierte a NaT si algo falla
    )
    return df

def filter_years(df: pd.DataFrame, start: int, end: int) -> pd.DataFrame:
    """
    Filtra el DataFrame para que sólo contenga filas con Year entre start y end (inclusive).
    """
    return df[(df['Incident year'] >= start) & (df['Incident year'] <= end)]

def clean_cause_route(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rellena nulos en 'Cause of death' y 'Migration route' con 'Unknown'.
    """
    df = df.copy()  # rompo la vista
    df['Cause of Death'] = df['Cause of Death'].fillna('Unknown')
    df['Migration route'] = df['Migration route'].fillna('Unknown')
    return df

def analyze_cause_route(df: pd.DataFrame, cause: str, top_n: int = 5) -> pd.Series:
    """
    Para un valor dado de 'cause', cuenta las rutas más frecuentes en 'Migration route'.
    Devuelve una Series con índices = rutas y valores = conteos.
    """
    subset = df[df['Cause of Death'] == cause]
    return subset['Migration route'].value_counts().head(top_n)
