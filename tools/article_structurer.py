"""Tool 11: Journal Article Structurer - Structure academic papers properly."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in academic writing and journal publication.

Article structures:
- IMRaD (Introduction, Methods, Results, Discussion)
- Theory-based
- Case study
- Review article
- Meta-analysis

Key elements:
- Abstract (structured vs unstructured)
- Literature review
- Research questions/hypotheses
- Methodology section
- Results presentation
- Discussion and implications
- Limitations and future research"""

def run():
    console.print("[bold cyan]📚 Journal Article Structurer[/bold cyan]")
    console.print("[dim]Structure academic papers properly[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["create-structure", "review-structure", "write-section", "abstract-help"],
        default="create-structure"
    )
    
    if mode == "create-structure":
        field = Prompt.ask("[green]Academic field[/green]")
        article_type = Prompt.ask("[green]Article type[/green]",
                                 choices=["empirical", "theoretical", "review", "case-study", "meta-analysis"],
                                 default="empirical")
        
        console.print("\n[yellow]Describe your research:[/yellow]")
        research = get_multiline_input("Enter description (type 'END' when done):")
        
        prompt = f"""Create article structure:

Field: {field}
Type: {article_type}
Research: {research}

Provide:
1. 📋 FULL OUTLINE
   For each section:
   - Purpose
   - Key elements
   - Approximate length
   - What to include

2. 📝 SECTION GUIDANCE
   - Title options
   - Abstract structure
   - Introduction framework
   - Literature review organization
   - Methods components
   - Results presentation
   - Discussion flow
   - Conclusion elements

3. 🎯 KEY REQUIREMENTS
   - What journals expect
   - Common structure for {field}

4. ⚠️ COMMON MISTAKES
   - What to avoid

5. ✅ CHECKLIST
   - Pre-submission checklist"""

    elif mode == "review-structure":
        console.print("\n[yellow]Paste your article or outline:[/yellow]")
        article = get_multiline_input("Enter content (type 'END' when done):")
        
        prompt = f"""Review article structure:

{article}

Provide:
1. 📊 STRUCTURE ASSESSMENT
   - Overall organization
   - Section balance
   - Flow and logic

2. ✅ STRENGTHS
   - Well-structured elements

3. ⚠️ ISSUES
   - Missing sections
   - Structural problems
   - Balance issues

4. 🔧 RECOMMENDATIONS
   - Reorganization suggestions
   - Section improvements

5. 📋 REVISED OUTLINE
   - Improved structure"""

    elif mode == "write-section":
        section = Prompt.ask("[green]Which section?[/green]",
                            choices=["abstract", "introduction", "literature-review", 
                                    "methods", "results", "discussion", "conclusion"],
                            default="introduction")
        
        console.print("\n[yellow]Describe what to include:[/yellow]")
        content = get_multiline_input("Enter content/notes (type 'END' when done):")
        
        prompt = f"""Help write {section} section:

Notes/Content:
{content}

Provide:
1. 📝 SECTION DRAFT
   [Well-structured {section}]

2. 🎯 KEY ELEMENTS
   - What's included
   - Why each matters

3. 📋 CHECKLIST
   - {section.title()} requirements

4. 💡 TIPS
   - Common pitfalls to avoid"""

    else:  # abstract-help
        console.print("\n[yellow]Describe your research for abstract:[/yellow]")
        research = get_multiline_input("Enter research summary (type 'END' when done):")
        
        word_limit = Prompt.ask("[green]Word limit[/green]", default="250")
        
        prompt = f"""Write abstract:

Research: {research}
Word limit: {word_limit}

Provide:
1. 📝 STRUCTURED ABSTRACT
   - Background
   - Objective
   - Methods
   - Results
   - Conclusions
   
   [Within {word_limit} words]

2. 📝 UNSTRUCTURED VERSION
   [Paragraph format]

3. 🎯 KEYWORDS
   - Suggested keywords

4. 💡 ABSTRACT TIPS
   - What makes it effective"""

    console.print("\n[yellow]Processing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📚 Article Structure", result, "blue")

if __name__ == "__main__":
    run()
