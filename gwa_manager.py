class GwaManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    def find_top_student(self):
        top_name, top_gwa = "", -1.0
        with open(self.filename, 'r') as f:
            for line in f:
                parts = line.strip().rsplit(' ', 1)
                name, gwa = parts[0], float(parts[1])
                if gwa > top_gwa:
                    top_gwa = gwa
                    top_name = name
        print(f"Highest GWA: {top_name} ({top_gwa})")