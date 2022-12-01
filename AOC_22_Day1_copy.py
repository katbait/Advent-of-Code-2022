from pathlib import Path
p = Path("input.txt")
    
sorted_sums = sorted(map(sum, map(lambda x : map(int, x.strip().split('\n')),
                    p.read_text().split('\n\n'))))

print(sorted_sums[-1]) 
print(sum(sorted_sums[-3:]))