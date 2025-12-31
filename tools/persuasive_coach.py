"""Tool 4: Persuasive Writing Coach - Master persuasive writing techniques."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in rhetoric and persuasive communication.

Persuasion principles (Cialdini):
- Reciprocity
- Commitment/Consistency
- Social proof
- Authority
- Liking
- Scarcity

Rhetorical appeals:
- Ethos (credibility)
- Pathos (emotion)
- Logos (logic)
- Kairos (timing)

Techniques:
- Power words
- Storytelling
- Repetition
- Rhetorical questions
- Call to action"""

def run():
    console.print("[bold cyan]🎯 Persuasive Writing Coach[/bold cyan]")
    console.print("[dim]Master persuasive writing techniques[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["analyze", "improve", "create", "learn-techniques"],
        default="improve"
    )
    
    if mode == "analyze":
        console.print("\n[yellow]Paste persuasive writing to analyze:[/yellow]")
        text = get_multiline_input("Enter text (type 'END' when done):")
        
        prompt = f"""Analyze persuasive techniques:

{text}

Provide:
1. 📊 PERSUASION SCORE
   - Overall effectiveness (1-10)
   - Likely impact on audience

2. 🎭 RHETORICAL APPEALS
   - Ethos: How credibility is built
   - Pathos: Emotional appeals used
   - Logos: Logical arguments
   - Balance assessment

3. 🧠 PERSUASION PRINCIPLES
   - Which Cialdini principles used
   - How effectively applied

4. 💪 TECHNIQUES IDENTIFIED
   - Power words
   - Storytelling elements
   - Rhetorical devices

5. ⚠️ WEAKNESSES
   - What's missing
   - What falls flat

6. ✨ ENHANCEMENT IDEAS
   - Specific improvements"""

    elif mode == "improve":
        console.print("\n[yellow]Paste writing to make more persuasive:[/yellow]")
        text = get_multiline_input("Enter text (type 'END' when done):")
        
        audience = Prompt.ask("[green]Target audience[/green]", default="general")
        goal = Prompt.ask("[green]Persuasion goal[/green]", default="convince")
        
        prompt = f"""Make this more persuasive:

Audience: {audience}
Goal: {goal}

Original:
{text}

Provide:
1. 🔍 CURRENT ASSESSMENT
   - What works
   - What needs improvement

2. ✨ ENHANCED VERSION
   [Rewritten with persuasive techniques]

3. 📝 CHANGES MADE
   - Specific techniques added
   - Why each helps

4. 💪 POWER ADDITIONS
   - Stronger words used
   - Emotional hooks added
   - Call to action"""

    elif mode == "create":
        topic = Prompt.ask("[green]What are you trying to persuade about?[/green]")
        audience = Prompt.ask("[green]Target audience[/green]")
        format_type = Prompt.ask("[green]Format[/green]",
                                choices=["essay", "speech", "email", "ad-copy", "proposal"],
                                default="essay")
        
        prompt = f"""Create persuasive content:

Topic: {topic}
Audience: {audience}
Format: {format_type}

Provide:
1. 📝 PERSUASIVE DRAFT
   [Complete {format_type} using all techniques]

2. 🎯 TECHNIQUES USED
   - List of techniques
   - Where each appears

3. 💡 VARIATIONS
   - Alternative hooks
   - Different emotional angles

4. 📋 CUSTOMIZATION TIPS
   - Adapt for different audiences"""

    else:  # learn-techniques
        prompt = """Teach persuasive writing techniques:

1. 🎭 RHETORICAL APPEALS
   - Ethos: Building credibility
   - Pathos: Emotional connection
   - Logos: Logical persuasion
   - Examples of each

2. 🧠 CIALDINI'S PRINCIPLES
   For each principle:
   - How it works
   - Writing application
   - Example

3. 💪 POWER TECHNIQUES
   - Power words (list)
   - Storytelling structure
   - Rhetorical questions
   - Rule of three
   - Repetition

4. 🎯 CALL TO ACTION
   - How to write effective CTAs
   - Examples

5. ✅ CHECKLIST
   - Persuasive writing checklist"""

    console.print("\n[yellow]Processing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🎯 Persuasive Writing", result, "magenta")

if __name__ == "__main__":
    run()
