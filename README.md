# CleverRespond - AI-Powered Email Management System

<div align="center">

![Django](https://img.shields.io/badge/Django-5.1.4-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/AI-LangChain-FF6B6B?style=for-the-badge&logo=openai&logoColor=white)
![Gmail API](https://img.shields.io/badge/Gmail-API-EA4335?style=for-the-badge&logo=gmail&logoColor=white)

**An intelligent email management platform that leverages AI to analyze, understand, and automatically generate contextual email responses.**

[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

</div>

---

## Overview

**CleverRespond** is a cutting-edge Django web application that revolutionizes email management through artificial intelligence. By integrating Gmail API, sentiment analysis, and advanced language models, it provides intelligent email analysis and automated response generation, significantly improving productivity and communication efficiency.

### Key Features

- **AI-Powered Email Analysis**: Advanced sentiment analysis using TextBlob and Google Translate
- **Gmail Integration**: Seamless OAuth2 authentication with Gmail API
- **Intelligent Reply Generation**: Context-aware responses using Llama 3.2 language model
- **Real-time Sentiment Detection**: Automatic emotion analysis with visual indicators
- **Modern UI/UX**: Responsive Bootstrap-based interface with professional design
- **Secure Authentication**: Google OAuth2 implementation for safe access
- **Mobile-Responsive**: Optimized for all device sizes

---

## Technology Stack

### Backend Technologies
- **Django 5.1.4** - Modern Python web framework
- **LangChain** - AI/ML orchestration framework
- **Ollama** - Local LLM integration (Llama 3.2:1b)
- **Google API Client** - Gmail API integration
- **TextBlob** - Natural language processing
- **Deep Translator** - Multi-language support

### Frontend Technologies
- **Bootstrap 5** - Responsive UI framework
- **Font Awesome** - Professional iconography
- **Custom CSS/JavaScript** - Enhanced user experience
- **AJAX** - Dynamic content loading

### AI/ML Components
- **Sentiment Analysis**: TextBlob + Google Translate
- **Language Model**: Llama 3.2 (1B parameters)
- **Natural Language Processing**: Advanced text analysis
- **Multi-language Support**: Automatic translation

---

## Architecture

```
CleverRespond/
├── Email_Bot/                    # Django project root
│   ├── mail_app/                 # Main application
│   │   ├── views.py              # Business logic & API endpoints
│   │   ├── models.py             # Data models
│   │   ├── gmail_api.py          # Gmail API integration
│   │   ├── email_generator.py    # AI response generation
│   │   ├── sentiment_analysis.py # Sentiment analysis
│   │   └── templates/            # HTML templates
│   ├── static/                   # CSS, JS, assets
│   └── settings.py               # Django configuration
├── requirements.txt              # Dependencies
└── README.md                     # Documentation
```

---

## Quick Start

### Prerequisites
- Python 3.10+
- Gmail account with API access
- Ollama installed locally

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mertcaliskan34/CleverRespond.git
   cd CleverRespond
   ```

2. **Create virtual environment**
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
   ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Gmail API credentials**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project and enable Gmail API
   - Download credentials.json and place in project root

5. **Install and configure Ollama**
   ```bash
   # Install Ollama
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Pull Llama model
   ollama pull llama3.2:1b
   ```

6. **Run database migrations**
    ```bash
    python manage.py migrate
    ```

7. **Start the development server**
    ```bash
    python manage.py runserver
    ```

8. **Access the application**
   - Open http://127.0.0.1:8000 in your browser
   - Click "Gmail ile Giriş Yap" to authenticate
   - Start managing your emails intelligently!

---

## Core Functionality

### Email Management
- **Inbox Integration**: Direct access to Gmail inbox
- **Email Parsing**: Automatic extraction of sender, subject, content
- **Status Tracking**: Read/unread status management
- **Pagination**: Efficient handling of large email volumes

### AI-Powered Features
- **Sentiment Analysis**: 
  - Very Happy - Polarity > 0.30
  - Happy - Polarity > 0.10
  - Neutral - Polarity -0.10 to 0.10
  - Angry - Polarity < -0.10
  - Very Angry - Polarity < -0.30

- **Intelligent Reply Generation**:
  - Context-aware responses
  - Tone adaptation based on sentiment
  - Multi-language support
  - Professional formatting

### Technical Implementation

#### Gmail API Integration
```python
# Secure OAuth2 authentication
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send'
]
```

#### AI Response Generation
```python
# LangChain + Ollama integration
model = OllamaLLM(model="llama3.2:1b")
chain = prompt | model
result = chain.invoke({"email": email_text, "sentiment_score": sentiment_score})
```

#### Sentiment Analysis Pipeline
```python
# Multi-language sentiment analysis
translated_text = GoogleTranslator(source='auto', target='en').translate(email_text)
analysis = TextBlob(translated_text)
polarity = analysis.sentiment.polarity
```

---

## Performance & Scalability

- **Efficient API Usage**: Optimized Gmail API calls with pagination
- **Local AI Processing**: Ollama integration for privacy and speed
- **Caching Strategy**: Token-based authentication caching
- **Database Optimization**: SQLite for development, PostgreSQL ready
- **Responsive Design**: Mobile-first approach

---

## Security Features

- **OAuth2 Authentication**: Secure Google account integration
- **Token Management**: Automatic refresh and secure storage
- **CSRF Protection**: Django's built-in security measures
- **Input Validation**: Comprehensive data sanitization
- **Error Handling**: Graceful error management

---

## User Interface

### Modern Design Elements
- **Professional Color Scheme**: Slate theme with Bootstrap 5
- **Intuitive Navigation**: Clean, user-friendly interface
- **Real-time Feedback**: Dynamic status updates and notifications
- **Responsive Layout**: Optimized for desktop, tablet, and mobile
- **Accessibility**: WCAG compliant design patterns

### Key UI Components
- **Dashboard**: Overview of email statistics and sentiment
- **Inbox View**: Tabular email listing with status indicators
- **Email Details**: Comprehensive email viewer with metadata
- **Reply Interface**: AI-powered response generation and editing
- **Authentication**: Seamless Google OAuth integration

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Google** for Gmail API and OAuth2
- **LangChain** for AI orchestration framework
- **Ollama** for local LLM capabilities
- **Django** for the robust web framework
- **Bootstrap** for the responsive UI components

---

<div align="center">

**Star this repository if you found it helpful!**

Made with love by Mert Çalışkan

</div>
