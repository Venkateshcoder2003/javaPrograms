"""text=input("Enter the text:")
freq={}

for i in text:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(f"Frequency of occurance of each digit in {text} is:","\n",freq)"""

# A naive recursive Python implementation


def binomial_coef(N,K):
	if K==0 or K==N:
		return 1
	if K>N:
		return 0
	else:
		return binomial_coef(N-1,K-1)+binomial_coef(N-1,K)
def factorial(num):
	if num==0 or num==1:
		return 1
	else:
		return num*factorial(num-1)
N=int(input("Enter N:"))
K=int(input("Enter K:"))
result=binomial_coef(N,K)
print("The bionomial Coefficient is:",result)
num=int(input("Enter the number :"))
fact_res=factorial(num)
print("The factorial of a given number is:",fact_res)
