"""
FastAPI server for AI Assistant with Telegram integration
"""
from fastapi import FastAPI, HTTPException, Header, BackgroundTasks
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import asyncio
import logging
from ai_assistant import assistant
from config import config
from telegram_handler import send_telegram_message

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Assistant API",
    description="Code assistant and task automation API",
    version="1.0.0"
)


# Pydantic models for request/response
class CodeGenerationRequest(BaseModel):
    prompt: str
    description: Optional[str] = None


class CodeExplanationRequest(BaseModel):
    code: str


class RefactorRequest(BaseModel):
    code: str
    requirements: Optional[str] = None


class DebugRequest(BaseModel):
    code: str
    error_message: str


class TaskAutomationRequest(BaseModel):
    task_description: str


class ChatRequest(BaseModel):
    message: str


class AssistantResponse(BaseModel):
    success: bool
    result: str
    error: Optional[str] = None


def verify_api_key(x_api_key: str = Header(None)) -> bool:
    """Verify API key from request header"""
    if not x_api_key or x_api_key != config.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return True


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "service": "AI Assistant API"
    }


@app.post("/generate-code", response_model=AssistantResponse)
async def generate_code(
    request: CodeGenerationRequest,
    background_tasks: BackgroundTasks,
    x_api_key: str = Header(None)
):
    """
    Generate code based on a natural language prompt
    
    Example:
    ```
    {
        "prompt": "Write a Python function to calculate factorial"
    }
    ```
    """
    verify_api_key(x_api_key)
    
    try:
        result = assistant.generate_code(request.prompt)
        
        # Send to Telegram in background
        if config.TELEGRAM_BOT_TOKEN:
            background_tasks.add_task(
                send_telegram_message,
                f"💻 Code Generated:\n\n{request.prompt}\n\n{result}"
            )
        
        return AssistantResponse(success=True, result=result)
    except Exception as e:
        logger.error(f"Error generating code: {str(e)}")
        return AssistantResponse(
            success=False,
            result="",
            error=f"Error generating code: {str(e)}"
        )


@app.post("/explain-code", response_model=AssistantResponse)
async def explain_code(
    request: CodeExplanationRequest,
    background_tasks: BackgroundTasks,
    x_api_key: str = Header(None)
):
    """
    Explain what a piece of code does
    
    Example:
    ```
    {
        "code": "def factorial(n):\n    return 1 if n <= 1 else n * factorial(n-1)"
    }
    ```
    """
    verify_api_key(x_api_key)
    
    try:
        result = assistant.explain_code(request.code)
        
        if config.TELEGRAM_BOT_TOKEN:
            background_tasks.add_task(
                send_telegram_message,
                f"📖 Code Explanation:\n\n{result}"
            )
        
        return AssistantResponse(success=True, result=result)
    except Exception as e:
        logger.error(f"Error explaining code: {str(e)}")
        return AssistantResponse(
            success=False,
            result="",
            error=f"Error explaining code: {str(e)}"
        )


@app.post("/refactor-code", response_model=AssistantResponse)
async def refactor_code(
    request: RefactorRequest,
    background_tasks: BackgroundTasks,
    x_api_key: str = Header(None)
):
    """
    Refactor code to improve quality
    
    Example:
    ```
    {
        "code": "x = [1,2,3,4,5]\ny = []\nfor i in x:\n    y.append(i*2)",
        "requirements": "Make it more pythonic"
    }
    ```
    """
    verify_api_key(x_api_key)
    
    try:
        result = assistant.refactor_code(request.code, request.requirements)
        
        if config.TELEGRAM_BOT_TOKEN:
            background_tasks.add_task(
                send_telegram_message,
                f"♻️ Code Refactoring:\n\n{result}"
            )
        
        return AssistantResponse(success=True, result=result)
    except Exception as e:
        logger.error(f"Error refactoring code: {str(e)}")
        return AssistantResponse(
            success=False,
            result="",
            error=f"Error refactoring code: {str(e)}"
        )


@app.post("/debug-code", response_model=AssistantResponse)
async def debug_code(
    request: DebugRequest,
    background_tasks: BackgroundTasks,
    x_api_key: str = Header(None)
):
    """
    Debug code based on error messages
    
    Example:
    ```
    {
        "code": "x = int('abc')",
        "error_message": "ValueError: invalid literal for int() with base 10: 'abc'"
    }
    ```
    """
    verify_api_key(x_api_key)
    
    try:
        result = assistant.debug_code(request.code, request.error_message)
        
        if config.TELEGRAM_BOT_TOKEN:
            background_tasks.add_task(
                send_telegram_message,
                f"🐛 Debug Help:\n\n{result}"
            )
        
        return AssistantResponse(success=True, result=result)
    except Exception as e:
        logger.error(f"Error debugging code: {str(e)}")
        return AssistantResponse(
            success=False,
            result="",
            error=f"Error debugging code: {str(e)}"
        )


@app.post("/automate-task", response_model=AssistantResponse)
async def automate_task(
    request: TaskAutomationRequest,
    background_tasks: BackgroundTasks,
    x_api_key: str = Header(None)
):
    """
    Generate automation solutions for a task
    
    Example:
    ```
    {
        "task_description": "I need to convert all PNG images in a folder to JPG format"
    }
    ```
    """
    verify_api_key(x_api_key)
    
    try:
        result = assistant.automate_task(request.task_description)
        
        if config.TELEGRAM_BOT_TOKEN:
            background_tasks.add_task(
                send_telegram_message,
                f"⚙️ Task Automation:\n\n{result}"
            )
        
        return AssistantResponse(success=True, result=result)
    except Exception as e:
        logger.error(f"Error automating task: {str(e)}")
        return AssistantResponse(
            success=False,
            result="",
            error=f"Error automating task: {str(e)}"
        )


@app.post("/chat", response_model=AssistantResponse)
async def chat(
    request: ChatRequest,
    background_tasks: BackgroundTasks,
    x_api_key: str = Header(None)
):
    """
    General conversation with the AI assistant
    
    Example:
    ```
    {
        "message": "How do I handle exceptions in Python?"
    }
    ```
    """
    verify_api_key(x_api_key)
    
    try:
        result = assistant.chat(request.message)
        
        if config.TELEGRAM_BOT_TOKEN:
            background_tasks.add_task(
                send_telegram_message,
                f"💬 Chat Response:\n\n{result}"
            )
        
        return AssistantResponse(success=True, result=result)
    except Exception as e:
        logger.error(f"Error in chat: {str(e)}")
        return AssistantResponse(
            success=False,
            result="",
            error=f"Error in chat: {str(e)}"
        )


@app.get("/")
async def root():
    """Root endpoint with API documentation"""
    return {
        "message": "AI Assistant API",
        "version": "1.0.0",
        "documentation": "/docs",
        "endpoints": [
            "/health",
            "/generate-code",
            "/explain-code",
            "/refactor-code",
            "/debug-code",
            "/automate-task",
            "/chat"
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=config.API_HOST,
        port=config.API_PORT,
        log_level="info"
    )