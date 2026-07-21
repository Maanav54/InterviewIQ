from typing import Any
def questions(role: str, difficulty: str, company: str, skills: list[str]) -> list[dict[str,Any]]:
    focus = skills[0] if skills else "data structures"
    return [{"id":1,"category":"Technical","question":f"Explain a production use case for {focus} in a {role} role.","difficulty":difficulty},{"id":2,"category":"Problem solving","question":"How would you reason about time complexity and edge cases before coding?","difficulty":difficulty},{"id":3,"category":"Behavioral","question":f"Tell me about a time you handled conflicting priorities on a {company} team.","difficulty":difficulty}]
def evaluate(answer: str, topic: str) -> dict:
    length_score=min(35,len(answer.split())//3); score=min(92,45+length_score)
    return {"score":score,"strengths":["Clear response structure","Relevant technical vocabulary"],"weaknesses":[f"Add a concrete {topic} example","Discuss trade-offs and edge cases"],"improvement":"Lead with your approach, then validate it with complexity and an example."}
