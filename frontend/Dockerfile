FROM node:20 as build

WORKDIR /app

COPY package*.json ./
COPY . .

RUN npm install
RUN npm run build

RUN mkdir -p /app/public && echo "Placeholder for public folder" > /app/public/index.html

FROM nginx:alpine

COPY --from=build /app/.next /usr/share/nginx/html/.next

COPY --from=build /app/public /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
