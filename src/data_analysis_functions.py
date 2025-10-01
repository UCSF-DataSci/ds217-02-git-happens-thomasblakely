#!/usr/bin/python3

def load_data(filename):
    """Generic loader that checks file extension"""
    # TODO - Complete Function
    if filename.endswith('.csv'):
        return load_csv(filename)
    else:
        print("ERROR, file not a '.csv'")
        return -1

def load_csv(filename):
    """Load CSV data (same technique as basic script)"""
    # TODO - Complete Function
    student_data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            student_data.append(line.strip().split(','))
    return student_data

def analyze_data(students):
    """Return dictionary with multiple statistics"""
    # TODO - Complete Function
    grades = [int(record[2]) for record in students]
    subject_count = {}
    for record in students:
        subject = record[3]
        if subject in subject_count:
            subject_count[subject] += 1
        else:
            subject_count[subject] = 1
    data_dictionary = {
        'total_students' : len(students),
        'max_grade' : max(grades),
        'min_grade' : min(grades),
        'avg_grade' : sum(grades) / len(students),
        'subject_counts' : subject_count
    }
    return(data_dictionary)

def analyze_grade_distribution(grades):
    """Count grades by letter grade ranges"""
    # TODO - Complete Function
    grade_distribution = {
        'A' : 0,
        'B' : 0,
        'C' : 0,
        'D' : 0,
        'F' : 0 
    }
    for grade in grades:
        grade = int(grade)
        if grade >= 90 and grade <= 100:
            grade_distribution['A'] += 1
        elif grade >= 80 and grade < 90:
            grade_distribution['B'] += 1
        elif grade >= 70 and grade < 80:
            grade_distribution['C'] += 1
        elif grade >= 60 and grade < 70:
            grade_distribution['D'] += 1
        else:
            grade_distribution['F'] += 1
    return grade_distribution

def save_results(results, filename):
    """Save detailed report"""
    # TODO - Complete Function
    report = f"""Outputting 'Data Analysis Functions' Formatted Report
    Number of Students: {results['total_students']}
    Max Grade: {results['max_grade']}
    Min Grade: {results['min_grade']}
    Avg Grade: {results['avg_grade']:.1f}
    """
    report +=    "Subject Count:\n"
    for subject, count in results['subject_counts'].items():
        report += f"        {subject}: {count}\n"
    report += '    Grade Distribution:\n'
    for grade, number in results['grade_distribution'].items():
        percent = number / results['total_students'] * 100
        report += f"        {grade}: {number} ({percent:.1f}%)\n"
    with open(filename, 'w') as file:
        file.write(report)
    
def main():
    """Orchestrate the analysis using all functions"""
    # TODO - Complete Function
    student_data = load_data('data/students.csv')
    data_dictionary = analyze_data(student_data)
    grades = [int(record[2]) for record in student_data]
    grade_distribution = analyze_grade_distribution(grades)
    data_dictionary['grade_distribution'] = grade_distribution
    save_results(data_dictionary, 'output/analysis_report.txt')

if __name__ == "__main__":
    main()