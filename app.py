import streamlit as st
from streamlit_ace import st_ace

from llm_client import get_llm_client, LLMProvider
from context import build_candidate_context, INTERVIEW_TYPES, EXPERIENCE_LEVELS
from prompts import generate_question_prompt, evaluate_answer_prompt, interview_summary_prompt

# Page config
st.set_page_config(
    page_title="NovaMentor AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium CSS styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 50%, #0f0f23 100%);
    }
    
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #00d4ff 0%, #7c3aed 50%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1.5rem 0;
        letter-spacing: -1px;
    }
    
    .sub-header {
        text-align: center;
        color: #a1a1aa;
        margin-bottom: 2rem;
        font-size: 1.1rem;
        font-weight: 300;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .question-card {
        background: linear-gradient(135deg, rgba(124, 58, 237, 0.3) 0%, rgba(0, 212, 255, 0.2) 100%);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(124, 58, 237, 0.3);
        padding: 2rem;
        border-radius: 16px;
        color: #ffffff;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(124, 58, 237, 0.2);
        font-size: 1.1rem;
        line-height: 1.7;
    }
    
    .feedback-card {
        background: rgba(16, 185, 129, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-left: 4px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        color: #e4e4e7;
    }
    
    .type-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .type-card:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(124, 58, 237, 0.5);
        transform: translateY(-4px);
    }
    
    .type-icon {
        font-size: 2.5rem;
        margin-bottom: 0.75rem;
    }
    
    .type-title {
        color: #ffffff;
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    
    .type-desc {
        color: #a1a1aa;
        font-size: 0.85rem;
        line-height: 1.4;
    }
    
    .stat-card {
        background: linear-gradient(135deg, rgba(124, 58, 237, 0.2) 0%, rgba(124, 58, 237, 0.05) 100%);
        border: 1px solid rgba(124, 58, 237, 0.3);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        color: #7c3aed;
    }
    
    .stat-label {
        color: #a1a1aa;
        font-size: 0.85rem;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a3e 0%, #0f0f23 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    section[data-testid="stSidebar"] .stMarkdown h2 {
        color: #ffffff;
        font-weight: 600;
    }
    
    /* Input styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        color: #ffffff !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #7c3aed !important;
        box-shadow: 0 0 0 2px rgba(124, 58, 237, 0.2) !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed 0%, #5b21b6 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.4);
    }
    
    .stButton > button[kind="secondary"] {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: none;
    }
    
    /* Form styling */
    .stForm {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 1rem;
    }
    
    /* Divider */
    hr {
        border-color: rgba(255, 255, 255, 0.1);
    }
    
    /* Info box */
    .stAlert {
        background: rgba(0, 212, 255, 0.1);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 12px;
        color: #00d4ff;
    }
    
    /* Success box */
    .stSuccess {
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 12px;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #7c3aed !important;
    }
    
    /* Labels */
    .stMarkdown p, .stMarkdown li {
        color: #e4e4e7;
    }
    
    label {
        color: #a1a1aa !important;
        font-weight: 500 !important;
    }
    
    /* Metric */
    [data-testid="stMetricValue"] {
        color: #7c3aed;
    }
    
    /* Slider */
    .stSlider > div > div > div {
        background: #7c3aed !important;
    }
    
    /* Welcome cards animation */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animate-in {
        animation: fadeInUp 0.5s ease forwards;
    }
    
    /* Code editor styling */
    .ace_editor {
        border-radius: 12px !important;
        border: 1px solid rgba(124, 58, 237, 0.3) !important;
    }
    
    .ace-monokai {
        background-color: #1a1a2e !important;
    }
    
    .ace_gutter {
        background: #12121f !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    defaults = {
        "profile_set": False,
        "candidate_context": "",
        "current_question": None,
        "interview_type": None,
        "qa_history": [],
        "interview_started": False,
        "llm_client": None,
        "current_feedback": None
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

# Initialize LLM client (Ollama by default, can switch to Nova)
@st.cache_resource
def get_client():
    return get_llm_client(LLMProvider.NOVA)

# Sidebar - Candidate Profile Setup
with st.sidebar:
    st.markdown("## 👤 Candidate Profile")
    
    with st.form("profile_form"):
        name = st.text_input("Name", placeholder="John Doe")
        
        experience_level = st.selectbox(
            "Experience Level",
            EXPERIENCE_LEVELS
        )
        
        years_exp = st.slider("Years of Experience", 0, 20, 2)
        
        target_role = st.text_input(
            "Target Role",
            placeholder="e.g., Backend Engineer, ML Engineer"
        )
        
        tech_stack = st.text_area(
            "Tech Stack (comma-separated)",
            placeholder="Python, JavaScript, React, PostgreSQL, AWS"
        )
        
        interests = st.text_area(
            "Areas of Interest (comma-separated)",
            placeholder="Machine Learning, Distributed Systems, Web Development"
        )
        
        additional_notes = st.text_area(
            "Additional Notes (optional)",
            placeholder="Any specific areas to focus on or avoid..."
        )
        
        submitted = st.form_submit_button("💾 Save Profile", use_container_width=True)
        
        if submitted:
            if name and target_role:
                tech_list = [t.strip() for t in tech_stack.split(",") if t.strip()]
                interest_list = [i.strip() for i in interests.split(",") if i.strip()]
                
                st.session_state.candidate_context = build_candidate_context(
                    name=name,
                    experience_level=experience_level,
                    target_role=target_role,
                    tech_stack=tech_list,
                    interests=interest_list,
                    years_of_experience=years_exp,
                    additional_notes=additional_notes
                )
                st.session_state.profile_set = True
                st.success("✅ Profile saved!")
            else:
                st.error("Please fill in Name and Target Role")
    
    st.divider()
    
    # Interview stats
    if st.session_state.qa_history:
        st.markdown("## 📊 Session Stats")
        st.metric("Questions Answered", len(st.session_state.qa_history))
        
        if st.button("📋 Get Interview Summary", use_container_width=True):
            st.session_state.show_summary = True

# Main content
st.markdown('<h1 class="main-header">🤖 NovaMentor AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Interview Coach - Practice & Improve</p>', unsafe_allow_html=True)

if not st.session_state.profile_set:
    # Welcome screen
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <p style="color: #a1a1aa; font-size: 1.1rem;">👈 Set up your candidate profile in the sidebar to begin</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ✨ Interview Types Available")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="type-card">
            <div class="type-icon">🎯</div>
            <div class="type-title">Interest-Based</div>
            <div class="type-desc">Questions tailored to your background, projects, and interests</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="type-card">
            <div class="type-icon">🎭</div>
            <div class="type-title">Scenario-Based</div>
            <div class="type-desc">Real-world problem-solving and workplace situations</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="type-card">
            <div class="type-icon">🏗️</div>
            <div class="type-title">System Design</div>
            <div class="type-desc">Architecture, scalability, and design challenges</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="type-card">
            <div class="type-icon">💻</div>
            <div class="type-title">LeetCode/DSA</div>
            <div class="type-desc">Data structures, algorithms, and coding problems</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Features section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🚀 Features")
    
    feat1, feat2, feat3 = st.columns(3)
    with feat1:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #00d4ff; margin-bottom: 0.5rem;">🤖 AI-Powered</h4>
            <p style="color: #a1a1aa; font-size: 0.9rem;">Dynamic questions generated based on your profile and experience level</p>
        </div>
        """, unsafe_allow_html=True)
    with feat2:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #7c3aed; margin-bottom: 0.5rem;">📊 Smart Evaluation</h4>
            <p style="color: #a1a1aa; font-size: 0.9rem;">Detailed feedback with scores, strengths, and improvement areas</p>
        </div>
        """, unsafe_allow_html=True)
    with feat3:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #f472b6; margin-bottom: 0.5rem;">📋 Session Summary</h4>
            <p style="color: #a1a1aa; font-size: 0.9rem;">Comprehensive interview report with hiring recommendations</p>
        </div>
        """, unsafe_allow_html=True)

else:
    # Interview interface - Profile loaded
    st.markdown("""
    <div class="glass-card" style="text-align: center; padding: 1rem;">
        <span style="color: #10b981; font-size: 1.1rem;">✅ Profile loaded! Ready to interview.</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interview type selection with styled cards
    st.markdown("### 🎯 Select Interview Type")
    
    col1, col2, col3, col4 = st.columns(4)
    
    interview_types_ui = [
        ("interest", "🎯", "Interest-Based", "Based on your background"),
        ("scenario", "🎭", "Scenario-Based", "Real-world situations"),
        ("system_design", "🏗️", "System Design", "Architecture challenges"),
        ("leetcode", "💻", "LeetCode/DSA", "Coding problems"),
    ]
    
    for col, (type_key, icon, title, desc) in zip([col1, col2, col3, col4], interview_types_ui):
        with col:
            is_selected = st.session_state.interview_type == type_key
            border_color = "#7c3aed" if is_selected else "rgba(255, 255, 255, 0.08)"
            bg_color = "rgba(124, 58, 237, 0.15)" if is_selected else "rgba(255, 255, 255, 0.03)"
            
            st.markdown(f"""
            <div style="background: {bg_color}; border: 2px solid {border_color}; border-radius: 16px; padding: 1.25rem; text-align: center; min-height: 140px;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
                <div style="color: #ffffff; font-weight: 600; font-size: 0.95rem;">{title}</div>
                <div style="color: #a1a1aa; font-size: 0.8rem; margin-top: 0.25rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Select", key=f"btn_{type_key}", use_container_width=True):
                st.session_state.interview_type = type_key
                st.session_state.current_question = None
                st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.session_state.interview_type:
        interview_info = INTERVIEW_TYPES[st.session_state.interview_type]
        
        # Current interview type indicator
        st.markdown(f"""
        <div style="background: rgba(124, 58, 237, 0.1); border: 1px solid rgba(124, 58, 237, 0.3); border-radius: 10px; padding: 0.75rem 1rem; display: inline-block; margin-bottom: 1rem;">
            <span style="color: #a1a1aa;">Current Mode:</span> 
            <span style="color: #7c3aed; font-weight: 600;">{interview_info['name']}</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate question button
        if st.session_state.current_question is None:
            st.markdown("<br>", unsafe_allow_html=True)
            col_btn, col_empty = st.columns([1, 2])
            with col_btn:
                if st.button("🎲 Generate Question", use_container_width=True, type="primary"):
                    with st.spinner("🤔 Generating personalized question..."):
                        try:
                            client = get_client()
                            prompt = generate_question_prompt(
                                st.session_state.candidate_context,
                                interview_info["name"],
                                interview_info["description"]
                            )
                            st.session_state.current_question = client.generate(prompt)
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error generating question: {str(e)}")
        
        # Display current question
        if st.session_state.current_question:
            st.markdown(f"### 📝 {interview_info['name']}")
            st.markdown(f'<div class="question-card">{st.session_state.current_question}</div>', unsafe_allow_html=True)
            
            # Answer input - Code editor for LeetCode, text area for others
            is_coding_question = st.session_state.interview_type == "leetcode"
            
            if is_coding_question:
                st.markdown("""
                <p style="color: #a1a1aa; font-size: 0.9rem; margin-bottom: 0.5rem;">💻 Write your code solution below</p>
                """, unsafe_allow_html=True)
                
                # Language selector
                lang_col1, lang_col2 = st.columns([1, 3])
                with lang_col1:
                    language = st.selectbox(
                        "Language",
                        ["python", "javascript", "java", "cpp", "c", "go", "rust", "typescript"],
                        index=0,
                        label_visibility="collapsed"
                    )
                
                # Code editor
                answer = st_ace(
                    placeholder="# Write your solution here...\n\ndef solution():\n    pass",
                    language=language,
                    theme="monokai",
                    height=350,
                    font_size=14,
                    tab_size=4,
                    show_gutter=True,
                    show_print_margin=False,
                    wrap=False,
                    auto_update=True,
                    key="code_editor"
                )
            else:
                st.markdown("""
                <p style="color: #a1a1aa; font-size: 0.9rem; margin-bottom: 0.5rem;">💡 Tip: Be thorough and explain your thought process</p>
                """, unsafe_allow_html=True)
                
                answer = st.text_area(
                    "Your Answer",
                    height=200,
                    placeholder="Type your answer here...",
                    label_visibility="collapsed"
                )
            
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                submit_btn = st.button("✅ Submit & Evaluate", use_container_width=True, type="primary")
            
            with col2:
                next_btn = st.button("⏭️ Next Question", use_container_width=True)
            
            with col3:
                change_btn = st.button("🔄 Change Type", use_container_width=True)
            
            # Handle submit
            if submit_btn:
                if answer.strip():
                    with st.spinner("🔍 Evaluating your answer..."):
                        try:
                            client = get_client()
                            eval_prompt = evaluate_answer_prompt(
                                st.session_state.candidate_context,
                                interview_info["name"],
                                st.session_state.current_question,
                                answer
                            )
                            feedback = client.generate(eval_prompt, max_tokens=1500)
                            
                            # Store feedback in session state
                            st.session_state.current_feedback = feedback
                            
                            # Store in history
                            st.session_state.qa_history.append({
                                "type": st.session_state.interview_type,
                                "question": st.session_state.current_question,
                                "answer": answer,
                                "feedback": feedback
                            })
                            st.rerun()
                            
                        except Exception as e:
                            st.error(f"Error evaluating answer: {str(e)}")
                else:
                    st.warning("⚠️ Please enter an answer before submitting.")
            
            # Handle next question
            if next_btn:
                st.session_state.current_question = None
                st.session_state.current_feedback = None
                st.rerun()
            
            # Handle change type
            if change_btn:
                st.session_state.current_question = None
                st.session_state.current_feedback = None
                st.session_state.interview_type = None
                st.rerun()
            
            # Display feedback if available
            if st.session_state.current_feedback:
                st.markdown("### 📊 AI Feedback")
                st.markdown('<div class="feedback-card">', unsafe_allow_html=True)
                st.markdown(st.session_state.current_feedback)
                st.markdown('</div>', unsafe_allow_html=True)
    
    # Show interview summary if requested
    if st.session_state.get("show_summary") and st.session_state.qa_history:
        st.divider()
        st.markdown("## 📋 Interview Summary")
        
        with st.spinner("Generating comprehensive summary..."):
            try:
                client = get_client()
                summary_prompt = interview_summary_prompt(
                    st.session_state.candidate_context,
                    st.session_state.qa_history
                )
                summary = client.generate(summary_prompt, max_tokens=2000)
                st.markdown('<div class="feedback-card">', unsafe_allow_html=True)
                st.markdown(summary)
                st.markdown('</div>', unsafe_allow_html=True)
                st.session_state.show_summary = False
            except Exception as e:
                st.error(f"Error generating summary: {str(e)}")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; padding: 2rem 0; border-top: 1px solid rgba(255, 255, 255, 0.1);">
    <p style="color: #52525b; font-size: 0.85rem; margin: 0;">
        Powered by <span style="color: #7c3aed;">AI</span> | Built for 
        <span style="background: linear-gradient(90deg, #f97316, #eab308); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 600;">Amazon Nova Hackathon</span>
    </p>
</div>
""", unsafe_allow_html=True)