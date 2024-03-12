import os
import csv

from HireClass import Candidates

def read_file(file_path):
    first_name = []
    last_name = []
    degree = []
    employment = []
    projects = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        for data in reader:
            first_name.append(data[0])
            last_name.append(data[1])
            degree.append(data[2])
            employment.append(data[3])
            projects.append(data[4])
    return first_name, last_name, degree, employment, projects

if __name__ == '__main__':
    file_path = os.path.join("data", "Candidate_Info.csv")
    first_name, last_name, degree, employment, projects = read_file(file_path)
    candidates = []
    for i in range(len(first_name)):
        candidate = Candidates(first_name[i], last_name[i], degree[i], employment[i], projects[i])
        candidates.append(candidate)

    # Sort candidates based on points
    candidates.sort(reverse=True)

    for candidate in candidates:
        print(candidate)