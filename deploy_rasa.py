#!/usr/bin/env python
"""
Deploy Rasa - Helper script for deploying the Kurdish Chatbot Rasa model

This script helps prepare and deploy the Rasa model to various cloud providers.
It creates the necessary configuration files and provides guidance on deployment steps.
"""

import os
import sys
import argparse
import shutil
import json
from pathlib import Path


def setup_parser():
    """Set up command line argument parser"""
    parser = argparse.ArgumentParser(
        description="Helper script for deploying Kurdish Chatbot Rasa model"
    )
    parser.add_argument(
        "provider",
        choices=["heroku", "render", "railway"],
        help="Cloud provider to deploy to",
    )
    parser.add_argument(
        "--app-name",
        default="kurdish-chatbot",
        help="Application name (used for Heroku and cloud providers)",
    )
    parser.add_argument(
        "--pack-model",
        action="store_true",
        help="Pack the latest model for deployment",
    )
    return parser


def ensure_requirements():
    """Ensure requirements.txt file is properly configured"""
    print("Checking requirements.txt...")
    
    required_packages = [
        "rasa==3.6.21",
        "SQLAlchemy<2.0.0",
        "requests==2.32.3",
        "pytz==2022.7.1",
        "pyyaml==6.0.2",
        "typing-extensions==4.13.0"
    ]
    
    with open("requirements.txt", "r") as f:
        current_requirements = f.read().splitlines()
    
    # Check if all required packages are in requirements.txt
    missing_packages = [pkg for pkg in required_packages if pkg not in current_requirements]
    
    if missing_packages:
        print("Adding missing packages to requirements.txt...")
        with open("requirements.txt", "a") as f:
            for pkg in missing_packages:
                f.write(f"{pkg}\n")
                print(f"  Added {pkg}")
    else:
        print("Requirements file looks good.")


def configure_heroku(app_name):
    """Configure files for Heroku deployment"""
    print(f"Configuring for Heroku deployment with app name: {app_name}")
    
    # Create or update Procfile
    with open("Procfile", "w") as f:
        f.write("web: python -m rasa run --enable-api --cors \"*\" --port $PORT\n")
        f.write("worker: python -m rasa run actions\n")
    print("Created Procfile")
    
    # Create runtime.txt
    with open("runtime.txt", "w") as f:
        f.write("python-3.9.11\n")
    print("Created runtime.txt")
    
    # Create app.json for Heroku
    app_json = {
        "name": app_name,
        "description": "Kurdish Chatbot built with Rasa",
        "repository": "https://github.com/enki-somer/kurdish",
        "keywords": ["rasa", "chatbot", "kurdish"],
        "env": {
            "RASA_X_PASSWORD": {
                "description": "Password for Rasa X (if used)",
                "generator": "secret"
            }
        },
        "buildpacks": [
            {
                "url": "heroku/python"
            }
        ]
    }
    
    with open("app.json", "w") as f:
        json.dump(app_json, f, indent=2)
    print("Created app.json")
    
    print("\nHeroku Deployment Instructions:")
    print("1. Install the Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli")
    print("2. Login to Heroku CLI: heroku login")
    print(f"3. Create a new Heroku app: heroku create {app_name}")
    print("4. Push to Heroku: git push heroku main")
    print("5. Scale the worker dyno: heroku ps:scale worker=1")
    print("6. Open the app: heroku open")


def configure_render(app_name):
    """Configure files for Render.com deployment"""
    print(f"Configuring for Render.com deployment with service name: {app_name}")
    
    # Create render.yaml
    render_yaml = f"""
services:
  # Rasa Server
  - type: web
    name: {app_name}
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python -m rasa run --enable-api --cors "*" --port $PORT
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.11

  # Action Server
  - type: web
    name: {app_name}-actions
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python -m rasa run actions
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.11
"""
    
    with open("render.yaml", "w") as f:
        f.write(render_yaml)
    print("Created render.yaml")
    
    print("\nRender.com Deployment Instructions:")
    print("1. Create a Render.com account: https://render.com")
    print("2. From the Render dashboard, click 'New' and select 'Blueprint'")
    print("3. Connect your GitHub repository")
    print("4. Render will use the render.yaml file to set up your services")
    print("5. Click 'Apply' to deploy both services")


def configure_railway(app_name):
    """Configure files for Railway.app deployment"""
    print(f"Configuring for Railway.app deployment with app name: {app_name}")
    
    # Create railway.json
    railway_json = {
        "build": {
            "builder": "NIXPACKS"
        },
        "deploy": {
            "startCommand": "python -m rasa run --enable-api --cors \"*\" --port $PORT",
            "restartPolicyType": "ON_FAILURE",
            "restartPolicyMaxRetries": 3
        }
    }
    
    with open("railway.json", "w") as f:
        json.dump(railway_json, f, indent=2)
    print("Created railway.json")
    
    # Create actions-railway.json for the actions server
    actions_railway_json = {
        "build": {
            "builder": "NIXPACKS"
        },
        "deploy": {
            "startCommand": "python -m rasa run actions",
            "restartPolicyType": "ON_FAILURE",
            "restartPolicyMaxRetries": 3
        }
    }
    
    # Create actions directory if it doesn't exist
    os.makedirs("railway", exist_ok=True)
    
    with open("railway/actions.json", "w") as f:
        json.dump(actions_railway_json, f, indent=2)
    print("Created railway/actions.json")
    
    print("\nRailway.app Deployment Instructions:")
    print("1. Install the Railway CLI: npm i -g @railway/cli")
    print("2. Login to Railway: railway login")
    print("3. Initialize your project: railway init")
    print("4. Deploy your project: railway up")
    print("5. For the actions server, create a separate service and use the railway/actions.json configuration")


def pack_model():
    """Pack the latest model for deployment"""
    print("Packing the latest model for deployment...")
    
    # Find the latest model
    models_dir = Path("models")
    if not models_dir.exists() or not models_dir.is_dir():
        print("Error: models directory not found. Have you trained a model?")
        return False
    
    model_files = list(models_dir.glob("*.tar.gz"))
    if not model_files:
        print("Error: No model files found in the models directory.")
        return False
    
    # Get the latest model file
    latest_model = max(model_files, key=lambda x: x.stat().st_mtime)
    print(f"Latest model: {latest_model}")
    
    # Create a copy with a fixed name for easier deployment
    fixed_name = models_dir / "model.tar.gz"
    shutil.copy2(latest_model, fixed_name)
    print(f"Created deployment model at: {fixed_name}")
    
    return True


def main():
    """Main function"""
    parser = setup_parser()
    args = parser.parse_args()
    
    # Ensure we're in the root directory of the project
    if not os.path.exists("domain.yml") or not os.path.exists("config.yml"):
        print("Error: This script must be run from the root directory of the Kurdish Chatbot project.")
        sys.exit(1)
    
    # Check requirements.txt
    ensure_requirements()
    
    # Pack model if requested
    if args.pack_model and not pack_model():
        print("Warning: Failed to pack model. Continuing with configuration...")
    
    # Configure for the selected provider
    if args.provider == "heroku":
        configure_heroku(args.app_name)
    elif args.provider == "render":
        configure_render(args.app_name)
    elif args.provider == "railway":
        configure_railway(args.app_name)
    
    print("\nConfiguration complete. Follow the instructions above to deploy your Rasa chatbot.")
    print("Once deployed, copy the webhook URL and use it to connect to the chatbot from the GitHub Pages interface.")
    print("Example webhook URL: https://your-app-name.herokuapp.com/webhooks/rest/webhook")


if __name__ == "__main__":
    main() 