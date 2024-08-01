# Script de Renombrado de Archivos

Este proyecto es un script de Python diseñado para renombrar múltiples archivos en un directorio. Ofrece la posibilidad de añadir prefijos, sufijos y numeración a los nombres de los archivos.

## Tecnologías

- Python
- Módulos: `os`, `argparse`

## Descripción

El script permite renombrar archivos en masa utilizando diferentes opciones:

- **Prefijo**: Añade un texto al inicio del nombre de cada archivo.
- **Sufijo**: Añade un texto al final del nombre de cada archivo antes de la extensión.
- **Numeración**: Añade un número incremental al inicio del nombre de cada archivo.

## Instalación

Para utilizar este script, debes tener Python instalado en tu sistema.

1. Asegúrate de que las dependencias estén instaladas. Este script no tiene dependencias adicionales aparte de Python estándar.

## Uso

Ejecuta el script desde la línea de comandos proporcionándole los argumentos necesarios:

```bash
python r.py "ruta/del/directorio" [--prefijo PREFIJO] [--sufijo SUFIJO] [--numerar]
```

### Argumentos

- `ruta`: **(requerido)** Ruta al directorio que contiene los archivos que deseas renombrar.
- `--prefijo`: **(opcional)** Prefijo que deseas añadir a los archivos.
- `--sufijo`: **(opcional)** Sufijo que deseas añadir a los archivos.
- `--numerar`: **(opcional)** Si se proporciona, añade numeración a los archivos renombrados.

### Ejemplos

1. **Renombrar con prefijo**:

   ```bash
   python r.py "C:\mis\archivos" --prefijo "nuevo_"
   ```

2. **Renombrar con sufijo**:

   ```bash
   python r.py "C:\mis\archivos" --sufijo "_backup"
   ```

3. **Renombrar con numeración**:

   ```bash
   python r.py "C:\mis\archivos" --numerar
   ```

4. **Combinación de prefijo, sufijo, y numeración**:

   ```bash
   python r.py "C:\mis\archivos" --prefijo "nuevo_" --sufijo "_backup" --numerar
   ```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, crea un "fork" del repositorio, realiza tus cambios, y envía un "pull request".
