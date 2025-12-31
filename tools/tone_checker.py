"""Tool 5: Tone Consistency Checker - Ensure consistent tone throughout."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert editor specializing in voice and tone.

Tone dimensions:
- Formality (formal ↔ casual)
- Emotion (serious ↔ playful)
- Authority (authoritative ↔ humble)
- Distance (personal ↔ impersonal)
- Energy (dynamic ↔ calm)

Common tone issues:
- Register shifts
- Inconsistent formality
- Mixed emotional signals
- Audience mismatch
- Voice breaks"""

def run():
    console.print("[bold cyan]🎭 Tone Consistency Checker[/bold cyan]")
    console.print("[dim]Ensure consistent tone throughout your writing[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["check-consistency", "identify-tone", "adjust-tone", "match-tone"],
        default="check-consistency"
    )
    
    if mode == "check-consistency":
        console.print("\n[yellow]Paste your text:[/yellow]")
        text = get_multiline_input("Enter text (type 'END' when done):")
        
        prompt = f"""Check tone consistency:

{text}

Provide:
1. 📊 CONSISTENCY SCORE
   - Overall consistency (1-10)
   - Variation level

2. 🎭 TONE PROFILE
   - Dominant tone
   - Formality level
   - Emotional register

3. ⚠️ INCONSISTENCIES FOUND
   For each issue:
   - Location (quote the text)
   - What shifts
   - Why it's jarring

4. 📈 TONE MAP
   - Paragraph-by-paragraph tone
   - Visual representation

5. 🔧 FIXES
   - Specific rewrites
   - How to unify tone

6. ✨ CONSISTENT VERSION
   - Fully revised text"""

    elif mode == "identify-tone":
        console.print("\n[yellow]Paste text to analyze:[/yellow]")
        text = get_multiline_input("Enter text (type 'END' when done):")
        
        prompt = f"""Identify the tone:

{text}

Provide:
1. 🎭 TONE ANALYSIS
   - Primary tone
   - Secondary tones

2. 📊 TONE DIMENSIONS
   | Dimension | Rating (1-10) |
   - Formality
   - Warmth
   - Authority
   - Energy
   - Emotion

3. 👤 VOICE CHARACTERISTICS
   - Writer persona
   - Relationship to reader

4. 🎯 AUDIENCE FIT
   - Who this tone suits
   - Who it might alienate

5. 📝 TONE WORDS
   - Key words creating this tone"""

    elif mode == "adjust-tone":
        console.print("\n[yellow]Paste text to adjust:[/yellow]")
        text = get_multiline_input("Enter text (type 'END' when done):")
        
        target_tone = Prompt.ask("[green]Target tone[/green]",
                                choices=["formal", "casual", "professional", "friendly", 
                                        "authoritative", "empathetic", "enthusiastic"],
                                default="professional")
        
        prompt = f"""Adjust to {target_tone} tone:

Original:
{text}

Provide:
1. 🔍 CURRENT TONE
   - What it is now
   - Key characteristics

2. ✨ ADJUSTED VERSION
   [Rewritten in {target_tone} tone]

3. 📝 CHANGES MADE
   - Word substitutions
   - Sentence restructuring
   - Removed elements
   - Added elements

4. 💡 TIPS
   - Maintaining this tone"""

    else:  # match-tone
        console.print("\n[yellow]Paste the reference text (tone to match):[/yellow]")
        reference = get_multiline_input("Enter reference (type 'END' when done):")
        
        console.print("\n[dim]Paste the text to rewrite:[/dim]")
        text = get_multiline_input("Enter text (type 'END' when done):")
        
        prompt = f"""Match this tone:

Reference tone:
{reference}

Text to rewrite:
{text}

Provide:
1. 🎭 REFERENCE ANALYSIS
   - Tone characteristics
   - Key techniques

2. ✨ MATCHED VERSION
   [Rewritten to match reference tone]

3. 📝 TECHNIQUES APPLIED
   - What was changed
   - How tone was achieved"""

    console.print("\n[yellow]Analyzing tone...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🎭 Tone Analysis", result, "cyan")

if __name__ == "__main__":
    run()
