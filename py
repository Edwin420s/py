# File Read & Write Challenge with Error Handling

def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file to read
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (for example, converting all text to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Successfully read from {input_filename} and wrote to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    
    except IOError:
        print(f"Error: There was an issue reading or writing the file.")

def get_filename_and_process():
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write to: ")
    
    # Call the function to read and write the file
    read_and_modify_file(input_filename, output_filename)

# Start the process
get_filename_and_process()
