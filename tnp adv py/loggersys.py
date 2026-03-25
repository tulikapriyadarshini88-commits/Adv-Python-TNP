class Logger:
    def __init__(self, file):
        self.f = open(file, "w")

    def log(self, msg):
        self.f.write("INFO: " + msg + "\n")

    def log_warning(self, msg):
        self.f.write("WARNING: " + msg + "\n")

    def log_error(self, msg):
        self.f.write("ERROR: " + msg + "\n")

    def __del__(self):
        self.f.close()