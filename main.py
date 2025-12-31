#!/usr/bin/env python3
"""
Ollama Writing & Communication Tools - 15 AI-Powered Writing Assistants
Run: python main.py
"""

import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import IntPrompt

console = Console()

TOOLS = {
    1: ("Essay Structure Analyzer", "tools.essay_analyzer", "Analyze and improve essay organization"),
    2: ("Topic Sentence Generator", "tools.topic_sentence", "Create effective topic sentences"),
    3: ("Argument Strength Evaluator", "tools.argument_evaluator", "Evaluate and strengthen arguments"),
    4: ("Persuasive Writing Coach", "tools.persuasive_coach", "Master persuasive techniques"),
    5: ("Tone Consistency Checker", "tools.tone_checker", "Ensure consistent tone throughout"),
    6: ("Public Speaking Coach", "tools.speaking_coach", "Prepare and deliver great speeches"),
    7: ("Storytelling Structure Guide", "tools.storytelling_guide", "Craft compelling narratives"),
    8: ("Technical Writing Simplifier", "tools.tech_simplifier", "Make complex content accessible"),
    9: ("Email Etiquette Advisor", "tools.email_advisor", "Write professional emails"),
    10: ("Cross-Cultural Communication", "tools.cultural_guide", "Navigate cultural differences"),
    11: ("Journal Article Structurer", "tools.article_structurer", "Structure academic papers"),
    12: ("Cover Letter Customizer", "tools.cover_letter", "Create tailored cover letters"),
    13: ("Grant Writing Assistant", "tools.grant_writing", "Write compelling grant proposals"),
    14: ("Peer Review Response Helper", "tools.peer_review", "Respond to peer reviews"),
    15: ("Conference Presentation Builder", "tools.presentation_builder", "Create effective presentations"),
}

def show_menu():
    console.clear()
    console.print(Panel.fit(
        "[bold cyan]✍️ Ollama Writing & Communication Tools[/bold cyan]\n"
        "[dim]15 AI-Powered Tools for Writers[/dim]",
        border_style="cyan"
    ))
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("#", style="cyan", width=4)
    table.add_column("Tool", style="green", width=35)
    table.add_column("Description", style="dim")
    
    for num, (name, _, desc) in TOOLS.items():
        table.add_row(str(num), name, desc)
    
    table.add_row("0", "Exit", "Quit the application")
    console.print(table)
    console.print()

def run_tool(choice: int):
    if choice == 0:
        console.print("[yellow]Goodbye! Happy writing! ✍️[/yellow]")
        sys.exit(0)
    
    if choice not in TOOLS:
        console.print("[red]Invalid choice. Please try again.[/red]")
        return
    
    name, module_path, _ = TOOLS[choice]
    console.print(f"\n[bold green]Starting {name}...[/bold green]\n")
    
    try:
        module = __import__(module_path, fromlist=['run'])
        module.run()
    except ImportError as e:
        console.print(f"[red]Error loading module: {e}[/red]")
    except Exception as e:
        console.print(f"[red]Error running tool: {e}[/red]")
    
    console.print("\n[dim]Press Enter to return to menu...[/dim]")
    input()

def main():
    try:
        import ollama
        ollama.list()
        console.print("[green]✓ Ollama connected successfully[/green]\n")
    except Exception as e:
        console.print(f"[red]✗ Ollama not running. Please start Ollama first.[/red]")
        console.print(f"[dim]Run: ollama serve[/dim]\n")
        sys.exit(1)
    
    while True:
        show_menu()
        try:
            choice = IntPrompt.ask("Select a tool", default=0)
            run_tool(choice)
        except KeyboardInterrupt:
            console.print("\n[yellow]Goodbye![/yellow]")
            break

if __name__ == "__main__":
    main()
