import os


def read_repo_files(repo_path):
    code_files = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(('.py', '.txt', '.md', '.json')):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        code_files.append(f"### {file}\n" + f.read())
                except:
                    pass
    return "\n\n".join(code_files)