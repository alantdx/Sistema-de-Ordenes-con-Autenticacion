
# Usamos una imagen base de Node.js
FROM node:18-alpine

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todo el contenido del proyecto al contenedor
COPY . .

# Instalar las dependencias del proyecto
RUN npm install

# Construir la aplicación de React
RUN npm run build

# Exponer el puerto 3000 para que la app pueda ser accesible
EXPOSE 3000

# Ejecutar la aplicación de React en el contenedor
CMD ["npm", "start"]
