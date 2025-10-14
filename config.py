# config.py

GEMINI_API_KEY = "your-google-gemini-api-key-here"  # Replace with your actual API key

BANNER_PATH = "assets/banner.png"
PROMPT_TEMPLATE_PATH = "templates/event_prompt.txt"
DEFAULT_COLLEGE = "Pimpri Chinchwad College Of Engineering"
DEFAULT_DEPARTMENT = "Department of CSE(AIML)"

OUTPUT_DIR = "generated_reports"
THEMES = {
    "Academic Blue": {
        "heading_color": "1F4E79",  # Professional blue
        "font": "Calibri",
        "title_size": 16,
        "heading_size": 14,
        "body_size": 11,
        "accent_color": "2E75B6"
    },
    "Professional Black": {
        "heading_color": "2F2F2F", 
        "font": "Arial",
        "title_size": 16,
        "heading_size": 14,
        "body_size": 11,
        "accent_color": "4F4F4F"
    },
    "Elegant Navy": {
        "heading_color": "1C2951",
        "font": "Times New Roman", 
        "title_size": 16,
        "heading_size": 14,
        "body_size": 12,
        "accent_color": "34558B"
    },
    "Modern Corporate": {
        "heading_color": "0066CC",
        "font": "Segoe UI", 
        "title_size": 17,
        "heading_size": 14,
        "body_size": 11,
        "accent_color": "4488DD"
    }
}
