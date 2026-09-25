# File: list_data.py

# Import toàn bộ dữ liệu và hàm từ file input_data.py
import input_data

def list_courses():
    """List all courses"""
    print("\n--- List of Courses ---")
    # Lấy danh sách courses từ file input_data
    for c in input_data.courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def list_students():
    """List all students"""
    print("\n--- List of Students ---")
    # Lấy danh sách students từ file input_data
    for s in input_data.students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_student_marks():
    """Show student marks for a given course"""
    if not input_data.marks:
        print("\nNo marks have been inputted yet.")
        return
        
    list_courses()
    course_id = input("\nSelect a course ID to view marks: ")
    
    if course_id not in input_data.marks:
        print("No marks available for this course.")
        return
        
    print(f"\n--- Marks for Course '{course_id}' ---")
    for student in input_data.students:
        s_id = student['id']
        if s_id in input_data.marks[course_id]:
            print(f"  {student['name']} (ID: {s_id}): {input_data.marks[course_id][s_id]}")

# --- MAIN PROGRAM ---

def main():
    while True:
        print("\n" + "="*30)
        print("  STUDENT MARK MANAGEMENT")
        print("="*30)
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-6): ")
        
        if choice == '1':
            input_data.input_students() # Gọi hàm từ file input
        elif choice == '2':
            input_data.input_courses()
        elif choice == '3':
            input_data.input_marks()
        elif choice == '4':
            list_students()             # Gọi hàm nội bộ trong file list
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks()
        elif choice == '0':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()