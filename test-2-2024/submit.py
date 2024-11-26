import json
import os
import subprocess
import sys
import warnings
from builtins import input

try:
    import requests
except ModuleNotFoundError:
    print("Downloading package requests")
    process = subprocess.run("python -m pip install requests".split())
    import requests


def main() -> None:
    warnings.filterwarnings("ignore")

    payload = []
    for path, sub_directories, file_names in os.walk("src"):
        for file_name in file_names:
            if file_name.endswith(".py") and file_name != "__init__.py":
                with open(os.path.join(path, file_name), encoding="utf-8") as file:
                    payload.append({
                        "name": os.path.join(path, file_name),
                        "content": file.read()
                    })

    print("The following files will be uploaded:")
    print(*[f"* {entry['name']}" for entry in payload], sep="\n")

    session_id = "88e0078a-a3a0-4577-8d74-9e6991c07ac5"
    try:
        response = requests.post(
            f"https://codexe.inf.unideb.hu/exam-new/api/exam/{session_id}/file",
            json.dumps(payload),
            headers={
                "Content-Type": "application/json"
            },
            verify=False
        )
        payload = json.loads(response.content)

        print()
        print("Successfully uploaded the files on behalf of the following student:")
        print("* ID:", payload["studentId"])
        print("* Neptun:", payload["studentNeptun"])
        print("* Name:", payload["studentName"])
        print("* IP:", payload["studentIp"])
        print("* token:", payload["sessionId"])

    except Exception as e:
        print(file=sys.stderr)
        print("Could not upload the solutions. Check the availability of the exam.", file=sys.stderr)
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
