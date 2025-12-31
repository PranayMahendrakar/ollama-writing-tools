"""Tool 12: Cover Letter Customizer - Create tailored cover letters."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert career coach and cover letter writer.

Cover letter principles:
- Tailored to specific job
- Show don't tell
- Quantify achievements
- Address their needs
- Show enthusiasm
- Clear call to action

Structure:
- Hook opening
- Why this company
- Why you're qualified
- Specific examples
- Closing with action"""

def run():
    console.print("[bold cyan]✉️ Cover Letter Customizer[/bold cyan]")
    console.print("[dim]Create tailored cover letters[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["create", "customize", "improve", "opening-hooks"],
        default="create"
    )
    
    if mode == "create":
        console.print("\n[yellow]Paste the job description:[/yellow]")
        job_desc = get_multiline_input("Enter job description (type 'END' when done):")
        
        console.print("\n[dim]Describe your relevant experience:[/dim]")
        experience = get_multiline_input("Enter experience (type 'END' when done):")
        
        tone = Prompt.ask("[green]Tone[/green]",
                         choices=["professional", "enthusiastic", "confident", "creative"],
                         default="professional")
        
        prompt = f"""Create a tailored cover letter:

Job Description:
{job_desc}

My Experience:
{experience}

Tone: {tone}

Provide:
1. 📝 COVER LETTER
   [Complete, tailored cover letter]

2. 🎯 KEY ALIGNMENTS
   - Job requirements matched to your skills

3. 💪 POWER PHRASES
   - Strong phrases used
   - Why they work

4. 🔄 ALTERNATIVE OPENINGS
   - 2-3 different hooks

5. ✅ CUSTOMIZATION CHECKLIST
   - What's been tailored"""

    elif mode == "customize":
        console.print("\n[yellow]Paste your existing cover letter:[/yellow]")
        letter = get_multiline_input("Enter cover letter (type 'END' when done):")
        
        console.print("\n[dim]Paste the new job description:[/dim]")
        job_desc = get_multiline_input("Enter job description (type 'END' when done):")
        
        prompt = f"""Customize this cover letter:

Existing letter:
{letter}

New job:
{job_desc}

Provide:
1. 📝 CUSTOMIZED VERSION
   [Tailored for new position]

2. 📋 CHANGES MADE
   - What was adapted
   - Why each change matters

3. 🎯 KEY ADDITIONS
   - What was added for this job"""

    elif mode == "improve":
        console.print("\n[yellow]Paste your cover letter:[/yellow]")
        letter = get_multiline_input("Enter cover letter (type 'END' when done):")
        
        prompt = f"""Improve this cover letter:

{letter}

Provide:
1. 📊 ASSESSMENT
   - Strengths
   - Weaknesses
   - Overall score (1-10)

2. ⚠️ ISSUES FOUND
   - Generic phrases
   - Weak statements
   - Missing elements

3. ✨ IMPROVED VERSION
   [Polished cover letter]

4. 📝 SPECIFIC IMPROVEMENTS
   - Before → After examples"""

    else:  # opening-hooks
        job_type = Prompt.ask("[green]What type of job?[/green]")
        
        console.print("\n[dim]One standout achievement:[/dim]")
        achievement = get_multiline_input("Enter achievement (type 'END' when done):")
        
        prompt = f"""Create opening hooks:

Job type: {job_type}
Key achievement: {achievement}

Provide:
1. 🎯 HOOK OPTIONS
   
   Option 1: Achievement Lead
   [Opening paragraph]
   
   Option 2: Passion Lead
   [Opening paragraph]
   
   Option 3: Connection Lead
   [Opening paragraph]
   
   Option 4: Bold Statement
   [Opening paragraph]
   
   Option 5: Story Lead
   [Opening paragraph]

2. 💡 WHEN TO USE EACH
   - Best context for each style

3. ⚠️ OPENINGS TO AVOID
   - Clichés to skip"""

    console.print("\n[yellow]Creating...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("✉️ Cover Letter", result, "green")

if __name__ == "__main__":
    run()
