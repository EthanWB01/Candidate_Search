class Candidates:
    def __init__(self, first_name, last_name, degree, employment, projects, points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.degree = degree
        self.employment = employment
        self.projects = projects
        self.points = points
        # Call point_system to calculate points
        self.points += self.point_system()

    def point_system(self):
        points = 0  # Initialize points counter

        if self.degree == " Yes":
            points += 5

        if "/" in self.employment:
            points += len(self.employment.split("/")) * 2
        elif self.employment != "N/A":
            points += 2

        if "/" in self.projects:
            points += len(self.projects.split("/")) * 3
        elif self.projects != "N/A":
            points += 3

        return points

    def __gt__(self, other):
        if isinstance(other, Candidates):
            return self.points > other.points
        else:
            raise TypeError("Comparison with unsupported types")

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name} | Degree: {self.degree} | Past Employment: {self.employment} | Projects: {self.projects} | Rating: {self.points}"
