# Use the official Node.js image as the base image
FROM node:16.3.0-alpine3.11

# Set the working directory to /app
WORKDIR /frontend

# Copy the project files to the container
COPY . .

# Install dependencies
RUN npm install

# Build the application
RUN npm run build

# Expose port 3000
EXPOSE 5173

# Start the application
CMD [ "npm", "start" ]
