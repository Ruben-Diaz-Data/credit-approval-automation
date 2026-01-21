# Credit Approval Automation

Este proyecto simula un **sistema de aprobación de crédito** para una fintech de crédito al consumo.  
El objetivo es demostrar un flujo end-to-end de recepción de solicitudes, evaluación mediante reglas y automatización de decisiones mediante una API.

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd credit-approval-automation

2. Crear un entorno virtual
bash
Copiar código
python -m venv venv

3. Activar el entorno virtual
Windows
source venv/bin/activate

4. Instalar dependencias
pip install -r requirements.tx

5. Ejecutar la aplicación
uvicorn app.main:app --reload

📄 Documentación interactiva (Swagger)
Una vez levantado el servidor, puedes acceder a la documentación de la API en:
arduino
Copiar código
http://127.0.0.1:8000/docs
