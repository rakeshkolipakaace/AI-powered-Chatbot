
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
#     st.session_state["menu"] = "Login"

# # Sidebar Navigation
# st.sidebar.title("📘 EduBot")

# if not st.session_state["logged_in"]:
#     menu = st.sidebar.radio("🔐 Menu", ["Login", "Register"])
# else:
#     menu = st.sidebar.radio("📚 Menu", ["Learn", "Exam", "Results"])
    
#     if st.sidebar.button("🚪 Logout"):
#         st.session_state["logged_in"] = False
#         st.session_state["username"] = None
#         st.session_state["chat_history"] = []
#         st.session_state["exam_active"] = False
#         st.session_state["menu"] = "Login"
#         st.success("✅ Logged out successfully!")
#         st.rerun()

# # Main Logic
# if menu == "Login":
#     st.title("🔑 Login to EduBot")
#     username = st.sidebar.text_input("👤 Username")
#     password = st.sidebar.text_input("🔒 Password", type="password")
    
#     if st.sidebar.button("Login"):
#         if login_user(username, password):
#             st.session_state["logged_in"] = True
#             st.session_state["username"] = username
#             st.session_state["menu"] = "Results"
#             st.success("✅ Logged in successfully!")
#             st.rerun()
#         else:
#             st.error("❌ Invalid credentials or error connecting to database.")

# elif menu == "Register":
#     st.title("📝 Register for EduBot")
#     username = st.sidebar.text_input("👤 New Username")
#     password = st.sidebar.text_input("🔒 New Password", type="password")
    
#     if st.sidebar.button("Register"):
#         try:
#             register_user(username, password)
#             st.success("✅ Registered successfully! Please log in.")
#         except Exception as e:
#             st.error(f"❌ Registration failed: {str(e)}")

# elif menu == "Learn":
#     st.title(f"👋 Welcome, {st.session_state['username']}!")
    
#     try:
#         st.image("static/images/banner.jpg", use_column_width=True)
#     except Exception:
#         st.warning("⚠️ Banner image not found. Continuing without it.")

#     prompt = st.text_area("💬 Ask me anything to learn!", key="learn_input")
    
#     if st.button("🚀 Submit"):
#         if prompt:
#             try:
#                 response = get_learning_response(prompt)
#                 st.session_state["chat_history"].append({"user": prompt, "ai": response})
#                 st.success("✅ Response received!")
#             except Exception as e:
#                 st.error(f"❌ Error with chatbot: {str(e)}")

#     if st.session_state["chat_history"]:
#         st.subheader("📜 Chat History")
#         for chat in st.session_state["chat_history"]:
#             st.markdown(f"**🧑 You**: {chat['user']}")
#             st.markdown(f"**🤖 AI**: {chat['ai']}")

# elif menu == "Exam":
#     st.title("📝 Take an Exam")
#     topic = st.text_input("📚 Enter a topic for the exam")
    
#     if st.button("🎯 Start Exam") and topic:
#         try:
#             questions = generate_exam(topic)
#             st.session_state["exam_questions"] = questions
#             st.session_state["exam_active"] = True
#             st.success("✅ Exam started! Answer the questions below.")
#         except Exception as e:
#             st.error(f"❌ Error generating exam: {str(e)}")

#     if st.session_state["exam_active"]:
#         st.subheader("📄 Questions")
#         st.write(st.session_state["exam_questions"])
#         answers = st.text_area("✏️ Enter your answers (one per line)", key="exam_input")
        
#         if st.button("📤 Submit Answers"):
#             try:
#                 marks, mistakes = evaluate_exam(st.session_state["exam_questions"], answers)
#                 store_result(st.session_state["username"], topic, marks, mistakes)
#                 st.success("✅ Exam submitted successfully!")
#                 st.write(f"🎓 **Your Score:** {marks}/5")
#                 st.write("🧠 **Mistakes & Feedback:**")
#                 st.markdown(mistakes)
#                 st.session_state["exam_active"] = False
#             except Exception as e:
#                 st.error(f"❌ Error evaluating exam: {str(e)}")

# elif menu == "Results":
#     st.title("📊 Your Results")
    
#     try:
#         results = get_user_results(st.session_state["username"])
#         if results:
#             for result in results:
#                 st.markdown(f"""
#                 #### 📌 Topic: {result['topic']}
#                 - 🏆 Score: **{result['marks']}/5**
#                 - 🗓️ Date: {result['date']}
#                 - ❗ Mistakes: {result['mistakes']}
#                 ---
#                 """)
#         else:
#             st.info("ℹ️ No results yet. Take an exam!")
#     except Exception as e:
#         st.error(f"❌ Error fetching results: {str(e)}")





# import streamlit as st
# from streamlit_lottie import st_lottie
# import requests
# import google.generativeai as genai
# from utils.auth import login_user, register_user
# from utils.chatbot import get_learning_response
# from utils.exam import generate_exam, evaluate_exam
# from utils.db import store_result, get_user_results

# # Load custom CSS
# with open("static/style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # Helper to load Lottie animation
# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# # Initialize session state
# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False
#     st.session_state["username"] = None
#     st.session_state["chat_history"] = []
#     st.session_state["exam_active"] = False
#     st.session_state["exam_questions"] = ""
#     st.session_state["menu"] = "Login"

# # Sidebar Navigation
# st.sidebar.title("📘 EduBot")

# if not st.session_state["logged_in"]:
#     menu = st.sidebar.radio("🔐 Menu", ["Login", "Register"])
# else:
#     menu = st.sidebar.radio("📚 Menu", ["Learn", "Exam", "Results"])

#     if st.sidebar.button("🚪 Logout"):
#         st.session_state["logged_in"] = False
#         st.session_state["username"] = None
#         st.session_state["chat_history"] = []
#         st.session_state["exam_active"] = False
#         st.session_state["menu"] = "Login"
#         st.success("✅ Logged out successfully!")
#         st.rerun()

# # Main Logic
# if menu == "Login":
#     st.title("🤖 GenEDxAI")
#     # Lottie Animation
#     lottie_login = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_1pxqjqps.json")
#     if lottie_login:
#         st_lottie(lottie_login, height=570, width=1180)
        
#         st.write("👋 Welcome to GenEDxAI! A platform that uses AI to create educational content and evaluate your learning. Whether you’re a student or educator, we provide personalized support and quizzes to help you succeed!")


#     username = st.sidebar.text_input("👤 Username")
#     password = st.sidebar.text_input("🔒 Password", type="password")
    
#     if st.sidebar.button("Login"):
#         if login_user(username, password):
#             st.session_state["logged_in"] = True
#             st.session_state["username"] = username
#             st.session_state["menu"] = "Results"
#             st.success("✅ Logged in successfully!")
#             st.rerun()
#         else:
#             st.error("❌ Invalid credentials or error connecting to database.")

# elif menu == "Register":
#     st.title("📝 Register for EduBot")
#     username = st.sidebar.text_input("👤 New Username")
#     password = st.sidebar.text_input("🔒 New Password", type="password")
    
#     if st.sidebar.button("Register"):
#         try:
#             register_user(username, password)
#             st.success("✅ Registered successfully! Please log in.")
#         except Exception as e:
#             st.error(f"❌ Registration failed: {str(e)}")

# elif menu == "Learn":
#     st.title(f"👋 Welcome, {st.session_state['username']}!")

#     try:
#         st.image("static/images/banner.jpg", use_column_width=True)
#     except Exception:
#         st.warning("⚠️ Banner image not found. Continuing without it.")

#     prompt = st.text_area("💬 Ask me anything to learn!", key="learn_input")
    
#     if st.button("🚀 Submit"):
#         if prompt:
#             try:
#                 response = get_learning_response(prompt)
#                 st.session_state["chat_history"].append({"user": prompt, "ai": response})
#                 st.success("✅ Response received!")
#             except Exception as e:
#                 st.error(f"❌ Error with chatbot: {str(e)}")

#     if st.session_state["chat_history"]:
#         st.subheader("📜 Chat History")
#         for chat in st.session_state["chat_history"]:
#             st.markdown(f"**🧑 You**: {chat['user']}")
#             st.markdown(f"**🤖 AI**: {chat['ai']}")

# elif menu == "Exam":
#     st.title("📝 Take an Exam")
#     topic = st.text_input("📚 Enter a topic for the exam")
    
#     if st.button("🎯 Start Exam") and topic:
#         try:
#             questions = generate_exam(topic)
#             st.session_state["exam_questions"] = questions
#             st.session_state["exam_active"] = True
#             st.success("✅ Exam started! Answer the questions below.")
#         except Exception as e:
#             st.error(f"❌ Error generating exam: {str(e)}")

#     if st.session_state["exam_active"]:
#         st.subheader("📄 Questions")
#         st.write(st.session_state["exam_questions"])
#         answers = st.text_area("✏️ Enter your answers (one per line)", key="exam_input")
        
#         if st.button("📤 Submit Answers"):
#             try:
#                 marks, mistakes = evaluate_exam(st.session_state["exam_questions"], answers)
#                 store_result(st.session_state["username"], topic, marks, mistakes)
#                 st.success("✅ Exam submitted successfully!")
#                 st.write(f"🎓 **Your Score:** {marks}/5")
#                 st.write("🧠 **Mistakes & Feedback:**")
#                 st.markdown(mistakes)
#                 st.session_state["exam_active"] = False
#             except Exception as e:
#                 st.error(f"❌ Error evaluating exam: {str(e)}")

# elif menu == "Results":
#     st.title("📊 Your Results")

#     try:
#         results = get_user_results(st.session_state["username"])
#         if results:
#             for result in results:
#                 st.markdown(f"""
#                 #### 📌 Topic: {result['topic']}
#                 - 🏆 Score: **{result['marks']}/5**
#                 - 🗓️ Date: {result['date']}
#                 - ❗ Mistakes: {result['mistakes']}
#                 ---
#                 """)
#         else:
#             st.info("ℹ️ No results yet. Take an exam!")
#     except Exception as e:
#         st.error(f"❌ Error fetching results: {str(e)}")







# required code .........
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai
from utils.auth import login_user, register_user
from utils.chatbot import get_learning_response
from utils.exam import generate_exam, evaluate_exam
from utils.db import store_result, get_user_results
# from fpdf import FPDF
# import io


# Load custom CSS
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Helper to load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

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
    st.title("🤖 GenEDxAI")
    
    # Add space between title and content
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    
    # Display responsive welcome section with animation and text side by side
    # Smaller column for text, larger for animation
    col1, col2 = st.columns([2, 5])  # Adjusted ratio to make animation bigger than text
    
    with col1:
        st.markdown("""
        <div style="padding: 20px 0;">
            <h3>😊 Welcome to GenEDxAI!</h3>
            <p style="font-size: 18px; line-height: 1.5;">
                👋 A platform that uses AI to create educational content and evaluate your learning. 
                Whether you're a student or educator, we provide personalized support and quizzes 
                to help you succeed!
            </p>
            <p style="margin-top: 20px; font-size: 16px;">
                Please login using the sidebar to get started.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Lottie Animation - larger size
        lottie_login = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_1pxqjqps.json")
        if lottie_login:
            st_lottie(lottie_login, height=450, key="welcome_animation")
        else:
            st.warning("⚠️ Could not load animation")

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
    
    # Add space between title and content
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    
    # Add similar layout for register page with same proportions as login page
    col1, col2 = st.columns([2, 5])  # Match the login page ratio
    
    with col1:
        st.markdown("""
        <div style="padding: 20px 0;">
            <h3>Join our learning community!</h3>
            <p style="font-size: 16px; line-height: 1.5;">
                Create your account to access personalized learning content,
                take exams, and track your progress.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        lottie_login = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_1pxqjqps.json")
        if lottie_login:
            st_lottie(lottie_login, height=450, key="welcome_animation")
        else:
            st.warning("⚠️ Could not load animation")
        # Different animation for register page with larger size
        # lottie_register = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_kU51j8.json")
        # if lottie_register:
        #     st_lottie(lottie_register, height=450, key="register_animation")
        
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

    # Make banner responsive
    # try:
    #     st.image("static/images/banner.jpg", use_column_width=True)
    # except Exception:
    #     st.warning("⚠️ Banner image not found. Continuing without it.")

    # Make chat interface responsive
    col1, col2 = st.columns([4, 1])  # Main content and padding/space
    
    with col1:
        prompt = st.text_area("💬 Ask me anything to learn!", key="learn_input", height=100)
        
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
        for chat in reversed(st.session_state["chat_history"][-5:]):  # Show last 5 chats, newest first
            st.markdown("""
            <div style="border-left: 3px solid #2e7d32; padding-left: 10px; margin-bottom: 10px;">
                <p><strong>🧑 You:</strong> {user}</p>
            </div>
            <div style="border-left: 3px solid #1976d2; padding-left: 10px; margin-bottom: 20px;">
                <p><strong>🤖 AI:</strong> {ai}</p>
            </div>
            """.format(user=chat['user'], ai=chat['ai']), unsafe_allow_html=True)
            pdf_file = generate_pdf(st.session_state["chat_history"])
            st.sidebar.download_button("📄 Download PDF", pdf_file, "chat_history.pdf", "application/pdf")


            


elif menu == "Exam":
    st.title("📝 Take an Exam")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
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
        
        # Make questions stand out with styled container
        st.markdown(f"""
        <div style="background-color: ""; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
            {st.session_state["exam_questions"]}
        </div>
        """, unsafe_allow_html=True)
        
        answers = st.text_area("✏️ Enter your answers (one per line)", key="exam_input", height=200)
        
        if st.button("📤 Submit Answers"):
            try:
                marks, mistakes = evaluate_exam(st.session_state["exam_questions"], answers)
                store_result(st.session_state["username"], topic, marks, mistakes)
                
                # Results with better styling
                st.markdown(f"""
                <div style="background-color: ""; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <h3>Exam Results</h3>
                    <h4>🎓 Your Score: {marks}/5</h4>
                    <h5>🧠 Feedback:</h5>
                    <div>{mistakes}</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.session_state["exam_active"] = False
            except Exception as e:
                st.error(f"❌ Error evaluating exam: {str(e)}")

elif menu == "Results":
    st.title("📊 Your Results")

    try:
        results = get_user_results(st.session_state["username"])
        if results:
            # Creating a more responsive results display
            for i, result in enumerate(results):
                st.markdown(f"""
                <div style="background-color: {'' if i % 2 == 0 else ''}; 
                            padding: 15px; border-radius: 5px; margin-bottom: 10px; 
                            border-left: 4px solid {'#1976d2' if result['marks'] >= 3 else '#e57373'};">
                    <h4>📌 {result['topic']}</h4>
                    <div style="display: flex; flex-wrap: wrap; gap: 20px;">
                        <div>
                            <strong>🏆 Score:</strong> {result['marks']}/5
                        </div>
                        <div>
                            <strong>🗓️ Date:</strong> {result['date']}
                        </div>
                    </div>
                    <div style="margin-top: 10px;">
                        <strong>❗ Feedback:</strong><br>
                        {result['mistakes']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            # Empty state with animation
            col1, col2 = st.columns([2, 3])
            
            with col1:
                st.markdown("""
                <div style="padding: 20px 0;">
                    <h3>No results yet!</h3>
                    <p>Take an exam to see your results here.</p>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                lottie_empty = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ydo1amjm.json")
                if lottie_empty:
                    st_lottie(lottie_empty, height=200, key="empty_results")
                    
    except Exception as e:
        st.error(f"❌ Error fetching results: {str(e)}") 
        
        
        
st.markdown("""
<hr style="border: none; border-top: 2px solid #ccc; margin: 40px 0;" />

<div style="text-align: center; padding: 10px 0;">
    <p style="font-size: 16px; color: gray;">
        © 2025 <strong>GenEDxAI</strong>. All rights reserved.
    </p>
    <p style="font-size: 14px; color: gray;">
        Crafted with <span style="color: #e74c3c;">❤️</span> using <strong>Streamlit</strong>. Designed for Lifelong Learners.
    </p>
    <div style="margin-top: 10px;">
        <a href="https://www.linkedin.com" target="_blank" style="margin: 0 10px; text-decoration: none; color: #0e76a8;">LinkedIn</a>
        <a href="https://github.com" target="_blank" style="margin: 0 10px; text-decoration: none; color: #333;">GitHub</a>
        <a href="https://www.facebook.com/" style="margin: 0 10px; text-decoration: none; color: #d44638;">Facebook</a>
    </div>
</div>
""", unsafe_allow_html=True)
        
    