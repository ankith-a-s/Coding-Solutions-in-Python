class Solution:
	# @param A : string
	# @return a strings
	def simplifyPath(self, A):
        pathStack = []
        A = A.split('/')
        for word in A:
            if word == '/' or word == '.' or not word:
                continue
            elif word == '..':
                if pathStack:
                    pathStack.pop()
            else:
                pathStack.append(word)
        result = ''
        while pathStack:
            result = '/' + pathStack.pop() + result
        return result if result else '/'