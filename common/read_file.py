
class ReadFile:
    @staticmethod
    def read_file(file_path):
        
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

if __name__ == "__main__":
    # Example usage
    file_content = ReadFile.read_file('example.txt')
    print(file_content)