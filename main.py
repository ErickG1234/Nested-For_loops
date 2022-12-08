# # nested loop = A loop within another loop(outer, inner)
#      # outer loop:
#        # Inner Loop:
# for x in range(1,10): 
#   print(x, end = "") #end = "" makes all numbers printed on the same line(You can pt something in bwtween the quotation marks)

# for x in range(3):
#   for y in range(1,10): 
#     print(y, end = "")
#   print() # print code on a new line

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")


for x in range(rows):
  for y in range(columns): 
    print(symbol, end = "")
  print()



  
