import datamanagement
import gradecalculator
import comparision
import sys

def find_class_avg():
    # will help finding class avg for better comparision
    df = datamanagement.load_complete_data()
    if df.empty:
        return {}
    avg_df = df.groupby('Semester')['Marks'].mean()
    return {Semester: round(mark/10, 2) for Semester, mark in avg_df.items()}

def main():
    print("="*50)
    print("======STUDENT MANAGMENT SYSTEM======")
    print("="*50)
    
    # FROM HERE THE LOGIN PROCESS STARTS 
    while True:
        try:
            input_id = input("PLEASE ENTER STUDENT ID(for e.g 101...) TO CONTINUE THE LOGIN PROCESS AND ACCESS YOUR DATA: ")
            if not input_id.strip(): continue 
            # JUST NEED TO PRESS ENTER
            current_id = int(input_id)
            break
        except ValueError:
            print("PLEASE ENTER THE VALID ID (for eg-101,102 etc).")

    student_name = datamanagement.take_student_name(current_id)
    if student_name == "NO DATA FOUND":
        print("Error: Student ID not found.")
        return

    print(f"\nYAYYY!!! Login Successful! Welcome, {student_name}.")
    
    # NOW WILL COME THE MAIN MENU PHASE
    while True:
        print("\n" + "-"*30)
        print(f" Dashboard: {student_name}")
        print("-"*30)
        print("1. SEE My Report Card")
        print("2. Visualize My Growth")
        print("3. Comparision with Class Average")
        print("4. Comparision with Peer")
        print("5. Predict Future GPA")
        print("6. Add New Marks")
        print("7. Exit")
        
        choice = input("Please Select Option (1-7): ")
        
        # fetching user data from the database
        records = datamanagement.take_studentdata(current_id)
        my_gpas = gradecalculator.finding_GPA(records)

        if choice == '1':
            print(f"\n[Transcript: {student_name}]")
            if  len(my_gpas) == 0:
                print("No such records found.")
            for Semester, gpa in my_gpas.items():
                print(f"Semester {Semester}: {gpa} SGPA")

        elif choice == '2':
            if my_gpas:
                comparision.gpa_trend_plotting(my_gpas, student_name)
            else:
                print("No data to visualize.")

        elif choice == '3':
            class_avg = find_class_avg()
            comparision.compare_sketch(my_gpas, class_avg)

        elif choice == '4':
            try:
                friend_id = int(input("Please Enter Friend's Student ID: "))
                
                if friend_id == current_id:
                    print("DAMN! You cannot compare with yourself!")
                else:
                    friend_name = datamanagement.take_studentdata(friend_id)
                    
                    if friend_name == "Unknown":
                        print(f"Student ID {friend_id} not found.")
                    else:
                        
                        friend_records = datamanagement.take_studentdata(friend_id)
                        friend_gpas = gradecalculator.finding_GPA(friend_records)
                        
                        comparision.sketch_peercompare(my_gpas, friend_gpas, student_name, friend_name)
            except ValueError:
                print("Invalid ID format,PLEASE ENTER THE VALID ONE.")

        elif choice == '5':
            predict = gradecalculator.next_semGPA_prdct(my_gpas)
            print(f"\nBased on the trend, next GPA prediciton: {predict}")

        elif choice == '6':
            try:
                Semesters = int(input("Semester Number: "))
                subj = input("Subject Name: ")
                creds = int(input("Credits (1-4): "))
                marksobtained = int(input("Marks obtained (0-100): "))
                if 0 <= marksobtained <= 100:
                    datamanagement.add_record(current_id, student_name, Semesters, subj, creds, marksobtained)
                    print("Record Added Successfully.")
                else:
                    print("Marks obtained should be between 0-100.")
            except ValueError:
                print("Invalid input. Please enter numbers for Semesters/Credits/Marks.")

        elif choice == '7':
            print("Logging out, Good luck!")
            break
        
        else:
            print("Invalid choice.Please Try again.")

if __name__ == "__main__":
    main()