# Prompts for dynamic question generation and evaluation

QUESTION_GENERATION_PROMPT = """
You are an expert technical interviewer conducting a personalized interview.

{candidate_context}

## Interview Type: {interview_type}

Based on the candidate's profile above, generate ONE {interview_type_description} question.

Guidelines:
- Tailor the difficulty to the candidate's experience level
- Focus on their tech stack and interests when relevant
- Make the question specific and clear
- For LeetCode questions: include a clear problem statement with input/output examples
- For System Design: specify scale requirements and constraints
- For Scenario-based: create realistic workplace situations
- For Interest-based: connect to their background and interests

Respond with ONLY the question, no additional text or explanation.
"""

EVALUATE_ANSWER_PROMPT = """
You are an expert technical interviewer evaluating a candidate's response.

{candidate_context}

## Interview Type: {interview_type}

## Question Asked:
{question}

## Candidate's Answer:
{answer}

## Evaluation Instructions:
Evaluate the answer STRICTLY and ACCURATELY. Be honest and fair.

**CRITICAL SCORING GUIDELINES:**
- **0-1/10**: No answer, gibberish, completely irrelevant, or just random characters
- **2-3/10**: Minimal effort, very incomplete, shows little understanding
- **4-5/10**: Partial answer, some relevant points but missing key concepts
- **6-7/10**: Good answer with most key points covered, minor gaps
- **8-9/10**: Excellent answer, comprehensive with good depth
- **10/10**: Perfect answer, exceptional insight and completeness

**IMPORTANT**: 
- If the answer is empty, nonsensical, or just random text, score it 0-1/10
- Do NOT be generous with scores for incomplete or low-effort answers
- Actually read and evaluate what the candidate wrote, not what they might have meant

Respond in the following format:

### Score: X/10

### Strengths:
- [What the candidate did well - if nothing, say "None - answer was incomplete/irrelevant"]

### Areas for Improvement:
- [What concepts or details were missing]

### Suggestions:
- [Specific actionable advice to improve]

### Follow-up Question (Optional):
[A follow-up question to probe deeper understanding, if appropriate]

Be honest, specific, and fair in your evaluation.
"""

INTERVIEW_SUMMARY_PROMPT = """
You are an expert technical interviewer providing a final assessment.

{candidate_context}

## Interview Session Summary

The candidate answered {num_questions} questions during this session.

### Questions and Responses:
{qa_history}

## Task:
Provide a comprehensive interview summary including:

### Overall Assessment:
[2-3 sentences summarizing the candidate's performance]

### Technical Competency Score: X/10

### Communication Score: X/10

### Problem-Solving Score: X/10

### Key Strengths:
- [Top 3 strengths observed]

### Areas for Development:
- [Top 3 areas to improve]

### Hiring Recommendation:
[Strong Yes / Yes / Maybe / No / Strong No] with brief justification

### Suggested Learning Resources:
- [2-3 specific resources based on gaps identified]
"""


def generate_question_prompt(candidate_context: str, interview_type: str, interview_type_description: str) -> str:
    """Generate a prompt for creating interview questions."""
    return QUESTION_GENERATION_PROMPT.format(
        candidate_context=candidate_context,
        interview_type=interview_type,
        interview_type_description=interview_type_description
    )


def evaluate_answer_prompt(
    candidate_context: str,
    interview_type: str,
    question: str,
    answer: str
) -> str:
    """Generate a prompt for evaluating candidate answers."""
    return EVALUATE_ANSWER_PROMPT.format(
        candidate_context=candidate_context,
        interview_type=interview_type,
        question=question,
        answer=answer
    )


def interview_summary_prompt(candidate_context: str, qa_history: list) -> str:
    """Generate a prompt for the final interview summary."""
    formatted_history = ""
    for i, qa in enumerate(qa_history, 1):
        formatted_history += f"\n**Q{i} ({qa['type']}):** {qa['question']}\n"
        formatted_history += f"**Answer:** {qa['answer']}\n"
        formatted_history += f"**Score:** {qa.get('score', 'N/A')}\n"
    
    return INTERVIEW_SUMMARY_PROMPT.format(
        candidate_context=candidate_context,
        num_questions=len(qa_history),
        qa_history=formatted_history
    )