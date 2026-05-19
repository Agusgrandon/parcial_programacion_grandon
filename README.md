# 🔐 Sistema de Procesamiento de Contraseñas

Proyecto realizado en Python para el análisis y validación de contraseñas utilizando estructuras condicionales, estructuras repetitivas, funciones y validaciones manuales.

---

# 📌 Descripción

Este programa permite ingresar una contraseña y realizar distintos análisis sobre ella, tales como:

* Validar el nivel de seguridad.
* Contar tipos de caracteres.
* Buscar caracteres específicos.
* Invertir la contraseña.
* Generar reportes estadísticos.
* Verificar si es palíndromo.
* Ordenar caracteres manualmente.

---

# 🛠 Tecnologías utilizadas

* Python 3

---

# 📂 Estructura del proyecto

```bash
📦 parcial_programacion_uno
 ┣ 📜 main.py
 ┣ 📜 validaciones.py
 ┣ 📜 analisis.py
 ┣ 📜 estadisticas.py
 ┣ 📜 utilidades.py
 ┗ 📜 README.md
```

---

# ⚙️ Funcionalidades

## 1️⃣ Ingresar contraseña

Validaciones implementadas:

* La contraseña no puede estar vacía.
* Debe tener al menos 8 caracteres.
* No puede comenzar con espacios.
* Debe contener al menos una letra.

---

## 2️⃣ Validar nivel de seguridad

Clasificación de contraseñas:

### 🔴 Débil

* Entre 8 y 9 caracteres.
* Solo letras.

### 🟡 Media

* Contiene letras y números.

### 🟢 Fuerte

* Contiene:

  * letras,
  * números,
  * símbolos especiales,
  * y al menos 12 caracteres.

---

## 3️⃣ Contar tipos de caracteres

El programa informa:

* Cantidad de letras.
* Cantidad de números.
* Cantidad de caracteres especiales.
* Cantidad de espacios.

---

## 4️⃣ Buscar carácter específico

Permite:

* Buscar un carácter ingresado por el usuario.
* Mostrar cuántas veces aparece.
* Mostrar las posiciones donde se encuentra.

---

## 5️⃣ Mostrar contraseña invertida

Invierte manualmente la contraseña recorriendo la cadena desde el final hacia el inicio.

---

## 6️⃣ Generar reporte estadístico

El sistema muestra:

* Longitud total.
* Porcentaje de letras.
* Porcentaje de números.
* Porcentaje de símbolos.
* Caracteres repetidos consecutivamente.

---

## 7️⃣ Verificar si es palíndromo

Determina si la contraseña se lee igual de izquierda a derecha y viceversa.

---

## 8️⃣ Ordenar caracteres de la contraseña

Ordenamiento utilizando algoritmo Bubble Sort.

Opciones:

* Orden ascendente.
* Orden descendente.

---

# 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/Agusgrandon/parcial_programacion_grandon.git
```

2. Ejecutar el archivo principal:

```bash
python main.py
```

---

# ✨ Autor

Proyecto desarrollado por agus :)

---


