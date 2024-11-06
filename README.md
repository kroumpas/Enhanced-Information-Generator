# Enhanced Lesson Plan Generator

This project is a GUI application for generating educational content in different formats (Lesson Plan, Presentation Outline, Song, or Plain Text) based on user-provided topics. The app uses the Wikipedia API to fetch relevant information, and PyQt5 for a user-friendly interface. The app can also interpret natural language queries such as "Tell me about photosynthesis" or "I want to learn about photosynthesis."

## Features

- **Natural Language Understanding**: Recognizes different ways to ask about a topic (e.g., "Explain photosynthesis").
- **Wikipedia API Integration**: Fetches topic summaries directly from Wikipedia.
- **Flexible Output Formats**: Provides content in multiple formats including Lesson Plans, Presentation Outlines, and Songs.
- **Modern UI**: Uses a cohesive color palette with an attractive, intuitive layout.

## Installation

### Prerequisites

- Python 3.7 or higher

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Enhanced-Lesson-Plan-Generator.git
   cd Enhanced-Lesson-Plan-Generator
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Download the ```en_core_web_sm``` model for spaCy:
    ```bash
    python -m spacy download en_core_web_sm
    ```

## Usage
Run the application with:
```bash
python gui-llmlp.py
```
### Once the app is open:

1. Enter a topic or question, e.g., "Explain photosynthesis" or "What is gravity?"
2. Choose an output format from the dropdown menu.
3. Click "Generate Lesson Content" to display the formatted content in the selected format.
### Example Queries
- "Tell me about World War II"
- "I need information on photosynthesis"
- "Can you explain quantum mechanics?"
### Project Structure
- ```gui-llmlp.py```: The main application file containing GUI code and logic.
- ```requirements.txt```: Lists all required Python packages.
- ```README.md```: Project documentation.
### Requirements
See ```requirements.txt``` for the complete list of dependencies.

## Built With
- PyQt5 for the GUI
- spaCy and fuzzywuzzy for natural language processing
- Wikipedia API for fetching topic summaries
- Python 3.7+
## Future Enhancements
- Support for more output formats (e.g., quiz, interactive activity).
- Ability to pull information from multiple sources beyond Wikipedia.
- Customizable lesson plans with user-defined objectives and materials.