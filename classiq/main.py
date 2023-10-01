import classiq
from classiq import (
    synthesize,
    execute,
    show,
    construct_grover_model,
    RegisterUserInput,
    GeneratedCircuit
)
from classiq import set_constraints, Constraints, set_preferences, Preferences


grover_model = construct_grover_model(
    definitions=[
        ("x2", RegisterUserInput(size=2)),
        ("x3", RegisterUserInput(size=2)),
        ("x4", RegisterUserInput(size=2)),
        ("x5", RegisterUserInput(size=2)),
        ("x6", RegisterUserInput(size=2)),
        ("x8", RegisterUserInput(size=2)),
        ("x9", RegisterUserInput(size=2)),
        ("x11", RegisterUserInput(size=2)),
        ("x12", RegisterUserInput(size=2)),
        ("x13", RegisterUserInput(size=2)),
        ("x14", RegisterUserInput(size=2)),
        ("x15", RegisterUserInput(size=2)),
    ],
    expression=
    "(2 != x2) and (2 != x3) and (2 != x4) and (x2 != x3) and " +
    "(x2 != x4) and (x3 != x4) and (x5 != x6) and (x5 != 3) and (x5 != x8)" +
    " and (x6 != 3) and (x6 != x8) and (3 != x8) and (x9 != 4) and " +
    "(x9 != x11) and "
    "(x9 != x12) and (4 != x11) and (4 != x12) and (x11 != x12) and " +
    "(x13 != x14) and (x13 != x15) and (x13 != 1) and (x14 != x15) and " +
    "(x14 != 1) and (x15 != 1) and (2 != x5) and (2 != x9) and (2 != x13)" +
    " and (x5 != x9) and (x5 != x13) and (x9 != x13) and (x2 != x6) and " +
    "(x2 != 4) and (x2 != x14) and (x6 != 4) and (x6 != x14) and " +
    "(4 != x14) and (x3 != 3) and (x3 != x11) and (x3 != x15) and " +
    "(3 != x11) and (3 != x15) and (x11 != x15) and (x4 != x8) and " +
    "(x4 != x12) " +
    "and (x4 != 1) and (x8 != x12) and (x8 != 1) and (x12 != 1) and " +
    "(2 != x6) and (x9 != x14) and (x3 != x8) and (x11 != 1) and (x2 != x5) " +
    "and (4 != x13) and (x4 != 3) and (x12 != x15)",
    num_reps=2,
)
grover_model = set_constraints(grover_model, Constraints(max_width=82))
#grover_model = set_preferences(grover_model, Preferences(optimization_timeout_seconds=600))
qprog = synthesize(grover_model)

res = execute(qprog).result()
results = res[0].value
print(results)