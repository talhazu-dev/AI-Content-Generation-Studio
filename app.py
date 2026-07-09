import streamlit as st
import json
import urllib.request
import urllib.error

# Page Configuration
st.set_page_config(page_title="AI Content Generation Studio", page_icon="✍️", layout="wide")

st.title("✍️ AI Content Generation Studio")
st.caption("Generate high-quality, structured content using tailored AI templates.")
st.markdown("---")

# --- SIDEBAR: DIRECT USER KEY INPUT ---
st.sidebar.header("🔑 Authentication")
api_key = st.sidebar.text_input("Enter Gemini API Key to Activate Studio", type="password", help="Paste your AQ... key here")

# --- SIDEBAR: CONTENT CONTROLS ---
st.sidebar.header("🎛️ Content Controls")
tone = st.sidebar.selectbox("Select Tone", ["Professional", "Casual", "Witty", "Persuasive", "Inspirational"])
length = st.sidebar.select_slider("Content Length", options=["Short (100 words)", "Medium (300 words)", "Long (500+ words)"])
audience = st.sidebar.text_input("Target Audience", placeholder="e.g., Students, Tech Professionals")

# --- MAIN INTERFACE ---
template = st.selectbox(
    "Choose a Content Template",
    ["Blog Post", "Social Media Caption", "Ad Copy", "Cold Email", "LinkedIn Post"]
)

st.subheader(f"📝 Topic Details for {template}")
topic = st.text_input("What is your content about?", placeholder="e.g., Importance of Programming")
key_points = st.text_area("Key points to include (Optional)", placeholder="Point 1\nPoint 2")

# --- NO-LIBRARY DIRECT API CALL ENGINE ---
def generate_content_no_lib(api_key, template, topic, points, tone, length, audience):
    # Bilkul safe v1beta standard endpoint aur updated model structure
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    prompt_text = f"""
    You are an expert Content Writer. Write a highly professional, engaging, and directly usable {template}.
    Topic: {topic}
    Key Points to Include: {points if points else 'Use professional judgment.'}
    Tone: {tone}
    Target Length: {length}
    Target Audience: {audience if audience else 'General Audience'}
    
    Formatting Requirements:
    - Format properly using Markdown (headings, bullet points, and bold text).
    - Do not include introductory or concluding filler commentary.
    """
    
    # Standard complete structure format
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt_text}
                ]
            }
        ]
    }
    
    data = json.dumps(payload).encode('utf-8')
    headers = {
        'Content-Type': 'application/json'
    }
    
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = response.read().decode('utf-8')
            res_json = json.loads(res_data)
            return res_json['candidates'][0]['content']['parts'][0]['text']
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode('utf-8')
        return f"API Error ({e.code}): {error_msg}"
    except Exception as e:
        return f"Connection Error: {str(e)}"

# --- GENERATE BUTTON ---
st.markdown("---")
if st.button("🚀 Generate Content", type="primary"):
    if not api_key:
        st.error("❌ Please paste your Gemini API Key in the sidebar first!")
    elif not topic:
        st.error("❌ Please enter a topic or subject for your content!")
    else:
        with st.spinner("Writing magic... ✨"):
            output = generate_content_no_lib(api_key, template, topic, key_points, tone, length, audience)
            
            if "API Error" in output or "Connection Error" in output:
                st.error(output)
                st.info("💡 Tip: If 404 persists, make sure your API key from Google AI Studio is fully copied.")
            else:
                st.success("✨ Generated Content")
                st.markdown("---")
                st.markdown(output)
                st.markdown("---")
                
                st.download_button(
                    label="📥 Download Content as MD File",
                    data=output,
                    file_name=f"{template.lower().replace(' ', '_')}.md",
                    mime="text/markdown"
                )