const http = require("http");
const app = require("./src/app");
require('dotenv').config()

const port = process.env.PORT || process.env.SERVER_PORT;

const server = http.createServer(app);

server.listen(port);
console.log('server ok')



// TESTE DE SERVIDOR BASICO PARA VER SE ESTÁ RODANDO.
// const express = require('express')
// require('dotenv').config()

// const api = express();

// api.get('/', (rec, res) => {
//     res.send('Ola Mundo!')
// });
// api.listen(process.env.SERVER_PORT);
// console.log('server ok');