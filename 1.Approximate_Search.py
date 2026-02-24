import difflib

def approximate_search():
    try:
        with open('1.words.txt', 'r') as f:
            word_list = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Error: 1.words.txt not found. Please create it first.")
        return

    print("Program started. Type 'exit' to stop.")
    while True:
        user_input = input("Input >> ").strip().lower()
        if user_input == 'exit':
            break

        suggestions = difflib.get_close_matches(user_input, word_list, n=3, cutoff=0.4)
        
        if suggestions:
            print(f"Output >> {', '.join(suggestions)}")
        else:
            print("Output >> No matches found.")

if __name__ == "__main__":
    approximate_search()