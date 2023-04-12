import os
def read_template(path):
    """
    read_template function that takes in a path to text file and returns a stripped string of the file's contents.
    read_template should raise a FileNotFoundError if path is invalid.
    """
    try:
        with open(path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError as e:
        print(f"FileNotFoundError successfully handled:\n{e}")
        raise e
    
   



def parse_template(template):
    """
    parse_template function that takes in a template string and returns a string with language parts removed and a separate tuple of those language parts.
    """
    parts = []
    parsed_template = ''
    i = 0
    while i < len(template):
        if template[i] == '{':
            second_bracket = template.find('}', i)
           
            language_part = template[i + 1: second_bracket].strip()
            parts.append(language_part)
            parsed_template += '{}'
            i = second_bracket + 1
        else:
            parsed_template += template[i]
            i += 1

    return parsed_template, tuple(parts)

def merge(bare,parts):
   """
   merge function that takes in a “bare” template and a list of user entered language parts, 
   and returns a string with the language parts inserted into the template
   """
   return bare.format(*parts)
   

def run_madlib():
    print("Welcome to Madlib!")
    print("MadLibs is a phrasal template word game,It consists of one player prompting others for a list of words to substitute for blanks in a story before reading aloud")
    print("So please enter words to fill in the blanks")
    
    template_path = read_template("assets/madlib.txt")
    parsed_template, parts = parse_template(template_path)
    inputs = []
    for language_part in parts:
        input_prompt = f"Please enter a {language_part}: "
        user_input = input(input_prompt)
        inputs.append(user_input)

    completed_madlib = merge(parsed_template, inputs)
    print("\n" + completed_madlib)

    with open("assets/completed.txt", 'w') as file:
        file.write(completed_madlib)


run_madlib()

if __name__=="__main__":
  path="assets/dark_and_stormy_night_template.txt"
