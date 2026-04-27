class GwaManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    def find_top_student(self):
        top_name = ""
        # Initialize with a very high number so the first student's 
        # GWA (e.g., 1.75) will be lower than this.
        top_gwa = 5.0 

        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    parts = line.strip().rsplit(' ', 1)
                    if len(parts) < 2: continue
                    
                    name = parts[0]
                    gwa = float(parts[1])
                    
                    # Logic: If you want the "Best" grade (closest to 1.0)
                    if gwa < top_gwa:
                        top_gwa = gwa
                        top_name = name
                        
            print(f"The top student is {top_name} with a GWA of {top_gwa}")
        except FileNotFoundError:
            print("Error: Please make sure 'students.txt' is in this folder.")