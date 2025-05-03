import os

class Config:
    TEMP_DIR = os.path.join(os.path.dirname(__file__), "..", "temp")
    ALLOWED_FILE_TYPES = ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
    MAX_FILE_SIZE_MB = 5  # Maximum file size in MB