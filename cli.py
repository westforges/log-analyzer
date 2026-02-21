import sys
from analyzer import analyze_log

def main():
    if len(sys.argv) != 2:
        print("Usage: python cli.py <logfile>")
        return

    results = analyze_log(sys.argv[1])

    print("\nLog Summary:")
    for level, count in results.items():
        print(f"{level}: {count}")

if __name__ == "__main__":
    main()
