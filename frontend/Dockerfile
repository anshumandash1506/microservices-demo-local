# Use official Node.js slim image as base
FROM node:20-slim

# Set working directory inside the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install --omit=dev --no-audit --no-fund

# Copy application code
COPY app.js ./

# Expose port 3000 for Express
EXPOSE 3000

# Set environment variable for production-like config
ENV NODE_ENV=production

# Command to run the Express app
CMD ["npm", "start"]
