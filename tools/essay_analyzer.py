"""Tool 1: Essay Structure Analyzer - Analyze and improve essay organization."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert writing instructor specializing in essay structure.

Essay structures:
- Five-paragraph essay
- Compare/contrast
- Cause and effect
- Problem-solution
- Argumentative
- Narrative
- Analytical

Structural elements:
- Introduction (hook, context, thesis)
- Body paragraphs (topic sentence, evidence, analysis, transition)
- Conclusion (synthesis, implications, call to action)

Evaluate logical flow, paragraph unity, and coherence."""

def run():
    console.print("[bold cyan]📝 Essay Structure Analyzer[/bold cyan]")
    console.print("[dim]Analyze and improve essay organization[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["analyze-essay", "create-outline", "fix-structure", "learn-structures"],
        default="analyze-essay"
    )
    
    if mode == "analyze-essay":
        console.print("\n[yellow]Paste your essay:[/yellow]")
        essay = get_multiline_input("Enter essay (type 'END' when done):")
        
        essay_type = Prompt.ask("[green]Essay type[/green]",
                               choices=["argumentative", "analytical", "narrative", "expository", "unknown"],
                               default="unknown")
        
        prompt = f"""Analyze this essay's structure:

Type: {essay_type}

Essay:
{essay}

Provide:
1. 📊 STRUCTURE ASSESSMENT
   - Overall organization score (1-10)
   - Essay type identified
   - Structure followed

2. 🎯 THESIS ANALYSIS
   - Thesis statement identified
   - Clarity and strength
   - Position in essay

3. 📋 PARAGRAPH BREAKDOWN
   For each paragraph:
   - Purpose
   - Topic sentence quality
   - Evidence/support
   - Connection to thesis
   - Transition quality

4. 🔄 LOGICAL FLOW
   - Progression of ideas
   - Coherence between paragraphs
   - Gap identification

5. ✅ STRENGTHS
   - What works well
   - Effective elements

6. ⚠️ ISSUES
   - Structural problems
   - Missing elements
   - Weak transitions

7. 🔧 RECOMMENDATIONS
   - Priority fixes
   - Reorganization suggestions
   - Outline of improved structure"""

    elif mode == "create-outline":
        topic = Prompt.ask("[green]Essay topic[/green]")
        essay_type = Prompt.ask("[green]Essay type[/green]",
                               choices=["argumentative", "analytical", "compare-contrast", "cause-effect", "narrative"],
                               default="argumentative")
        length = Prompt.ask("[green]Target length[/green]",
                           choices=["short (500 words)", "medium (1000 words)", "long (2000+ words)"],
                           default="medium (1000 words)")
        
        prompt = f"""Create essay outline:

Topic: {topic}
Type: {essay_type}
Length: {length}

Provide:
1. 📋 DETAILED OUTLINE
   I. Introduction
      A. Hook ideas
      B. Context
      C. Thesis statement
   
   II. Body Paragraphs
      For each:
      A. Topic sentence
      B. Evidence/points
      C. Analysis notes
      D. Transition idea
   
   III. Conclusion
      A. Synthesis
      B. Implications
      C. Closing

2. 🎯 THESIS OPTIONS
   - 2-3 thesis statement options

3. 📝 TOPIC SENTENCES
   - Draft topic sentence for each body paragraph

4. 🔗 TRANSITION SUGGESTIONS
   - Transition phrases between sections

5. 💡 TIPS
   - Key points to develop
   - Evidence to gather"""

    elif mode == "fix-structure":
        console.print("\n[yellow]Paste the essay with structural issues:[/yellow]")
        essay = get_multiline_input("Enter essay (type 'END' when done):")
        
        issues = Prompt.ask("[green]Main issues (optional)[/green]", default="general structure")
        
        prompt = f"""Fix this essay's structure:

Issues: {issues}

Essay:
{essay}

Provide:
1. 🔍 DIAGNOSIS
   - Main structural problems
   - Root causes

2. 📋 REORGANIZED OUTLINE
   - How to restructure

3. ✨ REWRITTEN SECTIONS
   - Fixed introduction
   - Improved transitions
   - Stronger conclusion

4. 📝 BEFORE/AFTER
   - Key improvements shown"""

    else:  # learn-structures
        prompt = """Teach essay structures:

1. 📚 ESSAY TYPES
   For each type:
   - When to use
   - Basic structure
   - Example outline

   Types:
   - Five-paragraph
   - Argumentative
   - Analytical
   - Compare/Contrast
   - Cause/Effect
   - Narrative

2. 🏗️ STRUCTURAL ELEMENTS
   - Introduction components
   - Body paragraph formula
   - Conclusion elements

3. 🔗 TRANSITIONS
   - Types of transitions
   - Example phrases

4. ✅ CHECKLIST
   - Self-review checklist"""

    console.print("\n[yellow]Analyzing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📝 Essay Structure Analysis", result, "blue")
    
    if Prompt.ask("\n[cyan]Save analysis?[/cyan]", choices=["y", "n"], default="n") == "y":
        filename = Prompt.ask("Filename", default="essay_analysis.md")
        with open(filename, 'w') as f:
            f.write(f"# Essay Structure Analysis\n\n{result}")
        console.print(f"[green]Saved to {filename}[/green]")

if __name__ == "__main__":
    run()
