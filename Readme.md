# 🧠 Prospección de Datos Abiertos – Ayuntamiento de Arganda del Rey

Este proyecto automatiza la recopilación de datos abiertos (Contratos Menores) del Ayuntamiento de Arganda del Rey.  
Detecta nuevos registros y envía un correo con las novedades usando la API de Gmail (en formato HTML).

---

## 🚀 Cómo usarlo en Google Colab

1. Abre el notebook `notebooks/Prospeccion_Arganda.ipynb` en Google Colab.
2. Sube tu archivo `client_secret.json` (credenciales OAuth 2.0 de Gmail).
3. Modifica:
   - `DEST_EMAIL` → tu correo.
   - `URL_CSV` → dataset deseado.
4. Ejecuta todas las celdas.
5. Si hay registros nuevos, recibirás un correo HTML con el resumen.

---

## 🧱 Estructura del proyecto

prospect-arganda/
├── notebooks/
│ └── Prospeccion_Arganda.ipynb
├── utils/
│ └── email_utils.py
├── requirements.txt
├── README.md
└── .gitignore
