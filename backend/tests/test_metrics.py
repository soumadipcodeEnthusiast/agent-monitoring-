from app.evaluation.metrics import calculate_task_success_rate

def test_metrics():
    res = calculate_task_success_rate([{'success': True}, {'success': False}])
    assert res == 0.5
