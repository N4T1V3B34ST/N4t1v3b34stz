"""
Examples of using the AI Assistant API
Run this script to test the API locally
"""
import requests
import json

# Configuration
API_URL = "http://localhost:8000"
API_KEY = "secret-key-change-me"  # Change this to your configured API key
HEADERS = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY
}


def print_response(title, response_json):
    """Pretty print API response"""
    print(f"\n{'='*60}")
    print(f"📌 {title}")
    print(f"{'='*60}")
    if response_json.get("success"):
        print(response_json.get("result"))
    else:
        print(f"❌ Error: {response_json.get('error')}")
    print()


def example_generate_code():
    """Example: Generate code"""
    print("🔄 Testing: Generate Code")
    
    payload = {
        "prompt": "Write a Python function that validates email addresses using regex"
    }
    
    response = requests.post(
        f"{API_URL}/generate-code",
        json=payload,
        headers=HEADERS
    )
    
    print_response("Generated Code", response.json())


def example_explain_code():
    """Example: Explain code"""
    print("🔄 Testing: Explain Code")
    
    code_sample = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
    
    payload = {"code": code_sample}
    
    response = requests.post(
        f"{API_URL}/explain-code",
        json=payload,
        headers=HEADERS
    )
    
    print_response("Code Explanation", response.json())


def example_refactor_code():
    """Example: Refactor code"""
    print("🔄 Testing: Refactor Code")
    
    code_sample = """
x = [1, 2, 3, 4, 5]
y = []
for i in x:
    if i % 2 == 0:
        y.append(i * 2)
"""
    
    payload = {
        "code": code_sample,
        "requirements": "Make it more pythonic and efficient"
    }
    
    response = requests.post(
        f"{API_URL}/refactor-code",
        json=payload,
        headers=HEADERS
    )
    
    print_response("Refactored Code", response.json())


def example_debug_code():
    """Example: Debug code"""
    print("🔄 Testing: Debug Code")
    
    payload = {
        "code": "result = int('123abc')",
        "error_message": "ValueError: invalid literal for int() with base 10: '123abc'"
    }
    
    response = requests.post(
        f"{API_URL}/debug-code",
        json=payload,
        headers=HEADERS
    )
    
    print_response("Debug Assistance", response.json())


def example_automate_task():
    """Example: Automate task"""
    print("🔄 Testing: Automate Task")
    
    payload = {
        "task_description": "I need to rename all files in a directory to add a timestamp prefix"
    }
    
    response = requests.post(
        f"{API_URL}/automate-task",
        json=payload,
        headers=HEADERS
    )
    
    print_response("Task Automation Solution", response.json())


def example_chat():
    """Example: Chat"""
    print("🔄 Testing: Chat")
    
    payload = {
        "message": "What are the best practices for writing clean code?"
    }
    
    response = requests.post(
        f"{API_URL}/chat",
        json=payload,
        headers=HEADERS
    )
    
    print_response("Chat Response", response.json())


def example_health_check():
    """Example: Health check"""
    print("🔄 Testing: Health Check")
    
    response = requests.get(f"{API_URL}/health")
    
    print_response("Health Status", response.json())


def main():
    """Run all examples"""
    print("\n" + "="*60)
    print("🤖 AI Assistant API - Example Tests")
    print("="*60)
    print(f"\nAPI URL: {API_URL}")
    print(f"API Key: {'*' * len(API_KEY)}")
    
    try:
        # Test health first
        example_health_check()
        
        # Run all examples
        example_generate_code()
        example_explain_code()
        example_refactor_code()
        example_debug_code()
        example_automate_task()
        example_chat()
        
        print("\n" + "="*60)
        print("✅ All tests completed!")
        print("="*60)
        print("\nNext steps:")
        print("1. Check the responses above")
        print("2. Visit http://localhost:8000/docs for interactive API docs")
        print("3. Configure Telegram integration in .env for notifications")
        print("4. Deploy to production when ready!")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to API")
        print(f"Make sure the server is running at {API_URL}")
        print("Run: python main.py")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()