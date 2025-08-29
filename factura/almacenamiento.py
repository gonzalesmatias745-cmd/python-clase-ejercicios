import json
import os
from typing import List, Dict, Any

ARCHIVO_INVENTARIO = os.path.join(os.path.dirname(__file__), "inventario.txt")
ARCHIVO_FACTURAS = os.path.join(os.path.dirname(__file__), "facturas.txt")

def _asegurar_archivo(ruta: str) -> None:
    if not os.path.exists(ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            pass

def leer_jsonl(ruta: str) -> List[Dict[str, Any]]:
    _asegurar_archivo(ruta)
    filas = []
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            try:
                filas.append(json.loads(linea))
            except json.JSONDecodeError:
                continue
    return filas

def escribir_jsonl(ruta: str, filas: List[Dict[str, Any]]) -> None:
    _asegurar_archivo(ruta)
    with open(ruta, "w", encoding="utf-8") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

def agregar_jsonl(ruta: str, fila: Dict[str, Any]) -> None:
    _asegurar_archivo(ruta)
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(json.dumps(fila, ensure_ascii=False) + "\n")
