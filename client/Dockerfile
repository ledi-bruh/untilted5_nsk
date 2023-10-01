FROM node:12-alpine as build
WORKDIR /client
COPY package.json /client/package.json
RUN npm install --only=prod
RUN npm install @mui/material @emotion/react @emotion/styled
COPY . /client
RUN npm run build
FROM nginx:1.16.0-alpine
COPY --from=build /client/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
