# Proyecto ETL Modular: Missing Migrants Dataset

Este repositorio implementa un pipeline ETL en **Python puro**, organizado en módulos `extract`, `transform` y `load`, junto a un script `main.py` que orquesta todo el proceso.

---

## 1. Estructura del proyecto

```
Trabajo_Practico_1/
├── data/
│   └── global-missing-migrants-dataset.csv   
├── extract/
│   ├── __init__.py
│   └── extract.py      # funciones de extracción
├── transform/
│   ├── __init__.py
│   └── transform.py    # funciones de transformación
├── load/
│   ├── __init__.py
│   └── load.py         # funciones de carga y generación de gráficos
└── main.py            # orquestador del pipeline
```

---

## 2. Dependencias

* pandas
* matplotlib

Instalación con pip:

```bash
pip install pandas matplotlib
```

O con conda:

```bash
conda install pandas matplotlib
```

---

## 3. Flujo ETL y responsabilidades de cada módulo

1. **Extracción** (`extract/extract.py`)

   * Lectura del CSV original mediante `extract_data(filepath)`.
   * Devuelve un DataFrame con los datos crudos.

2. **Transformación** (`transform/transform.py`)

   * **`transform_date`**: combina las columnas `Reported Month` y `Incident year` en un campo `datetime64`.
   * **`filter_years`**: selecciona un rango de años.
   * **`clean_cause_route`**: imputa valores faltantes en `Cause of Death` y `Migration route`.
   * **`analyze_cause_route`**: genera conteos de rutas por causa de muerte.

3. **Carga** (`load/load.py`)

   * **`plot_incidents_by_month`**: gráfico de incidentes por mes, guardado en PNG.
   * **`plot_cause_route`**: gráfico de rutas según causa, guardado en PNG.

4. **Orquestación** (`main.py`)

   * Llama en orden a extracción → transformación → carga.
   * Genera gráficos en `outputs/` y muestra un mensaje al finalizar.

---

## 4. Ejecución del pipeline

Desde la raíz del proyecto:

```bash
python main.py
```

Los resultados (PNG) se almacenarán en la carpeta `outputs/`.

---

## 5. Buenas prácticas y extensiones sugeridas

Más allá del flujo básico, un pipeline ETL robusto puede incluir:

* **Control de calidad de datos**: informe de nulos, duplicados, rango de valores, detección de outliers.
* **Configuración parametrizable**: leer rutas, filtros de años o causas desde un archivo `config.yaml` o argumentos CLI.
* **Carga avanzada**: exportar tablas agregadas a CSV/Parquet o insertar en una base de datos SQL.
* **Carga incremental**: procesar solo registros nuevos en cada ejecución, manteniendo un log de fechas.
* **Orquestación**: integrar en Airflow, cron jobs o sistemas de scheduling.
* **Testing y CI/CD**: pruebas unitarias con `pytest` para cada módulo y pipeline en GitHub Actions.
* **Logging y métricas**: uso de la librería `logging` para registrar volúmenes y tiempos de ejecución.

Con estas prácticas, el pipeline será más **mantenible**, **testeable** y **escalable**.
