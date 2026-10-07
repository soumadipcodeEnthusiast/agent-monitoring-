from app.perturbations.tool_failures import TimeoutPerturbation

def test_timeout():
    p = TimeoutPerturbation()
    ctx = {}
    p.apply(ctx)
    assert ctx.get('error') == 'TimeoutError'
