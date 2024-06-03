# AI Joke Generator

## Introduction

This project creates humorous jokes based on news article content using Amazon Bedrock's `titan-text-express-v1` model. The application is built with Streamlit and allows users to input news articles, generate jokes, and provide feedback. Additionally, it supports fine-tuning the model with custom data stored in AWS S3.

## Requirements

- Python 3.12.3
- pip 24.0
- AWS credentials configured for `boto3`

## Installation

### Install the required packages: pip install -r requirements.txt

### o run the Streamlit application, use the following command: streamlit run app.py


## Project Structure

- app.py: Main application file that runs the Streamlit app, handling user inputs, generating jokes, and saving feedback.

- Streamlit.py: Main file to create the front end of project.

- responses.json: Stores user inputs, generated jokes, and feedback in a structured JSON format for later use or analysis.

- s3_creation.py: Contains the function to upload files to AWS S3 and generate S3 URIs for storing fine-tuning data.

- fine_tunnig.py: Fine tunned the model from the feedback data stored in json file.   







🚀 Excited to Share My Latest Project! 🚀

I’m thrilled to announce the completion of my latest project - A GenAI app that transforms standard news headlines into humorous ones! 📰😂

Here’s a sneak peek into what I’ve built:

✨ Generate Joke Headlines: The app takes everyday news articles and turns them into witty, humorous headlines.

✨ Model Training & Improvement: Leveraging user interactions, I’ve developed a feedback loop that collects data on user reactions to the generated jokes. This data is then used to fine-tune the model, continuously improving the quality of the humor.

Tech Stack & Tools:

AWS Bedrock: Powered by the Amazon Titan Express model, providing robust and scalable machine learning capabilities.
LangChain: Used for seamless integration and efficient API calls to Bedrock.
Prompt Templates: Custom templates for API interactions, ensuring precise and contextually accurate joke generation.

Check the code on github 

#GeeksVisor #TeamGeeksVisor #AI #MachineLearning #GenAI #AWS #Bedrock #LangChain #Innovation #Tech #HumorInTech #JokeGeneration #ContinuousLearning #UserFeedback #LinkedIn