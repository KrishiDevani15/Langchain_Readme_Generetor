import streamlit as st
from services.repo_clone import clone_repo
from services.read_repo_files import read_repo_files
from services.generate_readme import generate_readme
import shutil


# Create UI
st.set_page_config(page_title="GitHub README Generator", page_icon="📘")
st.title("📘 README Generator from GitHub Repo")

repo_url = st.text_input("Enter GitHub Repository URL (e.g., https://github.com/user/repo)")
generate_button = st.button("Generate README")


if generate_button and repo_url:
    with st.spinner("Cloning repository and analyzing code..."):
        repo_path = clone_repo(repo_url)
        st.write(repo_path)
        if repo_path:
            try:
                codebase_text = read_repo_files(repo_path)
                if codebase_text:
                    readme = generate_readme(codebase_text)
                    st.subheader("📝 Generated README.md")
                    st.code(readme, language="markdown")
                    st.download_button("📥 Download README.md", readme, file_name="README.md")
                else:
                    st.warning("No readable source files found in the repository.")
            finally:
                shutil.rmtree(repo_path)  # Clean up cloned repo