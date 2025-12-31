"""Tool 6: Public Speaking Coach - Prepare and deliver great speeches."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert public speaking coach and speechwriter.

Speech elements:
- Opening hook
- Clear structure
- Memorable phrases
- Stories and examples
- Transitions
- Call to action
- Strong close

Delivery aspects:
- Pacing and pauses
- Vocal variety
- Body language cues
- Audience engagement
- Handling nerves"""

def run():
    console.print("[bold cyan]🎤 Public Speaking Coach[/bold cyan]")
    console.print("[dim]Prepare and deliver great speeches[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["write-speech", "improve-speech", "practice-tips", "handle-qa"],
        default="write-speech"
    )
    
    if mode == "write-speech":
        topic = Prompt.ask("[green]Speech topic[/green]")
        duration = Prompt.ask("[green]Duration[/green]", 
                             choices=["2 min", "5 min", "10 min", "20 min"],
                             default="5 min")
        occasion = Prompt.ask("[green]Occasion[/green]",
                             choices=["conference", "meeting", "wedding", "graduation", "pitch", "other"],
                             default="conference")
        
        prompt = f"""Write a speech:

Topic: {topic}
Duration: {duration}
Occasion: {occasion}

Provide:
1. 📝 FULL SPEECH
   [Complete speech with timing notes]

2. 🎯 STRUCTURE BREAKDOWN
   - Hook (first 30 seconds)
   - Main points
   - Transitions
   - Memorable moments
   - Closing

3. 💬 KEY QUOTES
   - Tweetable lines
   - Applause points

4. 🎭 DELIVERY NOTES
   - [PAUSE] markers
   - [EMPHASIZE] markers
   - Gesture suggestions

5. 📋 SPEAKER NOTES
   - Key word outline
   - Memory triggers"""

    elif mode == "improve-speech":
        console.print("\n[yellow]Paste your speech draft:[/yellow]")
        speech = get_multiline_input("Enter speech (type 'END' when done):")
        
        prompt = f"""Improve this speech:

{speech}

Provide:
1. 📊 ASSESSMENT
   - Strengths
   - Weaknesses
   - Impact potential

2. 🎯 OPENING
   - Current opening analysis
   - Stronger alternatives

3. 📝 STRUCTURE
   - Flow improvements
   - Better transitions

4. 💪 LANGUAGE
   - Weak phrases → Strong phrases
   - Added power words
   - Rhetorical devices

5. 🎭 CLOSING
   - Current close analysis
   - More memorable ending

6. ✨ IMPROVED VERSION
   [Full rewritten speech]"""

    elif mode == "practice-tips":
        speech_type = Prompt.ask("[green]Type of speech[/green]", default="presentation")
        concern = Prompt.ask("[green]Main concern[/green]",
                            choices=["nerves", "memory", "engagement", "timing", "questions"],
                            default="nerves")
        
        prompt = f"""Speaking practice tips:

Speech type: {speech_type}
Main concern: {concern}

Provide:
1. 🎯 ADDRESSING {concern.upper()}
   - Specific strategies
   - Exercises to try
   - Mental techniques

2. 🗣️ VOCAL TECHNIQUES
   - Pace control
   - Volume variation
   - Pause usage
   - Filler word elimination

3. 🤸 BODY LANGUAGE
   - Stance and movement
   - Hand gestures
   - Eye contact
   - Facial expressions

4. 📋 PRACTICE ROUTINE
   - Day-before checklist
   - Morning-of routine
   - Last-minute prep

5. 💡 PRO TIPS
   - Expert secrets"""

    else:  # handle-qa
        topic = Prompt.ask("[green]Presentation topic[/green]")
        
        prompt = f"""Prepare for Q&A:

Topic: {topic}

Provide:
1. ❓ ANTICIPATED QUESTIONS
   - 10 likely questions
   - Difficult questions

2. 💬 ANSWER FRAMEWORKS
   - PREP method
   - Bridge technique
   - Acknowledge-Bridge-Communicate

3. 🛡️ HANDLING TOUGH QUESTIONS
   - Hostile questions
   - "I don't know" gracefully
   - Off-topic redirects

4. 💡 Q&A TIPS
   - Opening the floor
   - Managing time
   - Closing Q&A"""

    console.print("\n[yellow]Preparing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🎤 Speaking Coach", result, "green")

if __name__ == "__main__":
    run()
