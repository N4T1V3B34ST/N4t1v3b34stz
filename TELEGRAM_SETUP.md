# Telegram Bot Setup Guide

## ⚡ Quick Start (5 Minutes)

### Step 1: Create a Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send: `/newbot`
3. Choose a name: `My AI Assistant`
4. Choose username: `my_ai_assistant_bot` (must end with `bot`)
5. BotFather gives you a **TOKEN**:
   ```
   123456789:ABCdefGHIjklmnoPQRstuvWXYZabcdefghi
   ```

📌 **Save this token!**

---

### Step 2: Get Your Chat ID

1. Send any message to your bot in Telegram
2. Visit: `https://api.telegram.org/bot<TOKEN>/getUpdates`
3. Find your chat ID in the response:
   ```json
   {"chat": {"id": 123456789}}  ← YOUR CHAT ID
   ```

📌 **Save this chat ID!**

---

### Step 3: Update `.env` File

```bash
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklmnoPQRstuvWXYZabcdefghi
TELEGRAM_CHAT_ID=123456789
```

---

### Step 4: Run the System

**Option A: Two Terminals**

Terminal 1:
```bash
python main.py
```

Terminal 2:
```bash
python telegram_bot.py
```

**Option B: Docker Compose (Easiest)**

```bash
docker-compose up
```

---

### Step 5: Test Your Bot!

In Telegram, send to your bot:

```
/start          → Welcome message
/help           → Show all commands
/generate Write a sorting function  → Bot generates code
/chat What are design patterns?    → Bot answers
```

---

## 📖 All Commands

| Command | Usage |
|---------|-------|
| `/generate <prompt>` | Generate code |
| `/explain <code>` | Explain code |
| `/refactor <code>` | Improve code |
| `/debug <code> Error: <error>` | Fix errors |
| `/automate <task>` | Create automation |
| `/chat <message>` | Chat with AI |
| `/help` | Show commands |
| `/start` | Welcome |

---

## 🚀 Production Deployment

### Using Docker Compose

```bash
cp .env.example .env
nano .env  # Add your keys
docker-compose up -d
docker-compose logs -f
```

### Using PM2

```bash
npm install -g pm2
pm2 start main.py --name api
pm2 start telegram_bot.py --name bot
pm2 save
pm2 startup
```

---

## ❌ Troubleshooting

**Bot doesn't respond:**
```bash
# Check API
curl http://localhost:8000/health

# Check .env
cat .env | grep TELEGRAM
```

**Invalid token:**
- Get new token from @BotFather
- Update .env
- Restart

**API errors:**
- Verify OPENAI_API_KEY is valid
- Check API_KEY matches in code
- Ensure main.py is running first

---

## 🏗️ Architecture

```
Telegram User → Bot (telegram_bot.py) → API (main.py) → OpenAI
```

---

**That's it! Your bot is ready! 🎉**

For more: https://github.com/N4T1V3B34ST/N4t1v3b34stz
