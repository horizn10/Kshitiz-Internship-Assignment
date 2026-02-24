import os

def solve_expressions(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' was not found in this folder.")
        return

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                original_line = line.strip()
                if not original_line:
                    continue
                clean_expr = original_line.replace('=', '').replace('^', '**')
                
                clean_expr = clean_expr.replace(')(', ')*(').replace('](', ']*(').replace('}(', '}*(')
                
                try:
                    result = eval(clean_expr)
                    outfile.write(f"{original_line}{result}\n")
                except Exception as e:
                    outfile.write(f"{original_line} Error in calculation: {e}\n")
                    
        print(f"Process complete! Results saved to '{output_file}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    solve_expressions('2.input.txt', '2.output.txt')