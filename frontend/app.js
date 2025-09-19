const express = require('express');
const axios = require('axios');
const app = express();

const BACKEND_URL = process.env.BACKEND_URL || 'http://backend:5000';

app.get('/', async (req, res) => {
  try {
    const response = await axios.get(`${BACKEND_URL}/api/users`);
    const users = response.data;
    let html = '<h1>User List</h1><ul>';
    users.forEach(user => {
      html += `<li>${user.name} (ID: ${user.id})</li>`;
    });
    html += '</ul>';
    res.send(html);
  } catch (error) {
    res.status(500).send('Error fetching users from backend.');
  }
});

const port = process.env.PORT || 3000;
app.listen(port, '0.0.0.0', () => {
  console.log(`Frontend listening on port ${port}`);
});
