class Solution:
    def simplifyPath(self,path:str)->str:
        folders=path.split("/")
        result=[]

        i=0

        while i < len(folders):
            folder=folders[i]
            if folder == ""or folder == ".":
               pass
            elif folder == "..":
                if len(result) > 0:
                    result.pop()
            else:
                result.append(folder)
            i +=1

        answer = ""

        for folder in result :
            answer += "/"+folder
        if answer == "":
            return "/"
        return answer