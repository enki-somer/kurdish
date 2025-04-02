
const express = require('express');
const cors = require('cors');
const { spawn } = require('child_process');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Serve the Rasa endpoint
app.post('/webhooks/rest/webhook', async (req, res) => {
  // Process the request using the Rasa model
  // This is a simplified version for demonstration
  const message = req.body.message;
  const sender = req.body.sender;
  
  // TODO: Process with Rasa model
  // For now, return a simple response
  res.json([
    {
      "recipient_id": sender,
      "text": "Hello! This is a test response. How can I help you?"
    }
  ]);
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
