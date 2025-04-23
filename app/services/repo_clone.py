import tempfile
import git


def clone_repo(repo_url):
    temp_dir = tempfile.mkdtemp(dir='/Users/krishi/Coding/Learning/Youtube/Langchain/Project/Generate Readme/app/tempfile')
    print("Temporary directory created at:", temp_dir)
    try:
        git.Repo.clone_from(repo_url,temp_dir)
        return temp_dir
    except Exception as e:
        return None