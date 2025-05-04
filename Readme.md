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

## 4. Ventajas de la modularización

* **Mantenibilidad**: cada módulo cumple una única responsabilidad, lo que facilita la lectura, el refactorizado y la incorporación de cambios futuros.
* **Reutilización y pruebas**: las funciones y clases en cada módulo pueden probarse de forma aislada (tests unitarios) y reutilizarse en otros proyectos o notebooks sin copiar código.
* **Colaboración**: varios desarrolladores pueden trabajar simultáneamente en distintos módulos (extract, transform, load) sin interferencias.
* **Claridad de responsabilidades**: la separación en módulos deja explícito qué parte del pipeline se encarga de cada fase ETL.
* **Automatización y orquestación**: es más sencillo integrar el pipeline en herramientas de scheduling (cron, Airflow, GitHub Actions) y notificar al terminar.
* **Escalabilidad**: nuevos pasos o variantes del proceso (por ejemplo, otra fuente de datos o destino) pueden añadirse creando o extendiendo módulos sin afectar al resto del código.

---

## 5. Ejecución del pipeline

Desde la raíz del proyecto:

```bash
python main.py
```

Los resultados (PNG) se almacenarán en la carpeta `outputs/`.

---

## 6. Buenas prácticas y extensiones sugeridas

Más allá del flujo básico, un pipeline ETL robusto puede incluir:

* **Control de calidad de datos**: informe de nulos, duplicados, rango de valores, detección de outliers.
* **Configuración parametrizable**: leer rutas, filtros de años o causas desde un archivo `config.yaml` o argumentos CLI.
* **Carga avanzada**: exportar tablas agregadas a CSV/Parquet o insertar en una base de datos SQL.
* **Carga incremental**: procesar solo registros nuevos en cada ejecución, manteniendo un log de fechas.
* **Orquestación**: integrar en Airflow, cron jobs o sistemas de scheduling.
* **Testing y CI/CD**: pruebas unitarias con `pytest` para cada módulo y pipeline en GitHub Actions.
* **Logging y métricas**: uso de la librería `logging` para registrar volúmenes y tiempos de ejecución.

Con estas prácticas, el pipeline será más **mantenible**, **testeable** y **escalable**.

---

## 7. ¿Por qué modularizar?

* **Facilita pruebas unitarias**: puedo probar `transform_date` aislada, sin levantar todo el pipeline.
* **Reutilización**: extracción o carga pueden usarse en otros proyectos sin copiar código.
* **Claridad de responsabilidades**: cada archivo hace sólo una cosa.
* **Ventajas del pipeline “puro”**:

  * Se puede versionar con Git como un proyecto Python normal.
  * Ejecutable desde consola (`python main.py`), fácil de automatizar (cron, Airflow).

---

## 8. Ideas para profundizar en ETL

* **Profundizar la calidad de datos**

  * Regla de negocio: descartar eventos con fechas inválidas (`date.isna()`).
  * Chequeos de consistencia: validar meses en 1–12 y que `Incident year` no sea futuro.
  * Generar informe de calidad automático: conteo de nulos, duplicados y rangos de valores.

* **Parámetros y configuración**

  * Leer rutas, filtros de años o causas desde `config.yaml` o argumentos CLI.
  * Permite usar el mismo pipeline con diferentes parámetros sin cambiar el código.

* **Carga avanzada**

  * Exportar tablas agregadas a CSV/Parquet o insertar en base de datos SQL.
  * Generar un dashboard interactivo (por ejemplo, HTML con Bokeh o Streamlit).

* **Incremental load**

  * Registrar hasta qué fecha se procesó en un log o tabla.
  * Leer solo registros nuevos en ejecuciones posteriores para acelerar el proceso.

* **Orquestación y scheduling**

  * Integrar `main.py` en un DAG de Apache Airflow o con cron jobs.
  * Añadir notificaciones al terminar o en caso de errores (correo/Slack).

* **Testing y CI/CD**

  * Escribir tests unitarios con `pytest` para cada módulo.
  * Configurar un pipeline en GitHub Actions para validar cambios automáticamente.

* **Logging y métricas**

  * Usar la librería `logging` para registrar cuántos registros entran y salen de cada fase.
  * Exponer métricas de tiempo de ejecución y errores en un panel de control.
