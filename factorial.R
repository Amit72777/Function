factorial <- function(n)
{
  n2 <- 1 
  for ( i in  1:n)
  {
    n2 <- i * n2  
  }
  return (n2)  
}


num <- as.integer(readline(prompt = "Enter your number: "))

print(factorial(num))  # print the input factorial 


