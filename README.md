# Student Academic Guidance - Backward Chaining

This program is a simple rule-based expert system for student academic guidance.

It uses four student facts and four rules to check different academic conditions. The selected goal is **EligibleForPlacement**.

The program uses **Backward Chaining** by starting with the goal and working backwards to check what conditions are needed. It then checks whether those conditions are known facts or can be proved using other rules.

If all the required conditions are satisfied, the goal is proved and the final conclusion is displayed.

**Flow:**

EligibleForPlacement → GoodAcademicPerformance + StrongSkills → Required facts → Goal proved
