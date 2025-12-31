"""Tool 13: Grant Writing Assistant - Write compelling grant proposals."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert grant writer with experience in research and nonprofit funding.

Grant proposal elements:
- Executive summary
- Statement of need
- Goals and objectives (SMART)
- Methods/approach
- Evaluation plan
- Budget justification
- Organizational capacity
- Sustainability plan

Key principles:
- Align with funder priorities
- Clear, measurable outcomes
- Compelling narrative
- Evidence-based approach
- Realistic budget"""

def run():
    console.print("[bold cyan]💰 Grant Writing Assistant[/bold cyan]")
    console.print("[dim]Write compelling grant proposals[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["write-section", "review-proposal", "needs-statement", "objectives"],
        default="write-section"
    )
    
    if mode == "write-section":
        section = Prompt.ask("[green]Which section?[/green]",
                            choices=["executive-summary", "needs-statement", "goals-objectives",
                                    "methods", "evaluation", "budget-narrative", "sustainability"],
                            default="needs-statement")
        
        console.print("\n[yellow]Describe your project:[/yellow]")
        project = get_multiline_input("Enter project info (type 'END' when done):")
        
        grant_type = Prompt.ask("[green]Grant type[/green]",
                               choices=["research", "nonprofit", "education", "community", "arts"],
                               default="research")
        
        prompt = f"""Write grant {section}:

Project: {project}
Grant type: {grant_type}

Provide:
1. 📝 {section.upper().replace('-', ' ')}
   [Complete section draft]

2. 🎯 KEY ELEMENTS INCLUDED
   - What funders look for
   - How this addresses them

3. 💪 STRONG PHRASES
   - Compelling language used

4. ⚠️ COMMON MISTAKES
   - What to avoid in this section

5. ✅ CHECKLIST
   - Section requirements"""

    elif mode == "review-proposal":
        console.print("\n[yellow]Paste your proposal or section:[/yellow]")
        proposal = get_multiline_input("Enter proposal (type 'END' when done):")
        
        prompt = f"""Review this grant proposal:

{proposal}

Provide:
1. 📊 OVERALL ASSESSMENT
   - Strength score (1-10)
   - Fundability assessment

2. ✅ STRENGTHS
   - What works well
   - Compelling elements

3. ⚠️ WEAKNESSES
   - Missing elements
   - Weak arguments
   - Unclear sections

4. 🔧 SPECIFIC IMPROVEMENTS
   - Section-by-section feedback

5. ✨ ENHANCED VERSION
   - Key sections rewritten"""

    elif mode == "needs-statement":
        console.print("\n[yellow]Describe the problem/need:[/yellow]")
        problem = get_multiline_input("Enter problem description (type 'END' when done):")
        
        prompt = f"""Create compelling needs statement:

Problem: {problem}

Provide:
1. 📝 NEEDS STATEMENT
   [Compelling, evidence-based statement]

2. 📊 DATA TO INCLUDE
   - Statistics needed
   - Research to cite

3. 🎯 EMOTIONAL + LOGICAL BALANCE
   - Human impact
   - Systemic issues

4. 💡 STRENGTHENING TIPS
   - How to make it more compelling

5. 🔗 CONNECTING TO SOLUTION
   - Transition to your approach"""

    else:  # objectives
        console.print("\n[yellow]Describe your project goals:[/yellow]")
        goals = get_multiline_input("Enter goals (type 'END' when done):")
        
        prompt = f"""Create SMART objectives:

Goals: {goals}

Provide:
1. 🎯 SMART OBJECTIVES
   For each objective:
   - Specific: What exactly
   - Measurable: How measured
   - Achievable: Why realistic
   - Relevant: Why it matters
   - Time-bound: When

2. 📊 OUTCOMES VS OUTPUTS
   - Distinguish between them
   - Both types listed

3. 📈 EVALUATION METRICS
   - How to measure success

4. 💡 TIPS
   - Making objectives fundable"""

    console.print("\n[yellow]Writing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("💰 Grant Writing", result, "yellow")

if __name__ == "__main__":
    run()
