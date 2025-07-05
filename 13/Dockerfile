FROM node:18-alpine

WORKDIR /app

RUN apk add --no-cache git && \
    git clone https://github.com/eMahtab/node-express-hello-world . && \
    npm install

EXPOSE 3000

CMD ["npm", "start"]