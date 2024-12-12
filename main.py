import sys
from filesystem import FyleSystem

def get_input():
    choice = input("\n$ ").strip()
    return choice.split(" ")

def get_args(input):
    input.pop(0)
    return " ".join(input)

def main():
    try:
        fs = FyleSystem()

        while True:
            input = get_input()
            action = input[0]
            args = get_args(input)

            if action == 'mkdir':
                fs.createDir(args)

    except KeyboardInterrupt:
        print("\nInterrupção detectada! Saindo do programa...")
        sys.exit(0)


if __name__ == '__main__':
    main()