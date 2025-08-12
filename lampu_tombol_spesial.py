def lampuDanTombolSpesial(N, L):
    min_presses = float('inf')
    found_solution = False
    
    for i in range(4):
        # i represents the state of the first two buttons (2 and 3)
        # Binary representation: 00, 01, 10, 11
        # 0 means the button is not pressed, 1 means the button is pressed

        presses = 0
        buttons = [0] * (N - 1)  # buttons[i] represents button i+2
        lights = L[:]

        # Initialize the first two buttons
        if (i >> 0) & 1:  # Check if the first bit is set (button 3)
            buttons[1] = 1
            presses += 1
            lights[1-1] ^= 1
            lights[1] ^= 1
            lights[1+1] ^= 1
        if (i >> 1) & 1:  # Check if the second bit is set (button 2)
            buttons[0] = 1
            presses += 1
            lights[0-1+1] ^= 1
            lights[0+1] ^= 1
            lights[0+2] ^= 1

        # Determine the state of the remaining buttons
        for j in range(2, N - 1):
            if lights[j-1] == 0:
                buttons[j] = 1
                presses += 1
                lights[j-1] ^= 1
                lights[j] ^= 1
                lights[j+1] ^= 1

        # Check if all lights are on
        all_on = all(light == 1 for light in lights)

        if all_on:
            found_solution = True
            min_presses = min(min_presses, presses)

    if found_solution:
        return (f"YES {min_presses}")
    else:
        return ("NO -1")