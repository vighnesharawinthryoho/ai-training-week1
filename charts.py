import matplotlib.pyplot as plt


def main():
    weeks = ["W1", "W2", "W3"]
    scores = [80, 88, 95]

    plt.plot(weeks, scores, marker="o")
    plt.title("Week 1 Progress")
    plt.xlabel("Week")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.savefig("progress.png")


if __name__ == "__main__":
    main()