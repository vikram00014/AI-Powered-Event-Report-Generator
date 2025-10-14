# report_generator.py
from google import genai
from config import GEMINI_API_KEY, PROMPT_TEMPLATE_PATH

def load_prompt_template():
    with open(PROMPT_TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return f.read()

def build_event_prompt(details):
    template = load_prompt_template()
    # Add report style to the details for template formatting
    details_with_style = details.copy()
    details_with_style["report_style"] = details.get("report_style", "Concise & Realistic")
    return template.format(**details_with_style)

def generate_report(details):
    try:
        prompt = build_event_prompt(details)
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Error generating report: {str(e)}")
        # Return a basic template if AI fails
        return f"""**1. Event Title**
{details.get('event_title', 'Event Title')}

**2. College and Department Information**
{details.get('college_name', 'College Name')}
{details.get('dept_name', 'Department Name')}

**3. Date and Venue**
**Date:** {details.get('date', 'Date')}
**Venue:** {details.get('venue', 'Venue')}

**4. Organizer and Speaker(s)**
**Organizer:** {details.get('organizer', 'Organizer')}
**Speaker(s):** {details.get('speaker', 'Speaker')}

**5. Introduction**
This report provides an overview of the {details.get('event_type', 'event')} conducted.

**6. Objectives**
• {details.get('objectives', 'Event objectives')}

**7. Key Highlights and Activities**
• The event was successfully conducted with active participation.

**8. Learning Outcomes and Feedback**
• {details.get('outcomes', 'Positive feedback received from participants')}

**9. Conclusion**
The event was successfully conducted and achieved its intended objectives."""
