'''
Module for calculating Takahashi's score based on judges' grades.
'''
def calculate_score(N, grades):
    """
    Calculate Takahashi's score by removing the highest and lowest N grades
    and averaging the remaining grades.
    Parameters:
    N (int): Number of judges to invalidate from both highest and lowest grades.
    grades (list): List of grades from judges.
    Returns:
    float: The average score after removing the highest and lowest grades.
    """
    # Sort the grades
    grades.sort()
    # Remove the highest N and lowest N grades
    remaining_grades = grades[N:len(grades)-N]
    # Calculate the sum of the remaining grades
    total_sum = sum(remaining_grades)
    # Calculate Takahashi's score
    takahashi_score = total_sum / (3 * N)
    return takahashi_score