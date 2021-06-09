from src.data.entities import storyname


# domain file
def make_domain(predicates, operators):

    domainfile = predicates + "\n" + operators + ")"
    print("\n", "Domain file...", "\n", "\n ")
    print(domainfile)

    # writing to file
    f = open(storyname + "domain.pddl", "w")
    f.write(domainfile)
    f.close()


# problem file
def make_problem(initial_objects, initial_state, goals):

    problemfile = initial_objects + "\n" + initial_state + "\n" + goals + ")"
    print("\n", "Problem file...", "\n", "\n ")
    print(problemfile)

    # writing to file
    f = open(storyname + "problem.pddl", "w")
    f.write(problemfile)
    f.close()
