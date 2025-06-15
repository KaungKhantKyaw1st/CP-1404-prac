"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILE_PATH = "../../../CP-1404-prac/prac_04/subject_data.txt"  # Renamed constant for better clarity

def main():
    subject_details = load_subject_data()  # Renamed variables for clarity
    display_subject_data(subject_details)  # Renamed function for clarity

def load_subject_data():
    subjects = []  # Renamed variable for clarity
    with open(FILE_PATH, 'r') as file:  # Renamed variable and added 'r' for read mode clarity
        for line in file:
            clean_line = line.strip()  # Renamed to 'clean_line' for better readability
            details = clean_line.split(',')
            details[2] = int(details[2])  # Parsing number of students to int
            subjects.append(details)
    return subjects

def display_subject_data(subjects):
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students enrolled.")  # Altered print message slightly

main()



