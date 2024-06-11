# Import necessary libraries
import pandas as pd
import os

# Define ClassOne with a process method
class ClassOne:
    def process(self):
        # Print a message when the process method is called
        print("Processing in ClassOne")

# Define ClassTwo with a process method
class ClassTwo:
    def process(self):
        # Print a message when the process method is called
        print("Processing in ClassTwo")

# Define ClassThree with a process method
class ClassThree:
    def process(self):
        # Print a message when the process method is called
        print("Processing in ClassThree")

# Define ClassFour with a process method
class ClassFour:
    def process(self):
        # Print a message when the process method is called
        print("Processing in ClassFour")

# Define ClassFive with a process method
class ClassFive:
    def process(self, output_folder):
        # Print a message when the process method is called
        print("Processing in ClassFive and generating Excel output")
        
        # Create a DataFrame for demonstration purposes
        df = pd.DataFrame({
            'Column1': [1, 2, 3],
            'Column2': ['A', 'B', 'C']
        })
        
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)
        
        # Define the output path
        output_path = os.path.join(output_folder, 'output.xlsx')
        
        # Save the DataFrame to an Excel file at the output path
        df.to_excel(output_path, index=False)
        
        # Print the location of the saved Excel file
        print(f"Output Excel saved to: {output_path}")# Import necessary libraries

# Define the MasterClass
class MasterClass:
    # Initialize the MasterClass with input_variable, output_folder, and instances of ClassOne to ClassFive
    def __init__(self, input_variable, output_folder):
        self.input_variable = input_variable
        self.output_folder = output_folder
        self.class_one = ClassOne()
        self.class_two = ClassTwo()
        self.class_three = ClassThree()
        self.class_four = ClassFour()
        self.class_five = ClassFive()

    # Define the run method to execute the process method of each class
    def run(self):
        print(f"Running MasterClass with input: {self.input_variable}")
        self.class_one.process()
        self.class_two.process()
        self.class_three.process()
        self.class_four.process()
        self.class_five.process(self.output_folder)

# Define a function to run the MasterClass for each subdirectory in a main directory
def run_for_each_folder(main_folder, output_base_folder):
    # Get the list of subdirectories
    subdirectories = [d for d in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, d))]

    # Loop through each subdirectory
    for subdir in subdirectories:
        # Create an input variable based on the folder name or some other logic
        input_variable = subdir
        # Define the output folder for each subdirectory
        output_folder = os.path.join(output_base_folder, subdir, 'output')
        # Instantiate and run the master class
        master_instance = MasterClass(input_variable, output_folder)
        master_instance.run()
        print("completed processing for", subdir)

# Example usage
# Define the main data folder and output base folder
# main_data_folder = 'path/to/main/data/folder'
# output_base_folder = 'path/to/output/base/folder'

main_data_folder = 'data'
output_base_folder = 'output'



# Run the function for each subdirectory in the main data folder
run_for_each_folder(main_data_folder, output_base_folder)