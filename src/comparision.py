import matplotlib.pyplot as plt

def gpa_trend_plotting(gpa_results, student_name):
    # it will be plotting single line trend to tell about of_student performance
    if not gpa_results:
        print("INVVALID")
        return

    # here we will be sorting data for different emester to keep it organized
    semesters = sorted(gpa_results.keys())
    gpas = [gpa_results[s] for s in semesters]
    
    plt.figure(figsize=(8, 5))
    
    # PLOTTING THE LINEEEEEEEEEEEEE WHICH WILL TELL of_student PERFORMANCE
    plt.plot(semesters, gpas, marker='o', color='#2c3e50', linestyle='-', linewidth=2, label=student_name)
    
    # in this we will adddd refernce line for distinction
    plt.axhline(y=8.5, color='green', linestyle='--', alpha=0.3, label='Distinction (8.5)')
    
    plt.title(f'Academic Performance Trend: {student_name}')
    plt.xlabel('Semesters')
    plt.ylabel('GPA')
    plt.ylim(0, 10)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    print("here is the personal growth graph")
    plt.show()

def compare_sketch(gpa_of_student, gpa_of_classavg):
    # it will compare of_student's growth with the class avg
    if not gpa_of_student:
        print("Data not Found.")
        return

    sems = sorted(gpa_of_student.keys())
    sgpa_value = [gpa_of_student[s] for s in sems]
    
    # finding class avg for the semesterss
    classgpa_value = [gpa_of_classavg.get(s, 0) for s in sems]

    x = range(len(sems))
    
    plt.figure(figsize=(10, 6))
    
    # here we will get the bar of student gpa
    plt.bar([i - 0.2 for i in x], sgpa_value, width=0.4, label='You', color='black')
#    here we will get the bar of class gpa
    plt.bar([i + 0.2 for i in x], classgpa_value, width=0.4, label='Class Avg', color='green', alpha=0.7)
    
    plt.xticks(x, [f"Sem {s}" for s in sems])
    plt.title('comparision of performance between YOU and CLASS AVG')
    plt.ylabel('GPA')
    plt.ylim(0, 10)
    plt.legend()
    
    print("........======PRESENTING THE CLASS COMPARISION CHART======........")
    plt.show()

def sketch_peercompare(your_gpa, your_friend_gpa, your_name, your_friend_name):
    # in this a graph will be plotted where comparision of two peers 
    # also taking the semesters marks of both to compare nicely
    all_sems = sorted(set(list(your_gpa.keys()) + list(your_friend_gpa.keys())))
    
    if not all_sems:
        print("there are no common semesters to compare")
        return
    
    # a data list will be prepare, no data list if student has skipped a semesters
    your_gpavals = [your_gpa.get(s, None) for s in all_sems]
    friend_gpavals = [your_friend_gpa.get(s, None) for s in all_sems]
    
    plt.figure(figsize=(9, 5))
    
    # your graph line will be plotted
    plt.plot(all_sems, your_gpavals, marker='o', linewidth=2, color='blue', label=f"{your_name} (You)")
    
    # frnd's graph line will be plotted
    plt.plot(all_sems, friend_gpavals, marker='s', linewidth=2, color='orange', linestyle='--', label=your_friend_name)
    
    plt.title(f'one to one Analysis: {your_name} vs {your_friend_name}')
    plt.xlabel('semesters')
    plt.ylabel('GPA')
    plt.ylim(0, 10)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    print(f"......=====Presenting the comparision graph: You vs {your_friend_name}=====......")
    plt.show()