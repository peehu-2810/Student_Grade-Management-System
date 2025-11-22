import numpy as np

def finding_GPA(student_record):
   
    # it will be calculating the GPA of the student id provided
    sem_data = {}
    
    for r in student_record:
        sem = r["Semester"]
        if sem not in sem_data:
            sem_data[sem] = {'points': 0, 'credits': 0}
            
        grade = r['Marks'] / 10
        sem_data[sem]['points'] += grade * r['Credits']
        sem_data[sem]['credits'] += r['Credits']
        
    results = {}
    for sem, data in sem_data.items():
        if data['credits'] > 0:
            results[sem] = round(data['points'] / data['credits'], 2)
            
    return results

def next_semGPA_prdct(resultGPA):
    # it will be predicting next sem GPA on the basis of trend
    if not resultGPA:
        return 0.0
    gpa = list(resultGPA.values())
    prediction = np.mean(gpa[-3:]) if len(gpa) >= 3 else np.mean(gpa)
    return round(prediction, 2)