#Longest common subsecuence en O(n*m) 
def lcs(str1, str2):
	m = len(str1)
	n = len(str2)
	matriz = [[0 for i in range(n+1)] for j in range(m+1)] #Matriz de n+1*m+1
	for i in range(1, m+1):
		for j in range(1, n+1):
			if str1[i-1] == str2[j-1]: 
				matriz[i][j] = matriz[i-1][j-1] + 1
			else:
				matriz[i][j] = max(matriz[i][j-1], matriz[i-1][j])
	return matriz[m][n]

str1 = "A scrambled version 13, 3, 2, 21, 1, 1, 8, 5 (OEIS A117540) of the first eight Fibonacci numbers appear as one of the clues left by "
str2 = "murdered museum curator Jacque Sauniere in D. Brown's novel The Da Vinci Code (Brown 2003, pp. 43, 60-61, and 189-192). In the "
print (lcs(str1, str2))