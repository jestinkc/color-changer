import time

def countdown(n):
    print("Countdown begins!")
    for i in range(n, 0, -1):
        print(f"{i}... Just kidding!")
        time.sleep(1)
    print("Blast off into the useless void!")

if __name__ == "__main__":
    countdown(5)
