# 🤖 AI Placement Preparation Assistant

**Prepare Smarter. Practice Better. Crack Your Interviews with AI.**

An AI-powered placement preparation application that helps candidates prepare for technical interviews through role-specific questions, detailed model answers, beginner-friendly explanations, practical examples, and challenging follow-up questions.

Built using **Python, LangChain, OpenRouter, Pydantic, and Streamlit**, this application generates structured and personalized interview preparation material based on the candidate's selected job role, experience level, and difficulty.

---

## ✨ Features

- **Role-Based Preparation:** Generate questions for Python Developer, Java Developer, AI Engineer, Machine Learning Engineer, Data Analyst, Data Scientist, GenAI Engineer, and Backend Developer roles.
- **Experience-Level Customization:** Tailor questions for freshers and candidates with different levels of experience.
- **Adjustable Difficulty:** Choose Easy, Medium, or Hard interview questions.
- **Custom Question Count:** Generate between 3 and 15 questions per session.
- **Interview-Oriented Questions:** Focus on practical, scenario-based, coding, debugging, conceptual, and problem-solving questions.
- **Detailed Model Answers:** Get technically accurate answers with reasoning and implementation details.
- **Beginner-Friendly Explanations:** Understand complex concepts through simple explanations and relatable examples.
- **Practical Examples:** Explore code snippets and real-world applications.
- **Important Keywords:** Identify technical terms worth remembering during interviews.
- **Follow-Up Questions:** Practice deeper questions that interviewers may ask.
- **Structured AI Responses:** Use Pydantic to validate and organize generated output.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM orchestration and chain creation |
| OpenRouter | Access to AI language models |
| Streamlit | Interactive web application |
| Pydantic | Structured output and data validation |
| python-dotenv | Secure environment variable management |

---

## 🏗️ Project Architecture

The application follows a simple LangChain-based workflow:

```text
          User
           |
           v
    Streamlit Interface
           |
           v
    Interview Configuration
    - Job Role
    - Experience Level
    - Difficulty
    - Number of Questions
           |
           v
      Prompt Template
        (prompts.py)
           |
           v
      OpenRouter LLM
       (generator.py)
           |
           v
     Pydantic Output Parser
           |
           v
    Structured Interview Data
        (schemas.py)
           |
           v
    Display Results in Streamlit
           |
           v
    Model Answers + Explanations
    Practical Examples + Keywords
         + Follow-up Questions
```

The application uses LangChain Expression Language (LCEL) to connect the prompt, language model, and output parser:

```python
chain = interview_prompt | llm | parser
```

---

## 📂 Project Structure

```text
AI-Placement-Preparation-Assistant/
│
├── app.py              # Streamlit application interface
├── generator.py        # LLM initialization and chain execution
├── prompts.py          # Interview prompt and output parser
├── schemas.py          # Pydantic response schemas
├── test.py             # OpenRouter API connection test
│
├── requirements.txt    # Project dependencies
├── .env                # API key and model configuration
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Placement-Preparation-Assistant.git
```

### 2. Navigate to the project directory

```bash
cd AI-Placement-Preparation-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root directory:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
MODEL_NAME=openai/gpt-4o-mini
```

Replace `your_openrouter_api_key` with your own OpenRouter API key.

The application uses `openai/gpt-4o-mini` as the default model if `MODEL_NAME` is not specified.

### 7. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🚀 How to Use

1. Launch the application.
2. Select your desired job role from the sidebar.
3. Choose your experience level.
4. Select the interview difficulty.
5. Set the number of questions you want to practice.
6. Click **Generate Interview Questions**.
7. Expand each question to explore:
   - Interview question
   - Question type and difficulty
   - Detailed model answer
   - Simple explanation
   - Practical example
   - Important keywords
   - Interviewer's follow-up question

---

## 🧠 Structured Output with Pydantic

The project uses Pydantic models to ensure that generated interview responses follow a consistent structure.

Each interview question contains:

- `question`
- `question_type`
- `difficulty`
- `model_answer`
- `explanation`
- `practical_example`
- `keywords`
- `follow_up`

The complete response also includes the selected job role, experience level, and generated questions.

This structured approach makes AI responses easier to validate, process, and display in the application.

---

## 🔐 Security

- Store API credentials in the `.env` file.
- Never hardcode API keys in Python source files.
- Add `.env` and virtual environment folders to `.gitignore`.
- Never upload private API credentials to GitHub.

Example `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
```

---

## 🔮 Future Enhancements

Potential improvements for future versions:

- Resume-based interview question generation.
- Mock interview mode with interactive AI conversations.
- Coding challenges with automated evaluation.
- Interview performance tracking and feedback.
- Question history and personalized practice sessions.
- Export interview questions and answers as PDF.
- Voice-based interview practice.

---

## 🎯 Project Objective

The main objective of this project is to make technical interview preparation more personalized, practical, and accessible.

Instead of relying only on generic textbook questions, the application focuses on realistic interview scenarios and helps candidates understand not just **what to answer, but why and how**.

--