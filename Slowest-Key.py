class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        # Initialize the max duration and the corresponding key
        max_duration = releaseTimes[0]
        result_key = keysPressed[0]

        # Iterate over the releaseTimes and keysPressed
        for i in range(1, len(releaseTimes)):
            # Calculate the duration of the current key press
            duration = releaseTimes[i] - releaseTimes[i - 1]
            key = keysPressed[i]

            # Update the result if the current duration is greater than max_duration
            # or if the duration is the same but the key is lexicographically larger
            if duration > max_duration or (duration == max_duration and key > result_key):
                max_duration = duration
                result_key = key

        return result_key

# Example usage
sol = Solution()
releaseTimes1 = [9,29,49,50]
keysPressed1 = "cbcd"
print(sol.slowestKey(releaseTimes1, keysPressed1))  # Output: "c"

releaseTimes2 = [12,23,36,46,62]
keysPressed2 = "spuda"
print(sol.slowestKey(releaseTimes2, keysPressed2))  # Output: "a"
