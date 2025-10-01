#!/usr/bin/python3

def load_students(filename):
    """Read CSV and return list of student data"""
    # TODO - Complete Function
    student_data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            student_data.append(line.strip().split(','))
    return student_data

def calculate_average_grade(students):
    """Calculate and return average"""
    # TODO - Complete Function
    average = []
    for record in students:
        average.append(int(record[2]))
    return sum(average) / len(average)

def count_math_students(students):
    """Count students in Math"""
    # TODO - Complete Function
    n_math = 0
    for record in students:
        if record[3] == "Math":
            n_math += 1
    return n_math

def generate_report():
    """Create formatted report string"""
    # TODO - Complete Function
    student_data = load_students('data/students.csv')
    average_grade = calculate_average_grade(student_data)
    math_students = count_math_students(student_data)
    report = f"""Outputting data_analysis.py Formatted Report
    Number of Students: {len(student_data)}
    Average Grade: {average_grade:.1f}
    Number of Math Students: {math_students}
    """
    return report

def save_report(report, filename): 
    """Write report to file"""
    # TODO - Complete Function
    with open(filename, 'w') as file:
        file.write(report)

def main():
    """Orchestrate the analysis"""
    # TODO - Complete Function
    report = generate_report()
    save_report(report, 'output/analysis_report.txt')

if __name__ == "__main__":
    main()