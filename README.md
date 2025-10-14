# 📄 AI-Powered Event Report Generator

An intelligent Streamlit application that generates professional college event reports using AI. Simply input basic event details, and let AI create comprehensive, formatted reports in Microsoft Word format.

## ✨ Features

- **🤖 AI-Powered Content Generation**: Uses Google Gemini AI to create detailed reports from minimal input
- **📝 Professional Formatting**: Multiple themes with custom Word document styling
- **🎯 Minimal Input Required**: Just event title, date, and basic details needed
- **📊 Smart Report Styles**: Choose between "Concise & Realistic" or "Detailed & Comprehensive"
- **📷 Photo Integration**: Optional photo upload with automatic captions
- **🎨 Multiple Themes**: Academic Blue, Professional Black, Elegant Navy, Modern Corporate
- **✏️ Preview & Edit**: Review and modify AI-generated content before download
- **📱 Modern UI**: Clean, user-friendly Streamlit interface

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vikram00014/AI-Powered-Event-Report-Generator.git
   cd AI-Powered-Event-Report-Generator
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit google-generativeai python-docx
   ```

3. **Configure API Key**
   - Edit `config.py` and add your Google Gemini API key:
   ```python
   GEMINI_API_KEY = "your-api-key-here"
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   - Navigate to `http://localhost:8501`

## 🎯 How to Use

1. **Fill Basic Details**
   - Event Title (required)
   - Date (required)
   - Speaker, Venue, Organizer
   - Brief description and key topics

2. **Choose Report Style**
   - **Concise & Realistic**: Natural, focused content
   - **Detailed & Comprehensive**: Academic, elaborate language

3. **Select Theme**
   - Academic Blue (recommended)
   - Professional Black
   - Elegant Navy
   - Modern Corporate

4. **Generate & Download**
   - AI creates comprehensive report
   - Preview and edit if needed
   - Download professional Word document

## 📋 Generated Report Structure

1. Event Title
2. College and Department Information
3. Date and Venue
4. Organizer and Speaker(s)
5. Introduction
6. Objectives
7. Key Highlights and Activities
8. Learning Outcomes and Feedback
9. Participant Testimonials
10. Participants and Contributors
11. Event Documentation (if photos uploaded)
12. Conclusion
13. Report Authorization

## 🛠️ Project Structure

```
event_report/
├── app.py                    # Main Streamlit application
├── config.py                 # Configuration settings
├── report_generator.py       # AI report generation
├── docx_builder.py          # Word document creation
├── assets/                   # Images and banners
├── templates/                # AI prompt templates
├── generated_reports/        # Output directory
└── README.md                # This file
```

## ⚙️ Configuration

### Default Settings (config.py)
- **College**: Pimpri Chinchwad College Of Engineering
- **Department**: Department of CSE(AIML)
- **Themes**: 4 professional styles available
- **AI Model**: Google Gemini 2.5 Flash

### Customization
- Modify default college/department in `config.py`
- Add custom themes in the THEMES dictionary
- Adjust AI prompt in `templates/event_prompt.txt`

## 🎨 Themes

| Theme | Font | Colors | Best For |
|-------|------|--------|----------|
| Academic Blue | Calibri | Professional Blue | Most reports |
| Professional Black | Arial | Corporate Gray | Business events |
| Elegant Navy | Times New Roman | Navy Blue | Formal events |
| Modern Corporate | Segoe UI | Modern Blue | Tech events |

## 🤖 AI Features

- **Smart Content Expansion**: 2-3 lines become full professional sections
- **Realistic Details**: Generates authentic names, quotes, and activities
- **Context Awareness**: Understands different event types
- **Industry Knowledge**: Creates relevant technical content
- **Authentic Language**: Natural, institutional tone

## 📝 Example Usage

**Input:**
- Title: "Cloud Computing Workshop"
- Date: "5 October 2025"
- Speaker: "Dr. Priya Deshmukh, Microsoft"
- Description: "Workshop on cloud fundamentals"

**AI Output:**
- Complete 13-section professional report
- Realistic activities and outcomes
- Authentic student testimonials
- Industry-relevant content
- Perfect formatting

## 🔧 Technical Details

- **Framework**: Streamlit for web interface
- **AI Engine**: Google Gemini 2.5 Flash
- **Document Processing**: python-docx for Word formatting
- **Session Management**: Streamlit session state
- **File Handling**: Temporary file processing for downloads

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```

### Production Deployment
- Deploy on Streamlit Cloud
- Set up environment variables for API keys
- Ensure proper file permissions for output directory

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for intelligent content generation
- Streamlit for the amazing web framework
- python-docx for Word document processing

## 📧 Contact

**Vikram** - [GitHub Profile](https://github.com/vikram00014)

Project Link: [https://github.com/vikram00014/AI-Powered-Event-Report-Generator](https://github.com/vikram00014/AI-Powered-Event-Report-Generator)

---

⭐ **Star this repository if you found it helpful!**