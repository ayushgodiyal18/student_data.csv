import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("student_data.csv")

# Display first 5 rows
print("Student Dataset Preview:")
print(data.head())

# Calculate average marks
data["Average"] = (data["Math"] + data["Science"] + data["English"]) / 3

# Show average marks of students
print("\nAverage Marks:")
print(data[["Student_Name", "Average"]])

# Find top performing student
top_student = data.loc[data["Average"].idxmax()]
print("\nTop Performing Student:")
print(top_student["Student_Name"], "-", top_student["Average"])

# Plot subject-wise marks comparison
subjects = ["Math", "Science", "English"]
data[subjects].mean().plot(kind="bar")

plt.title("Average Marks by Subject")
plt.ylabel("Marks")
plt.xlabel("Subjects")
plt.show()
