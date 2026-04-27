class GwaManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    def find_top_student(self):
        with open(self.filename, 'r') as f:
            for line in f:
                parts = line.strip().rsplit(' ', 1)
                name, gwa = parts[0], float(parts[1])