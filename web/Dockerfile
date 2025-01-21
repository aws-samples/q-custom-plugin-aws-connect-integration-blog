# Stage 1: Build the Angular app
FROM --platform=linux/amd64 public.ecr.aws/docker/library/node:18 as build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Serve the app with Nginx
FROM --platform=linux/amd64 public.ecr.aws/nginx/nginx:alpine
COPY --from=build /app/dist/banking-website /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY src/assets/env.template.js /usr/share/nginx/html/assets/env.template.js
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
EXPOSE 80
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
