import customtkinter as ctk

def lexer():
    filename = fileentry.get()
    if filename.startswith('"') and filename.endswith('"'):
        filename = filename[1:-1]
    f = open(filename,"r")
    code = f.read()
    lines = code.strip().split("\n")
    tokens = [line.strip().split() for line in lines]
    return tokens

def interpreter(tokens):
    variables = {}

    for token in tokens:
        if not token:
            continue
        command = token[0].upper()

        if command == "STR":
            var_name = token[1]
            if token[2].startswith('"') and token[2].endswith('"'):
                value = token[2][1:-1]
                variables[var_name] = value
            elif token[2].startswith('"'):
                value = " ".join(token[2:][1:-1])
                variables[var_name] = value
            else:
                print("Not a valid string")

        elif command == "INT":
            var_name = token[1]
            value = token[2]
            variables[var_name] = value

        elif command == "PRINT":
            printobj = token[1]
            if printobj.startswith('"') and printobj.endswith('"'):
                printobj = printobj[1:-1]
                print(printobj)

            elif printobj.startswith('"') and not printobj.endswith('"'):
                printobj = " ".join(token[1:])[1:-1]
                print(printobj)
            else:
                print(variables[token[1]])

        elif command == "INPUT":
            var_name = token[1]
            prompt_text = " ".join(token[2:])[1:-1]
            userinput = input(prompt_text)
            variables[var_name] = userinput
        else:
            print(f"Unkown command: " + command)

        
def runcode():
    tokens = lexer()
    interpreter(tokens)
                

window = ctk.CTk()
window.geometry("350x300")
window.title("UPfile Interpreter")

title = ctk.CTkLabel(window, text="UPfile (.up) Interpreter", font=("Arial", 18))
sp0 = ctk.CTkLabel(window, text="  ")
fileentry = ctk.CTkEntry(window, placeholder_text="Filename or path")
runBtn = ctk.CTkButton(window, text="Run Code", command=runcode)


title.pack()
sp0.pack()
fileentry.pack()
runBtn.pack()

window.mainloop()