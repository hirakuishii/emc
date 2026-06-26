import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str, default="name")

    args = parser.parse_args()

    print(f"name:{args.name}")
    
if __name__ == "__main__":
    main()