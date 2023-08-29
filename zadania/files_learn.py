import datetime

PATH = "../files/{}"
input_file = PATH.format("file1.txt")
output_file = PATH.format("output.txt")
log_path = PATH.format("log.txt")

def add_to_log(text):
    with open(log_path, "a") as f:
        f.write(text)


with open(input_file, "r") as f:
    with open(output_file, "w") as f_output:
        # print(f.read())
        # f.write("textdsda")
        # content = f.read()
        # content = content.replace("s", "").replace("g", "")
        # print(content)
        add_to_log("\n\nStart processing files\n")
        for line in f.readlines():
            print(f"to jest linia  {line}")
            add_to_log(f"czas {datetime.datetime.now().isoformat()}: {line}")
            try:
                number = float(line)
            except Exception:
                ...
            else:
                f_output.write(f'{number*2=}\n')
