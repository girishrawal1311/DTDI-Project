const express = require('express');
const path = require('path');
const app = express();

// Serve static files from frontend directory
app.use(express.static(path.join(__dirname, 'frontend')));

// Route all requests to index.html (for single-page app)
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'frontend', 'index.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Frontend server running on port ${PORT}`);
});
