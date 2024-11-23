from datetime import date, timedelta
class Beta:
    def __init__(self,filename):
        with open(filename, "r") as infile:
            lines = infile.readlines()
            time = []
            beta_value = []
            for i in range(0, len(lines)):
                a = lines[i].split(" ")
                time.append(a[0])
                beta_value.append(float(a[2]))
        self.beta_value = beta_value
        self.time = time
    def __call__(self):
