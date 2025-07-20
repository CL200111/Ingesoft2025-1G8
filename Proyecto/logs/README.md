# 📝 Carpeta de Logs

Este directorio contiene los resultados generados por las herramientas de análisis y pruebas estáticas del proyecto.

Cada archivo en esta carpeta documenta el resultado de una herramienta específica que se ejecuta como parte del proceso de revisión del código fuente.

## Archivos Generados

- `ruff.log`: Salida del análisis de estilo y errores con [Ruff](https://docs.astral.sh/ruff/). Revisa convenciones de estilo, errores comunes y problemas de calidad del código.
- `mypy.log`: Resultados del chequeo de tipos estáticos con [Mypy](http://mypy-lang.org/). Ayuda a detectar errores de tipo antes de ejecutar el código.
- `bandit.log`: Reporte de análisis de seguridad con [Bandit](https://bandit.readthedocs.io/). Identifica patrones inseguros de programación en el código Python.
- `coverage_run.log`: Salida de la ejecución de pruebas automáticas usando `unittest` bajo cobertura.
- `coverage_report.log`: Resumen de cobertura de pruebas, indicando qué partes del código fueron ejecutadas durante las pruebas.

## Propósito

El objetivo de esta carpeta es centralizar los resultados de validación del proyecto. Puedes revisar los archivos `.log` después de ejecutar los scripts de análisis (`run_linters.sh`) para verificar la calidad, seguridad y correctitud del código.

## Notas

- Los archivos `.log` se sobrescriben en cada ejecución del script.
- Es buena práctica revisar estos archivos antes de hacer un commit o push al repositorio.

---
