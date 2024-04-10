from itertools import islice

def compare_and_print_diff(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as output:
        # Skip the first 5 lines in each file
        f1 = islice(f1, 5, None)
        f2 = islice(f2, 5, None)

        # Process the remaining lines
        for line1, line2 in zip(f1, f2):
            try:
                # Split each line into columns
                parts1 = line1.strip().split(',')
                parts2 = line2.strip().split(',')

                # Extract values for comparison
                n1 = int(parts1[1])
                n2 = int(parts2[1])

                # Compare and calculate the difference
                if n1 != n2:
                    diff = n2 - n1
                    output.write(f"{parts1[0]}, {diff}, {parts1[2]}\n")

            except (IndexError):
                # Handle IndexError (skip the line)
                print(f"Skipping line: {line1.strip()} or {line2.strip()}")


if __name__ == "__main__":
    compare_and_print_diff('drops1.txt', 'drops2.txt', 'difference.txt')
