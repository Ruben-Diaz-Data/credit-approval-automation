# Credit Application API – Prueba Técnica

Este proyecto es una API REST desarrollada con **FastAPI** que simula el flujo básico de evaluación de una solicitud de crédito, desde la captura de datos del solicitante hasta la decisión final (aprobado o rechazado).

El objetivo del proyecto es demostrar el diseño de endpoints, lógica de negocio básica y estructuración de un backend sencillo, enfocado en un caso realista del sector financiero.

---

## 📌 Flujo General del Sistema

1. Crear una solicitud de crédito.
2. Subir documentos asociados a la solicitud.
3. Obtener un score de crédito (simulado).
4. Evaluar la solicitud con base en reglas simples.
5. Obtener la decisión final de la solicitud.

---

## 🚀 Endpoints Disponibles

### 1️⃣ Crear solicitud de crédito
**POST** `/applications/`

Crea una nueva solicitud de crédito con los datos del solicitante.

Ejemplo de request:
```json
{
  "name": "Juan Pérez",
  "rfc": "JUAP800101XXX",
  "curp": "JUAP800101HDFXXX01",
  "age": 35,
  "monthly_income": 20000
}
