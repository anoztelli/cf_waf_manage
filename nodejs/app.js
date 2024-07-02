const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('public'));
app.use(express.static('public/tr'));

app.listen(port, () => {
    console.log(`Node.js app listening at http://localhost:${port}`);
});
