import sys, msvcrt

def main(argv):
    array, content = [0], open(argv[1], "r").read()
    pointer, pos, start = 0, 0, []

    while len(content) > pos:
        if content[pos] == "<": pointer -= 1
        elif content[pos] == ">": pointer += 1
        elif content[pos] == "+": array[pointer] += 1
        elif content[pos] == "-": array[pointer] -= 1
        elif content[pos] == ".": print(chr(array[pointer]), end = "")
        elif content[pos] == ",": array[pointer] = ord(msvcrt.getch())
        elif content[pos] == "[": start.append(pos)
        elif content[pos] == "]":
            if array[pointer] > 0: pos = start[len(start) - 1] - 1
            else: start.pop(len(start) - 1)
        else: ...
        if pointer > len(array) - 1: array.append(0)
        if "--no-limit" not in argv and (array[pointer] > 255 or array[pointer] < 0):
            print(f"numbers must be between 0 and 255"); sys.exit(-1)
        if pointer < 0:
            print(f"pointer must point a positive number"); sys.exit(-1)
        pos += 1

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))