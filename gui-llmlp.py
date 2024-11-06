import requests
import spacy
from fuzzywuzzy import fuzz
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QPushButton, 
                             QVBoxLayout, QWidget, QLabel, QTextEdit, QComboBox, QHBoxLayout)
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt

# Load spaCy's English NLP model
nlp = spacy.load("en_core_web_sm")

# Pattern matching phrases to identify topics
patterns = [
    "I want to learn about", "Tell me about", "I'm interested in",
    "What is", "What are", "Explain", "Give me information about",
    "Who was", "Who is", "How does", "I’m curious about", "I’d like to know about",
    "Tell me more about", "Can you explain", "Could you tell me about",
    "Help me understand", "Teach me about", "Describe", "I need help with",
    "I need information on", "Help me study", "Prepare me for",
    "I want details on", "I am learning about"
]

# Function to clean and extract topic from user input
def extract_topic_from_input(user_input):
    doc = nlp(user_input)
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            return token.text
    for pattern in patterns:
        if fuzz.partial_ratio(pattern.lower(), user_input.lower()) > 70:
            topic = user_input.lower().replace(pattern.lower(), "").strip()
            if topic:
                return topic
    return user_input

# Wikipedia API Function
def fetch_wikipedia_summary(topic):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": topic,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True
    }
    response = requests.get(url, params=params)
    data = response.json()
    pages = data.get("query", {}).get("pages", {})
    for page_id, page_info in pages.items():
        if "extract" in page_info:
            return page_info["extract"]
    return "No information found on Wikipedia for this topic."

# Function to format content based on selected style
def format_content(content, format_type):
    if format_type == "Lesson Plan":
        return f"Lesson Plan on {content[:30]}...\n\nObjectives:\n- Understand {content[:30]}\n\nMaterials Needed:\n- Pen, Paper\n\nLesson Outline:\n{content}"
    
    elif format_type == "Presentation Outline":
        return f"Presentation on {content[:30]}...\n\nSlide 1: Introduction\n- {content[:100]}...\n\nSlide 2: Key Points\n- {content[100:200]}...\n\nSlide 3: Conclusion"
    
    elif format_type == "Song":
        lines = content.split(". ")
        return "\n".join([f"{line} 🎶" for line in lines[:6]])

    else:
        return content  # Default to plain text

# Function to generate the lesson plan with Wikipedia content in specified format
def generate_formatted_content(user_input, format_type):
    topic = extract_topic_from_input(user_input)
    wikipedia_info = fetch_wikipedia_summary(topic)
    formatted_content = format_content(wikipedia_info, format_type)
    return formatted_content

# PyQt5 app structure
class LessonPlanApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up window
        self.setWindowTitle("Enhanced Lesson Plan Generator")
        self.setGeometry(200, 200, 1000, 700)
        
        # Set modern color palette styles
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: #363537;
            }}
            QLabel {{
                font-size: 16px;
                color: #fffffc;
            }}
            QLineEdit, QTextEdit {{
                border: 1px solid #beb7a4;
                padding: 6px;
                font-size: 14px;
                background-color: #beb7a4;
                color: #363537;
            }}
            QComboBox {{
                padding: 8px;
                font-size: 14px;
                background-color: #beb7a4;
                color: #363537;
            }}
            QPushButton {{
                padding: 8px;
                font-size: 14px;
                background-color: #ff7f11;
                color: #fffffc;
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: #ff3f00;
            }}
        """)

        # Main layout for the central widget
        self.layout = QVBoxLayout()

        # Input prompt and text box for topic
        self.topic_label = QLabel("Enter your topic or request (e.g., 'Explain photosynthesis')")
        self.layout.addWidget(self.topic_label)
        
        self.topic_input = QLineEdit()
        self.layout.addWidget(self.topic_input)

        # Format dropdown setup
        self.format_label = QLabel("Choose your preferred output format")
        self.layout.addWidget(self.format_label)
        
        self.format_dropdown = QComboBox()
        self.format_dropdown.addItems(["Plain Text", "Lesson Plan", "Presentation Outline", "Song"])
        self.layout.addWidget(self.format_dropdown)
        
        # Generate button
        self.generate_button = QPushButton("Generate Lesson Content")
        self.generate_button.clicked.connect(self.generate_content)
        self.layout.addWidget(self.generate_button)
        
        # Output label and text display for generated content
        self.output_label = QLabel("Your generated content:")
        self.layout.addWidget(self.output_label)

        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        self.output_display.setStyleSheet("background-color: #beb7a4; border: 1px solid #CCC; padding: 10px; font-size: 14px; color: #363537;")
        self.layout.addWidget(self.output_display)
        
        # Set central widget
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def generate_content(self):
        user_input = self.topic_input.text()
        format_type = self.format_dropdown.currentText()
        content = generate_formatted_content(user_input, format_type)
        self.output_display.setPlainText(content)

# Run the app
app = QApplication([])
window = LessonPlanApp()
window.show()
app.exec_()
