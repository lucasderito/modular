from extract.extract import extract_data
from transform.transform import transform_date, filter_years, clean_cause_route, analyze_cause_route
from load.load import plot_incidents_by_month, plot_cause_route

def main():
    # 1) Extracción
    df_raw = extract_data('data/global-missing-migrants-dataset.csv')

    # 2) Transformaciones
    df = transform_date(df_raw)
    df = filter_years(df, 2014, 2020)      # ejemplo: años 2014–2020
    df = clean_cause_route(df)

    # 3) Reporte / Gráficos
    plot_incidents_by_month(df, 'outputs/incidents_by_month.png')

    # Análisis de causas y rutas
    cause = 'Violence'  # ejemplo de causa
    counts = analyze_cause_route(df, cause)
    plot_cause_route(counts, cause, f'outputs/routes_{cause.lower()}.png')

    print("ETL completado. Gráficos guardados en carpeta outputs/")

if __name__ == '__main__':
    main()
