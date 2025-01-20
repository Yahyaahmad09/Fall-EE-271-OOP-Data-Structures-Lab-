# Employee
class EEDJ_Employee:
    def __init__(self, emp_id, name, position, workload, scale, base_pay):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.workload = workload
        self.scale = scale
        self.base_pay = base_pay

    def display(self):
        return (f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, "
                f"Workload: {self.workload}, Scale: {self.scale}, Base Pay: {self.base_pay}")

# ---------------------------------------------------------------------------------------------------------

# Faculty

class Faculty(EEDJ_Employee):
    def __init__(self, emp_id, name, position, workload, scale, base_pay, subject):
        super().__init__(emp_id, name, position, workload, scale, base_pay)
        self.subject = subject

    def display(self):
        return super().display() + f", Subject: {self.subject}"


class Professor(Faculty):
    def __init__(self, emp_id, name, position, workload, scale, base_pay, subject, status, net_pay):
        super().__init__(emp_id, name, position, workload, scale, base_pay, subject)
        self.status = status
        self.net_pay = net_pay

    def display(self):
        return super().display() + f", Status: {self.status}, Net Pay: {self.net_pay}"


class AssociateProf(Faculty):
    def __init__(self, emp_id, name, position, workload, scale, base_pay, subject, research_area, net_pay):
        super().__init__(emp_id, name, position, workload, scale, base_pay, subject)
        self.research_area = research_area
        self.net_pay = net_pay

    def display(self):
        return super().display() + f", Research Area: {self.research_area}, Net Pay: {self.net_pay}"


class AssistantProf(Faculty):
    def __init__(self, emp_id, name, position, workload, scale, base_pay, subject, experience, net_pay):
        super().__init__(emp_id, name, position, workload, scale, base_pay, subject)
        self.experience = experience
        self.net_pay = net_pay

    def display(self):
        return super().display() + f", Experience: {self.experience} years, Net Pay: {self.net_pay}"


class Lecturer(Faculty):
    def __init__(self, emp_id, name, position, workload, scale, base_pay, subject, term, net_pay):
        super().__init__(emp_id, name, position, workload, scale, base_pay, subject)
        self.term = term
        self.net_pay = net_pay

    def display(self):
        return super().display() + f", Term: {self.term}, Net Pay: {self.net_pay}"


#=---------------------------------------------------------------------------------------------------------

# Admin

class Admin(EEDJ_Employee):
    def __init__(self, emp_id, name, position, workload, scale, base_pay, lab_subject, department):
        super().__init__(emp_id, name, position, workload, scale, base_pay)
        self.lab_subject = lab_subject
        self.department = department

    def display(self):
        return super().display() + f", Lab Subject: {self.lab_subject}, Department: {self.department}"


class LabEngineer(Admin):
    def __init__(self, emp_id, name, position, workload, scale, base_pay, lab_subject, department, projects):
        super().__init__(emp_id, name, position, workload, scale, base_pay, lab_subject, department)
        self.projects = projects

    def display(self):
        return super().display() + f", Projects: {self.projects}"


class LabTechnician(Admin):
    def __init__(self, emp_id, name, position, workload, scale, base_pay, lab_subject, department, skills):
        super().__init__(emp_id, name, position, workload, scale, base_pay, lab_subject, department)
        self.skills = skills

    def display(self):
        return super().display() + f", Skills: {self.skills}"


class LabAssistant(Admin):
    def __init__(self, emp_id, name, position, workload, scale, base_pay, lab_subject, department, years_assisting):
        super().__init__(emp_id, name, position, workload, scale, base_pay, lab_subject, department)
        self.years_assisting = years_assisting

    def display(self):
        return super().display() + f", Years Assisting: {self.years_assisting}"


class LabAttendant(Admin):
    def __init__(self, emp_id, name, position, workload, scale, base_pay, lab_subject, department, attendance_rate):
        super().__init__(emp_id, name, position, workload, scale, base_pay, lab_subject, department)
        self.attendance_rate = attendance_rate

    def display(self):
        return super().display() + f", Attendance Rate: {self.attendance_rate}"

#--------------------------------------------------------------------------------------------------------------------------------

# Chairman

class Chairman(Admin, Faculty):
    def __init__(self, emp_id, name, position, workload, scale, base_pay, subject, department, term_duration):
        Faculty.__init__(self, emp_id, name, position, workload, scale, base_pay, subject)
        self.term_duration = term_duration

    def display(self):
        return (f"{Faculty.display(self)}, Term Duration: {self.term_duration} years")