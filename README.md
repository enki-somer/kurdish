# Kurdish Chatbot with Rasa

A conversational AI chatbot built with Rasa that speaks Kurdish, collects user information (name, phone, address), and stores it in a JSON file.

## Features

- 🗣️ Replies instantly to customers in Kurdish
- 📝 Collects user name, phone number, and address
- 💾 Stores collected information in a JSON file
- 🌐 Can be deployed on GitHub Pages for public access
- 🧠 Natural language understanding for flexible user inputs

## Project Structure

```
.
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

### Deploying to GitHub Pages

1. Create a new GitHub repository.
2. Push your code to the repository.
3. Enable GitHub Pages in your repository settings.
4. Set the source to the main branch and the root folder.

For the web interface to communicate with your Rasa server, you'll need to deploy the Rasa API server to a hosting service like Heroku, Render, or Railway.

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
