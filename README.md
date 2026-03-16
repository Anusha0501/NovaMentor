# 🤖 NovaMentor AI – Interview Coach

NovaMentor AI is an AI-powered mock interview platform built using **Amazon Nova foundation models via AWS Bedrock**.
The system simulates technical interview questions and evaluates candidate responses, providing structured feedback to help users improve their interview performance.

This project demonstrates how **Amazon Nova Lite reasoning capabilities** can power intelligent coaching systems for students and job seekers.

---

# 🚀 Problem

Preparing for technical interviews is challenging because many students lack:

* Real-time feedback on answers
* Structured evaluation of their responses
* Practice environments similar to real interviews

Traditional preparation methods rely on self-study or static question banks without interactive feedback.

---

# 💡 Solution

NovaMentor AI acts as a **virtual AI interviewer** that:

1. Presents technical interview questions
2. Allows the candidate to submit an answer
3. Uses **Amazon Nova Lite** to evaluate the response
4. Provides structured feedback including:

   * Score out of 10
   * Correct concepts
   * Missing concepts
   * Suggestions for improvement

This allows users to practice interviews in an **interactive AI-driven environment**.

---

# 🧠 How Amazon Nova is Used

The system uses **Amazon Nova Lite via AWS Bedrock** to perform:

* Reasoning over candidate responses
* Technical answer evaluation
* Generating improvement suggestions

Amazon Nova's advanced reasoning capabilities allow the system to provide **context-aware feedback** similar to a real interviewer.

---

# 🏗 Architecture

User Input → Streamlit UI → Python Backend → Amazon Bedrock API → Nova Lite Model → AI Feedback

---

# 🛠 Tech Stack

Frontend

* Streamlit

Backend

* Python

AI Model

* Amazon Nova Lite (via AWS Bedrock)

Libraries

* boto3
* streamlit

---

# 📂 Project Structure

```
novamentor-ai/
│
├── app.py
├── nova_client.py
├── prompts.py
├── questions.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/your-username/novamentor-ai.git
cd novamentor-ai
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# 🔑 AWS Setup

Configure AWS credentials:

```
aws configure
```

Enter:

```
AWS Access Key
AWS Secret Key
Region: us-east-1
```

Make sure **Amazon Nova models are enabled in Amazon Bedrock**.

---

# ▶️ Run the Application

```
streamlit run app.py
```

Open the application in your browser:

```
http://localhost:8501
```

---

# 🎥 Demo

The demo shows:

1. The AI presenting an interview question
2. The user submitting an answer
3. Amazon Nova evaluating the response
4. The system generating structured feedback

---

# 🌍 Impact

NovaMentor AI helps students and job seekers:

* Practice technical interviews
* Receive instant AI-powered feedback
* Improve their communication and problem-solving skills

This system can scale to support **millions of learners globally**, providing accessible AI-driven interview preparation.

---

# 🔮 Future Improvements

* Voice-based interviews using **Nova Sonic**
* Personalized learning recommendations
* Resume-based question generation
* Interview difficulty levels

---

# 🏁 Hackathon Submission

Built for the **Amazon Nova AI Hackathon** using Amazon Nova foundation models.

#AmazonNova
