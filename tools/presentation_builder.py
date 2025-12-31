"""Tool 15: Conference Presentation Builder - Create effective presentations."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in academic and professional presentations.

Presentation elements:
- Strong opening hook
- Clear structure
- Visual design principles
- Speaker notes
- Timing and pacing
- Q&A preparation
- Handouts/supplements

Presentation types:
- Conference paper
- Poster session
- Keynote
- Workshop
- Lightning talk
- Thesis defense"""

def run():
    console.print("[bold cyan]🎪 Conference Presentation Builder[/bold cyan]")
    console.print("[dim]Create effective presentations[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["create-outline", "slide-content", "speaker-notes", "poster-design"],
        default="create-outline"
    )
    
    if mode == "create-outline":
        console.print("\n[yellow]Describe your presentation topic:[/yellow]")
        topic = get_multiline_input("Enter topic (type 'END' when done):")
        
        duration = Prompt.ask("[green]Duration[/green]",
                             choices=["5 min", "10 min", "15 min", "20 min", "30 min", "45 min"],
                             default="15 min")
        
        pres_type = Prompt.ask("[green]Presentation type[/green]",
                              choices=["research", "practice", "workshop", "lightning", "keynote"],
                              default="research")
        
        prompt = f"""Create presentation outline:

Topic: {topic}
Duration: {duration}
Type: {pres_type}

Provide:
1. 📋 SLIDE-BY-SLIDE OUTLINE
   For each slide:
   - Slide title
   - Key points (3-5 max)
   - Visual suggestion
   - Time allocation

2. 🎯 OPENING (First 2 min)
   - Hook options
   - Roadmap slide

3. 📊 BODY STRUCTURE
   - Main sections
   - Flow between sections

4. 🎬 CLOSING
   - Summary approach
   - Call to action
   - Final slide

5. ⏱️ TIMING GUIDE
   - Section breakdowns
   - Buffer time

6. 💡 DESIGN TIPS
   - Visual themes
   - Font/color suggestions"""

    elif mode == "slide-content":
        slide_topic = Prompt.ask("[green]Slide topic[/green]")
        slide_type = Prompt.ask("[green]Slide type[/green]",
                               choices=["title", "content", "data", "quote", "comparison", "summary"],
                               default="content")
        
        console.print("\n[dim]Key points for this slide:[/dim]")
        points = get_multiline_input("Enter points (type 'END' when done):")
        
        prompt = f"""Create slide content:

Topic: {slide_topic}
Type: {slide_type}
Points: {points}

Provide:
1. 📝 SLIDE CONTENT
   Title: [Concise, engaging title]
   
   Bullet points:
   - [Clear, concise points]
   
   Visual: [Suggested graphic/image]

2. 🎤 SPEAKER NOTES
   [What to say for this slide - 1-2 minutes]

3. 🔄 ALTERNATIVES
   - Different title options
   - Alternative visualizations

4. 💡 DESIGN TIP
   - Best way to present this"""

    elif mode == "speaker-notes":
        console.print("\n[yellow]Paste your slide content/outline:[/yellow]")
        slides = get_multiline_input("Enter slides (type 'END' when done):")
        
        prompt = f"""Create speaker notes:

Slides:
{slides}

Provide:
1. 🎤 FULL SPEAKER NOTES
   For each slide:
   - What to say
   - Key phrases to emphasize
   - Transitions to next slide
   - Timing notes

2. 💬 OPENING SCRIPT
   - First 30 seconds verbatim

3. 🔗 TRANSITION PHRASES
   - Between each section

4. 🎯 KEY PHRASES
   - Memorable lines to nail

5. 📋 CUE CARDS
   - Abbreviated notes version"""

    else:  # poster-design
        console.print("\n[yellow]Describe your research/topic:[/yellow]")
        research = get_multiline_input("Enter research summary (type 'END' when done):")
        
        prompt = f"""Design conference poster:

Research:
{research}

Provide:
1. 📋 POSTER STRUCTURE
   Section layout:
   - Title bar
   - Introduction
   - Methods
   - Results
   - Conclusions
   - References

2. 📝 SECTION CONTENT
   For each section:
   - Word count limit
   - Key points
   - Visual suggestions

3. 🎨 DESIGN RECOMMENDATIONS
   - Color scheme
   - Font choices
   - Visual hierarchy

4. 📊 FIGURE SUGGESTIONS
   - What to visualize
   - Graph types

5. 💡 POSTER TIPS
   - Standing out
   - Conversation starters

6. 🎤 ELEVATOR PITCH
   - 1-minute poster summary"""

    console.print("\n[yellow]Building presentation...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🎪 Presentation", result, "magenta")
    
    if Prompt.ask("\n[cyan]Save presentation plan?[/cyan]", choices=["y", "n"], default="y") == "y":
        filename = Prompt.ask("Filename", default="presentation_plan.md")
        with open(filename, 'w') as f:
            f.write(f"# Presentation Plan\n\n{result}")
        console.print(f"[green]Saved to {filename}[/green]")

if __name__ == "__main__":
    run()
