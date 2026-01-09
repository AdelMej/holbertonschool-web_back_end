const express = require('express');
const router = require('./routes');

const app = express();
const PORT = 1245;

app.use('/', router);

app.listen(PORT);

export default app;
