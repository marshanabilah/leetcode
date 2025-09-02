def solve_matrix_rotation():
    # Read matrix dimensions
    n, m = map(int, input().split())
    
    # Read the matrix
    matrix = []
    for i in range(n):
        matrix.append(input().strip())
    
    # Read number of queries
    q = int(input())
    
    # Process each query
    for _ in range(q):
        line = input().split()
        r = int(line[0]) - 1  # Convert to 0-based indexing
        s = line[1]
        
        total_operations = 0
        
        # For each column
        for col in range(m):
            target_char = s[col]
            min_operations = float('inf')
            
            # Try to find target_char in this column
            for row in range(n):
                if matrix[row][col] == target_char:
                    # Calculate operations to move this character to row r
                    # Option 1: Move up
                    up_ops = (row - r) % n
                    # Option 2: Move down  
                    down_ops = (r - row) % n
                    
                    min_operations = min(min_operations, up_ops, down_ops)
            
            total_operations += min_operations
        
        print(total_operations)

solve_matrix_rotation()