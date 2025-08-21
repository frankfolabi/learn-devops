# This Dockerfile is using multistage build to reduce the container image
# This is the build stage
FROM node:22 AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json/
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# This is to reduce the image size
FROM node:alpine AS main

# SE the working directory
WORKDIR /app

# Copy application files
COPY --from=build /app .

# Expose port 3000
EXPOSE 3000

# Start the application
CMD ["node", "server.js"]

