# CleverRespond: AI-Powered Email Automation

## Overview

CleverRespond is an intelligent email automation tool designed to streamline email management and response generation. By leveraging the power of AI, CleverRespond analyzes incoming emails, understands their context and sentiment, and generates appropriate responses, saving you time and improving customer satisfaction.

## Key Features

-   **Intelligent Email Analysis:** Automatically reads and analyzes incoming emails from Gmail.
-   **Sentiment Analysis:** Detects the emotional tone of emails (positive, negative, neutral) to tailor responses accordingly.
-   **AI-Powered Response Generation:** Generates contextually relevant and personalized email replies using the Llama 3 NLP model.
-   **Fast Reply Interface:** Provides a quick interface for generating replies without requiring Gmail login.
-   **Gmail Integration:** Seamlessly integrates with Gmail via the Gmail API for secure and efficient email handling.
-   **Email Listing and Details:** Lists recent emails with key details and allows users to view full email content.
-   **Automated Email Sending:** Sends generated replies directly through the Gmail API.

## Technologies Used

-   **Backend:**
    -   Django Framework
    -   Python
    -   Gmail API
    -   Langchain
    -   Ollama
    -   TextBlob
    -   Deep Translator
-   **Frontend:**
    -   HTML
    -   CSS
    -   Bootstrap
    -   JavaScript

## Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone [repository URL]
    cd CleverRespond
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    -   **On Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

    -   **On macOS and Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up Gmail API credentials:**

    -   Follow the instructions in the Gmail API documentation to create a project and download your `credentials.json` file.
    -   Place the `credentials.json` file in the root directory of the project.

6.  **Run migrations:**

    ```bash
    python manage.py migrate
    ```

7.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

8.  **Access the application in your browser:**

    Open your web browser and navigate to `http://localhost:8000`.

## Usage

1.  **Gmail Authentication:**
    -   On the home page, click the "Gmail ile Giriş Yap" button to authenticate with your Google account.
2.  **Inbox:**
    -   After successful authentication, navigate to the "Gelen Kutusu" to view your emails.
3.  **Email Details:**
    -   Click on "Detaylar" to view the full content and details of an email.
4.  **Generate Reply:**
    -   Click on "Yanıt Oluştur" to generate an AI-powered reply for the email.
5.  **Fast Reply:**
    -   Use the "Hızlı Yanıt Oluştur" feature to generate replies without authenticating with Gmail.
6.  **Send Reply:**
    -   Review the generated reply and click "Yanıtı Gönder" to send the email.

## Acknowledgements

-   This project uses the Llama 3 NLP model developed by Meta.
-   Uses Bootswatch Slate theme for styling.
-   Utilizes Font Awesome for icons.