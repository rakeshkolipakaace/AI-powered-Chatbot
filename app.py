
# import streamlit as st
# import google.generativeai as genai
# from utils.auth import login_user, register_user
# from utils.chatbot import get_learning_response
# from utils.exam import generate_exam, evaluate_exam
# from utils.db import store_result, get_user_results

# # Load custom CSS
# with open("static/style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # Initialize session state
# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False
#     st.session_state["username"] = None
#     st.session_state["chat_history"] = []
#     st.session_state["exam_active"] = False
#     st.session_state["exam_questions"] = ""
#     st.session_state["menu"] = "Login"  # Default menu

# # Sidebar Navigation
# st.sidebar.title("EduBot")

# if not st.session_state["logged_in"]:
#     menu = st.sidebar.radio("Menu", ["Login", "Register"])
# else:
#     menu = st.sidebar.radio("Menu", ["Learn", "Exam", "Results"])
    
#     if st.sidebar.button("Logout"):
#         st.session_state["logged_in"] = False
#         st.session_state["username"] = None
#         st.session_state["chat_history"] = []
#         st.session_state["exam_active"] = False
#         st.session_state["menu"] = "Login"
#         st.success("Logged out successfully!")
#         st.experimental_rerun()

# # Main Logic
# if menu == "Login":
#     st.title("Login to EduBot")
#     username = st.sidebar.text_input("Username")
#     password = st.sidebar.text_input("Password", type="password")
    
#     if st.sidebar.button("Login"):
#         if login_user(username, password):
#             st.session_state["logged_in"] = True
#             st.session_state["username"] = username
#             st.session_state["menu"] = "Results"  # Redirect to Results
#             st.success("Logged in successfully!")
#             st.experimental_rerun()  # Redirect to Results
#         else:
#             st.error("Invalid credentials or error connecting to database.")

# elif menu == "Register":
#     st.title("Register for EduBot")
#     username = st.sidebar.text_input("New Username")
#     password = st.sidebar.text_input("New Password", type="password")
    
#     if st.sidebar.button("Register"):
#         try:
#             register_user(username, password)
#             st.success("Registered successfully! Please log in.")
#         except Exception as e:
#             st.error(f"Registration failed: {str(e)}")

# elif menu == "Learn":
#     st.title(f"Welcome, {st.session_state['username']}!")
    
#     try:
#         st.image("static/images/banner.jpg", use_column_width=True)
#     except Exception:
#         st.warning("Banner image not found. Continuing without it.")

#     prompt = st.text_area("Ask me anything to learn!", key="learn_input")
    
#     if st.button("Submit"):
#         if prompt:
#             try:
#                 response = get_learning_response(prompt)
#                 st.session_state["chat_history"].append({"user": prompt, "ai": response})
#                 st.success("Response received!")
#             except Exception as e:
#                 st.error(f"Error with chatbot: {str(e)}")

#     # Display chat history
#     if st.session_state["chat_history"]:
#         st.subheader("Chat History")
#         for chat in st.session_state["chat_history"]:
#             st.write(f"**You**: {chat['user']}")
#             st.write(f"**AI**: {chat['ai']}")

# elif menu == "Exam":
#     st.title("Take an Exam")
#     topic = st.text_input("Enter a topic for the exam")
    
#     if st.button("Start Exam") and topic:
#         try:
#             questions = generate_exam(topic)
#             st.session_state["exam_questions"] = questions
#             st.session_state["exam_active"] = True
#             st.success("Exam started! Answer the questions below.")
#         except Exception as e:
#             st.error(f"Error generating exam: {str(e)}")

#     if st.session_state["exam_active"]:
#         st.write("Questions:", st.session_state["exam_questions"])
#         answers = st.text_area("Enter your answers (one per line)", key="exam_input")
        
#         if st.button("Submit Answers"):
#             try:
#                 marks, mistakes = evaluate_exam(st.session_state["exam_questions"], answers)
#                 store_result(st.session_state["username"], topic, marks, mistakes)
#                 st.write(f"Your Score: {marks}/5")
#                 st.write("Mistakes and Feedback:", mistakes)
#                 st.session_state["exam_active"] = False
#                 st.success("Exam submitted successfully!")
#             except Exception as e:
#                 st.error(f"Error evaluating exam: {str(e)}")

# elif menu == "Results":
#     st.title("Your Results")
    
#     try:
#         results = get_user_results(st.session_state["username"])
#         if results:
#             for result in results:
#                 st.write(f"Topic: {result['topic']}, Score: {result['marks']}/5, Date: {result['date']}")
#                 st.write(f"Mistakes: {result['mistakes']}")
#         else:
#             st.write("No results yet. Take an exam!")
#     except Exception as e:
#         st.error(f"Error fetching results: {str(e)}")




import streamlit as st
import google.generativeai as genai
from utils.auth import login_user, register_user
from utils.chatbot import get_learning_response
from utils.exam import generate_exam, evaluate_exam
from utils.db import store_result, get_user_results

# Load custom CSS
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.session_state["chat_history"] = []
    st.session_state["exam_active"] = False
    st.session_state["exam_questions"] = ""
    st.session_state["menu"] = "Login"

# Sidebar Navigation
st.sidebar.title("📘 EduBot")

if not st.session_state["logged_in"]:
    menu = st.sidebar.radio("🔐 Menu", ["Login", "Register"])
else:
    menu = st.sidebar.radio("📚 Menu", ["Learn", "Exam", "Results"])
    
    if st.sidebar.button("🚪 Logout"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = None
        st.session_state["chat_history"] = []
        st.session_state["exam_active"] = False
        st.session_state["menu"] = "Login"
        st.success("✅ Logged out successfully!")
        st.rerun()

# Main Logic
if menu == "Login":
    st.title("🔑 Login to EduBot")
    username = st.sidebar.text_input("👤 Username")
    password = st.sidebar.text_input("🔒 Password", type="password")
    
    if st.sidebar.button("Login"):
        if login_user(username, password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["menu"] = "Results"
            st.success("✅ Logged in successfully!")
            st.rerun()
        else:
            st.error("❌ Invalid credentials or error connecting to database.")

elif menu == "Register":
    st.title("📝 Register for EduBot")
    username = st.sidebar.text_input("👤 New Username")
    password = st.sidebar.text_input("🔒 New Password", type="password")
    
    if st.sidebar.button("Register"):
        try:
            register_user(username, password)
            st.success("✅ Registered successfully! Please log in.")
        except Exception as e:
            st.error(f"❌ Registration failed: {str(e)}")

elif menu == "Learn":
    st.title(f"👋 Welcome, {st.session_state['username']}!")
    
    try:
        st.image("static/images/banner.jpg", use_column_width=True)
    except Exception:
        st.warning("⚠️ Banner image not found. Continuing without it.")

    prompt = st.text_area("💬 Ask me anything to learn!", key="learn_input")
    
    if st.button("🚀 Submit"):
        if prompt:
            try:
                response = get_learning_response(prompt)
                st.session_state["chat_history"].append({"user": prompt, "ai": response})
                st.success("✅ Response received!")
            except Exception as e:
                st.error(f"❌ Error with chatbot: {str(e)}")

    if st.session_state["chat_history"]:
        st.subheader("📜 Chat History")
        for chat in st.session_state["chat_history"]:
            st.markdown(f"**🧑 You**: {chat['user']}")
            st.markdown(f"**🤖 AI**: {chat['ai']}")

elif menu == "Exam":
    st.title("📝 Take an Exam")
    topic = st.text_input("📚 Enter a topic for the exam")
    
    if st.button("🎯 Start Exam") and topic:
        try:
            questions = generate_exam(topic)
            st.session_state["exam_questions"] = questions
            st.session_state["exam_active"] = True
            st.success("✅ Exam started! Answer the questions below.")
        except Exception as e:
            st.error(f"❌ Error generating exam: {str(e)}")

    if st.session_state["exam_active"]:
        st.subheader("📄 Questions")
        st.write(st.session_state["exam_questions"])
        answers = st.text_area("✏️ Enter your answers (one per line)", key="exam_input")
        
        if st.button("📤 Submit Answers"):
            try:
                marks, mistakes = evaluate_exam(st.session_state["exam_questions"], answers)
                store_result(st.session_state["username"], topic, marks, mistakes)
                st.success("✅ Exam submitted successfully!")
                st.write(f"🎓 **Your Score:** {marks}/5")
                st.write("🧠 **Mistakes & Feedback:**")
                st.markdown(mistakes)
                st.session_state["exam_active"] = False
            except Exception as e:
                st.error(f"❌ Error evaluating exam: {str(e)}")

elif menu == "Results":
    st.title("📊 Your Results")
    
    try:
        results = get_user_results(st.session_state["username"])
        if results:
            for result in results:
                st.markdown(f"""
                #### 📌 Topic: {result['topic']}
                - 🏆 Score: **{result['marks']}/5**
                - 🗓️ Date: {result['date']}
                - ❗ Mistakes: {result['mistakes']}
                ---
                """)
        else:
            st.info("ℹ️ No results yet. Take an exam!")
    except Exception as e:
        st.error(f"❌ Error fetching results: {str(e)}")

