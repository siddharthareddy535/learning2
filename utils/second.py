import os
import subprocess
from datetime import datetime
import shutil
import argparse



def git_push(folder_path,dummy_message,tempBranchName):
    try:
        subprocess.run(["git", "add", folder_path],check=True)
        subprocess.run(['git', 'commit', '-m', dummy_message], check=True)
        subprocess.run(['git', 'push', 'origin', tempBranchName], check=True) 

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")



def raisePullRequest(actualBranchName, tempBranchName, title, body):
    """
    Raises a pull request from tempBranchName to actualBranchName with custom title and body.
    """
    try:
        subprocess.run([
            "gh", "pr", "create",
            "--base", actualBranchName,
            "--head", tempBranchName,
            
            "--title", title,
            "--body", body
        ], check=True)
        print("Pull request created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")



def create_new_branch_if_not_exists(actualBranchName, tempBranchName):
    """
    Creates a new branch from an existing branch only if the new branch doesn't already exist.
    Ensures the actualBranchName is available and handles unclean states.
    """
    try:
        # Ensure the repository is up to date
        subprocess.run(["git", "fetch", "--all"], check=True)

        # Check if the `actualBranchName` exists locally or remotely
        result = subprocess.run(
            ["git", "rev-parse", "--verify", actualBranchName],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print(f"Branch '{actualBranchName}' not found locally. Checking remote...")
            # Attempt to fetch the branch from the remote
            fetch_result = subprocess.run(
                ["git", "checkout", "--track", f"origin/{actualBranchName}"],
                check=False
            )
            if fetch_result.returncode != 0:
                print(f"Error: Branch '{actualBranchName}' does not exist locally or remotely.")
                return

        # Check if the `tempBranchName` already exists
        result = subprocess.run(
            ["git", "rev-parse", "--verify", tempBranchName],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"Branch '{tempBranchName}' already exists. Switching to it.")
            subprocess.run(["git", "checkout", tempBranchName], check=True)
        else:
            # Create and switch to the new branch
            subprocess.run(["git", "checkout", actualBranchName], check=True)
            subprocess.run(["git", "checkout", "-b", tempBranchName], check=True)
            print(f"New branch '{tempBranchName}' created successfully from '{actualBranchName}'.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def get_new_files(init_dir,status_dir):
    files_in_init = {file for file in os.listdir(init_dir) if file.endswith(".py")}
    files_in_status = {file for file in os.listdir(status_dir) if file.endswith(".py")}

    files_to_add_in_status = files_in_init - files_in_status

    for file in files_to_add_in_status:
        source = os.path.join(init_dir, file)
        destination = os.path.join(status_dir, file)
        shutil.copy(source, destination)


def get_version_no_from_logs():
    return "v8"




def files_improvemnets(output_dir,status_dir,project_name,commit_message,tempBranchName):
    for subdir in os.listdir(status_dir):
            new_file_path = os.path.join(output_dir, f'{subdir}.py')
            status_file_path = os.path.join(status_dir, f"{subdir}.py")

            if os.path.exists(new_file_path):
                with open(new_file_path, 'r') as new_file:
                    new_code = new_file.read()
                with open(status_file_path, 'w') as py_file:
                    py_file.write(new_code)
    git_push(f'projects/{project_name}/status/',commit_message,tempBranchName)

def files_need_to_be_improved(dist_dir,status_dir,project_name,commit_message,tempBranchName):
    for subdir in os.listdir(status_dir):
            fix_file_path = os.path.join(dist_dir, f'{subdir}.py')
            status_file_path = os.path.join(status_dir, f"{subdir}.py")

            if os.path.exists(fix_file_path):
                with open(fix_file_path, 'r') as new_file:
                    new_code = new_file.read()
                with open(status_file_path, 'w') as py_file:
                    py_file.write(new_code)
    git_push(f'projects/{project_name}/status/',commit_message,tempBranchName)

def get_back_to_old(init_dir,status_dir,project_name,commit_message,tempBranchName):
    for subdir in os.listdir(status_dir):
            status_file_path = os.path.join(status_dir, f"{subdir}.py")
            init_file_path = os.path.join(init_dir, f"{subdir}.py")
            

            if os.path.exists(init_file_path):
                with open(init_file_path, 'r') as new_file:
                    new_code = new_file.read()
                with open(status_file_path, 'w') as py_file:
                    py_file.write(new_code)
    git_push(f'projects/{project_name}/status/',commit_message,tempBranchName)
    



def push_the_files(init_dir,dist_dir,output_dir,status_dir,project_name,tempBranchName):
    get_new_files(init_dir,status_dir)
    version_no= get_version_no_from_logs()
    files_improvemnets(output_dir,status_dir,project_name,f'{version_no}_Improvements_{datetime.now()}',tempBranchName)
    files_need_to_be_improved(dist_dir,status_dir,project_name,f'{version_no}_Enhancements_{datetime.now()}',tempBranchName)
    get_back_to_old(init_dir,status_dir,project_name,f'{version_no}_back_to_old_{datetime.now()}',tempBranchName)

    print("Process completed.")


def main():
    parser = argparse.ArgumentParser(description="Extract project name from file path.")
    parser.add_argument("--file", type=str, required=True, help="The file path containing the project name")
    args = parser.parse_args()
    file_path = args.file
    path_parts = os.path.normpath(file_path).split(os.sep)
    try:
        projects_index = path_parts.index("projects")
        project_name = path_parts[projects_index + 1]
        print(f"Project Name: {project_name}")
        init_dir = f'projects/{project_name}/init/'
        dist_dir=f'projects/{project_name}/dist/'
        output_dir = f'projects/{project_name}/output/'
        status_dir = f'projects/{project_name}/status/'
        tempBranchName = 'main'
        push_the_files(init_dir,dist_dir,output_dir,status_dir,project_name,tempBranchName)

    except ValueError:
        print("Error: 'projects' folder not found in the file path.")
    except IndexError:
        print("Error: Project name could not be determined from the file path.")


main()



