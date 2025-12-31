"""Tool 9: Email Etiquette Advisor - Write professional, effective emails."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in professional email communication.

Email principles:
- Clear subject lines
- Appropriate greeting/closing
- Concise body
- Clear action items
- Professional tone
- Proper formatting

Consider:
- Recipient relationship
- Cultural differences
- Urgency level
- CC/BCC etiquette
- Reply expectations"""

def run():
    console.print("[bold cyan]📧 Email Etiquette Advisor[/bold cyan]")
    console.print("[dim]Write professional, effective emails[/dim]\n")
    
    mode = Prompt.ask(
        "[green]What would you like?[/green]",
        choices=["review-email", "write-email", "difficult-email", "learn-etiquette"],
        default="review-email"
    )
    
    if mode == "review-email":
        console.print("\n[yellow]Paste your email draft:[/yellow]")
        email = get_multiline_input("Enter email (type 'END' when done):")
        
        context = Prompt.ask("[green]Context[/green]",
                            choices=["internal", "client", "vendor", "executive", "cold-outreach"],
                            default="internal")
        
        prompt = f"""Review this email:

Context: {context}

{email}

Provide:
1. 📊 OVERALL ASSESSMENT
   - Professional score (1-10)
   - Clarity score (1-10)
   - Likely effectiveness

2. ✅ WHAT WORKS
   - Strong elements

3. ⚠️ ISSUES
   - Tone problems
   - Clarity issues
   - Etiquette concerns

4. 📝 SUBJECT LINE
   - Current assessment
   - Better alternatives

5. ✨ IMPROVED VERSION
   [Professionally polished email]

6. 💡 TIPS
   - Key improvements made"""

    elif mode == "write-email":
        purpose = Prompt.ask("[green]Email purpose[/green]")
        recipient = Prompt.ask("[green]Recipient relationship[/green]",
                              choices=["boss", "colleague", "client", "vendor", "stranger", "team"],
                              default="colleague")
        tone = Prompt.ask("[green]Desired tone[/green]",
                         choices=["formal", "friendly-professional", "casual", "urgent"],
                         default="friendly-professional")
        
        console.print("\n[dim]Key points to include:[/dim]")
        points = get_multiline_input("Enter key points (type 'END' when done):")
        
        prompt = f"""Write an email:

Purpose: {purpose}
Recipient: {recipient}
Tone: {tone}
Key points: {points}

Provide:
1. 📧 COMPLETE EMAIL
   Subject: [Effective subject line]
   
   [Full email body]

2. 🔄 ALTERNATIVE VERSIONS
   - More formal option
   - Shorter option

3. 💡 SENDING TIPS
   - Best time to send
   - Follow-up timing"""

    elif mode == "difficult-email":
        situation = Prompt.ask("[green]Situation[/green]",
                              choices=["declining-request", "giving-feedback", "apologizing", 
                                      "following-up", "asking-favor", "bad-news"],
                              default="giving-feedback")
        
        console.print("\n[yellow]Describe the situation:[/yellow]")
        details = get_multiline_input("Enter details (type 'END' when done):")
        
        prompt = f"""Write a difficult email:

Situation: {situation}
Details: {details}

Provide:
1. 📧 RECOMMENDED EMAIL
   [Tactfully written email]

2. 🎯 KEY TECHNIQUES
   - How to soften the message
   - Maintaining relationship

3. ⚠️ WHAT TO AVOID
   - Phrases that backfire
   - Tone pitfalls

4. 🔄 ALTERNATIVE APPROACHES
   - Different framings"""

    else:  # learn-etiquette
        prompt = """Teach email etiquette:

1. 📧 EMAIL STRUCTURE
   - Subject line best practices
   - Greeting options by context
   - Body structure
   - Closing options

2. 🎯 TONE GUIDE
   - Formal vs casual markers
   - Phrases to use/avoid
   - Cultural considerations

3. ⚡ ACTION ITEMS
   - Making requests clear
   - Setting expectations
   - Following up

4. 👥 CC/BCC ETIQUETTE
   - When to use each
   - Reply-all guidelines

5. ⚠️ COMMON MISTAKES
   - Top 10 email errors

6. ✅ CHECKLIST
   - Before-sending checklist"""

    console.print("\n[yellow]Processing...[/yellow]\n")
    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📧 Email Advisor", result, "cyan")

if __name__ == "__main__":
    run()
