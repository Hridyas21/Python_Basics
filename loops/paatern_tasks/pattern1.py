#Create python code for displaying the following patterns :
#Pattern - 1
'''
* * * * *
 * * * *
  * * *
   * *
    * 
'''
for r in range(5,0,-1):
    print(" "*int(5-r),"* "*r)