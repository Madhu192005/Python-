from collections import Counter
import re

def count_word_occurrences(filename):
    try:
        # Open the file and read its content
        with open(filename, 'r') as file:
            content = file.read()
        
        # Normalize the content by converting it to lowercase
        content = content.lower()
        
        # Use regular expressions to find words (handle punctuation)
        words = re.findall(r'\b\w+\b', content)
        
        # Count the occurrences of each word
        word_counts = Counter(words)
        
        return word_counts
    
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except IOError:
        return f"Error: An IOError occurred while reading the file '{filename}'."

def main():
    filename = input("Enter the filename: ")
    word_counts = count_word_occurrences(filename)
    
    if isinstance(word_counts, dict):
        print("Word occurrences:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")
    else:
        print(word_counts)

if __name__ == "__main__":
    main()
