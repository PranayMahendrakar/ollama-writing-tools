"""Tool 3: Argument Strength Evaluator - Evaluate and strengthen arguments."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in logic, rhetoric, and argumentation.

Argument components (Toulmin model):
- Claim (assertion)
- Grounds (evidence/data)
- Warrant (reasoning connecting evidence to claim)
- Backing (support for warrant)
- Qualifier (limitations)
- Rebuttal (counterarguments)

Logical fallacies to identify:
- Ad hominem, straw man, false dichotomy
- Slippery slope, circular reasoning
- Appeal to authority, emotion, tradition
- Hasty generalization, red herring

Evaluate evidence quality, logical validity, and persuasive power."""

def run():
    console.print("[bold cyan]⚖️ Argument Strength Evaluator[/bold cyan]")
    console.print("[dim]Evaluate and strengthen your arguments[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["evaluate", "find-fallacies", "strengthen", "counter-argument"],
        default="evaluate"
    )
    
    if mode == "evaluate":
        console.print("\n[yellow]Paste the argument to evaluate:[/yellow]")
        argument = get_multiline_input("Enter argument (type 'END' when done):")
        
        prompt = f"""Evaluate this argument:

{argument}

Provide:
1. 📊 OVERALL STRENGTH
   - Score (1-10)
   - Summary assessment

2. 🎯 ARGUMENT STRUCTURE (Toulmin)
   - Claim identified
   - Grounds/Evidence
   - Warrant (reasoning)
   - Backing
   - Qualifiers
   - Rebuttals addressed?

3. 📋 EVIDENCE QUALITY
   - Type of evidence
   - Credibility
   - Sufficiency
   - Relevance

4. 🔍 LOGICAL ANALYSIS
   - Validity of reasoning
   - Logical gaps
   - Fallacies present

5. 💪 PERSUASIVE POWER
   - Ethos (credibility)
   - Pathos (emotional appeal)
   - Logos (logic)

6. ⚠️ WEAKNESSES
   - Vulnerable points
   - Counterarguments possible

7. ✨ IMPROVEMENT SUGGESTIONS
   - How to strengthen"""

    elif mode == "find-fallacies":
        console.print("\n[yellow]Paste text to check for fallacies:[/yellow]")
        text = get_multiline_input("Enter text (type 'END' when done):")
        
        prompt = f"""Identify logical fallacies:

{text}

Provide:
1. 🔍 FALLACIES FOUND
   For each:
   - Fallacy name
   - Where it occurs (quote)
   - Why it's fallacious
   - How to fix

2. 📊 FALLACY TYPES
   - Formal vs informal
   - Severity rating

3. ✨ CORRECTED VERSION
   - Rewritten without fallacies

4. 💡 PREVENTION TIPS
   - How to avoid these"""

    elif mode == "strengthen":
        console.print("\n[yellow]Paste the argument to strengthen:[/yellow]")
        argument = get_multiline_input("Enter argument (type 'END' when done):")
        
        prompt = f"""Strengthen this argument:

{argument}

Provide:
1. 🔍 CURRENT WEAKNESSES
   - What's missing
   - What's weak

2. 📚 EVIDENCE SUGGESTIONS
   - Types of evidence to add
   - Where to find support

3. 🔗 LOGIC IMPROVEMENTS
   - Stronger reasoning
   - Better connections

4. ✨ STRENGTHENED VERSION
   - Rewritten argument

5. 🛡️ PREEMPTIVE REBUTTALS
   - Anticipated objections
   - How to address them"""

    else:  # counter-argument
        console.print("\n[yellow]Paste the argument to counter:[/yellow]")
        argument = get_multiline_input("Enter argument (type 'END' when done):")
        
        prompt = f"""Generate counter-arguments:

Original argument:
{argument}

Provide:
1. 🎯 MAIN COUNTER-ARGUMENTS
   - 3-5 strong counters
   - Evidence for each

2. 🔍 WEAKNESS EXPLOITATION
   - Logical gaps to target
   - Evidence problems

3. 💭 ALTERNATIVE PERSPECTIVES
   - Different viewpoints
   - Reframing the issue

4. ⚖️ STEELMAN
   - Strongest version of original
   - Then counter that"""

    console.print("\n[yellow]Analyzing argument...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("⚖️ Argument Analysis", result, "yellow")

if __name__ == "__main__":
    run()
