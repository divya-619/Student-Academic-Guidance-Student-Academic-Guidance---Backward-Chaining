
# Facts known about the student
facts = ["HighAttendance", "GoodMarks", "CompletedProjects", "HasInternship"]

rules = [
    (["HighAttendance", "GoodMarks"], "GoodAcademicPerformance"),
    (["CompletedProjects", "HasInternship"], "StrongSkills"),
    (["GoodAcademicPerformance", "StrongSkills"], "EligibleForPlacement"),
    (["LowCodingScore"], "NeedsExtraPractice"),
]
def prove(goal, depth=0):
    """Try to prove a goal. Returns True if proven, else False."""
    indent = "  " * depth
    print(f"{indent}Goal: {goal}")

    # Case 1: the goal is already a known fact
    if goal in facts:
        print(f"{indent}  -> '{goal}' is a known fact. PROVED")
        return True

    # Case 2: find rules that conclude this goal
    for conditions, conclusion in rules:
        if conclusion == goal:
            print(f"{indent}  Rule found: IF {' AND '.join(conditions)} THEN {goal}")

            # Prove every condition (these become new sub-goals)
            all_true = True
            for condition in conditions:
                if not prove(condition, depth + 2):
                    all_true = False
                    break

            if all_true:
                print(f"{indent}  -> All conditions true. '{goal}' PROVED")
                return True

    # Case 3: not a fact and no rule could prove it
    print(f"{indent}  -> '{goal}' cannot be proved. FAILED")
    return False

goal = "EligibleForPlacement"

print("Facts:", facts)
print("Proving goal:", goal)
print("-" * 50)

result = prove(goal)

print("-" * 50)
if result:
    print(f"Conclusion: The student is {goal}.")
else:
    print(f"Conclusion: Cannot prove {goal}.")