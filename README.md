# 🤖 NovaMentor AI – Interview Coach

> **AI-Powered Mock Interview Platform using Amazon Nova**

NovaMentor AI is an intelligent interview coaching platform that leverages **Amazon Nova Lite's advanced reasoning capabilities** to provide personalized, context-aware interview preparation for job seekers and students.

**#AmazonNova** | Built for the Amazon Nova AI Hackathon

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50-red.svg)
![AWS](https://img.shields.io/badge/AWS-Bedrock-orange.svg)
![Nova](https://img.shields.io/badge/Amazon-Nova%20Lite-purple.svg)

---

## 🚀 Problem Statement

Preparing for technical interviews is challenging because many candidates lack:

- **Real-time feedback** on their answers
- **Personalized questions** based on their experience and interests
- **Structured evaluation** calibrated to their skill level
- **Practice environments** that simulate real interviews

Traditional preparation relies on static question banks without interactive, intelligent feedback.

---

## 💡 Solution

NovaMentor AI acts as a **virtual AI interviewer** powered by Amazon Nova that:

### ✨ Key Features

| Feature | Description |
|---------|-------------|
| **🎯 Personalized Questions** | Dynamically generates questions based on candidate profile, tech stack, and interests |
| **📊 Smart Evaluation** | Strict, accurate scoring (0-10) with detailed feedback calibrated to experience level |
| **💻 Code Editor** | Built-in syntax-highlighted editor for LeetCode/DSA questions |
| **📋 Session Summary** | Comprehensive interview report with hiring recommendations |
| **🔄 Multiple Interview Types** | Interest-based, Scenario-based, System Design, and LeetCode/DSA |

### 🎭 Interview Types

1. **🎯 Interest-Based** – Questions tailored to your background and interests
2. **🎭 Scenario-Based** – Real-world problem-solving situations
3. **🏗️ System Design** – Architecture and scalability challenges
4. **💻 LeetCode/DSA** – Data structures and algorithms with code editor

---

## 🧠 How Amazon Nova is Used

NovaMentor leverages **Amazon Nova Lite via AWS Bedrock** for:

| Capability | Implementation |
|------------|----------------|
| **Dynamic Question Generation** | Nova generates personalized questions based on candidate context |
| **Answer Evaluation** | Advanced reasoning to assess technical accuracy and completeness |
| **Feedback Generation** | Context-aware suggestions calibrated to experience level |
| **Interview Summarization** | Comprehensive assessment with hiring recommendations |

Amazon Nova's **agentic reasoning capabilities** enable the system to act as an intelligent interviewer that adapts to each candidate's profile.

---

## 🏗️ Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Streamlit UI   │────▶│  Python Backend  │────▶│  AWS Bedrock    │
│  (Modern Dark   │     │  - LLM Client    │     │  - Nova Lite    │
│   Theme + Code  │◀────│  - Context Mgmt  │◀────│  - Reasoning    │
│   Editor)       │     │  - Prompts       │     │                 │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

### Scalable LLM Abstraction

The `llm_client.py` provides a clean abstraction that supports:
- **Amazon Nova** (production)
- **Ollama** (local development)

Switch between providers with a single line change.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Streamlit with custom dark theme, Streamlit-Ace code editor |
| **Backend** | Python 3.9+ |
| **AI Model** | Amazon Nova Lite (via AWS Bedrock) |
| **Libraries** | boto3, streamlit, streamlit-ace, requests |

---

## 📂 Project Structure

```
NovaMentor/
├── app.py              # Main Streamlit application
├── llm_client.py       # LLM abstraction (Nova/Ollama)
├── context.py          # Candidate profile management
├── prompts.py          # Question generation & evaluation prompts
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/novamentor-ai.git
cd novamentor-ai
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure AWS credentials

```bash
aws configure
```

Enter your AWS Access Key, Secret Key, and set region to `us-east-1`.

> ⚠️ **Important:** Ensure Amazon Nova models are enabled in your AWS Bedrock console.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open in browser: **http://localhost:8501**

---

## 🎥 Demo

The demo showcases:

1. **Profile Setup** – Enter candidate details (experience, tech stack, interests)
2. **Interview Type Selection** – Choose from 4 interview modes
3. **Dynamic Question Generation** – Nova creates personalized questions
4. **Answer Submission** – Text area or code editor based on question type
5. **AI Evaluation** – Detailed feedback with scoring
6. **Session Summary** – Comprehensive interview report

---

## 🌍 Impact

NovaMentor AI democratizes interview preparation by providing:

- **Accessible Practice** – Anyone can practice with an AI interviewer
- **Personalized Experience** – Questions tailored to individual backgrounds
- **Instant Feedback** – No waiting for human reviewers
- **Scalable Solution** – Can support millions of users globally

### Target Users
- 🎓 Students preparing for campus placements
- 💼 Professionals switching careers
- 🌐 Job seekers in underserved communities

---

## 🔮 Future Roadmap

- [ ] **Voice Interviews** – Real-time conversations using Nova Sonic
- [ ] **Resume Parsing** – Auto-generate questions from uploaded resumes
- [ ] **Interview History** – Track progress over multiple sessions
- [ ] **Difficulty Levels** – Adaptive difficulty based on performance
- [ ] **Multi-language Support** – Interviews in different languages

---

## 📊 Hackathon Category

**Agentic AI** – NovaMentor uses Amazon Nova's reasoning capabilities to:
- Understand candidate context and generate appropriate questions
- Evaluate answers with intelligent scoring
- Provide actionable feedback and recommendations

---

## 🏁 Hackathon Submission

Built for the **Amazon Nova AI Hackathon**

| Requirement | Status |
|-------------|--------|
| Uses Amazon Nova | ✅ Nova Lite via Bedrock |
| Gen AI Application | ✅ Interview Coach |
| Code Repository | ✅ GitHub |
| Demo Video | 🎬 [Link] |

**#AmazonNova**

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Built with ❤️ for the Amazon Nova AI Hackathon
