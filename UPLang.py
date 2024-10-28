import customtkinter as ctk
import threading

def runner():
    runBtn.configure(text="Running..")
    threading.Thread(target=run()).start()
    runBtn.configure(text="Run Code")


def lexer():
    code = codebox.get("1.0", "end")
    lines = code.strip().split('\n')
    tokens = [line.strip().split() for line in lines]
    return tokens

def interpreter(tokens):
    variables = {}

    for token_line in tokens:
        if not token_line:
            continue

        command = token_line[0].upper()

        if command == "INT":
            var_name = token_line[1]
            value = int(token_line[2])
            variables[var_name] = value

        elif command == "STR":
            var_name = token_line[1] # sets the variable name to the var name (second token)
            value = " ".join(token_line[2:])#[1:-1] # defines value as actual string no qoutes
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]  # Remove the surrounding quotes
            variables[var_name] = value # sets value of that var with that name in the var dictionary to value of actual string


        elif command == "PRINT":
            output = []
            for part in token_line[1:]:
                if part.startswith('"') and part.endswith('"'):
                    output.append(part[1:-1])
                elif part.startswith('"'):
                    literal_string = " ".join(token_line[token_line.index(part):])
                    output.append(literal_string[1:-1])
                    break
                else:
                    value = variables.get(part, "Undefined variable")
                    output.append(str(value))
            print(" ".join(output))



        elif command == "INPUT":
            var_name = token_line[1]
            prompt_text = " ".join(token_line[2:])[1:-1]  # Remove surrounding quotes
            variables[var_name] = input(prompt_text)

        else:
            print(f"Unknown command: {command}")

def run():
    tokens = lexer()
    interpreter(tokens)

window = ctk.CTk()
window.geometry("500x550")
window.title("UPLang Editor")
window.iconbitmap("UPlanglogo.ico")

title = ctk.CTkLabel(window, text="UPLang Code Editor", font=("Arial", 16))
codebox = ctk.CTkTextbox(window, width=350, height=400, font=('Consolas', 14))
sp0 = ctk.CTkLabel(window, text="  ")
runBtn = ctk.CTkButton(window, text="Run Code", command=runner)

title.pack()
codebox.pack()
sp0.pack()
runBtn.pack()

window.mainloop()


'''elif command == "PRINT":
    if token_line[1].startswith('"') and token_line[1].endswith('"'):
        print(token_line[1][1:-1])
    else:
        var_name = token_line[1]
        print(variables.get(var_name, "Undefined variable"))'''