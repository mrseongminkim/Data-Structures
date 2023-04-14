from collections import deque
from queue import Queue
from typing import TypeAlias

Stack: TypeAlias = list

def reverse_via_queue(D: deque, Q: Queue) -> None:
    n = len(D)
    for i in range(n):
        Q.put(D.pop())
    for i in range(n):
        D.append(Q.get())


def reverse_via_stack(D: deque, S: Stack) -> None:
    n = len(D)
    for i in range(n):
        S.append(D.popleft())
    for i in range(n):
        D.append(S.pop())


def main():
    D: deque = deque([1, 2, 3, 4, 5, 6, 7, 8])
    Q: Queue = Queue()
    S: Stack = Stack()
    reverse_via_queue(D, Q)
    #reverse_via_stack(D, S)

if __name__ == "__main__":
    main()
