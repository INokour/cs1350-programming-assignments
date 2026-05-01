
#Problem 1

grades = {
"alice": {"CS1350": [85, 92, 78], "MATH201": [90, 88]},
"bob": {"CS1350": [72, 75, 80], "PHYS100": [65, 70]},
"carol": {"CS1350": [95, 98, 92], "MATH201": [85, 90]},
}


def gradebook_summary(grades):
    student_averages = {}
    course_scores = {}
    course_best_info = {}

    for student, courses in grades.items():
        all_student_scores = []
        
        for course, scores in courses.items():
            if course not in course_scores:
                course_scores[course] = []
            course_scores[course].extend(scores)
            
            avg = sum(scores) / len(scores)
            if course not in course_best_info:
                course_best_info[course] = [student, avg]
            else:
                current_best_name, current_best_avg = course_best_info[course]
                if avg > current_best_avg or (avg == current_best_avg and student < current_best_name):
                    course_best_info[course] = [student, avg]
            
            all_student_scores.extend(scores)
            
        student_averages[student] = sum(all_student_scores) / len(all_student_scores)

    course_averages = {}
    for course, scores in course_scores.items():
        course_averages[course] = sum(scores) / len(scores)
        
    top_per_course = {}
    for course, info in course_best_info.items():
        top_per_course[course] = info[0]

    return {
        "student_averages": student_averages,
        "course_averages": course_averages,
        "top_per_course": top_per_course
    }

print(gradebook_summary(grades))

# Problem 3
import re
HASHTAG_PATTERN = re.compile(r"#(\w+)")
MENTION_PATTERN = re.compile(r"@(\w+)")
URL_PATTERN = re.compile(r"https?://\S+")

def parse_post(text):
    all_hashtags = HASHTAG_PATTERN.findall(text)
    hashtags = []
    for h in all_hashtags:
        if h not in hashtags:
            hashtags.append(h)
            
    all_mentions = MENTION_PATTERN.findall(text)
    mentions = []
    for m in all_mentions:
        if m not in mentions:
            mentions.append(m)
            
    all_urls = URL_PATTERN.findall(text)
    urls = []
    for u in all_urls:
        if u not in urls:
            urls.append(u)
            
    return {
        "hashtags": hashtags,
        "mentions": mentions,
        "urls": urls
    }
text = """
Check out #Python and #python tips by @alice_dev and @Bob!
    Links: https://example.com/path?q=1 and http://foo.org.
    Re-ping @alice_dev and share #Python again.
"""
    
print(parse_post(text))

# Problem 5
def subset_sum(nums, target):
    if target == 0:
        return True
    if not nums:
        return False
    
    first = nums[0]
    rest = nums[1:]

    return subset_sum(rest, target - first) or subset_sum(rest, target)

print(subset_sum([3, 34, 4, 12, 5, 2], 9)) # True (4 + 5 or 3 + 4 + 2)
print(subset_sum([3, 34, 4, 12, 5, 2], 30)) # False
print(subset_sum([1, 2, 3], 0)) # True (empty subset)
print(subset_sum([], 0)) # True
print(subset_sum([], 5)) # False
print(subset_sum([-2, 3, 5], 1)) # True (-2 + 3)
print(subset_sum([1, 2, 3], 7)) # False

