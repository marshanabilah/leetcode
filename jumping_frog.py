def solve_frog_jumps():
    def max_jumps(heights):
        n = len(heights)
        if n <= 1:
            return 0
        
        # dp[i] = maximum jumps starting from position i
        dp = [0] * n
        
        # For each position, pre-compute reachable positions using monotonic approach
        reachable = [[] for _ in range(n)]
        
        # Build reachability graph efficiently
        for i in range(n - 1):
            # Use a more efficient visibility check
            max_height_so_far = heights[i]
            
            for j in range(i + 1, n):
                if heights[j] >= heights[i]:
                    # Check if this position is visible
                    # A position j is visible from i if no position between them
                    # has height >= max(heights[i], heights[j])
                    
                    can_see = True
                    target_height = max(heights[i], heights[j])
                    
                    # Quick check: if we already passed a height >= target_height, skip
                    if max_height_so_far >= target_height and j > i + 1:
                        can_see = False
                    else:
                        # Detailed visibility check only when needed
                        for k in range(i + 1, j):
                            if heights[k] >= target_height:
                                can_see = False
                                break
                    
                    if can_see:
                        reachable[i].append(j)
                
                # Update max height seen so far for optimization
                max_height_so_far = max(max_height_so_far, heights[j])
                
                # Early termination: if current height is too high, 
                # future positions won't be reachable due to blocking
                if heights[j] > heights[i] and max_height_so_far >= heights[j]:
                    # This position might block future visibility
                    pass
        
        # Fill DP table from right to left
        for i in range(n - 2, -1, -1):
            for j in reachable[i]:
                dp[i] = max(dp[i], 1 + dp[j])
        
        return dp[0]
    
    def max_jumps_stack(heights):
        n = len(heights)
        if n <= 1:
            return 0
        
        # dp[i] = maximum jumps starting from position i
        dp = [0] * n
        
        # Use decreasing monotonic stack to track potential blocking positions
        for i in range(n - 2, -1, -1):
            stack = []  # Positions that might block future jumps
            
            for j in range(i + 1, n):
                if heights[j] >= heights[i]:
                    # Check visibility using stack
                    target_height = max(heights[i], heights[j])
                    
                    # Remove positions from stack that are lower than target height
                    visible = True
                    for pos in stack:
                        if heights[pos] >= target_height:
                            visible = False
                            break
                    
                    if visible:
                        dp[i] = max(dp[i], 1 + dp[j])
                
                # Maintain monotonic stack (decreasing heights)
                while stack and heights[stack[-1]] <= heights[j]:
                    stack.pop()
                stack.append(j)
        
        return dp[0]
    
    def max_jumps_ultra(heights):
        n = len(heights)
        if n <= 1:
            return 0
        
        # For small inputs, use simpler approach
        if n <= 50:
            return max_jumps(heights)
        
        # dp[i] = maximum jumps starting from position i
        dp = [0] * n
        
        # Process from right to left
        for i in range(n - 2, -1, -1):
            current_height = heights[i]
            max_blocking_height = 0
            
            for j in range(i + 1, n):
                if heights[j] >= current_height:
                    target_height = max(current_height, heights[j])
                    
                    # Quick visibility check: if we've seen a blocking height, skip detailed check
                    if max_blocking_height >= target_height:
                        continue
                    
                    # Detailed visibility check
                    visible = True
                    for k in range(i + 1, j):
                        if heights[k] >= target_height:
                            visible = False
                            max_blocking_height = max(max_blocking_height, heights[k])
                            break
                    
                    if visible:
                        dp[i] = max(dp[i], 1 + dp[j])
                
                # Early termination optimization
                if heights[j] > current_height:
                    max_blocking_height = max(max_blocking_height, heights[j])
        
        return dp[0]
    
    # Read input
    T = int(input())
    
    for _ in range(T):
        N, K = map(int, input().split())
        pillars = list(map(int, input().split()))
        starting_heights = list(map(int, input().split()))
        
        total_jumps = 0
        
        for start_height in starting_heights:
            heights = [start_height] + pillars
            total_jumps += max_jumps_ultra(heights)
        
        print(total_jumps)

solve_frog_jumps()