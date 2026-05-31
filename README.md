# AI Assistant API

A powerful AI-powered code assistant and task automation API built with FastAPI, LangChain, and OpenAI. Integrate it with Telegram for seamless automation!

## Features

- 🤖 **Code Generation** - Write code from natural language descriptions
- 📖 **Code Explanation** - Understand how code works
- ♻️ **Code Refactoring** - Improve code quality and readability
- 🐛 **Debug Assistance** - Get help fixing errors
- ⚙️ **Task Automation** - Automate repetitive tasks
- 💬 **General Chat** - Conversational AI assistance
- 📱 **Telegram Integration** - Receive responses via Telegram
- 🔐 **API Key Security** - Secure all endpoints with authentication

## Quick Start

### 1. Prerequisites

- Python 3.8+
- OpenAI API Key (get it from https://platform.openai.com/api-keys)
- Telegram Bot Token (optional, for Telegram integration)
- Git

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/N4T1V3B34ST/N4t1v3b34stz.git
cd N4t1v3b34stz

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your credentials
nano .env  # or use your favorite editor
```

Required environment variables:

```
OPENAI_API_KEY=your_openai_api_key_here
API_KEY=your_secret_api_key_for_requests

# Optional - for Telegram integration
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

### 4. Run the Server

```bash
python main.py
```

The API will be available at `http://localhost:8000`

Access the interactive API documentation at `http://localhost:8000/docs`

## API Endpoints

All endpoints require the `X-API-Key` header with your configured API key.

### Health Check
```bash
GET /health
```

### Generate Code
```bash
POST /generate-code
Content-Type: application/json
X-API-Key: your_api_key

{
    "prompt": "Write a Python function to calculate factorial"
}
```

### Explain Code
```bash
POST /explain-code
Content-Type: application/json
X-API-Key: your_api_key

{
    "code": "def factorial(n):\n    return 1 if n <= 1 else n * factorial(n-1)"
}
```

### Refactor Code
```bash
POST /refactor-code
Content-Type: application/json
X-API-Key: your_api_key

{
    "code": "x = [1,2,3,4,5]\ny = []\nfor i in x:\n    y.append(i*2)",
    "requirements": "Make it more pythonic"
}
```

### Debug Code
```bash
POST /debug-code
Content-Type: application/json
X-API-Key: your_api_key

{
    "code": "x = int('abc')",
    "error_message": "ValueError: invalid literal for int() with base 10: 'abc'"
}
```

### Automate Task
```bash
POST /automate-task
Content-Type: application/json
X-API-Key: your_api_key

{
    "task_description": "I need to convert all PNG images in a folder to JPG format"
}
```

### Chat
```bash
POST /chat
Content-Type: application/json
X-API-Key: your_api_key

{
    "message": "How do I handle exceptions in Python?"
}
```

## Usage Examples

### Using cURL

```bash
# Generate code
curl -X POST http://localhost:8000/generate-code \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your_api_key" \
  -d '{
    "prompt": "Write a function to check if a number is prime"
  }'

# Explain code
curl -X POST http://localhost:8000/explain-code \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your_api_key" \
  -d '{
    "code": "def is_prime(n):\n    if n < 2: return False\n    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))"
  }'
```

### Using Python

```python
import requests

API_URL = "http://localhost:8000"
API_KEY = "your_api_key"
HEADERS = {"X-API-Key": API_KEY}

# Generate code
response = requests.post(
    f"{API_URL}/generate-code",
    json={"prompt": "Write a function to reverse a string"},
    headers=HEADERS
)
print(response.json()["result"])

# Chat
response = requests.post(
    f"{API_URL}/chat",
    json={"message": "What is REST API?"},
    headers=HEADERS
)
print(response.json()["result"])
```

### Using JavaScript/Node.js

```javascript
const API_URL = "http://localhost:8000";
const API_KEY = "your_api_key";

async function generateCode(prompt) {
    const response = await fetch(`${API_URL}/generate-code`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-API-Key": API_KEY
        },
        body: JSON.stringify({ prompt })
    });
    const data = await response.json();
    return data.result;
}

// Usage
generatCode("Write a function to calculate Fibonacci").then(console.log);
```

## Telegram Integration

To enable Telegram notifications:

1. **Create a Telegram Bot:**
   - Chat with [@BotFather](https://t.me/botfather) on Telegram
   - Create a new bot and get your token

2. **Get Your Chat ID:**
   - Start a chat with your bot
   - Visit `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`
   - Find your chat ID in the response

3. **Configure Environment:**
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   TELEGRAM_CHAT_ID=your_chat_id_here
   ```

4. **Responses will automatically be sent to Telegram!**

## Deployment

### Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

Build and run:
```bash
docker build -t ai-assistant .
docker run -p 8000:8000 --env-file .env ai-assistant
```

### Environment Variables for Production

```
OPENAI_API_KEY=production_key
API_KEY=secure_random_key
API_HOST=0.0.0.0
API_PORT=8000
MODEL_NAME=gpt-4
TEMPERATURE=0.7
MAX_TOKENS=2000
TELEGRAM_BOT_TOKEN=optional_token
TELEGRAM_CHAT_ID=optional_chat_id
```

## Architecture

```
┌─────────────────────┐
│   Client/Telegram   │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│   FastAPI Server    │
│   (main.py)         │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│  LangChain + OpenAI │
│ (ai_assistant.py)   │
└─────────────────────┘
           │
┌──────────▼──────────┐
│   Telegram Bot      │
│(telegram_handler.py)│
└─────────────────────┘
```

## Configuration Options

Edit `config.py` or `.env` to customize:

- **MODEL_NAME** - Change AI model (gpt-3.5-turbo, gpt-4, etc.)
- **TEMPERATURE** - Creativity level (0-1, higher = more creative)
- **MAX_TOKENS** - Maximum response length
- **API_PORT** - Server port (default: 8000)

## Troubleshooting

### "Invalid API key" Error
- Check your OpenAI API key is correct
- Ensure it's set in `.env` file
- Verify it's not expired

### "Module not found" Error
- Ensure you activated the virtual environment
- Run `pip install -r requirements.txt`

### Telegram not sending messages
- Check TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are set
- Verify bot token is valid
- Ensure you've sent at least one message to the bot

### Slow responses
- Consider using gpt-3.5-turbo instead of gpt-4
- Reduce MAX_TOKENS
- Check your internet connection

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please open an issue on GitHub.

---

**Happy Coding! 🚀**

Made with ❤️ by N4T1V3B34ST