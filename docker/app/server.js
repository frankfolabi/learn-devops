const express = require('express');
const app = express();
const PORT = 3000;

const quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. - William James",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Dream big and dare to fail. - Norman Vaughan",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Quality means doing it right when no one is looking. - Henry Ford",
    "Perseverance is not a long race; it is many short races one after the other. - Walter Elliot"
];

// Middleware to serve static files
app.use(express.static('public'));

// Route to get a random quote
app.get('/quote', (req, res) => {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    const quote = quotes[randomIndex];
    res.send(`
        <html>
        <head>
            <title>Inspirational Quote</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(to right, #4facfe, #00f2fe);
                    color: white;
                    text-align: center;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .quote-box {
                    background: rgba(255, 255, 255, 0.2);
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                    max-width: 600px;
                }
                h1 {
                    font-size: 2em;
                }
                p {
                    font-size: 1.5em;
                }
                a {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background: white;
                    color: #4facfe;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                }
                a:hover {
                    background: #00f2fe;
                    color: white;
                }
            </style>
        </head>
        <body>
            <div class="quote-box">
                <h1>Inspirational Quote</h1>
                <p>"${quote}"</p>
                <a href="/quote">Get Another Quote</a>
            </div>
        </body>
        </html>
    `);
});

// Home route
app.get('/', (req, res) => {
    res.send(`
        <html>
        <head>
            <title>Inspirational Quotes</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(to right, #ff7e5f, #feb47b);
                    color: white;
                    text-align: center;
                    padding: 50px;
                }
                .container {
                    max-width: 600px;
                    margin: auto;
                    background: rgba(255, 255, 255, 0.2);
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    font-size: 2.5em;
                }
                p {
                    font-size: 1.5em;
                }
                a {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background: white;
                    color: #ff7e5f;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                }
                a:hover {
                    background: #feb47b;
                    color: white;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to the Inspirational Quotes App</h1>
                <p>Get a daily dose of inspiration!</p>
                <a href="/quote">Get a Random Quote</a>
            </div>
        </body>
        </html>
    `);
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server is running on http://0.0.0.0:${PORT}`);
});

