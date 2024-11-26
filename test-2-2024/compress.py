import os

from zipfile import ZipFile


def main() -> None:
    with ZipFile("solution.zip", "w") as file:
        for path, sub_directories, file_names in os.walk("src"):
            for file_name in file_names:
                if file_name.endswith(".py") and file_name != "__init__.py":
                    file.write(os.path.join(path, file_name), os.path.join(path, file_name))
                    print(os.path.join(path, file_name))


if __name__ == '__main__':
    main()
