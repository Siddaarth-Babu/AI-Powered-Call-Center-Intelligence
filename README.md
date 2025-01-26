# AI-based Stock Market Investment Support Chatbot

## Overview

This project is an AI-powered chatbot designed to assist users in making informed decisions about their stock market investments. The chatbot leverages advanced technologies such as **Langchain**, **Memory**, **Prompts**, **Streamlit**, **Speech Recognition**, and **Text to Speech Synthesis** to provide a seamless and interactive experience.

### Technologies & Features:
- **Langchain**: A framework that allows you to build powerful language models with easy integration of external tools. It helps us provide more context-aware and dynamic responses.
- **Memory**: Used to store and recall relevant past interactions, making the chatbot more efficient and personalized.
- **Prompts**: We design carefully crafted prompts to guide the AI's responses to investment-related queries, making the chatbot more contextually aware.
- **Streamlit**: A Python framework used for creating interactive web applications. It provides an easy way to deploy the chatbot as a web app for users to interact with.
- **Speech Recognition**: Allows the chatbot to recognize and process spoken queries, enabling voice-based interactions.
- **Text to Speech Synthesis**: Converts the AI’s responses into speech, so users can listen to the chatbot’s advice.

## Features
- **Investment Queries**: The chatbot can answer a wide range of stock market-related questions, such as trends, tips, stock prices, and news.
- **Personalized Suggestions**: It uses memory to recall previous conversations and offer personalized investment recommendations.
- **Voice Interaction**: Through Speech Recognition and Text to Speech, users can interact with the chatbot via voice.
- **Live Stock Data**: Fetches real-time stock data and trends from external sources to provide up-to-date investment advice.
- **Interactive Dashboard**: Built with Streamlit, the chatbot is accessible via a clean, user-friendly interface.


## Installation & Requirements

### Environment Setup

1. **Clone the Repository**:

   To get started, clone the repository to your local machine:

   ```bash
   git clone https://github.com/Siddaarth-Babu/AI-Powered-Call-Center-Intelligence.git
   cd stock-market-chatbot
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory with the following content:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   LANGSMITH_TRACING_V2=true
   LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
   LANGCHAIN_API_KEY="your-api-key"
   LANGSMITH_API_KEY="your-api-key"
   ```
   Replace `your_google_api_key` and `your-api-key` with the appropriate keys.

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```


## Deployed Application
You can access the live version of the chatbot on the following URL:
[Bot4Stock](https:)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Enjoy coding 😊