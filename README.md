# 🌿 Plant Stress AI Review Bot

A Semi-Automated Systematic Literature Review (SLR) Automation Tool for AI & Plant Imaging Research

---

Plant Stress AI Review Bot is a Python-based automation framework designed to perform large-scale systematic literature searches using programmable GUI bots.

It was originally developed to support the publication:

Walsh, J.J., Mangina, E., & Negrão, S. (2024). *Advancements in Imaging Sensors and AI for Plant Stress Detection: A Systematic Literature Review*. Plant Phenomics. https://doi.org/10.34133/plantphenomics.0153

The Plant Stress AI Review Bot automates repetitive database search tasks across multiple journal platforms using coordinate-driven interaction via PyAutoGUI.

---

## 🚀 What This Tool Does

The Plant Stress AI Review Bot enables researchers to:

- 🔍 Perform automated keyword-based database searches
- 📚 Systematically query multiple journal repositories
- 📊 Log study counts into structured spreadsheets
- 🗂 Archive search outputs into Zotero
- 🔁 Iterate thousands of search combinations
- 🧠 Reduce human error in repetitive SLR workflows

This bot was designed specifically for systematic review automation — not general web scraping.

---

## 🧠 Core Concept

Instead of manually performing thousands of search queries across academic databases, the Plant Stress AI Review Bot:

1. Uses predefined keyword groups:
   - Root keys (e.g., abiotic stress)
   - Parent keys (e.g., hyperspectral imaging)
   - Child keys (e.g., supervised learning)

2. Iteratively constructs search strings.

3. Navigates database interfaces via pixel-coordinate automation.

4. Records outputs into structured datasets.

The original SLR executed:

- 6 root keys  
- 56 parent keys  
- 14 child keys  
- Across 4 databases  
- Totaling **28,224 automated searches**

---

## 🖥 Software Architecture

From `Bot.py`:

- Automation Engine: PyAutoGUI
- Clipboard Handling: Pyperclip
- Timing Control: time
- Execution Environment: Ubuntu (tested), adaptable to any OS

This bot is **resolution-dependent** and must be customized to your screen.

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/plant-stress-ai-review-bot.git
cd plant-stress-ai-review-bot
```

### 2️⃣ Install Dependencies

```bash
python install.py
```

Or manually:

```bash
pip install pyautogui pyperclip
```

---

## ⚙️ Configuration (Important)

This bot **will not work out-of-the-box** without customization.

Before running:

### 1. Update Pixel Coordinates

Inside `Bot.py`, adjust:

- Screen resolution values
- X/Y click positions
- Row/column offsets
- Scroll positions
- Button locations

These must match your monitor and database layout.

The bot was originally built using:

```
1920 x 1080 resolution
Ubuntu OS
OneSearch database
```

If using another database (e.g., Google Scholar), you must redesign the navigation logic.

---

### 2. Adjust Runtime Controls

Inside the script:

```python
bot.PAUSE = 1.0
bot.FAILSAFE = False
```

- Increase `PAUSE` if pages load slowly.
- Enable `FAILSAFE = True` for safety (move mouse to top-left corner to abort).

---

## ▶️ Running the Bot

Once configured:

```bash
python Bot.py
```

The bot will:

- Navigate to target applications
- Perform database searches
- Extract result counts
- Log outputs into spreadsheets
- Continue iteratively

⚠️ Do not touch the keyboard or mouse during execution.

---

## 🧩 Project Structure

```
Plant-Stress-AI-Review-Bot/
│
├── Bot.py
├── install.py
├── README.md
└── LICENSE
```

---

## ⚠️ Limitations

- Fully dependent on screen resolution
- Sensitive to UI layout changes
- Not robust against CAPTCHA systems
- Requires Zotero pre-configured (if archiving enabled)
- Designed for academic database interfaces

This is not an API-based scraper — it is GUI automation.

---

## 🔐 Disclaimer

This tool interacts with live journal databases.  
Users are fully responsible for:

- Complying with database terms of service
- Ensuring institutional access permissions
- Avoiding excessive query rates

The authors accept no liability for misuse.

---

## 📖 Citation

If you use this bot in academic research, please cite:

Walsh, J.J., Mangina, E., & Negrão, S. (2024). *Advancements in Imaging Sensors and AI for Plant Stress Detection: A Systematic Literature Review*. Plant Phenomics. https://doi.org/10.34133/plantphenomics.0153

---

## 🤝 Contributing

Contributions welcome.

- Fork the repository
- Create a new branch
- Submit a pull request

---

## 🌿 Acknowledgements

University College Dublin School of Biology & Environmental Science and the School of Computer Science
