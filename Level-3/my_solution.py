found = 0
def solution(n):
    # Your code here
    def verify(last_total, check_list):
        global found
        
        for i in check_list:
            new_total = last_total + i
            
            if new_total > n:
                break
        
            elif new_total== n or new_total + i > n:
                found += 1
                break

            else:
                verify(new_total, list(range(i + 1, n - last_total)))
    
    verify(0, list(range(1, n//2 + 1)))
    
    return found
