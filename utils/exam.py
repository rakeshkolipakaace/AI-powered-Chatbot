



# from utils.chatbot import get_learning_response

# def generate_exam(topic):
#     prompt = f"Generate 5 multiple-choice questions on {topic}, without showing answers."
#     try:
#         response = get_learning_response(prompt)
#         return response  # Only questions, no answers
#     except Exception as e:
#         raise Exception(f"Error generating exam: {str(e)}")

# def evaluate_exam(questions, user_answers):
#     # Fetch correct answers separately
#     answer_prompt = f"Provide only correct answers (one per line) for these questions:\n{questions}"
#     correct_answers = get_learning_response(answer_prompt).splitlines()

#     print("Correct Answers:", correct_answers)  # Debugging Step

#     user_answer_lines = user_answers.splitlines()
#     marks = 0
#     mistakes = []

#     for i, (u_answer, correct_answer) in enumerate(zip(user_answer_lines, correct_answers)):
#         print(f"Q{i+1} - User: {u_answer}, Correct: {correct_answer}")  # Debugging Step
        
#         if u_answer.strip().lower() == correct_answer.strip().lower():
#             marks += 1
#         else:
#             mistakes.append(f"Q{i+1}: Your Answer: {u_answer}, Correct Answer: {correct_answer}")

#     feedback = "Great job! No mistakes." if not mistakes else "\n".join(mistakes)
#     return marks, feedback



from utils.chatbot import get_learning_response
import re

def generate_exam(topic):
    prompt = (
        f"Generate 5 multiple-choice questions on the topic '{topic}'.\n"
        f"Each question should be followed by four options labeled a), b), c), d), "
        f"each on a separate line. Number the questions (e.g., 1., 2., etc.).\n"
        f"Do NOT include the answers or explanations in this response.\n"
        f"Example format:\n"
        f"1. Question text\n"
        f"a) Option 1\n"
        f"b) Option 2\n"
        f"c) Option 3\n"
        f"d) Option 4\n"
    )
    try:
        response = get_learning_response(prompt)
        return format_mcq_text(response)
    except Exception as e:
        raise Exception(f"Error generating exam: {str(e)}")

def format_mcq_text(text):
    formatted = re.sub(r'(?<!\n)\s*([a-d]\))', r'\n\1', text)
    return formatted.strip()

def extract_option(answer):
    match = re.search(r'([a-dA-D])', answer)
    return match.group(1).lower() if match else None

def evaluate_exam(questions, user_answers):
    # Get correct answers
    answer_prompt = (
        f"Provide only the correct answer letters (a, b, c, or d) for these questions, one per line, numbered 1 to 5:\n"
        f"{questions}"
    )
    correct_answers_raw = get_learning_response(answer_prompt).strip()
    correct_answers = correct_answers_raw.splitlines()
    
    # Get explanations
    explanation_prompt = (
        f"For these questions, provide a one-line explanation for each correct answer, "
        f"numbered 1. to 5. to match the questions (e.g., '1. Explanation text'), one per line:\n"
        f"{questions}"
    )
    explanations_raw = get_learning_response(explanation_prompt).strip()
    explanations = explanations_raw.splitlines()

    # Debugging: Print raw responses to inspect
    print("Debug - Correct Answers Raw:\n", correct_answers_raw)
    print("Debug - Explanations Raw:\n", explanations_raw)

    user_answer_lines = user_answers.strip().splitlines()
    marks = 0
    mistakes = []

    # Ensure we have 5 answers and explanations
    if len(correct_answers) != 5 or len(explanations) != 5:
        raise ValueError(f"Expected 5 answers and explanations, got {len(correct_answers)} answers and {len(explanations)} explanations")

    for i, (u_answer, correct_answer, explanation) in enumerate(
        zip(user_answer_lines, correct_answers, explanations)
    ):
        user_opt = extract_option(u_answer)
        correct_opt = extract_option(correct_answer)
        # Clean explanation by removing numbering
        explanation_text = re.sub(r'^\d+\.\s*', '', explanation).strip()

        if user_opt == correct_opt:
            marks += 1
        else:
            mistakes.append(
                f"Q{i+1}: Your Answer: {user_opt}\n"
                f"Correct Answer: {correct_opt})\n"
                f"Explanation: {explanation_text}"
            )

    feedback = "🎉 Great job! No mistakes." if not mistakes else "\n\n".join(mistakes)
    return marks, feedback

# Example usage
if __name__ == "__main__":
    topic = "full-stack development"
    questions = generate_exam(topic)
    print("📄 Questions")
    print(questions)

    user_answers = "a\na\na\na\na"
    marks, feedback = evaluate_exam(questions, user_answers)
    print(f"\n✅ Exam submitted successfully!")
    print(f"🎓 Your Score: {marks}/5")
    print("🧠 Mistakes & Feedback:")
    print(feedback)