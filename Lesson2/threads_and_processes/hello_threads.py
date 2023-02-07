import threading
import time


def main():
    threads = [
        threading.Thread(target=greeter, args=('Vlad', 3), daemon=True),
        threading.Thread(target=greeter, args=('Misha', 2), daemon=True),
        threading.Thread(target=greeter, args=('Alex', 4), daemon=True),
    ]
    [thread.start() for thread in threads]
    print('Hello from main')
    [thread.join() for thread in threads]
    print('Done!')


def greeter(name: str, times: int):
    for _ in range(0, times):
        print(f'Hello {name}')
        time.sleep(1)


if __name__ == '__main__':
    main()
