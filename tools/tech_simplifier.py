"""Tool 8: Technical Writing Simplifier - Make complex content accessible."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert technical writer and plain language specialist.

Plain language principles:
- Short sentences (15-20 words avg)
- Active voice
- Common words over jargon
- Clear structure
- Reader-focused

Simplification techniques:
- Define terms on first use
- Use analogies
- Break down complex processes
- Visual descriptions
- Progressive disclosure"""

def run():
    console.print("[bold cyan]📋 Technical Writing Simplifier[/bold cyan]")
    console.print("[dim]Make complex content accessible[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["simplify", "jargon-bust", "structure", "audience-adapt"],
        default="simplify"
    )
    
    if mode == "simplify":
        console.print("\n[yellow]Paste technical content to simplify:[/yellow]")
        content = get_multiline_input("Enter content (type 'END' when done):")
        
        audience = Prompt.ask("[green]Target audience[/green]",
                             choices=["general-public", "business-users", "students", "new-employees"],
                             default="general-public")
        
        prompt = f"""Simplify this technical content:

Target audience: {audience}

Original:
{content}

Provide:
1. 📊 COMPLEXITY ANALYSIS
   - Reading level (grade)
   - Jargon count
   - Sentence complexity

2. ✨ SIMPLIFIED VERSION
   [Rewritten for {audience}]

3. 📝 CHANGES MADE
   - Jargon replaced
   - Sentences shortened
   - Structure improved

4. 📖 GLOSSARY
   - Key terms defined simply

5. 💡 ANALOGIES ADDED
   - Complex concepts explained

6. 📊 NEW METRICS
   - New reading level
   - Improvement summary"""

    elif mode == "jargon-bust":
        console.print("\n[yellow]Paste text with jargon:[/yellow]")
        text = get_multiline_input("Enter text (type 'END' when done):")
        
        prompt = f"""Remove jargon:

{text}

Provide:
1. 🔍 JARGON IDENTIFIED
   | Term | Plain Alternative | Definition |

2. ✨ JARGON-FREE VERSION
   [Rewritten without jargon]

3. 💡 WHEN TO KEEP JARGON
   - Terms worth keeping
   - How to introduce them"""

    elif mode == "structure":
        console.print("\n[yellow]Paste content to restructure:[/yellow]")
        content = get_multiline_input("Enter content (type 'END' when done):")
        
        doc_type = Prompt.ask("[green]Document type[/green]",
                             choices=["instructions", "explanation", "reference", "report"],
                             default="instructions")
        
        prompt = f"""Restructure for clarity:

Document type: {doc_type}

Content:
{content}

Provide:
1. 📋 CURRENT STRUCTURE
   - Issues identified
   - Flow problems

2. ✨ RESTRUCTURED VERSION
   - Clear headings
   - Logical flow
   - Appropriate formatting

3. 📝 STRUCTURE TIPS
   - Best practices for {doc_type}"""

    else:  # audience-adapt
        console.print("\n[yellow]Paste content to adapt:[/yellow]")
        content = get_multiline_input("Enter content (type 'END' when done):")
        
        from_audience = Prompt.ask("[green]Current audience[/green]", default="experts")
        to_audience = Prompt.ask("[green]Target audience[/green]", default="beginners")
        
        prompt = f"""Adapt for different audience:

From: {from_audience}
To: {to_audience}

Content:
{content}

Provide:
1. 🔍 ADAPTATION NEEDS
   - What must change
   - What can stay

2. ✨ ADAPTED VERSION
   [Rewritten for {to_audience}]

3. 📝 KEY CHANGES
   - Technical depth adjusted
   - Explanations added
   - Context provided"""

    console.print("\n[yellow]Simplifying...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📋 Simplified Content", result, "green")

if __name__ == "__main__":
    run()
