import json
import os
import sys
import warnings
import re

try:
    import requests
except ModuleNotFoundError:
    import subprocess

    print("Downloading package requests")
    process = subprocess.run("python -m pip install requests".split())
    import requests


def main() -> None:
    warnings.filterwarnings("ignore")
    session_id = input("Enter your sessionId: ")

    try:
        response = requests.get(
            url=f"https://codexe.inf.unideb.hu/exam-new/api/exam/{session_id}/init",
            verify=False
        )
        payload = json.loads(response.content)
        for entry in payload:
            entry["name"] = os.sep.join(re.split("\\|/", entry["name"]))
            if entry["name"] != "submit.py":
                os.makedirs(os.path.dirname(entry["name"]), exist_ok=True)
            with open(entry["name"], "w", encoding="utf-8") as file:
                file.write(entry["content"])
                print("*", f"{entry['name']} was created")


    except Exception as e:
        print(file=sys.stderr)
        print("Could not initialize the project.", file=sys.stderr)
        print(e, file=sys.stderr)
        raise e


if __name__ == '__main__':
    main()
