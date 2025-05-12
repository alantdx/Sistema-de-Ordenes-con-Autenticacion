```markdown
# Sistema de Órdenes con Autenticación (Microservicios + React + Docker)

Este proyecto es una aplicación full stack basada en microservicios. Incluye:

- Un **frontend en React** que consume servicios.
- Un **servicio de órdenes** (`orders-service`) en Node.js.
- Un **servicio de autenticación** (`auth-service`) en Node.js.
- Dos bases de datos **PostgreSQL** separadas para cada microservicio.
- Orquestado con **Docker Compose**.

---

## Estructura del Proyecto

```
.
├── auth-service/
│   ├── Dockerfile
│   ├── index.js
│   └── ...
├── orders-service/
│   ├── Dockerfile
│   ├── index.js
│   └── ...
├── frontend/
│   ├── Dockerfile
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.js
│   │   ├── index.css
│   │   └── reportWebVitals.js
│   └── package.json
├── docker-compose.yml
└── README.md
```

---

## ¿Cómo levantar el proyecto?

### 1. Clona el repositorio

```bash
git clone <URL-del-repositorio>
cd <nombre-del-proyecto>
```

### 2. Construye y levanta los contenedores

```bash
docker-compose up --build
```

Esto creará y levantará:

- Base de datos de autenticación (`db_auth`)
- Base de datos de órdenes (`db_orders`)
- Microservicio de autenticación (`auth-service`)
- Microservicio de órdenes (`orders-service`)
- Interfaz de usuario (`frontend`)

---

##  Acceso a la aplicación

Una vez que todo esté corriendo correctamente, abre tu navegador en:

```
http://localhost:3000
```

Desde allí podrás ver la interfaz que consume las órdenes.

---

## Datos de prueba

Puedes insertar datos manualmente en la base de datos de órdenes o modificar el archivo `orders-service/index.js` para agregar datos temporales al arrancar el servicio.

Ejemplo de orden en el backend (`orders-service/index.js`):

```js
orders = [
  { id: 1, item: 'Laptop', quantity: 2 },
  { id: 2, item: 'Mouse', quantity: 10 }
];
```

---

## 🛠 Tecnologías

- **Frontend**: React + Axios
- **Backend**: Node.js (Express)
- **DB**: PostgreSQL
- **Orquestación**: Docker & Docker Compose
- **Autenticación**: JWT (en desarrollo)

---

## Notas

- El servicio de autenticación y la validación JWT aún se pueden expandir para proteger rutas específicas.
- Asegúrate de no tener conflictos de puertos locales (`3000`, `8000`, `8001`, `5433`, `5434`).
- Si algo falla, puedes reiniciar con:

```bash
docker-compose down -v
docker-compose up --build
```

---
