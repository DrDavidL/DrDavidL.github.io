import streamlit as st

def primes():
    st.title("Let's Calculate Prime Numbers - Using Sieve of Eratosthenes")
    st.write('*Limiting processer for input < 10000!!!*')
    
    submission = st.text_input('Enter a number')

        
    if len(submission) !=0:
        try:
            number = int(submission)
        except ValueError:
            st.write("Please enter a valid input: a positive integer < 10000.")
    
        else:
            n = int(submission)
            if n >= 10000:
                st.write("Your number was too large!")

            else:
                isPrime = {}
                primes=[]


                # Establish range of interest.
                for i in range(2, n+1):
                    isPrime[i] = True

                # Mark the values false that are not prime.    
                for j in range(2, int(n**0.5+1)):
                    k = 0
                    notprime = j**2
                    if isPrime[j] == True:
                        while notprime <= n:
                            isPrime[notprime] = False
                            notprime = j**2 + k*j                
                            k += 1

                # Finalize your list of just prime values.           
                for n in isPrime:
                    if isPrime[n] == True:
                        primes.append(n)
                st.success(primes)