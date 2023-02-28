# Use the official Node.js image as the base image
FROM node:19-bullseye-slim

# Set the working directory to /app
WORKDIR /frontend

# Copy the project files to the container
COPY . .

# Install dependencies
RUN npm install

# Build the application
RUN npm run build

# Start the application
CMD [ "npm", "run", "serve" ]
