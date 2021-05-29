import sys

def prep(line):
    return line.lstrip(" ")

def transform(line):
    line = line.replace("integer(", "int(")
    line = line.replace("string(", "str(")
    line = line.replace("decimal(", "float(")
    line = line.replace("array(", "list(")
    line = line.replace("boolean(", "bool(")
    line = line.replace("length(", "len(")
    line = line.replace("minimum(", "min(")
    line = line.replace("maximum(", "max(")
    line = line.replace("true", "True")
    line = line.replace("false", "False")
    line = line.replace("null", "None")
    line = line.replace("++", " += 1")
    line = line.replace("--", " -= 1")
    line = line.replace("!", "not ")
    line = line.replace("none", "pass")
    line = line.replace("next", "continue")
    line = line.replace("stop", "break")
    return line

dev = False

opening = "program.txt" if dev else sys.argv[1]

content = None

with open(opening, "r") as f:
    content = [i.rstrip("\n") for i in f.readlines()]

file = open("outputfilefilefile.py", "w+")

declared_vars = []

for line in content:
    if prep(line).split(" ")[0] == "declare":
        for i in line:
            if i == " ":
                file.write("\t")
            else:
                break
        new = " ".join(prep(line).split(" ")[1:])
        new = transform(new)
        file.write(new + "\n")
        declared_vars.append(prep(line).split(" ")[1])
    elif prep(line).split(" ")[0] == "write":
        for i in line:
            if i == " ":
                file.write("\t")
            else:
                break
        new = "print(" + " ".join(prep(line).split(" ")[1:]) + ")"
        new = transform(new)
        file.write(new + "\n")
    elif prep(line).split(" ")[0] == "read":
        for i in line:
            if i == " ":
                file.write("\t")
            else:
                break
        new = prep(line).split(" ")[-1] + " = input(" + " ".join(prep(line).split(" ")[1:-1]) + ")"
        new = transform(new)
        file.write(new + "\n")
    elif prep(line).split(" ")[0] == "//":
        continue
    elif prep(line).split(" ")[0] in declared_vars:
        for i in line:
            if i == " ":
                file.write("\t")
            else:
                break
        new = prep(line)
        new = transform(new)
        if " push(" not in new and " pop(" not in new and " delete(" not in new and " split(" not in new and " fuse(" not in new and " index(" not in new and " rindex" not in new:
            file.write(new + "\n")
        elif " push(" in new:
            file.write(new.split(" ")[0] + ".append(" + new[new.index("push(") + len("push("): new.rindex(")")] + ")" + "\n")
        elif " pop(" in new:
            file.write(new.split(" ")[0] + ".pop(" + new[new.index("pop(") + len("pop("): new.rindex(")")] + ")" + "\n")
        elif " delete(" in new:
            file.write(new.split(" ")[0] + ".remove(" + new[new.index("delete(") + len("delete("): new.rindex(")")] + ")" + "\n")
        elif " split(" in new:
            file.write(new.split(" ")[0] + " = " + new.split(" ")[2] + ".split(" + new[new.index("split(") + len("split("): new.rindex(")")] + ")" + "\n")
        elif " fuse(" in new:
            file.write(new.split(" ")[0] + " = " + new[new.index("fuse(") + len("fuse("): new.rindex(")")] + ".join(" + new.split(" ")[2] + ")" + "\n")
        elif " index(" in new:
            file.write(new.split(" ")[0] + " = " + new.split(" ")[2] + ".index(" + new[new.index("index(") + len("index("): new.rindex(")")] + ")" + "\n")
        elif " rindex(" in new:
            file.write(new.split(" ")[0] + " = " + new.split(" ")[2] + ".rindex(" + new[new.index("index(") + len("index("): new.rindex(")")] + ")" + "\n")
    elif prep(line).split(" ")[0] == "declaref":
        new = prep(line)
        file.write("def " + new.split(" ")[1] + "(" + new[new.index("parameters(") + len("parameters("): new.rindex(")")] + ")" + ":\n")
    elif prep(line).split(" ")[0] == "if":
        for i in line:
            if i == " ":
                file.write("\t")
            else:
                break
        new = prep(line)
        new = transform(new)
        file.write("if " + new[new.index("condition(") + len("condition("): new.rindex(")")] + ":\n")
    elif prep(line).split(" ")[0] == "elseif":
        for i in line:
            if i == " ":
                file.write("\t")
            else:
                break
        new = prep(line)
        new = transform(new)
        file.write("elif " + new[new.index("condition(") + len("condition("): new.rindex(")")] + ":\n")
    elif prep(line).split(" ")[0] == "else":
        for i in line:
            if i == " ":
                file.write("\t")
            else:
                break
        file.write("else:\n")
    elif prep(line).split(" ")[0] == "while":
        for i in line:
            if i == " ":
                file.write("\t")
            else:
                break
        new = prep(line)
        new = transform(new)
        file.write("while " + new[new.index("condition(") + len("condition("): new.rindex(")")] + ":\n")
    elif prep(line).split(" ")[0] == "for":
        for i in line:
            if i == " ":
                file.write("\t")
            else:
                break
        new = prep(line)
        new = transform(new)
        if "through(" in new:
            file.write("for " + new.split(" ")[1] + " in " + new[new.index("through(") + len("through("): new.rindex(")")] + ":\n")
        elif "from(" in new:
            file.write("for " + new.split(" ")[1] + " in range(" + new[new.index("from(") + len("from("): new.rindex(")")] + "):\n")
        elif "to(" in new:
            file.write("for " + new.split(" ")[1] + " in range(" + new[new.index("to(") + len("to("): new.rindex(")")] + ", -1):\n")
    else:
        for i in line:
            if i == " ":
                file.write("\t")
            else:
                break
        new = prep(line)
        new = transform(line)
        file.write(new + "\n")

file.close()