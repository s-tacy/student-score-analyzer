import matplotlib.pyplot as plt

def load_scores(filename):
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file]

def get_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

def calculate_summary(scores):
    average = sum(scores) / len(scores)
    pass_count = sum(1 for score in scores if score >= 60)
    fail_count = len(scores) - pass_count

    return average, pass_count, fail_count


scores = load_scores("scores.txt")
grades = [get_grade(scores) for scores in scores]
average, pass_count, fail_count = calculate_summary(scores)

print("Scores:" , scores)
print("Grades:" , grades)


print("\n-----Analysis Summary-----")
print("Average score:", average)
print("Pass count:", pass_count)
print("Fail count:", fail_count)

if average >= 70:
    print("Class performance: above average")
else:
    print("Class performance: below average")

print("Highest scores:", max(scores))
print("Lowest scores:", min(scores))

#first graph for score analysis
plt.bar(range(len(scores)), scores)

plt.title("Score Analysis")
plt.xlabel("Student Index")
plt.xticks(range(len(scores)), [f"S{i+1}" for i in range(len(scores))])
plt.ylabel("Score")

plt.show()

#second graph for grade distribution
grade_counts = {}
for grade in grades:
    grade_counts[grade] = grade_counts.get(grade, 0) + 1

plt.bar(grade_counts.keys(), grade_counts.values())
plt.title("Grade Analysis")
plt.xlabel("Grade")
plt.ylabel("Number of students")
plt.show()