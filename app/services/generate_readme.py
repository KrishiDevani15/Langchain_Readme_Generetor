from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()
def generate_readme(codebase_text):
    llm = ChatOpenAI(model='gpt-4o')  # Requires OPENAI_API_KEY in environment
    prompt_template = PromptTemplate(
        input_variables=["codebase"],
        template="""
You are an expert developer. Based on the following codebase, generate a detailed and professional README.md file.
also use emoji to make attractive
Make sure to include:
- Project title
- Description
- Features
- Installation instructions
- Usage
- Example (if possible)
- License (if detected)

Codebase:
{codebase}

README:
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt_template)
    return chain.run(codebase=codebase_text)