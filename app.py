import streamlit as st
import langchain_helper as lh



st.set_page_config(page_title="Resume Review Tool ")
st.header("ATS & Resume Review")
job_description = st.text_area("Job Description: ",key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

if submit1:
    if uploaded_file is not None:
        text = lh.input_pdf_to_text(uploaded_file)
        prompt1 = f"""
        Hey, act like a professional, skilled and experienced HR or a Recruiter of a multinational tech company
        with a deep understanding of the tech field, software engineering, data science, data analyst, software development and big data engineer roles.
        Your task is to evaluate and summarize the following resume based on the given job description. You must consider the 
        job market is very competitive and you should provide best assistance for improving the resume for the users. 
        I want you to 1) Give Pros and Cons of the Resume 2)Summarize the resume 
        3)Generate snippets of sections of the resume that could be improved. 

        resume: {text}

        description: {job_description}

        Response structure:
        1) Pros: 
        2) Cons:
        3) Summary:
        4) Referral impoved snippet of the sections of resume:

        """
        response = lh.get_llm_response(prompt1)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        text = lh.input_pdf_to_text(uploaded_file)
        prompt1 = f"""
        Hey, act like a professional, skilled and experienced Senior Engineer of a MultiNational Tech Company
        with a deep understanding of the tech field, software engineering, data science, data analyst, software development and big data engineer roles.
        Your task is to evaluate the following resume based on the given job description. You must consider the 
        job market is very competitive and you should provide best assistance for improving the resume for the users. 
        After the evaluation, I want you to advice the user based on resume and job description what are the skills user
        is currently lacking for the specified role and how can a user improve upon them thoroughly in minimal time.
        You could also comment on the project specified 
        in the resume, about if it fits the criteria based on job description and if you want them to improve the project please feel free to say about that

        resume: {text}

        description: {job_description}

        Response structure:
        1) List of Skills currently Lacking:
        2) How can You improve lacking skills point each one out and explain
        2) Project Advice(optional):
        """
        response = lh.get_llm_response(prompt1)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")



elif submit3:
    if uploaded_file is not None:
        text = lh.input_pdf_to_text(uploaded_file)
        prompt1 = f"""
        Hey, act like a professional, skilled and experienced ATS(Application Tracking System) 
        with a deep understanding of the tech field, software engineering, data science, data analyst, software development and big data engineer roles.
        Your task is to evaluate the following resume based on the given job description. You must consider the 
        job market is very competitive and you should provide best assistance for improving the resume for the users. 
        I want you to 1) Assign percentage matching based on job description, indicating how likely one's resume will get selected
        2) Identify the missing keywords and give a list of those, which would help user to add those keywords to their resume
        Maintain high accuracy for both tasks.

        resume: {text}

        description: {job_description}

        Response structure:
        1) Percentage Match based on JD:
        2) List Of Missing Keywords:
        """
        response = lh.get_llm_response(prompt1)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")
