"""Base utilities for all Ollama writing tools."""

import ollama
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt

console = Console()

DEFAULT_MODEL = "llama3.2"

def get_model():
    """Get available model or use default."""
    try:
        models = ollama.list()
        available = [m['name'] for m in models.get('models', [])]
        if available:
            for preferred in ['llama3.2', 'llama3.1', 'llama3', 'mistral']:
                for m in available:
                    if preferred in m.lower():
                        return m
            return available[0]
    except:
        pass
    return DEFAULT_MODEL

def chat(prompt: str, system: str = None, model: str = None) -> str:
    """Send a chat message to Ollama and return response."""
    model = model or get_model()
    messages = []
    
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    
    try:
        with console.status(f"[bold cyan]Writing with {model}...[/bold cyan]"):
            response = ollama.chat(model=model, messages=messages)
        return response['message']['content']
    except Exception as e:
        return f"Error: {e}"

def get_multiline_input(prompt_text: str = "Enter text (type 'END' on a new line to finish):") -> str:
    """Get multiline input from user."""
    console.print(f"[cyan]{prompt_text}[/cyan]")
    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        except EOFError:
            break
    return '\n'.join(lines)

def display_result(title: str, content: str, style: str = "green"):
    """Display result in a panel."""
    console.print()
    console.print(Panel(
        Markdown(content),
        title=f"[bold {style}]{title}[/bold {style}]",
        border_style=style
    ))

def confirm(message: str = "Continue?") -> bool:
    """Ask for confirmation."""
    response = Prompt.ask(f"[yellow]{message}[/yellow]", choices=["y", "n"], default="y")
    return response.lower() == 'y'
