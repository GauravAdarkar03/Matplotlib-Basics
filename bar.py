import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
marks = [85, 90, 78]

plt.bar(subjects, marks, color='green')
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()