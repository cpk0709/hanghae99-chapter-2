
# telBtn = {
#     "2":"abc",
#     "3":"def",
#     "4":"ghi",
#     "5":"jkl",
#     "6":"mno",
#     "7":"pqrs",
#     "8":"tuv",
#     "9":"wxyz",
# }

def telletterCimbin(digits:str):

    def dfs(index,path):
        # print(len(path),len(digits))
        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index,len(digits)):
            for j in telBtn[digits[i]]:
                dfs(i + 1,path+j)

    if not digits:
        return []

    telBtn = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = []
    dfs(0,"")

    return  result

result = telletterCimbin("23")
print("#",result)