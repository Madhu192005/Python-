import re

def count_word_occurrences(filename):
    word_counts = {}
    
    try:
        # Open the file and read its content
        with open(filename, 'r') as file:
            for line in file:
                # Normalize the line to lowercase
                line = line.lower()
                # Use regular expressions to find words
                words = re.findall(r'\b\w+\b', line)
                
                # Count occurrences of each word
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except IOError:
        return f"Error: An IOError occurred while reading the file '{filename}'."
    
    return word_counts

def main():
    filename = input("Enter the filename: ")
    word_counts = count_word_occurrences(filename)
    
    if isinstance(word_counts, dict):
        print("Word occurrences:")
        for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"{word}: {count}")
    else:
        print(word_counts)

if __name__ == "__main__":
    main()
