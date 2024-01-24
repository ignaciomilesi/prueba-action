import random

def save_random_number() -> None:
    with open("report.txt", "w") as report_file:
        report_file.write("# El numero random es "+ str(random.randint(0,100)))
    print("listo")


if __name__ == "__main__":
    save_random_number()