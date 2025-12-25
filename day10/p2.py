import re
from ortools.sat.python import cp_model

def parse_buttons(buttons): 
    # Get button vectors 
    button_indices = []
    for b in buttons:
            indices = [int(x) for x in b.strip('()').split(',')]
            button_indices.append(tuple(indices))

    return button_indices

if __name__ == "__main__":
    cases = []
    with open('input.txt', 'r') as f:
        data = f.readlines()
        for k in range(len(data)):
            diagram = re.findall('\[.*\]', data[k])[0].strip('[]')
            buttons = re.findall('\(\d[,\d]*\)', data[k])
            reqs = [int(x) for x in re.findall('\{.*\}', data[k])[0].strip('{}').split(',')]

            buttons = parse_buttons(buttons)
            cases.append((diagram, buttons, reqs))

    _, buttons, req = cases[0]

    def solve_buttons_cpsat(req, buttons):
        """
        req: list[int] length R
        buttons: list[tuple[int]] length B; button j affects requirements in buttons[j]
        """
        R = len(req)
        B = len(buttons)

        # Upper bounds per button (safe)
        ub = [min(req[i] for i in idxs) if idxs else 0 for idxs in buttons]

        model = cp_model.CpModel()
        x = [model.NewIntVar(0, ub[j], f"x{j}") for j in range(B)]

        # Constraints: sum_{j affecting i} x_j == req[i]
        for i in range(R):
            model.Add(sum(x[j] for j in range(B) if i in buttons[j]) == req[i])

        # Objective: minimize total presses
        model.Minimize(sum(x))

        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = 10.0  # optional
        status = solver.Solve(model)

        if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            sol = [solver.Value(xj) for xj in x]
            return sol, sum(sol), status
        return None, None, status

    total_presses = 0
    for _, buttons, req in cases:
        sol, total, status = solve_buttons_cpsat(req, buttons)
        if sol is not None:
            total_presses += total
        else:
            print(f"No solution found, status {status}. You are probably missing some buttons.")

    print(total_presses)