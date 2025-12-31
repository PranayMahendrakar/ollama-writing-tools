"""Tool 2: Topic Sentence Generator - Create effective topic sentences."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert writing coach specializing in paragraph construction.

Effective topic sentences:
- State the main idea clearly
- Connect to the thesis
- Preview paragraph content
- Provide transition from previous
- Are specific, not vague

Types:
- Simple statement
- Complex (with subordinate clause)
- Question (rhetorical)
- Transitional
- Bridge sentences"""

def run():
    console.print("[bold cyan]✏️ Topic Sentence Generator[/bold cyan]")
    console.print("[dim]Create effective topic sentences for your paragraphs[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["generate", "improve", "check-alignment", "learn"],
        default="generate"
    )
    
    if mode == "generate":
        thesis = Prompt.ask("[green]Your thesis statement[/green]")
        num_paragraphs = Prompt.ask("[green]Number of body paragraphs[/green]", default="3")
        
        console.print("\n[dim]Main points for each paragraph (optional):[/dim]")
        points = get_multiline_input("Enter points (or 'END' to skip):")
        
        prompt = f"""Generate topic sentences:

Thesis: {thesis}
Number of paragraphs: {num_paragraphs}
{"Points: " + points if points.strip() else ""}

Provide:
1. 📝 TOPIC SENTENCES
   For each paragraph:
   - Option A (direct statement)
   - Option B (with transition)
   - Option C (creative approach)

2. 🔗 FLOW CHECK
   - How sentences connect
   - Logical progression

3. 🎯 ALIGNMENT CHECK
   - How each supports thesis

4. 💡 STRENGTHENING TIPS
   - Making each more specific
   - Adding power words"""

    elif mode == "improve":
        console.print("\n[yellow]Paste topic sentences to improve:[/yellow]")
        sentences = get_multiline_input("Enter sentences (type 'END' when done):")
        
        thesis = Prompt.ask("[green]Your thesis (optional)[/green]", default="")
        
        prompt = f"""Improve these topic sentences:

{sentences}

{"Thesis: " + thesis if thesis else ""}

Provide:
1. 🔍 ANALYSIS
   For each sentence:
   - Current strength
   - Issues

2. ✨ IMPROVED VERSIONS
   - Rewritten sentence
   - Why it's better

3. 🔗 TRANSITIONS
   - Added transition words
   - Flow improvements"""

    elif mode == "check-alignment":
        thesis = Prompt.ask("[green]Your thesis statement[/green]")
        
        console.print("\n[yellow]Paste your topic sentences:[/yellow]")
        sentences = get_multiline_input("Enter sentences (type 'END' when done):")
        
        prompt = f"""Check topic sentence alignment:

Thesis: {thesis}

Topic sentences:
{sentences}

Provide:
1. 📊 ALIGNMENT SCORE
   - Overall alignment (1-10)

2. 🔍 INDIVIDUAL ANALYSIS
   For each sentence:
   - Connection to thesis
   - Strength of support
   - Gaps or tangents

3. 🔧 RECOMMENDATIONS
   - Realignment suggestions
   - Reordering if needed"""

    else:  # learn
        prompt = """Teach topic sentence writing:

1. 📚 WHAT MAKES A GOOD TOPIC SENTENCE
   - Key characteristics
   - Common mistakes

2. 📝 TYPES OF TOPIC SENTENCES
   - Direct statement
   - Complex sentence
   - Question
   - Transitional
   - Examples of each

3. 🔗 CONNECTING TO THESIS
   - How to ensure alignment
   - Keywords to echo

4. 💪 POWER TECHNIQUES
   - Strong verbs
   - Specific language
   - Avoiding "this essay will..."

5. ✅ CHECKLIST
   - Self-review questions"""

    console.print("\n[yellow]Generating...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("✏️ Topic Sentences", result, "green")

if __name__ == "__main__":
    run()
