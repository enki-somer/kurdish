# Kurdish Chatbot with Rasa

A conversational AI chatbot built with Rasa that speaks Kurdish, collects user information (name, phone, address), and stores it in a JSON file.

## Live Demo

🔗 **[Try the Kurdish Chatbot on GitHub Pages](https://enki-somer.github.io/kurdish/)**

_Note: You'll need to deploy a Rasa server separately and connect to it by entering the server URL in the interface._

## Features

- 🗣️ Replies instantly to customers in Kurdish
- 📝 Collects user name, phone number, and address
- 💾 Stores collected information in a JSON file
- 🌐 Can be deployed on GitHub Pages for public access
- 🧠 Natural language understanding for flexible user inputs
- 🚀 Automated deployment via GitHub Actions

## Project Structure

```
.
├── .github/                  # GitHub specific configurations
│   └── workflows/            # GitHub Actions workflows
│       └── deploy.yml        # Workflow for deploying to GitHub Pages
├── actions/                  # Custom actions for the chatbot
│   └── actions.py            # Action to store user data
├── data/                     # Training data for the chatbot
│   ├── nlu.yml               # Natural language understanding examples
│   ├── rules.yml             # Rules for specific conversation paths
│   └── stories.yml           # Conversation flow examples
├── models/                   # Trained model files (generated)
├── .venv/                    # Virtual environment (not included in repo)
├── config.yml                # NLU and policy configuration
├── credentials.yml           # Credentials for various channels
├── domain.yml                # Domain specification (intents, entities, slots, actions)
├── endpoints.yml             # Endpoints configuration
├── index.html                # Web interface for GitHub Pages deployment
├── GITHUB_PAGES_DEPLOYMENT.md# Detailed deployment guide
├── Procfile                  # Configuration for Heroku deployment
├── runtime.txt               # Python runtime for Heroku
├── README.md                 # This documentation
└── user_data.json            # Stored user data (generated)
```

## Installation & Setup

### Prerequisites

- Python 3.9.11 or higher
- pip (Python package manager)

### Installation Steps

1. Clone this repository:

```bash
git clone https://github.com/yourusername/kurdish-chatbot.git
cd kurdish-chatbot
```

2. Create and activate a virtual environment:

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

3. Install the dependencies:

```bash
pip install rasa
```

## Local Development and Testing

### Training the Model

```bash
rasa train
```

### Starting the Action Server

```bash
rasa run actions
```

### Running the Chatbot in Command Line

```bash
rasa shell
```

### Running the Rasa API Server

```bash
rasa run --enable-api --cors "*" --debug
```

## Deployment

### Deploying to GitHub Pages with GitHub Actions

This project includes a GitHub Actions workflow that automatically deploys the chatbot interface to GitHub Pages whenever changes are pushed to the main branch.

1. Fork or clone this repository
2. Push your changes to the main branch
3. GitHub Actions will automatically build and deploy the site
4. Visit your GitHub Pages URL (usually `https://[your-username].github.io/kurdish/`)

To view the deployment status, check the Actions tab in your repository.

### Connecting to a Rasa Backend

For the web interface to function, you need to connect it to a running Rasa server:

1. Deploy your Rasa backend to a cloud provider (Heroku, Render, Railway, etc.)
2. Ensure your server is configured with CORS enabled: `rasa run --enable-api --cors "*"`
3. On the chatbot interface, enter your server URL (e.g., `https://your-app.herokuapp.com/webhooks/rest/webhook`)
4. Click "Connect" to establish the connection

For detailed deployment instructions, see the [GitHub Pages Deployment Guide](GITHUB_PAGES_DEPLOYMENT.md).

### Alternative Deployment Options

If direct hosting on GitHub Pages is not meeting your needs, you can consider these alternatives:

1. **Heroku**: Deploy the entire Rasa application to Heroku
2. **Render**: A cloud provider that can host both the frontend and backend
3. **Railway**: Simple deployment platform for Rasa applications

### Updating the Web Interface

After deploying your Rasa server, update the `RASA_SERVER_URL` in `index.html` to your deployed server URL.

## Testing the Chatbot

You can test the chatbot via:

1. **Command line**: Run `rasa shell`
2. **Web browser**: Open the deployed GitHub Pages URL
3. **API testing tools**: Use tools like Postman to send requests to your Rasa API endpoint

## Sample Conversations

**Basic user data collection:**

```
Bot: سڵاو! بەخێربێی بۆ بۆتی پرسیار و وەڵام. ناوت چییە؟
User: ناوم ئاریە
Bot: زۆر سوپاس ئاری. ژمارەی تەلەفۆنەکەت چییە؟
User: ٠٧٥٠١٢٣٤٥٦٧
Bot: زۆر باشە. ئێستا ناونیشانەکەت بنووسە تکایە
User: گەڕەکی سەروەری، کۆڵانی ٤٥، خانووی ١٢، سلێمانی
Bot: زۆر سوپاس بۆ زانیارییەکانت! ئێمە هەموو شتێکمان تۆمار کرد. ناو: ئاری, ژمارەی تەلەفۆن: ٠٧٥٠١٢٣٤٥٦٧, ناونیشان: گەڕەکی سەروەری، کۆڵانی ٤٥، خانووی ١٢، سلێمانی
```

## Troubleshooting

### Common Issues and Solutions

1. **Rasa server not starting**

   - Check if the port is already in use
   - Ensure the virtual environment is activated
   - Verify you have the right Rasa version installed

2. **Custom actions not working**

   - Confirm the action server is running
   - Check the endpoints.yml file for the correct URL
   - Ensure the action name in domain.yml matches the name in actions.py

3. **Web interface not connecting to Rasa**

   - Verify the RASA_SERVER_URL in index.html
   - Check CORS settings in your Rasa run command
   - Ensure your browser allows cross-origin requests

4. **Entity recognition issues**
   - Add more training examples in nlu.yml
   - Ensure your entities are properly annotated
   - Retrain the model after making changes

### Getting Help

If you encounter issues not covered here, please:

1. Check the [Rasa documentation](https://rasa.com/docs/)
2. Look for similar issues on the [Rasa forum](https://forum.rasa.com/)
3. Open an issue in the project's GitHub repository

## Customization

### Adding New Intents and Responses

1. Add new intent examples in `data/nlu.yml`
2. Define the response in `domain.yml`
3. Update the conversation flow in `data/stories.yml`
4. Retrain the model with `rasa train`

### Changing Languages or Adding Multilingual Support

1. Update the training data with examples in your target language
2. Consider using language-specific models or tokenizers
3. Modify the responses in domain.yml to include the new language

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Rasa](https://rasa.com/) for the open-source conversational AI framework
- Contributors to the Kurdish language resources

---

Created with ❤️ for Kurdish speakers everywhere.

## Continuous Integration/Continuous Deployment

This project uses GitHub Actions for CI/CD, which automatically:

1. Deploys the web interface to GitHub Pages when you push to the main branch
2. Makes updates available immediately to end users

To customize the CI/CD pipeline, edit the workflow file in `.github/workflows/deploy.yml`.
