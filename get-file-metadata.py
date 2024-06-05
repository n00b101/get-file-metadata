import subprocess

def get_file_metadata(file_name):
    result = subprocess.run(['stat', '-f', 'File: %N\nSize: %z\nBlocks: %b\nIO Block: %k\nType: %HT\nDevice: %Hd\nInode: %i\nLinks: %l\nAccess: %Sp\nUid: (%u/%Su)\nGid: (%g/%Sg)\nAccess: %Sa\nModify: %Sm\nChange: %Sc\nBirth: %SB\n', file_name], capture_output=True, text=True)
    return result.stdout

def display_metadata(metadata):
    print("File Metadata:")
    for line in metadata.split('\n'):
        if line.strip():
            print(line)

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    metadata = get_file_metadata(file_name)
    display_metadata(metadata)
