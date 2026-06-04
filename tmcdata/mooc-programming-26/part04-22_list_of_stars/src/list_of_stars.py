# Write your solution here
def list_of_stars(x:list):
  for i in x:
    print("*" * i)
  
if __name__ == "__main__":
  list_of_stars([3, 4, 5, 6, 7])