import os
import subprocess

heuristic = "astar(ipdb())"
def plan_quest():

    with open("garbage","w") as garbage:
        subprocess.call(["/Users/GBOYEs/PycharmProjects/conan-procedural-quest-generation-master/downward/src/translate/translate.py","domain.pddl", "problem.pddl"], stdout=garbage)
    with open("output.sas","r") as output:
        with open(os.path.join("","quest.soln"),"w") as solution:
            calc = subprocess.Popen(["/Users/GBOYEs/PycharmProjects/conan-procedural-quest-generation-master/downward/fast-downward.py","domain.pddl", "problem.pddl", '--search', heuristic], stdin=output, stdout=solution)
    os.chdir("..")
    os.chdir("..")
    return calc

plan_quest()
