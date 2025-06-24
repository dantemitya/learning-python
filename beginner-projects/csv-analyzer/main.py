# CSV DATA ANALAYZER
import utils

def get_avgs(data):
    """ get the averages of all exam scores for each student and return a dict """
    student_scores = {}
    for row in data:
        student_scores[row['Student ID']] = [float(row['Exam 1 Score']), float(row['Exam 2 Score']), float(row['Exam 3 Score'])]
    for student_id in student_scores:
        scores = student_scores[student_id]
        student_scores[student_id] = round((sum(scores) / len(scores)), 1)
    return student_scores

def main():
    filename = 'data.csv'
    headers, data = utils.get_csv(filename)
    utils.show_csv(headers, data)
    utils.hyphens()

    # get column statistics for exam 1 scores
    exam_1_scores = utils.get_column_data('Student ID', 'Exam 1 Score', data)
    print("Exam 1 Statistics")
    utils.get_max(exam_1_scores)
    utils.get_min(exam_1_scores)
    utils.get_avg(exam_1_scores)
    print()

    # get column statistics for exam 2 scores
    exam_2_scores = utils.get_column_data('Student ID', 'Exam 2 Score', data)
    print("Exam 2 Statistics")
    utils.get_max(exam_2_scores)
    utils.get_min(exam_2_scores)
    utils.get_avg(exam_2_scores)
    print()

    # get column statistics for exam 3 scores
    exam_3_scores = utils.get_column_data('Student ID', 'Exam 3 Score', data)
    print("Exam 3 Statistics")
    utils.get_max(exam_3_scores)
    utils.get_min(exam_3_scores)
    utils.get_avg(exam_3_scores)

    # get avgs for all students
    utils.hyphens()
    average_scores = get_avgs(data)
    print("Average scores")
    print("Student ID\tAverage Score")
    for key, value in average_scores.items():
        print(f"{key}\t\t{value}")
    print()

    # get best performing student
    print(f"Best perfoming student - {max(average_scores, key=average_scores.get)} ({max(average_scores.values())})")

    # get worst perfoming student
    print(f"Worst perfoming student - {min(average_scores, key=average_scores.get)} ({min(average_scores.values())})")

if __name__ == '__main__':
    main()
