# Resume Review Tool 📄🔍

A web-based application to review resumes, compare them with job descriptions, and provide insightful feedback using HuggingFace models. This tool empowers job seekers by summarizing their resumes, analyzing pros and cons, suggesting skill improvements, and generating a match percentage with the desired job role.

---

## Features ✨
- **Summarize Your Resume**: Provides a concise overview of your resume and highlights its strengths and weaknesses.
- **Personalized Skill Advice**: Identifies skills missing for the job role and offers actionable suggestions for improvement.
- **Percentage Match**: Calculates how closely your resume matches the job description and suggests missing keywords.
- **Streamlined Interface**: User-friendly design powered by Streamlit.

---

## How It Works 🛠️

1. **Upload Your Resume**: Submit a PDF version of your resume.
2. **Enter Job Description**: Provide the job description of the role you're applying for.
3. **Choose an Analysis**:
    - **Summarize Resume**: Get a detailed evaluation and suggested improvements.
    - **Improve Skills**: Receive tailored advice on skills to focus on and project feedback.
    - **Percentage Match**: Calculate ATS compatibility and find missing keywords.

---

## Technologies Used 💻
- **HuggingFace Models**: Leverages `mistralai/Mistral-7B-Instruct-v0.2` for natural language understanding.
- **LangChain**: Provides seamless LLM integration and prompt engineering.
- **Streamlit**: For creating the interactive and intuitive user interface.
- **PyPDF2**: To extract text from uploaded PDF resumes.
- **dotenv**: To securely manage environment variables.

---

## Installation 🚀

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/resume-review-tool.git
   cd resume-review-tool
   ```

2. **Set Up Environment Variables**:
   - Create a `.env` file and add your HuggingFace API token:
     ```
     HF_TOKEN=your_huggingface_token
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **Access the Tool**:
   Open `http://localhost:8501` in your browser.

---

## Usage 💼

1. **Upload Resume**: Use the file uploader to submit your resume (PDF format only).
2. **Input Job Description**: Paste the job description in the provided text area.
3. **Choose an Action**:
    - Click `Tell Me About the Resume` for a summary and evaluation.
    - Click `How Can I Improve My Skills` for actionable feedback.
    - Click `Percentage Match` to see how well your resume aligns with the job description.

---

## Screenshots 📸

Here’s a glimpse of how the application looks and works:

! [](https://imgur.com/a/WHcP11k)

---

## Example Prompts Used 📝

### Summarize Resume
```plaintext
Act as a professional HR specialist. Evaluate and summarize the resume based on the job description. Provide:
1. Pros
2. Cons
3. Summary
4. Suggested improved sections of the resume
```

### Skill Improvement
```plaintext
Analyze the resume and job description. List skills the user lacks and explain how to improve them. Optionally comment on the relevance of projects mentioned.
```

### Percentage Match
```plaintext
Act as an ATS system. Evaluate the resume against the job description:
1. Provide a percentage match.
2. List missing keywords for better alignment.
```

---

## Contribution Guidelines 🤝
We welcome contributions to enhance this tool! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Submit a pull request.

---

## Acknowledgements 🙌
- [HuggingFace](https://huggingface.co/) for providing state-of-the-art language models.
- [LangChain](https://python.langchain.com/) for prompt engineering capabilities.
- The open-source community for fostering innovation.

---

Start tailoring your resume today with **Resume Review Tool**! 🎯
