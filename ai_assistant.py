"""
Core AI Assistant module using LangChain and OpenAI
"""
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from config import config


class AIAssistant:
    """Main AI Assistant class for code generation and task automation"""
    
    def __init__(self):
        """Initialize the AI assistant with OpenAI"""
        self.llm = ChatOpenAI(
            openai_api_key=config.OPENAI_API_KEY,
            model_name=config.MODEL_NAME,
            temperature=config.TEMPERATURE,
            max_tokens=config.MAX_TOKENS,
        )
        
        self.system_prompt = SystemMessage(content="""You are an expert code assistant and task automation expert. 
Your capabilities include:
- Writing clean, well-documented code
- Explaining complex code concepts
- Refactoring and optimizing code
- Automating tasks and workflows
- Debugging and troubleshooting
- Best practices and design patterns

Always provide:
1. Clear, executable code
2. Explanations of what the code does
3. Usage examples when applicable
4. Any important caveats or considerations

Format code in markdown code blocks with the appropriate language tag.""")
    
    def generate_code(self, prompt: str) -> str:
        """
        Generate code based on a natural language prompt
        
        Args:
            prompt: Natural language description of what code to generate
            
        Returns:
            Generated code or explanation
        """
        messages = [
            self.system_prompt,
            HumanMessage(content=prompt)
        ]
        
        response = self.llm(messages)
        return response.content
    
    def explain_code(self, code: str) -> str:
        """
        Explain what a piece of code does
        
        Args:
            code: Code to explain
            
        Returns:
            Explanation of the code
        """
        prompt = f"""Please explain the following code in detail:

```
{code}
```

Explain:
1. What the code does
2. How it works step by step
3. What each function/method does
4. Any important considerations or edge cases"""
        
        messages = [
            self.system_prompt,
            HumanMessage(content=prompt)
        ]
        
        response = self.llm(messages)
        return response.content
    
    def refactor_code(self, code: str, requirements: str = None) -> str:
        """
        Refactor code to improve quality
        
        Args:
            code: Code to refactor
            requirements: Specific refactoring requirements (optional)
            
        Returns:
            Refactored code with explanations
        """
        req_text = f"\n\nSpecific requirements: {requirements}" if requirements else ""
        
        prompt = f"""Please refactor the following code to improve quality, readability, and performance:

```
{code}
```{req_text}

Provide:
1. The refactored code
2. Explanation of changes made
3. Benefits of the refactoring"""
        
        messages = [
            self.system_prompt,
            HumanMessage(content=prompt)
        ]
        
        response = self.llm(messages)
        return response.content
    
    def automate_task(self, task_description: str) -> str:
        """
        Generate automation solutions for a task
        
        Args:
            task_description: Description of the task to automate
            
        Returns:
            Code or workflow to automate the task
        """
        prompt = f"""I need to automate the following task:

{task_description}

Please provide:
1. A step-by-step approach
2. Code implementation (if applicable)
3. Tools or libraries I should use
4. Potential challenges and solutions"""
        
        messages = [
            self.system_prompt,
            HumanMessage(content=prompt)
        ]
        
        response = self.llm(messages)
        return response.content
    
    def debug_code(self, code: str, error_message: str) -> str:
        """
        Help debug code based on error messages
        
        Args:
            code: Code that's producing an error
            error_message: The error message or description
            
        Returns:
            Debugging advice and fixed code
        """
        prompt = f"""I'm getting an error in my code. Can you help debug it?

Code:
```
{code}
```

Error message:
{error_message}

Please provide:
1. Root cause of the error
2. Fixed code
3. Explanation of what was wrong
4. How to prevent this in the future"""
        
        messages = [
            self.system_prompt,
            HumanMessage(content=prompt)
        ]
        
        response = self.llm(messages)
        return response.content
    
    def chat(self, message: str) -> str:
        """
        General conversation with the AI assistant
        
        Args:
            message: User message
            
        Returns:
            AI response
        """
        messages = [
            self.system_prompt,
            HumanMessage(content=message)
        ]
        
        response = self.llm(messages)
        return response.content


# Create global instance
assistant = AIAssistant()