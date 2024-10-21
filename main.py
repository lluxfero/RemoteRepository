from reader import read_text
from writer import write_text

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    text = read_text(input_file)
    write_text(output_file, text)
