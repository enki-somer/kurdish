# Deploying Kurdish Chatbot on GitHub Pages

This guide provides step-by-step instructions for deploying the Kurdish chatbot to GitHub Pages and connecting it to a hosted Rasa backend.

## Overview of the Deployment Architecture

The deployment consists of two main components:

1. **Frontend**: The HTML/CSS/JavaScript web interface hosted on GitHub Pages
2. **Backend**: The Rasa server and action server running on a cloud provider

## Step 1: Prepare Your GitHub Repository

1. Create a new GitHub repository or use an existing one
2. Clone it to your local machine:
   ```bash
   git clone https://github.com/yourusername/kurdish-chatbot.git
   cd kurdish-chatbot
   ```
3. Copy all your project files to this directory
4. Make sure `index.html` is in the root directory of your repository

## Step 2: Deploy to GitHub Pages

1. Go to your GitHub repository
2. Click on "Settings"
3. Scroll down to the "GitHub Pages" section
4. Under "Source", select "main" branch and the root folder
5. Click "Save"
6. GitHub will provide you with a URL (e.g., `https://yourusername.github.io/kurdish-chatbot/`)

Your frontend is now deployed on GitHub Pages!

## Step 3: Deploy Rasa Server to a Cloud Provider

You'll need to host your Rasa server on a cloud platform. Here are three options:

### Option 1: Heroku

1. Create a Heroku account
2. Install the Heroku CLI
3. Create a `Procfile` in your project root:
   ```
   web: python -m rasa run --enable-api --cors "*" --port $PORT
   worker: python -m rasa run actions
   ```
4. Deploy to Heroku:
   ```bash
   heroku login
   heroku create kurdish-chatbot-backend
   git push heroku main
   ```

### Option 2: Render.com

1. Create a Render.com account
2. Create a new Web Service
3. Connect to your GitHub repository
4. Configure the service:
   - Build command: `pip install -U rasa`
   - Start command: `python -m rasa run --enable-api --cors "*" --port $PORT`
5. Create a second service for your action server:
   - Start command: `python -m rasa run actions`

### Option 3: Railway.app

1. Create a Railway.app account
2. Create a new project
3. Add a service from GitHub
4. Configure the service:
   - Build command: `pip install -U rasa`
   - Start command: `python -m rasa run --enable-api --cors "*" --port $PORT`
5. Create a second service for your action server

## Step 4: Connect Frontend to Backend

1. Open your deployed GitHub Pages site
2. In the connection configuration section, enter your Rasa server URL (the webhook endpoint)
   - Format: `https://your-rasa-server-url.com/webhooks/rest/webhook`
3. Click "Connect"
4. Test the chatbot by sending a message

## Troubleshooting

### Cross-Origin (CORS) Issues

If you're having CORS issues, make sure your Rasa server is configured to allow requests from your GitHub Pages domain:

```bash
rasa run --enable-api --cors "*" --port $PORT
```

Or for a specific origin:

```bash
rasa run --enable-api --cors "https://yourusername.github.io" --port $PORT
```

### Connection Problems

If the frontend can't connect to your Rasa server:

1. Check that your Rasa server is running
2. Verify the URL in the connection settings
3. Make sure your Rasa server is accessible from the public internet
4. Check for HTTPS requirements (GitHub Pages requires secure connections)

### Action Server Issues

If custom actions aren't working:

1. Verify your action server is running
2. Check the `endpoints.yml` file has the correct action server URL
3. Ensure the action server is accessible from your Rasa server

## Security Considerations

When deploying to production:

1. Set up proper authentication for your Rasa server
2. Consider using a CDN for your GitHub Pages site
3. Monitor your cloud resources for unusual traffic
4. Regularly update your Rasa and other dependencies

## Maintenance

To update your deployment:

1. Make changes to your local repository
2. Test locally
3. Push to GitHub:
   ```bash
   git add .
   git commit -m "Update chatbot"
   git push origin main
   ```
4. GitHub Pages will automatically update

For changes to the Rasa backend, redeploy to your cloud provider as needed.
