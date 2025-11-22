import streamlit as st
from pathlib import Path
import base64

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="Your Name | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========== CUSTOM CSS ==========
def local_css():
    st.markdown("""
    <style>
    /* Main Theme */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Responsive Container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Navigation */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        padding: 1.5rem 0;
        border-bottom: 1px solid #e0e0e0;
        margin-bottom: 2rem;
        flex-wrap: wrap;
    }
    
    .nav-link {
        text-decoration: none;
        color: #333;
        font-weight: 500;
        font-size: 1rem;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .nav-link:hover {
        background-color: #f0f0f0;
        color: #000;
    }
    
    /* Hero Section */
    .hero-section {
        text-align: center;
        padding: 4rem 0;
        animation: fadeIn 1s ease-in;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #666;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    /* Profile Image */
    .profile-img {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
        margin: 2rem auto;
        display: block;
        border: 4px solid #667eea;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    /* Cards */
    .card {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid #f0f0f0;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #333;
    }
    
    .card-subtitle {
        font-size: 1rem;
        color: #667eea;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .card-text {
        color: #666;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    /* Buttons */
    .custom-button {
        display: inline-block;
        padding: 0.75rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-decoration: none;
        border-radius: 25px;
        font-weight: 500;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        margin: 0.5rem;
    }
    
    .custom-button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        color: white;
    }
    
    /* Skills Pills */
    .skill-pill {
        display: inline-block;
        background: #f0f0f0;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.25rem;
        font-size: 0.9rem;
        color: #333;
        font-weight: 500;
    }
    
    /* Timeline */
    .timeline-item {
        border-left: 2px solid #667eea;
        padding-left: 2rem;
        margin-left: 1rem;
        margin-bottom: 2rem;
        position: relative;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 0;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: #667eea;
    }
    
    .timeline-date {
        color: #667eea;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    .timeline-title {
        font-size: 1.2rem;
        font-weight: 600;
        margin: 0.5rem 0;
    }
    
    .timeline-subtitle {
        color: #666;
        font-style: italic;
        margin-bottom: 0.5rem;
    }
    
    /* Social Links */
    .social-links {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin: 2rem 0;
        flex-wrap: wrap;
    }
    
    .social-link {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #f0f0f0;
        transition: all 0.3s ease;
        text-decoration: none;
        font-size: 1.5rem;
    }
    
    .social-link:hover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        transform: translateY(-5px);
        color: white;
    }
    
    /* Contact Form */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        padding: 0.75rem;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.6s ease-in;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
        }
        
        .profile-img {
            width: 150px;
            height: 150px;
        }
        
        .nav-container {
            gap: 1rem;
        }
        
        .card {
            padding: 1.5rem;
        }
    }
    
    /* Section Headers */
    .section-header {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin: 3rem 0 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Project Tags */
    .project-tag {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        margin: 0.25rem;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    /* Download Button */
    .download-btn {
        background: #4CAF50;
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        transition: all 0.3s ease;
    }
    
    .download-btn:hover {
        background: #45a049;
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(76, 175, 80, 0.4);
    }
    
    </style>
    """, unsafe_allow_html=True)

# ========== HELPER FUNCTIONS ==========
def img_to_base64(image_path):
    """Convert image to base64"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

def show_pdf(file_path):
    """Display PDF file"""
    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except:
        st.error("PDF file not found. Please add your resume.pdf to the project folder.")

# ========== NAVIGATION ==========
def navigation():
    st.markdown("""
    <div class="nav-container">
        <a href="#home" class="nav-link">🏠 Home</a>
        <a href="#about" class="nav-link">👤 About</a>
        <a href="#resume" class="nav-link">📄 Resume</a>
        <a href="#projects" class="nav-link">💼 Projects</a>
        <a href="#skills" class="nav-link">🚀 Skills</a>
        <a href="#contact" class="nav-link">📧 Contact</a>
    </div>
    """, unsafe_allow_html=True)

# ========== SECTIONS ==========
def home_section():
    st.markdown('<div class="hero-section fade-in">', unsafe_allow_html=True)
    
    # Profile Image (optional - uncomment and add your image)
    # img_base64 = img_to_base64("profile.jpg")
    # if img_base64:
    #     st.markdown(f'<img src="data:image/jpeg;base64,{img_base64}" class="profile-img">', unsafe_allow_html=True)
    
    st.markdown('<h1 class="hero-title">👋 Hi, I\'m Your Name</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Full Stack Developer | Data Scientist | Creative Problem Solver</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <a href="#contact" class="custom-button">Get In Touch</a>
            <a href="#projects" class="custom-button">View My Work</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def about_section():
    st.markdown('<h2 class="section-header" id="about">About Me</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2,1])
    
    with col1:
        st.markdown("""
        <div class="card fade-in">
            <p class="card-text">
                I'm a passionate developer with a love for creating elegant solutions to complex problems. 
                With <strong>X years</strong> of experience in software development, I specialize in building 
                scalable web applications and data-driven solutions.
            </p>
            <p class="card-text">
                My journey in tech started with curiosity and has evolved into a career where I get to 
                work on exciting projects that make a real impact. I'm always eager to learn new 
                technologies and collaborate with talented people.
            </p>
            <p class="card-text">
                When I'm not coding, you can find me exploring new technologies, contributing to 
                open-source projects, or enjoying a good cup of coffee while reading tech blogs.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card fade-in">
            <h3 class="card-title">Quick Facts</h3>
            <p class="card-text">📍 <strong>Location:</strong> Your City, Country</p>
            <p class="card-text">🎓 <strong>Education:</strong> Your Degree</p>
            <p class="card-text">💼 <strong>Experience:</strong> X Years</p>
            <p class="card-text">🌐 <strong>Languages:</strong> English, Others</p>
            <p class="card-text">☕ <strong>Coffee:</strong> Enthusiast</p>
        </div>
        """, unsafe_allow_html=True)

def resume_section():
    st.markdown('<h2 class="section-header" id="resume">Resume</h2>', unsafe_allow_html=True)
    
    # Download Resume Button
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <a href="#" class="download-btn" download>📥 Download Resume (PDF)</a>
        </div>
        """, unsafe_allow_html=True)
    
    # Experience
    st.markdown("### 💼 Work Experience")
    
    st.markdown("""
    <div class="timeline-item fade-in">
        <p class="timeline-date">2022 - Present</p>
        <h3 class="timeline-title">Senior Software Engineer</h3>
        <p class="timeline-subtitle">Company Name | City, Country</p>
        <p class="card-text">
            • Led development of microservices architecture serving 1M+ users<br>
            • Implemented CI/CD pipelines reducing deployment time by 60%<br>
            • Mentored junior developers and conducted code reviews
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item fade-in">
        <p class="timeline-date">2020 - 2022</p>
        <h3 class="timeline-title">Software Developer</h3>
        <p class="timeline-subtitle">Previous Company | City, Country</p>
        <p class="card-text">
            • Developed RESTful APIs using Python and FastAPI<br>
            • Built responsive web applications with React and TypeScript<br>
            • Collaborated with cross-functional teams in Agile environment
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Education
    st.markdown("### 🎓 Education")
    
    st.markdown("""
    <div class="timeline-item fade-in">
        <p class="timeline-date">2016 - 2020</p>
        <h3 class="timeline-title">Bachelor of Science in Computer Science</h3>
        <p class="timeline-subtitle">University Name | City, Country</p>
        <p class="card-text">
            • GPA: 3.8/4.0<br>
            • Relevant Coursework: Data Structures, Algorithms, Database Systems, Machine Learning<br>
            • Dean's List all semesters
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Certifications
    st.markdown("### 🏆 Certifications")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card fade-in">
            <p class="card-subtitle">AWS Certified Solutions Architect</p>
            <p class="card-text">Amazon Web Services - 2023</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card fade-in">
            <p class="card-subtitle">Google Cloud Professional</p>
            <p class="card-text">Google Cloud - 2022</p>
        </div>
        """, unsafe_allow_html=True)

def projects_section():
    st.markdown('<h2 class="section-header" id="projects">Projects</h2>', unsafe_allow_html=True)
    
    # Project 1
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="card fade-in">
            <h3 class="card-title">🚀 E-Commerce Platform</h3>
            <p class="card-text">
                A full-stack e-commerce solution with real-time inventory management, 
                payment processing, and admin dashboard. Built with React, Node.js, and MongoDB.
            </p>
            <div>
                <span class="project-tag">React</span>
                <span class="project-tag">Node.js</span>
                <span class="project-tag">MongoDB</span>
                <span class="project-tag">Stripe</span>
            </div>
            <br><br>
            <a href="https://github.com/yourusername/project1" target="_blank" class="custom-button">View on GitHub</a>
            <a href="https://project1-demo.com" target="_blank" class="custom-button">Live Demo</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card fade-in">
            <h3 class="card-title">📊 Data Analytics Dashboard</h3>
            <p class="card-text">
                Interactive dashboard for visualizing business metrics and KPIs. 
                Features real-time data updates, custom reports, and predictive analytics.
            </p>
            <div>
                <span class="project-tag">Python</span>
                <span class="project-tag">Streamlit</span>
                <span class="project-tag">Plotly</span>
                <span class="project-tag">PostgreSQL</span>
            </div>
            <br><br>
            <a href="https://github.com/yourusername/project2" target="_blank" class="custom-button">View on GitHub</a>
            <a href="https://project2-demo.com" target="_blank" class="custom-button">Live Demo</a>
        </div>
        """, unsafe_allow_html=True)
    
    # Project 3
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="card fade-in">
            <h3 class="card-title">🤖 AI Chatbot</h3>
            <p class="card-text">
                Intelligent chatbot using NLP and machine learning to provide customer support. 
                Achieves 90% accuracy in intent classification.
            </p>
            <div>
                <span class="project-tag">Python</span>
                <span class="project-tag">TensorFlow</span>
                <span class="project-tag">NLP</span>
                <span class="project-tag">FastAPI</span>
            </div>
            <br><br>
            <a href="https://github.com/yourusername/project3" target="_blank" class="custom-button">View on GitHub</a>
            <a href="https://project3-demo.com" target="_blank" class="custom-button">Live Demo</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card fade-in">
            <h3 class="card-title">🌐 Social Media App</h3>
            <p class="card-text">
                Full-featured social networking platform with posts, comments, likes, 
                and real-time messaging. Supports 10,000+ concurrent users.
            </p>
            <div>
                <span class="project-tag">React</span>
                <span class="project-tag">Firebase</span>
                <span class="project-tag">WebSocket</span>
                <span class="project-tag">Redux</span>
            </div>
            <br><br>
            <a href="https://github.com/yourusername/project4" target="_blank" class="custom-button">View on GitHub</a>
            <a href="https://project4-demo.com" target="_blank" class="custom-button">Live Demo</a>
        </div>
        """, unsafe_allow_html=True)

def skills_section():
    st.markdown('<h2 class="section-header" id="skills">Skills & Technologies</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card fade-in">
            <h3 class="card-title">💻 Frontend</h3>
            <span class="skill-pill">React</span>
            <span class="skill-pill">Vue.js</span>
            <span class="skill-pill">TypeScript</span>
            <span class="skill-pill">JavaScript</span>
            <span class="skill-pill">HTML/CSS</span>
            <span class="skill-pill">Tailwind</span>
            <span class="skill-pill">Bootstrap</span>
            <span class="skill-pill">Streamlit</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card fade-in">
            <h3 class="card-title">⚙️ Backend</h3>
            <span class="skill-pill">Python</span>
            <span class="skill-pill">Node.js</span>
            <span class="skill-pill">FastAPI</span>
            <span class="skill-pill">Django</span>
            <span class="skill-pill">Express</span>
            <span class="skill-pill">PostgreSQL</span>
            <span class="skill-pill">MongoDB</span>
            <span class="skill-pill">Redis</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card fade-in">
            <h3 class="card-title">🛠️ Tools & Others</h3>
            <span class="skill-pill">Git</span>
            <span class="skill-pill">Docker</span>
            <span class="skill-pill">AWS</span>
            <span class="skill-pill">CI/CD</span>
            <span class="skill-pill">Linux</span>
            <span class="skill-pill">Kubernetes</span>
            <span class="skill-pill">GraphQL</span>
            <span class="skill-pill">Agile</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Skill Bars
    st.markdown("### 📈 Proficiency Levels")
    
    skills_data = {
        "Python": 95,
        "JavaScript": 90,
        "React": 85,
        "Node.js": 80,
        "Data Analysis": 88,
        "Machine Learning": 75,
        "Cloud (AWS)": 70,
        "DevOps": 65
    }
    
    for skill, level in skills_data.items():
        st.markdown(f"**{skill}**")
        st.progress(level / 100)

def contact_section():
    st.markdown('<h2 class="section-header" id="contact">Get In Touch</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="card fade-in">
            <h3 class="card-title">📬 Contact Information</h3>
            <p class="card-text">
                <strong>📧 Email:</strong> your.email@example.com<br>
                <strong>📱 Phone:</strong> +1 (123) 456-7890<br>
                <strong>📍 Location:</strong> Your City, Country<br>
                <strong>🕐 Timezone:</strong> GMT+X
            </p>
            <br>
            <h3 class="card-title">🌐 Social Media</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="social-links">
            <a href="https://github.com/yourusername" target="_blank" class="social-link" title="GitHub">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
            </a>
            <a href="https://linkedin.com/in/yourusername" target="_blank" class="social-link" title="LinkedIn">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                </svg>
            </a>
            <a href="https://twitter.com/yourusername" target="_blank" class="social-link" title="Twitter">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
                </svg>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card fade-in">', unsafe_allow_html=True)
        st.markdown('<h3 class="card-title">💌 Send Me a Message</h3>', unsafe_allow_html=True)
        
        with st.form("contact_form"):
            name = st.text_input("Your Name *", placeholder="John Doe")
            email = st.text_input("Your Email *", placeholder="john@example.com")
            subject = st.text_input("Subject *", placeholder="Project Inquiry")
            message = st.text_area("Message *", placeholder="Tell me about your project...", height=150)
            
            submitted = st.form_submit_button("Send Message 🚀")
            
            if submitted:
                if name and email and subject and message:
                    st.success("✅ Message sent successfully! I'll get back to you soon.")
                    # Here you can add actual email sending logic using services like SendGrid, EmailJS, etc.
                else:
                    st.error("❌ Please fill in all fields.")
        
        st.markdown('</div>', unsafe_allow_html=True)

# ========== FOOTER ==========
def footer():
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; color: #666;">
        <p>Made with ❤️ using Streamlit | © 2024 Your Name | All Rights Reserved</p>
        <p style="font-size: 0.9rem; margin-top: 0.5rem;">
            <a href="#home" style="color: #667eea; text-decoration: none; margin: 0 0.5rem;">Home</a> |
            <a href="#about" style="color: #667eea; text-decoration: none; margin: 0 0.5rem;">About</a> |
            <a href="#projects" style="color: #667eea; text-decoration: none; margin: 0 0.5rem;">Projects</a> |
            <a href="#contact" style="color: #667eea; text-decoration: none; margin: 0 0.5rem;">Contact</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ========== MAIN APP ==========
def main():
    local_css()
    navigation()
    
    home_section()
    about_section()
    resume_section()
    projects_section()
    skills_section()
    contact_section()
    footer()

if __name__ == "__main__":
    main()