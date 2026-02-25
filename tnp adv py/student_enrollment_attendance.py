# -------------------------------
# STUDENT ENROLLMENT + ATTENDANCE SYSTEM
# -------------------------------

students = {}   # {roll: {"sec": sec, "name": name, "courses": {merge_id:{attendance, grade}}}}
courses = {}    # {course_id: {"name": name, "limit": limit, "students": []}}

MAX_COURSES = 3
ATT_LIMIT = 75


# ---------------- ADD STUDENT ----------------
def add_student():
    roll = input("Enter Roll No: ")
    sec = input("Enter Section: ")
    name = input("Enter Name: ")

    if roll in students:
        print("Student already exists!")
    else:
        students[roll] = {"sec": sec, "name": name, "courses": {}}
        print("Student added successfully!")


# ---------------- ADD COURSE ----------------
def add_course():
    cid = input("Enter Course ID: ")
    cname = input("Enter Course Name: ")
    limit = int(input("Enter Course Limit: "))

    if cid in courses:
        print("Course already exists!")
    else:
        courses[cid] = {"name": cname, "limit": limit, "students": []}
        print("Course added successfully!")


# ---------------- ENROLL STUDENT ----------------
def enroll_student():
    roll = input("Enter Roll No: ")
    cid = input("Enter Course ID: ")

    if roll not in students:
        print("Student not found!")
        return

    if cid not in courses:
        print("Course not found!")
        return

    if len(students[roll]["courses"]) >= MAX_COURSES:
        print("Student cannot enroll more than 3 courses!")
        return

    if len(courses[cid]["students"]) >= courses[cid]["limit"]:
        print("Course limit reached!")
        return

    merge_id = roll + "_" + cid   # StudentID + CourseID merge

    students[roll]["courses"][merge_id] = {"course_id": cid,
                                           "attendance": 0,
                                           "grade": None}

    courses[cid]["students"].append(roll)

    print("Student enrolled successfully!")
    print("Enrollment ID:", merge_id)


# ---------------- ASSIGN ATTENDANCE + GRADE ----------------
def assign_grade():
    roll = input("Enter Roll No: ")
    cid = input("Enter Course ID: ")

    merge_id = roll + "_" + cid

    if roll in students and merge_id in students[roll]["courses"]:
        attendance = int(input("Enter Attendance %: "))
        grade = input("Enter Grade: ")

        students[roll]["courses"][merge_id]["attendance"] = attendance
        students[roll]["courses"][merge_id]["grade"] = grade

        print("Updated successfully!")

        if attendance < ATT_LIMIT:
            print("⚠ WARNING: Attendance below 75%! Student is Defaulter.")

    else:
        print("Enrollment not found!")


# ---------------- VIEW STUDENT REPORT ----------------
def view_student_report():
    roll = input("Enter Roll No: ")

    if roll not in students:
        print("Student not found!")
        return

    print("\n------ STUDENT REPORT ------")
    print("Roll:", roll)
    print("Section:", students[roll]["sec"])
    print("Name:", students[roll]["name"])

    for merge_id, data in students[roll]["courses"].items():
        cid = data["course_id"]
        print("\nCourse:", courses[cid]["name"])
        print("Attendance:", data["attendance"])
        print("Grade:", data["grade"])

        if data["attendance"] < ATT_LIMIT:
            print("Status: DEFUALTER")
        else:
            print("Status: Regular")


# ---------------- COURSE WISE REPORT ----------------
def course_report():
    cid = input("Enter Course ID: ")

    if cid not in courses:
        print("Course not found!")
        return

    print("\n------ COURSE REPORT ------")
    print("Course:", courses[cid]["name"])

    for roll in courses[cid]["students"]:
        merge_id = roll + "_" + cid
        attendance = students[roll]["courses"][merge_id]["attendance"]
        name = students[roll]["name"]

        print("Roll:", roll,
              "| Name:", name,
              "| Attendance:", attendance)


# ---------------- DEFULTER LIST ----------------
def defaulter_list():
    print("\n------ DEFUALTER LIST (Attendance < 75%) ------")

    for roll, sdata in students.items():
        for merge_id, cdata in sdata["courses"].items():
            if cdata["attendance"] < ATT_LIMIT:
                cid = cdata["course_id"]
                print("Roll:", roll,
                      "| Name:", sdata["name"],
                      "| Course:", courses[cid]["name"],
                      "| Attendance:", cdata["attendance"])


# ---------------- MENU ----------------
while True:
    print("\n===== STUDENT ENROLLMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student")
    print("4. Assign Grade & Attendance")
    print("5. View Student Report")
    print("6. Course Wise Report")
    print("7. Defaulter List")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        enroll_student()
    elif choice == "4":
        assign_grade()
    elif choice == "5":
        view_student_report()
    elif choice == "6":
        course_report()
    elif choice == "7":
        defaulter_list()
    elif choice == "8":
        print("Exiting system...")
        break
    else:
        print("Invalid choice!")