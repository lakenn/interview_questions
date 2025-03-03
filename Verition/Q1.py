# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(S, C):
#     # Implement your solution here
#     company = C.lower()
#     names = [name.strip() for name in S.split('; ')]
#     email_count = {}
#     result = []
#
#     for name in names:
#         parts = [p.strip() for p in name.split(" ")]
#         first = parts[0].lower()
#         last = parts[-1].lower().replace('-', '')[:8]
#
#         email = f'{first}.{last}@{company}.com'
#
#         if email in email_count:
#             email_count[email] += 1
#             email = f"{first}.{last}{email_count[email]}@{company}.com"
#         else:
#             email_count[email] = 1
#
#         result.append(email)
#
#     return '; '.join(result)

def solution(S, C):
    # Implement your solution here
    company = C.lower()
    email_count = {}
    result = []

    for name in S.split('; '):
        parts = [p for p in name.split()]
        first = parts[0].lower()
        last = parts[-1].lower().replace('-', '')[:8]

        email = f'{first}.{last}@{company}.com'

        if email in email_count:
            email_count[email] += 1
            email = f"{first}.{last}{email_count[email]}@{company}.com"
        else:
            email_count[email] = 1

        result.append(email)

    return '; '.join(result)



print(solution("Joe Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe;", 'Company'))