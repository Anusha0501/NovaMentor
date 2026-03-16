def evaluate_answer(question, answer):

    prompt = f"""
You are an expert technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and provide:

1. Score out of 10
2. What was correct
3. What concepts were missing
4. Suggestions for improvement

Keep feedback concise and structured.
"""

    return prompt