class Solution:
    def reformatDate(self, date: str) -> str:
        # Mapping of month abbreviations to their numeric representation
        month_map = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }

        # Split the date string into day, month, and year
        parts = date.split()
        day = parts[0][:-2]  # Remove the suffix from the day part
        month = parts[1]
        year = parts[2]

        # Convert day to two-digit format
        if len(day) == 1:
            day = "0" + day

        # Convert month abbreviation to its numeric representation
        month = month_map[month]

        # Combine into the desired format
        formatted_date = f"{year}-{month}-{day}"
        return formatted_date

# Example usage:
solution = Solution()
print(solution.reformatDate("20th Oct 2052"))  # Output: "2052-10-20"
print(solution.reformatDate("6th Jun 1933"))   # Output: "1933-06-06"
print(solution.reformatDate("26th May 1960"))  # Output: "1960-05-26"
