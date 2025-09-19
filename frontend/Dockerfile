FROM node:20-slim

WORKDIR /app

COPY package.json ./
RUN npm install --omit=dev --no-audit --no-fund

COPY app.js ./

EXPOSE 3000
ENV NODE_ENV=production
CMD ["npm", "start"]
