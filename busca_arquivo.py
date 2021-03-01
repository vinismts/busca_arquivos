import os,sys,logging

from imp import reload
diretorio =os.path.dirname(os.path.abspath(sys.argv[0]))

reload(logging)
logging.basicConfig(format='%(message)s',filename=os.path.join(diretorio,'arquivos.log'), filemode='w', level=logging.DEBUG)

'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)

        else:

            allFiles.append(fullPath)
                
    return allFiles        
def main():
    try:
        dirName=input('Digite o diretório: ')    
        #dirName = 'P:\SOF'
    
        # Get the list of all files in directory tree at given path
        listOfFiles = getListOfFiles(dirName)
    except Exception as e:
        logging.error(e)
    
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        for file in filenames:
            if ('HPROF' in file.upper()) or ('VELHO' in file.upper()) or ('ANTIGO' in file.upper()) or ('CÓPIA' in file.upper()) or ('COPIA' in file.upper()) or ('COPY' in file.upper()) or ('BKP' in file.upper()) or ('OLD' in file.upper()) or ('BACKUP' in file.upper()) or (file.endswith('.zip'))\
            or (file.endswith('.rar') or (file.endswith('.7z'))):
                listOfFiles += [os.path.join(dirpath, file)]
        
        
    # Print the files    
    for elem in listOfFiles:
        logging.debug('del "'+elem+'"')    
        
        
        
        
if __name__ == '__main__':
    main()