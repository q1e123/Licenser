## @package engine
# Contains Engine class
import os
import utils
from datetime import date
## Does the licensing
class Engine:
    ## Constructor
    # @param file_name Settings file
    # @param project_path The path of the project
    def __init__(self,file_name,project_path):
        ## File containg the settings
        self.settings = self.__get_settings(file_name)
        ## List of files to ignore
        if "ignore" in self.settings:
            self.settings["ignore"] = self.settings["ignore"].split(",")
        ## Path to the project
        self.project = project_path
   
    ## Gets the settings
    # @param file_name settings file
    def __get_settings(self,file_name):
        settings = {}
        with open(file_name,'r') as f:
            lines = f.readlines()
            for line in lines:
                split = line.replace('\n','|').split('|')
                settings[split[0]] = split[1]
        return settings
    
    ## Does the licensing
    def license(self):
        lic_header = utils.get_content(self.settings["header"])
        author = "Copyright (C) " + str(date.today().year) + " " + self.settings["author"]
        
        headers = {}
        headers[".c"] = "/*\n" + author + "\n" + lic_header + "*/\n"
        headers[".cpp"] = "/*\n" + author + "\n" + lic_header + "*/\n"
        headers[".py"] = "# " + author + "\n# " + lic_header.replace("\n","\n# " )[:-5] + "\n"
        
        dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"  +self.project
        
        for path, subdirs, files in os.walk(dir_path):
            for name in files:
                if name not in self.settings["ignore"]:
                    f = path + "/" + name
                    extension = os.path.splitext(name)[1]
                    if extension in headers: 
                        ff = open(f,"r")
                        lines = ff.readlines()
                        ff.close()
                        if "Copyright" not in lines[0] and "Created by" not in lines[0] and "Copyright" not in lines[1] and "Created by" not in lines[1]:
                            cnt = headers[extension]
                            utils.line_prepender(f,cnt)

        os.system("cp " + "Licenses/"  + self.settings["license"] + " " + dir_path + "LICENSE")
