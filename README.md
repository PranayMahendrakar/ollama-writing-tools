# ✍️ Ollama Writing & Communication Tools

**15 AI-Powered Tools for Writers and Communicators**

A collection of local LLM-powered tools built with [Ollama](https://ollama.ai) to assist with writing, editing, communication, and presentation skills.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Ollama](https://img.shields.io/badge/Ollama-Required-orange.svg)

## 📋 Tools Included

| # | Tool | Description |
|---|------|-------------|
| 1 | **Essay Structure Analyzer** | Analyze and improve essay organization |
| 2 | **Topic Sentence Generator** | Create effective topic sentences |
| 3 | **Argument Strength Evaluator** | Evaluate and strengthen arguments |
| 4 | **Persuasive Writing Coach** | Master persuasive techniques |
| 5 | **Tone Consistency Checker** | Ensure consistent tone throughout |
| 6 | **Public Speaking Coach** | Prepare and deliver great speeches |
| 7 | **Storytelling Structure Guide** | Craft compelling narratives |
| 8 | **Technical Writing Simplifier** | Make complex content accessible |
| 9 | **Email Etiquette Advisor** | Write professional emails |
| 10 | **Cross-Cultural Communication** | Navigate cultural differences |
| 11 | **Journal Article Structurer** | Structure academic papers (IMRaD) |
| 12 | **Cover Letter Customizer** | Create tailored cover letters |
| 13 | **Grant Writing Assistant** | Write compelling grant proposals |
| 14 | **Peer Review Response Helper** | Respond to peer reviews professionally |
| 15 | **Conference Presentation Builder** | Create effective presentations |

## 🚀 Quick Start

### Prerequisites

1. **Install Ollama** (https://ollama.ai)
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

2. **Pull a model**
   ```bash
   ollama pull llama3.2
   ```

3. **Start Ollama**
   ```bash
   ollama serve
   ```

### Installation

```bash
cd ollama-writing-tools
pip install -r requirements.txt
python main.py
```

## 📖 Tool Details

### 1. Essay Structure Analyzer
- Five-paragraph, argumentative, analytical structures
- Thesis identification and evaluation
- Paragraph-by-paragraph breakdown
- Flow and coherence analysis

### 2. Topic Sentence Generator
- Generate topic sentences aligned to thesis
- Multiple options per paragraph
- Transition integration
- Alignment checking

### 3. Argument Strength Evaluator
- Toulmin model analysis
- Logical fallacy detection
- Evidence quality assessment
- Counter-argument generation

### 4. Persuasive Writing Coach
- Rhetorical appeals (ethos, pathos, logos)
- Cialdini's persuasion principles
- Power words and techniques
- Call-to-action crafting

### 5. Tone Consistency Checker
- Tone identification across text
- Consistency scoring
- Tone adjustment guidance
- Tone matching capability

### 6. Public Speaking Coach
- Speech writing
- Delivery notes and tips
- Q&A preparation
- Handling nerves

### 7. Storytelling Structure Guide
- Three-act, Hero's Journey, Story Circle
- Character and conflict design
- Pacing and tension
- Narrative problem-solving

### 8. Technical Writing Simplifier
- Plain language conversion
- Jargon elimination
- Audience adaptation
- Reading level optimization

### 9. Email Etiquette Advisor
- Professional email review
- Difficult email handling
- Tone and formality guidance
- Cultural considerations

### 10. Cross-Cultural Communication
- Culture-specific guides
- Message adaptation
- Meeting preparation
- Cultural comparison

### 11. Journal Article Structurer
- IMRaD structure guidance
- Section-by-section help
- Abstract writing
- Academic conventions

### 12. Cover Letter Customizer
- Job-tailored letters
- Achievement highlighting
- Opening hook variations
- ATS optimization tips

### 13. Grant Writing Assistant
- Proposal sections
- Needs statements
- SMART objectives
- Budget narratives

### 14. Peer Review Response Helper
- Point-by-point responses
- Professional disagreement
- Revision tracking
- Response letter formatting

### 15. Conference Presentation Builder
- Slide outlines
- Speaker notes
- Poster design
- Timing guidance

## 📁 Project Structure

```
ollama-writing-tools/
├── main.py                     # Main menu
├── requirements.txt            # Dependencies
├── README.md                   # This file
└── tools/
    ├── __init__.py
    ├── base.py                 # Shared utilities
    ├── essay_analyzer.py       # Tool 1
    ├── topic_sentence.py       # Tool 2
    ├── argument_evaluator.py   # Tool 3
    ├── persuasive_coach.py     # Tool 4
    ├── tone_checker.py         # Tool 5
    ├── speaking_coach.py       # Tool 6
    ├── storytelling_guide.py   # Tool 7
    ├── tech_simplifier.py      # Tool 8
    ├── email_advisor.py        # Tool 9
    ├── cultural_guide.py       # Tool 10
    ├── article_structurer.py   # Tool 11
    ├── cover_letter.py         # Tool 12
    ├── grant_writing.py        # Tool 13
    ├── peer_review.py          # Tool 14
    └── presentation_builder.py # Tool 15
```

## ⚙️ Configuration

Change the default model in `tools/base.py`:
```python
DEFAULT_MODEL = "llama3.2"
```

## 📝 License

MIT License - Free to use and modify!

---

**Happy Writing! ✍️**
