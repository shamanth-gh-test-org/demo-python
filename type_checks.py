import os
import sys

def raise_issues(issues=[1,2,3]):
    pass

def greet_all(names: list[str]) -> None:
    for name in names:
        print('Hello ' + name)

if __name__ == "__main__":
    heights = [5.5, 6, 5.9]
    greet_all(heights)
