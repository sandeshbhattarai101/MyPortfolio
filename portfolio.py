import streamlit as st
from pathlib import Path
import base64

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="Sandesh Bhattarai | AI/ML Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========== CUSTOM CSS ==========
def local_css():
    st.markdown("""
    <style>
    /* Main Theme */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    code, pre {
        font-family: 'JetBrains Mono', monospace;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Smooth Scroll */
    html {
        scroll-behavior: smooth;
    }
    
    /* Background */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Responsive Container */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    
    /* Glass Navigation */
    .nav-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0.5rem;
        padding: 1rem 2rem;
        margin: 1rem auto 2rem auto;
        max-width: 900px;
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 50px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        flex-wrap: wrap;
        position: sticky;
        top: 10px;
        z-index: 1000;
        animation: slideDown 0.5s ease-out;
    }
    
    @keyframes slideDown {
        from {
            transform: translateY(-100px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    .nav-link {
        text-decoration: none;
        color: #333;
        font-weight: 500;
        font-size: 0.95rem;
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .nav-link::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        transition: left 0.3s ease;
        z-index: -1;
        border-radius: 25px;
    }
    
    .nav-link:hover::before {
        left: 0;
    }
    
    .nav-link:hover {
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Hero Section */
    .hero-section {
        text-align: center;
        padding: 3rem 0 4rem 0;
        animation: fadeInUp 1s ease-out;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -2px;
        animation: gradient 3s ease infinite;
        background-size: 200% 200%;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #555;
        margin-bottom: 2.5rem;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    
    /* Glassmorphism Cards */
    .card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .card::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 20px;
        opacity: 0;
        transition: opacity 0.4s ease;
        z-index: -1;
    }
    
    .card:hover::before {
        opacity: 0.3;
    }
    
    .card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 60px 0 rgba(102, 126, 234, 0.3);
    }
    
    .card-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1.2rem;
        color: #222;
        position: relative;
        display: inline-block;
    }
    
    .card-title::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 50px;
        height: 3px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    .card-subtitle {
        font-size: 1.1rem;
        color: #667eea;
        font-weight: 600;
        margin-bottom: 0.8rem;
        letter-spacing: 0.3px;
    }
    
    .card-text {
        color: #555;
        line-height: 1.8;
        margin-bottom: 1rem;
        font-size: 1rem;
    }
    
    /* Fancy Buttons */
    .custom-button {
        display: inline-block;
        padding: 0.9rem 2.2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-decoration: none;
        border-radius: 30px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: none;
        cursor: pointer;
        margin: 0.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .custom-button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .custom-button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .custom-button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.5);
        color: white;
    }
    
    .custom-button:active {
        transform: translateY(-1px) scale(1.02);
    }
    
    /* Modern Skills Pills */
    .skill-pill {
        display: inline-block;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        margin: 0.4rem;
        font-size: 0.9rem;
        color: #667eea;
        font-weight: 600;
        border: 1px solid rgba(102, 126, 234, 0.2);
        transition: all 0.3s ease;
        cursor: default;
    }
    
    .skill-pill:hover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    
    /* Elegant Timeline */
    .timeline-item {
        border-left: 3px solid transparent;
        border-image: linear-gradient(to bottom, #667eea, #764ba2);
        border-image-slice: 1;
        padding-left: 2.5rem;
        margin-left: 1.5rem;
        margin-bottom: 3rem;
        position: relative;
        animation: slideInLeft 0.6s ease-out;
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -11px;
        top: 0;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.2);
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% {
            box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.2);
        }
        50% {
            box-shadow: 0 0 0 8px rgba(102, 126, 234, 0.1);
        }
    }
    
    .timeline-date {
        color: #667eea;
        font-weight: 700;
        font-size: 0.95rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    .timeline-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin: 0.8rem 0;
        color: #222;
    }
    
    .timeline-subtitle {
        color: #666;
        font-style: italic;
        margin-bottom: 1rem;
        font-size: 1.05rem;
    }
    
    /* Animated Social Links */
    .social-links {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin: 2rem 0;
        flex-wrap: wrap;
    }
    
    .social-link {
        width: 55px;
        height: 55px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        text-decoration: none;
        font-size: 1.5rem;
        border: 2px solid rgba(102, 126, 234, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .social-link::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        transform: scale(0);
        transition: transform 0.4s ease;
        border-radius: 50%;
        z-index: -1;
    }
    
    .social-link:hover::before {
        transform: scale(1);
    }
    
    .social-link:hover {
        transform: translateY(-8px) rotate(360deg);
        color: white;
        border-color: transparent;
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Section Headers */
    .section-header {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin: 4rem 0 3rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
        position: relative;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -15px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    /* Project Tags */
    .project-tag {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-size: 0.85rem;
        font-weight: 600;
        box-shadow: 0 3px 10px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }
    
    .project-tag:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.5);
    }
    
    /* Research Interest Box */
    .research-box {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.15) 100%);
        border-left: 5px solid #667eea;
        padding: 2rem;
        border-radius: 15px;
        margin: 2.5rem 0;
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .research-box::before {
        content: '🔬';
        position: absolute;
        right: 20px;
        top: 20px;
        font-size: 4rem;
        opacity: 0.1;
    }
    
    /* Stats Counter */
    .stat-box {
        text-align: center;
        padding: 2rem 1.5rem;
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        margin: 0.5rem;
        border: 1px solid rgba(102, 126, 234, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeInUp 0.6s ease-out;
    }
    
    .stat-box:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stat-label {
        font-size: 0.95rem;
        color: #666;
        margin-top: 0.5rem;
        font-weight: 500;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
            letter-spacing: -1px;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
        }
        
        .section-header {
            font-size: 2rem;
        }
        
        .nav-container {
            gap: 0.3rem;
            padding: 0.8rem 1rem;
        }
        
        .nav-link {
            font-size: 0.85rem;
            padding: 0.5rem 0.9rem;
        }
        
        .card {
            padding: 1.5rem;
        }
        
        .stat-number {
            font-size: 2rem;
        }
    }
    
    /* Custom Form Styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 15px;
        border: 2px solid rgba(102, 126, 234, 0.2);
        padding: 1rem;
        transition: all 0.3s ease;
        background: rgba(255, 255, 255, 0.9);
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Floating Animation */
    @keyframes float {
        0%, 100% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    
    .float {
        animation: float 3s ease-in-out infinite;
    }
    
    </style>
    """, unsafe_allow_html=True)

# ========== NAVIGATION ==========
def navigation():
    st.markdown("""
    <div class="nav-container">
        <a href="#home" class="nav-link">🏠 Home</a>
        <a href="#about" class="nav-link">👤 About</a>
        <a href="#experience" class="nav-link">💼 Experience</a>
        <a href="#projects" class="nav-link">🚀 Projects</a>
        <a href="#skills" class="nav-link">⚡ Skills</a>
        <a href="#contact" class="nav-link">📧 Contact</a>
    </div>
    """, unsafe_allow_html=True)

# ========== SECTIONS ==========
def home_section():
    st.markdown('<div class="hero-section" id="home">', unsafe_allow_html=True)
    
    st.markdown('<h1 class="hero-title">Sandesh Bhattarai</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">AI/ML Engineer • Full Stack Developer</p>', unsafe_allow_html=True)
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">2+</div>
            <div class="stat-label">Years Experience</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">10+</div>
            <div class="stat-label">Projects Built</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">5+</div>
            <div class="stat-label">Technologies Mastered</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">∞</div>
            <div class="stat-label">Lines of Code</div>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.markdown("""
        <div style="text-align: center; margin-top: 2.5rem;">
            <a href="#contact" class="custom-button">Let's Connect</a>
            <a href="#projects" class="custom-button">View Work</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def about_section():
    st.markdown('<h2 class="section-header" id="about">About Me</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2,1])
    
    with col1:
        st.markdown("""
        <div class="card">
            <p class="card-text">
                I'm a passionate <strong>AI/ML engineer</strong> and <strong>full-stack developer</strong> 
                dedicated to building intelligent systems that solve real-world problems. My journey in tech 
                spans from developing production-ready <strong>MERN stack applications</strong> to designing 
                <strong>deep learning models</strong> for complex challenges.
            </p>
            <p class="card-text">
                During my internship at <strong>Web Networks Pvt. Ltd.</strong>, I honed my full-stack 
                development skills, building scalable web applications and RESTful APIs. I've worked on 
                diverse projects ranging from job recommendation systems to computer vision applications.
            </p>
            <p class="card-text">
                I'm driven by curiosity and a commitment to continuous learning. Whether it's experimenting with 
                the latest LLM architectures, contributing to open-source projects, or optimizing neural networks 
                for production, I'm always seeking opportunities to grow and make an impact.
            </p>
            <p class="card-text">
                Beyond development, I'm fascinated by the intersection of AI and various domains including 
                healthcare, recommendation systems, and intelligent automation.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card float">
            <h3 class="card-title">Quick Facts</h3>
            <p class="card-text">👤 <strong>Name:</strong> Sandesh Bhattarai</p>
            <p class="card-text">📍 <strong>Based in:</strong> Nepal</p>
            <p class="card-text">💼 <strong>Focus:</strong> AI/ML & Full Stack</p>
            <p class="card-text">🌐 <strong>Stack:</strong> MERN + PyTorch</p>
            <p class="card-text">🤖 <strong>Interest:</strong> ML, DL, LLMs, RL</p>
            <p class="card-text">📧 <strong>Email:</strong> sandeshbhattarai6@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Research Interest Section
    st.markdown("""
    <div class="research-box">
        <h3 style="color: #667eea; margin-bottom: 1.2rem; font-weight: 700; font-size: 1.5rem;">🔬 Research Interests</h3>
        <p style="color: #333; line-height: 1.9; font-size: 1.05rem;">
            I have a strong interest in <strong>machine learning</strong> and its more advanced areas. 
            I am particularly interested in <strong>deep learning models</strong>, 
            <strong>Large Language Models (LLMs)</strong> and <strong>Reinforcement Learning</strong> 
            and their uses in decision-making systems, optimization processes and across different domains 
            such as recommendation systems, healthcare, and intelligent automation.
        </p>
    </div>
    """, unsafe_allow_html=True)

def experience_section():
    st.markdown('<h2 class="section-header" id="experience">Professional Experience</h2>', unsafe_allow_html=True)
    
    # Teaching Experience
    st.markdown("""
    <div class="timeline-item">
        <p class="timeline-date">August 2024 - Present</p>
        <h3 class="timeline-title">Secondary Level Teacher - Computer Science</h3>
        <p class="timeline-subtitle">Canon Secondary School</p>
        <p class="card-text">
            • Design comprehensive lesson plans and hands-on exercises for Python programming, algorithms, and web technologies<br>
            • Deliver engaging, interactive lessons that make complex CS concepts accessible and exciting<br>
            • Maintain detailed academic records and provide personalized feedback to 100+ students<br>
            • Create and grade assessments that accurately measure student understanding and growth<br>
            • Mentor students in coding competitions, project development, and career planning<br>
            • Foster collaborative learning environments that encourage innovation and critical thinking
        </p>
        <div style="margin-top: 1.2rem;">
            <span class="skill-pill">Python Teaching</span>
            <span class="skill-pill">Curriculum Design</span>
            <span class="skill-pill">Student Mentoring</span>
            <span class="skill-pill">Assessment Development</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Work Experience
    st.markdown("""
    <div class="timeline-item">
        <p class="timeline-date">April 2024 - July 2024</p>
        <h3 class="timeline-title">Web Developer Intern</h3>
        <p class="timeline-subtitle">Web Networks Pvt. Ltd.</p>
        <p class="card-text">
            • Built and maintained production-grade full-stack applications using <strong>MERN Stack</strong><br>
            • Architected and implemented RESTful APIs with Node.js and Express.js for optimal performance<br>
            • Integrated robust security features including JWT authentication, OAuth, and bcrypt hashing<br>
            • Collaborated with cross-functional teams using Git/GitHub for seamless version control<br>
            • Participated in agile sprints, code reviews, and continuous deployment processes<br>
            • Optimized application performance and implemented responsive, mobile-first designs
        </p>
        <div style="margin-top: 1.2rem;">
            <span class="skill-pill">MERN Stack</span>
            <span class="skill-pill">REST APIs</span>
            <span class="skill-pill">JWT Auth</span>
            <span class="skill-pill">Git/GitHub</span>
            <span class="skill-pill">Agile Development</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def projects_section():
    st.markdown('<h2 class="section-header" id="projects">Featured Projects</h2>', unsafe_allow_html=True)
    
    # Project 1 - CodeJobsNepal
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3 class="card-title">💼 CodeJobsNepal</h3>
            <p class="card-subtitle">Full Stack Job Portal | MERN + ML</p>
            <p class="card-text">
                A sophisticated job portal connecting tech professionals with opportunities in Nepal's growing 
                IT industry. Features an intelligent recommendation system using Content-Based Filtering to 
                match candidates with relevant positions based on skills, experience, and preferences.
            </p>
            <p class="card-text"><strong>✨ Key Features:</strong></p>
            <p class="card-text">
                • Secure JWT-based authentication and authorization system<br>
                • AI-powered job recommendations using Cosine Similarity algorithm<br>
                • Real-time job posting and application management<br>
                • Advanced search and filtering capabilities<br>
                • User profile management with resume upload<br>
                • Employer dashboard for applicant tracking<br>
                • Responsive design optimized for all devices
            </p>
            <p class="card-text"><strong>🛠️ Technical Implementation:</strong></p>
            <p class="card-text">
                • Built recommendation engine with NumPy and Pandas<br>
                • Implemented Content-Based Filtering for personalization<br>
                • Created scalable REST APIs for frontend-backend communication<br>
                • MongoDB for flexible document storage and queries<br>
                • React with modern hooks for dynamic UI
            </p>
            <div>
                <span class="project-tag">Python</span>
                <span class="project-tag">NumPy</span>
                <span class="project-tag">Pandas</span>
                <span class="project-tag">MongoDB</span>
                <span class="project-tag">Express.js</span>
                <span class="project-tag">React</span>
                <span class="project-tag">Node.js</span>
                <span class="project-tag">JWT</span>
                <span class="project-tag">Machine Learning</span>
            </div>
            <br><br>
            <a href="https://github.com/sandeshbhattarai101/CodeJobsNepal" target="_blank" class="custom-button">
                <span style="position: relative; z-index: 1;">View on GitHub</span>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3 class="card-title">🐍 Venomous Snake Classifier</h3>
            <p class="card-subtitle">Deep Learning | CNN Computer Vision</p>
            <p class="card-text">
                A potentially life-saving deep learning application that accurately classifies snakes as 
                venomous or non-venomous using advanced computer vision techniques. Built with PyTorch 
                and custom CNN architecture to achieve high accuracy in real-world scenarios.
            </p>
            <p class="card-text"><strong>🧠 Model Architecture:</strong></p>
            <p class="card-text">
                • Custom multi-layer Convolutional Neural Network<br>
                • ReLU activation functions for non-linear transformations<br>
                • Max pooling layers for feature dimensionality reduction<br>
                • Strategic dropout layers to prevent overfitting<br>
                • Fully connected layers for binary classification<br>
                • Binary cross-entropy loss with Adam optimizer
            </p>
            <p class="card-text"><strong>📊 Data Processing Pipeline:</strong></p>
            <p class="card-text">
                • Comprehensive image preprocessing (normalization, resizing)<br>
                • Train/Validation/Test split (70/15/15) for robust evaluation<br>
                • Advanced data augmentation (rotation, flip, zoom, brightness)<br>
                • Early stopping implementation to optimize training<br>
                • Detailed performance visualization with Matplotlib<br>
                • Confusion matrix and classification metrics analysis
            </p>
            <div>
                <span class="project-tag">Python</span>
                <span class="project-tag">PyTorch</span>
                <span class="project-tag">CNN</span>
                <span class="project-tag">Pandas</span>
                <span class="project-tag">Matplotlib</span>
                <span class="project-tag">NumPy</span>
                <span class="project-tag">Computer Vision</span>
                <span class="project-tag">Deep Learning</span>
            </div>
            <br><br>
            <a href="https://github.com/sandeshbhattarai101/VenomousSnakeClassifier" target="_blank" class="custom-button">
                <span style="position: relative; z-index: 1;">View on GitHub</span>
            </a>
        </div>
        """, unsafe_allow_html=True)

def skills_section():
    st.markdown('<h2 class="section-header" id="skills">Skills & Technologies</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3 class="card-title">💻 Languages</h3>
            <span class="skill-pill">Python</span>
            <span class="skill-pill">JavaScript</span>
            <span class="skill-pill">C/C++</span>
            <span class="skill-pill">HTML5</span>
            <span class="skill-pill">CSS3</span>
            <span class="skill-pill">SQL</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3 class="card-title">📚 Frameworks</h3>
            <span class="skill-pill">PyTorch</span>
            <span class="skill-pill">React.js</span>
            <span class="skill-pill">Node.js</span>
            <span class="skill-pill">Express.js</span>
            <span class="skill-pill">NumPy</span>
            <span class="skill-pill">Pandas</span>
            <span class="skill-pill">Matplotlib</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3 class="card-title">🛠️ Tools</h3>
            <span class="skill-pill">Git</span>
            <span class="skill-pill">GitHub</span>
            <span class="skill-pill">MySQL</span>
            <span class="skill-pill">MongoDB</span>
            <span class="skill-pill">VS Code</span>
            <span class="skill-pill">Jupyter</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Domain Expertise
    st.markdown("### 🎯 Domain Expertise")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h4 class="card-subtitle">🤖 Artificial Intelligence</h4>
            <p class="card-text">
                • Machine Learning<br>
                • Deep Learning & CNNs<br>
                • Large Language Models<br>
                • Reinforcement Learning<br>
                • Computer Vision<br>
                • Natural Language Processing<br>
                • Recommendation Systems
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h4 class="card-subtitle">🌐 Web Development</h4>
            <p class="card-text">
                • Full Stack MERN<br>
                • RESTful API Design<br>
                • Authentication & Security<br>
                • Responsive Design<br>
                • Database Architecture<br>
                • Version Control<br>
                • Agile Methodologies
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h4 class="card-subtitle">📊 Data Science</h4>
            <p class="card-text">
                • Data Analysis<br>
                • Data Visualization<br>
                • Statistical Modeling<br>
                • Feature Engineering<br>
                • Model Optimization<br>
                • Predictive Analytics<br>
                • Data Preprocessing
            </p>
        </div>
        """, unsafe_allow_html=True)

def contact_section():
    st.markdown('<h2 class="section-header" id="contact">Let\'s Connect</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3 class="card-title">📬 Contact Info</h3>
            <p class="card-text">
                <strong>👤 Name:</strong> Sandesh Bhattarai<br>
                <strong>📧 Email:</strong> <a href="mailto:sandeshbhattarai6@gmail.com" style="color: #667eea; text-decoration: none; font-weight: 600;">sandeshbhattarai6@gmail.com</a><br>
                <strong>📍 Location:</strong> Nepal<br>
                <strong>💼 Focus:</strong> AI/ML & Full Stack Development
            </p>
            <br>
            <h3 class="card-title">🌐 Let's Collaborate</h3>
            <p class="card-text">
                I'm always excited to connect with fellow developers, researchers, and innovators. 
                Whether you have a project idea, collaboration opportunity, or just want to chat 
                about AI and technology, I'd love to hear from you!
            </p>
            <p class="card-text">
                Feel free to reach out via email or connect with me on social platforms. 
                I typically respond within 24-48 hours.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="social-links">
            <a href="https://github.com/sandeshbhattarai101" target="_blank" class="social-link" title="GitHub">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
            </a>
            <a href="https://www.linkedin.com/in/sandesh-bhattarai101/" target="_blank" class="social-link" title="LinkedIn">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                </svg>
            </a>
            <a href="mailto:sandeshbhattarai6@gmail.com" class="social-link" title="Email">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M0 3v18h24v-18h-24zm6.623 7.929l-4.623 5.712v-9.458l4.623 3.746zm-4.141-5.929h19.035l-9.517 7.713-9.518-7.713zm5.694 7.188l3.824 3.099 3.83-3.104 5.612 6.817h-18.779l5.513-6.812zm9.208-1.264l4.616-3.741v9.348l-4.616-5.607z"/>
                </svg>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="card-title">💌 Send Message</h3>', unsafe_allow_html=True)
        
        with st.form("contact_form"):
            name = st.text_input("Your Name *", placeholder="John Doe")
            email = st.text_input("Your Email *", placeholder="john@example.com")
            subject = st.text_input("Subject *", placeholder="Collaboration / Job Opportunity / General Inquiry")
            message = st.text_area("Message *", placeholder="Tell me about your project or opportunity...", height=150)
            
            submitted = st.form_submit_button("Send Message 🚀", use_container_width=True)
            
            if submitted:
                if name and email and subject and message:
                    st.success("✅ Thank you for reaching out! I'll get back to you soon.")
                    st.info(f"📧 You can also email directly: sandeshbhattarai6@gmail.com")
                else:
                    st.error("❌ Please fill in all required fields.")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # What I'm Looking For
        st.markdown("""
        <div class="card" style="margin-top: 1rem;">
            <h4 class="card-subtitle">💡 Open To:</h4>
            <p class="card-text" style="font-size: 0.95rem;">
                ✓ AI/ML Development Roles<br>
                ✓ Full Stack Development Projects<br>
                ✓ Research Collaborations<br>
                ✓ Freelance Opportunities<br>
                ✓ Open Source Contributions
            </p>
        </div>
        """, unsafe_allow_html=True)

# ========== FOOTER ==========
def footer():
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2.5rem 0; color: #666;">
        <p style="font-size: 1.05rem; margin-bottom: 1rem;">
            Crafted with ❤️ using <strong>Streamlit</strong> & <strong>Python</strong>
        </p>
        <p style="font-size: 0.95rem; margin-bottom: 1rem;">
            <a href="#home" style="color: #667eea; text-decoration: none; margin: 0 0.5rem; font-weight: 500;">Home</a> •
            <a href="#about" style="color: #667eea; text-decoration: none; margin: 0 0.5rem; font-weight: 500;">About</a> •
            <a href="#experience" style="color: #667eea; text-decoration: none; margin: 0 0.5rem; font-weight: 500;">Experience</a> •
            <a href="#projects" style="color: #667eea; text-decoration: none; margin: 0 0.5rem; font-weight: 500;">Projects</a> •
            <a href="#skills" style="color: #667eea; text-decoration: none; margin: 0 0.5rem; font-weight: 500;">Skills</a> •
            <a href="#contact" style="color: #667eea; text-decoration: none; margin: 0 0.5rem; font-weight: 500;">Contact</a>
        </p>
        <p style="font-size: 0.9rem; color: #999; margin-top: 1.5rem;">
            © 2024 <strong>Sandesh Bhattarai</strong> • All Rights Reserved
        </p>
        <p style="font-size: 0.85rem; margin-top: 1rem; color: #999;">
            🤖 AI/ML Engineer • 💻 Full Stack Developer • 🔬 Researcher
        </p>
    </div>
    """, unsafe_allow_html=True)

# ========== MAIN APP ==========
def main():
    local_css()
    navigation()
    
    home_section()
    about_section()
    experience_section()
    projects_section()
    skills_section()
    contact_section()
    footer()

if __name__ == "__main__":
    main()