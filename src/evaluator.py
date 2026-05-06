import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

load_dotenv()

def evaluate_candidate(resume_text, job_description):
    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    # Define how we want the data back
    schemas = [
        ResponseSchema(name="score", description="Fit score from 0-100"),
        ResponseSchema(name="fit_summary", description="Summary of candidate fit"),
        ResponseSchema(name="missing_skills", description="List of missing requirements")
    ]
    parser = StructuredOutputParser.from_response_schemas(schemas)
    
    prompt = ChatPromptTemplate.from_template(
        "Analyze the following resume against the job description.\n"
        "Job: {jd}\nResume: {resume}\n{format_instructions}"
    )

    messages = prompt.format_messages(
        jd=job_description,
        resume=resume_text,
        format_instructions=parser.get_format_instructions()
    )
    
    response = llm.invoke(messages)
    return parser.parse(response.content)