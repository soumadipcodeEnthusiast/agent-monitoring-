def calculate_task_success_rate(results: list) -> float:
    if not results: return 0.0
    successes = sum(1 for r in results if r.get('success'))
    return successes / len(results)
