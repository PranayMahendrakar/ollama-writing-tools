"""Tool 10: Cross-Cultural Communication Guide - Navigate cultural communication."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in cross-cultural communication and global business.

Cultural dimensions (Hofstede):
- Power distance
- Individualism vs Collectivism
- Masculinity vs Femininity
- Uncertainty avoidance
- Long-term orientation
- Indulgence

Communication styles:
- High-context vs Low-context
- Direct vs Indirect
- Formal vs Informal
- Linear vs Circular reasoning

Consider business etiquette, negotiation styles, and relationship building."""

def run():
    console.print("[bold cyan]🌍 Cross-Cultural Communication Guide[/bold cyan]")
    console.print("[dim]Navigate cultural communication differences[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["culture-guide", "adapt-message", "meeting-prep", "compare-cultures"],
        default="culture-guide"
    )
    
    if mode == "culture-guide":
        culture = Prompt.ask("[green]Which culture/region?[/green]")
        context = Prompt.ask("[green]Context[/green]",
                            choices=["business", "academic", "social", "negotiations"],
                            default="business")
        
        prompt = f"""Cultural communication guide:

Culture: {culture}
Context: {context}

Provide:
1. 📊 CULTURAL PROFILE
   - Communication style
   - High/Low context
   - Directness level
   - Formality expectations

2. 💬 COMMUNICATION NORMS
   - Greetings and titles
   - Small talk topics
   - Taboo subjects
   - Humor appropriateness

3. 📧 WRITTEN COMMUNICATION
   - Email style
   - Formality level
   - Response expectations

4. 🤝 MEETING ETIQUETTE
   - Punctuality norms
   - Decision-making style
   - Hierarchy in meetings

5. ⚠️ COMMON MISTAKES
   - What outsiders get wrong

6. ✅ DO's AND DON'Ts
   - Essential tips"""

    elif mode == "adapt-message":
        console.print("\n[yellow]Paste message to adapt:[/yellow]")
        message = get_multiline_input("Enter message (type 'END' when done):")
        
        target_culture = Prompt.ask("[green]Target culture[/green]")
        
        prompt = f"""Adapt this message:

Target culture: {target_culture}

Original:
{message}

Provide:
1. 🔍 CULTURAL ANALYSIS
   - What might not translate well
   - Potential misunderstandings

2. ✨ ADAPTED VERSION
   [Culturally appropriate version]

3. 📝 CHANGES MADE
   - Why each change was needed
   - Cultural reasoning

4. 💡 ADDITIONAL TIPS
   - Delivery considerations"""

    elif mode == "meeting-prep":
        cultures = Prompt.ask("[green]Cultures involved[/green]")
        meeting_type = Prompt.ask("[green]Meeting type[/green]",
                                 choices=["first-meeting", "negotiation", "presentation", "team-meeting"],
                                 default="first-meeting")
        
        prompt = f"""Prepare for cross-cultural meeting:

Cultures: {cultures}
Type: {meeting_type}

Provide:
1. 📋 PREPARATION CHECKLIST
   - Research to do
   - Materials to prepare

2. 🤝 OPENING THE MEETING
   - Greeting protocol
   - Introductions
   - Small talk

3. 💬 DURING THE MEETING
   - Communication style to use
   - Decision-making approach
   - Handling disagreement

4. ⏰ TIME & STRUCTURE
   - Punctuality expectations
   - Agenda flexibility

5. 🎯 CLOSING
   - How to end
   - Follow-up expectations

6. ⚠️ PITFALLS TO AVOID
   - Cultural missteps"""

    else:  # compare-cultures
        culture1 = Prompt.ask("[green]First culture[/green]")
        culture2 = Prompt.ask("[green]Second culture[/green]")
        
        prompt = f"""Compare communication cultures:

Culture 1: {culture1}
Culture 2: {culture2}

Provide:
1. 📊 COMPARISON TABLE
   | Aspect | {culture1} | {culture2} |
   - Communication style
   - Directness
   - Formality
   - Time orientation
   - Hierarchy

2. ⚡ KEY DIFFERENCES
   - Most important contrasts
   - Potential friction points

3. 🔗 COMMON GROUND
   - Shared values
   - Bridge points

4. 💡 BRIDGING STRATEGIES
   - How to communicate effectively
   - Meeting in the middle"""

    console.print("\n[yellow]Analyzing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🌍 Cultural Guide", result, "magenta")

if __name__ == "__main__":
    run()
