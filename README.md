# AI-Powered Gold Investment Assistant

## Project Description

This project creates a two-API backend system that emulates the Kuberai workflow for gold investment. It features an AI-powered conversational interface to interact with users, identify investment intent, and provide factual information, nudging them towards investment. Additionally, it includes a transactional API to execute digital gold purchases and record transactions.

## Technology Stack

*   **Programming Language:** Python 3.10+
*   **API Framework:** FastAPI
*   **AI / LLM Integration:** Google Gemini API (via `google-generativeai` library)
*   **Database:** SQLite with SQLAlchemy ORM
*   **Deployment Platform:** Render

## Local Development Setup

### 1. Prerequisites
- Python 3.10+
- An active Google Gemini API Key

### 2. Setup Instructions
1. **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd kuberai_assignment
    ```
2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *(On Windows, use `venv\Scripts\activate`)*
3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up your environment variables:**
    Create a file named `.env` in the root directory and add your Gemini API key:
    ```
    GEMINI_API_KEY="your_gemini_api_key"
    ```

### 3. Running the Application
1. **Start the FastAPI server:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`.
2. **Open the frontend:**
    Run the following command to open the frontend in your default browser:
    ```bash
    open frontend/index.html
    ```
    Or manually open the `frontend/index.html` file in your web browser to interact with the application.

### 4. Resetting the Database
To clear all data from the database, run the following command from the project root:
```bash
python app/clear_db.py
```

## Features
- Conversational AI assistant for gold investment queries
- Digital gold purchase simulation and transaction recording
- User purchase history view (frontend and API)
- Google Gemini LLM integration
- SQLite database with SQLAlchemy ORM
- Easy database reset for development

## API Endpoints

### API 1: Conversational

*   **Endpoint:** `POST /ask_kuberai`
*   **Description:** Analyzes a user's query about gold investment using an LLM. It provides a factual answer and nudges the user to invest if the intent is related to gold.
*   **Example Request (curl):**
    ```bash
    curl -X POST "YOUR_RENDER_URL/ask_kuberai" \
    -H "Content-Type: application/json" \
    -d '{"user_id": 1, "query": "Is now a good time to invest in gold?"}'
    ```

### API 2: Transactional

*   **Endpoint:** `POST /purchase_gold`
*   **Description:** Simulates the purchase of digital gold, records the transaction in the database, and returns a success confirmation.
*   **Example Request (curl):**
    ```bash
    curl -X POST "YOUR_RENDER_URL/purchase_gold" \
    -H "Content-Type: application/json" \
    -d '{"user_id": 1, "amount_inr": 10.0}'
    ```

### GET `/history/{user_id}`
- **Description:** Returns the user's gold purchase history
- **Response:** List of transactions with date, amount, and gold grams

## Deployment

The entire system is designed for deployment on Render. Ensure your `GEMINI_API_KEY` is set as a secret environment variable on the Render platform.
