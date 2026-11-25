import os

PURCHASE = "I bought a standing desk and now I just stand there,"
PAYOFF = "procrastinating at a higher altitude."

PURCHASE = "I bought a standing desk and now I just stand there,"
PAYOFF = "procrastinating at a higher altitude."
LINE = " ".join([PURCHASE, PAYOFF])

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    target = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(target, "w", encoding="utf-8") as out:
        out.write(LINE)
        out.write("\n")


if __name__ == "__main__":
    main()
