"""Tool 14: Peer Review Response Helper - Respond to peer reviews professionally."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in academic peer review and journal publication.

Response principles:
- Thank reviewers genuinely
- Address every point
- Be respectful even if disagreeing
- Provide evidence for responses
- Show changes clearly
- Maintain professional tone

Response types:
- Accept and revise
- Partially accept
- Respectfully disagree
- Request clarification"""

def run():
    console.print("[bold cyan]📋 Peer Review Response Helper[/bold cyan]")
    console.print("[dim]Respond to peer reviews professionally[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["respond-to-review", "response-letter", "handle-rejection", "tips"],
        default="respond-to-review"
    )
    
    if mode == "respond-to-review":
        console.print("\n[yellow]Paste reviewer comment:[/yellow]")
        comment = get_multiline_input("Enter comment (type 'END' when done):")
        
        response_type = Prompt.ask("[green]Your response type[/green]",
                                  choices=["accept", "partially-accept", "disagree", "need-clarification"],
                                  default="accept")
        
        console.print("\n[dim]What did you do to address it (if applicable)?[/dim]")
        action = get_multiline_input("Enter action taken (or 'END' to skip):")
        
        prompt = f"""Draft response to reviewer:

Reviewer comment:
{comment}

Response type: {response_type}
{"Action taken: " + action if action.strip() else ""}

Provide:
1. 📝 RESPONSE
   [Professional, complete response]

2. 🎯 KEY ELEMENTS
   - How gratitude is expressed
   - How concerns are addressed
   - Evidence/justification provided

3. 🔄 ALTERNATIVE PHRASINGS
   - Different ways to express same response

4. ⚠️ TONE CHECK
   - Ensure appropriate tone
   - Avoid defensive language

5. 📋 MANUSCRIPT CHANGES
   - Summary of revisions made"""

    elif mode == "response-letter":
        console.print("\n[yellow]Paste all reviewer comments:[/yellow]")
        comments = get_multiline_input("Enter comments (type 'END' when done):")
        
        prompt = f"""Create complete response letter:

Reviewer comments:
{comments}

Provide:
1. 📝 RESPONSE LETTER
   
   [Complete formatted response letter including:]
   - Opening to editor
   - General response
   - Point-by-point responses
   - Closing

2. 📋 RESPONSE SUMMARY TABLE
   | Comment | Response Type | Page/Line |

3. 💡 TIPS FOR THIS REVISION
   - Key areas to strengthen"""

    elif mode == "handle-rejection":
        console.print("\n[yellow]Paste rejection feedback:[/yellow]")
        feedback = get_multiline_input("Enter feedback (type 'END' when done):")
        
        prompt = f"""Handle rejection constructively:

Feedback:
{feedback}

Provide:
1. 🔍 FEEDBACK ANALYSIS
   - Main concerns
   - Fixable issues
   - Fundamental problems

2. 🎯 DECISION FRAMEWORK
   - Revise and resubmit here?
   - Submit elsewhere?
   - Major revision needed?

3. 📝 REVISION PLAN
   - Priority changes
   - How to address each concern

4. ✉️ APPEAL OPTION (if appropriate)
   - When to appeal
   - How to write appeal

5. 💪 CONSTRUCTIVE FRAMING
   - Learning from feedback"""

    else:  # tips
        prompt = """Peer review response best practices:

1. 📋 RESPONSE STRUCTURE
   - Opening
   - Point-by-point format
   - Closing

2. 💬 LANGUAGE GUIDE
   - Phrases for agreeing
   - Phrases for disagreeing
   - Expressing gratitude

3. ⚠️ WHAT TO AVOID
   - Defensive language
   - Dismissive responses
   - Incomplete addressing

4. 🔧 REVISION TRACKING
   - How to show changes
   - Color coding
   - Line references

5. ⏰ TIMELINE TIPS
   - How long to respond
   - Requesting extensions

6. ✅ CHECKLIST
   - Before submitting revision"""

    console.print("\n[yellow]Processing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📋 Peer Review Response", result, "cyan")

if __name__ == "__main__":
    run()
