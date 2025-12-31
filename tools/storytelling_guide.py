"""Tool 7: Storytelling Structure Guide - Craft compelling narratives."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in narrative structure and storytelling.

Story structures:
- Three-act structure
- Hero's Journey (Campbell)
- Story Circle (Dan Harmon)
- Freytag's Pyramid
- In medias res
- Frame narrative

Story elements:
- Character (want, need, flaw)
- Conflict (internal, external)
- Stakes (personal, universal)
- Setting (world, atmosphere)
- Theme (meaning, message)
- Voice (POV, style)"""

def run():
    console.print("[bold cyan]📖 Storytelling Structure Guide[/bold cyan]")
    console.print("[dim]Craft compelling narratives[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["analyze-story", "create-structure", "fix-narrative", "learn-structures"],
        default="create-structure"
    )
    
    if mode == "analyze-story":
        console.print("\n[yellow]Paste your story/narrative:[/yellow]")
        story = get_multiline_input("Enter story (type 'END' when done):")
        
        prompt = f"""Analyze this story's structure:

{story}

Provide:
1. 📊 STRUCTURE ANALYSIS
   - Structure type used
   - How well it follows the pattern

2. 🎭 CHARACTER ANALYSIS
   - Protagonist want/need/flaw
   - Character arc
   - Supporting characters

3. ⚡ CONFLICT & STAKES
   - Central conflict
   - Internal/external balance
   - Stakes evaluation

4. 📈 PACING
   - Tension curve
   - Slow/fast spots

5. 🎯 THEME
   - Core theme identified
   - How it's conveyed

6. ✅ STRENGTHS
   - What works well

7. ⚠️ WEAKNESSES
   - Structural issues
   - Missing elements

8. 🔧 RECOMMENDATIONS
   - Specific improvements"""

    elif mode == "create-structure":
        story_type = Prompt.ask("[green]Story type[/green]",
                               choices=["fiction", "personal-narrative", "business-story", 
                                       "brand-story", "case-study"],
                               default="fiction")
        
        console.print("\n[yellow]Describe your story idea:[/yellow]")
        idea = get_multiline_input("Enter idea (type 'END' when done):")
        
        structure = Prompt.ask("[green]Preferred structure[/green]",
                              choices=["three-act", "heros-journey", "story-circle", "open"],
                              default="three-act")
        
        prompt = f"""Create story structure:

Type: {story_type}
Idea: {idea}
Structure: {structure}

Provide:
1. 📋 FULL OUTLINE
   Using {structure}:
   [Detailed beat-by-beat outline]

2. 🎭 CHARACTER DESIGN
   - Protagonist profile
   - Want/Need/Flaw
   - Arc description

3. ⚡ CONFLICT DESIGN
   - Central conflict
   - Obstacles
   - Climax moment

4. 📈 TENSION MAP
   - Scene-by-scene tension levels
   - Key turning points

5. 🎯 THEME INTEGRATION
   - Core theme
   - How to weave it in

6. 💬 KEY SCENES
   - Opening hook
   - Midpoint shift
   - Climax
   - Resolution"""

    elif mode == "fix-narrative":
        console.print("\n[yellow]Paste your story with issues:[/yellow]")
        story = get_multiline_input("Enter story (type 'END' when done):")
        
        issue = Prompt.ask("[green]Main issue[/green]", default="pacing/engagement")
        
        prompt = f"""Fix this narrative:

Issue: {issue}

Story:
{story}

Provide:
1. 🔍 DIAGNOSIS
   - What's not working
   - Root causes

2. 🔧 STRUCTURAL FIXES
   - Reordering suggestions
   - Scenes to add/remove

3. ⚡ TENSION FIXES
   - How to raise stakes
   - Conflict enhancement

4. 🎭 CHARACTER FIXES
   - Deeper motivation
   - Clearer arc

5. ✨ REVISED OUTLINE
   - New structure

6. 📝 SAMPLE REWRITES
   - Key scenes rewritten"""

    else:  # learn-structures
        prompt = """Teach storytelling structures:

1. 📖 THREE-ACT STRUCTURE
   - Setup, Confrontation, Resolution
   - Key plot points
   - Example

2. 🦸 HERO'S JOURNEY
   - 12 stages explained
   - Modern applications
   - Example

3. 🔄 STORY CIRCLE
   - 8 steps
   - Why it works
   - Example

4. 📈 FREYTAG'S PYRAMID
   - 5 parts
   - Best for what
   - Example

5. 🎯 CHOOSING A STRUCTURE
   - Decision guide
   - When to use each

6. ✅ UNIVERSAL ELEMENTS
   - What all good stories have"""

    console.print("\n[yellow]Processing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📖 Storytelling Guide", result, "blue")

if __name__ == "__main__":
    run()
