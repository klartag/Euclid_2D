from ruamel.yaml import YAML
from mergedeep import merge
import networkx as nx
import os
import glob

yaml = YAML(typ='safe', pure=True)

# constructions_list = ['distance', 'Line', 'center', 'Circle', 'radius', 'midpoint', 'excircle', 'incircle', 'line_intersection', 'orientation', 'median', 'perpendicular_line', 'altitude', 'point_reflection', 'projection', 'line_reflection', 'orthocenter', 'circumcenter', 'centroid', 'abs', 'angle', 'exp', 'radical_axis', 'Circle_from_radius', 'parallel_line', 'line_circle_other_intersection', 'circle_circle_other_intersection', 'internal_angle_bisector', 'external_angle_bisector', 'midline', 'excenter', 'incenter', 'distance_from_line', 'perpendicular_bisector', 'nine_points_circle', 'euler_line', 'intersection_of_tangent_line_and_circle']
# predicates_list = ['parallel', 'inside_infinite_hourglass', 'between', 'inside_triangle', 'outside_triangle', 'tangent', 'triangle', 'perpendicular', 'concurrent', 'outside_infinite_hourglass', 'distinct', 'collinear', 'parallelogram', 'identical', 'trapezoid', 'convex', 'rectangle', 'concyclic', 'bisect', 'inside_convex_quadrilateral', 'outside_convex_quadrilateral', 'acute_triangle', 'isosceles_triangle', 'right_triangle', 'kite', 'isosceles_trapezoid', 'rhombus', 'square']

# load data from databases ymls

with open(f'rules/constructions_and_predicates/predicates_database.yml', 'r') as file:
    predicates_database = yaml.load(file)

with open(f'rules/constructions_and_predicates/constructions_database.yml', 'r') as file:
    constructions_database = yaml.load(file)

predicates_list = list(predicates_database.keys())
constructions_list = list(constructions_database.keys())


def get_constrdicates_from_text(t: str) -> list[str]:
    return [t_.split(' ')[-1] for t_ in t.split('(')[:-1]]


# example
get_constrdicates_from_text('distance(A, B) == radius(center(c))')

# predicates defined as Class
hard_predicates = [
    'identical',
    'distinct',
    'convex',
    'tangent',
    'between',
    'collinear',
    'not_collinear',
    'exists',
    'not_one_of'
]


construdicates_database = merge(predicates_database, constructions_database)
construdicates_names = list(construdicates_database.keys())

# print(len(construdicates_database))

# build the dictionary construdicates_relations that tell which construdicates does certian construdicate use
construdicates_relations = {}
for construdicate in construdicates_names:
    construdicate_id = construdicates_database[construdicate]
    list_of_where_and_conclude = [
        p[1] for p in construdicate_id.items() if p[0] in ['where', 'conclude', 'possible_conclusions']
    ]
    if len(list_of_where_and_conclude) > 0:
        output_list: list[list] = []
        for l in list_of_where_and_conclude:
            l = [get_constrdicates_from_text(t) for t in l]
            l = list(set().union(*l))
            output_list = output_list + l
        construdicates_relations[construdicate] = output_list
    else:
        construdicates_relations[construdicate] = []


# graph
def from_relations_to_edges(relations):
    edges = []
    for k in relations.keys():
        for v in relations[k]:
            edges.append((k, v))
    return edges


# Create a directed graph
G = nx.DiGraph()

# Add some edges to the graph
G.add_edges_from(from_relations_to_edges(construdicates_relations))
# nx.draw(G)

# Use Tarjan's algorithm to find strongly connected components
sccs = nx.strongly_connected_components(G)

# Print the cycles in the graph
print("Cycles in the graph:")
for scc in sccs:
    if len(scc) > 1:
        print(scc)

# fig = plt.figure(1, figsize=(60, 60), dpi=120)
# nx.draw(G, with_labels=True, font_weight='normal')
# print(G)


# build the dictionary construdicate_complexity that tell what is the complexity of each construdicate
construdicate_complexity = {}  # {construdicate:0 for construdicate in construdicates_names}
for hard_predicate in hard_predicates:
    construdicate_complexity[hard_predicate] = -1

num = 0
while len(list(set(construdicates_names).difference(set(construdicate_complexity.keys())))) > 0:
    #print(list(set(construdicates_names).difference(set(construdicate_complexity.keys()))))
    # num += 1
    # if num > 10: break
    for construdicate in construdicates_names:
        if len(construdicates_relations[construdicate]) == 0:  # there are no sons
            construdicate_complexity[construdicate] = 0
        else:  # there are sons
            all_sons_are_labeled = True
            for son in construdicates_relations[construdicate]:
                #if construdicate in list(set(construdicates_names).difference(set(construdicate_complexity.keys()))):
                #    print(f'son of {construdicate} is {son}')
                if not son in construdicate_complexity.keys():
                    all_sons_are_labeled = False
            if all_sons_are_labeled:
                construdicate_complexity[construdicate] = (
                    max(construdicate_complexity[son] for son in construdicates_relations[construdicate]) + 1
                )


# check wheter there are construdicates in construdicates_names which are not in predicates_list + constructions_list
unknown = [x for x in construdicates_names if x not in predicates_list]
unknown = [x for x in unknown if x not in constructions_list]


# check wheter there are construdicates in predicates_list + constructions_list which are not in construdicates_names
# and there are - the 'hard predicates'
too_much1 = [x for x in predicates_list if x not in construdicates_names]
too_much2 = [x for x in constructions_list if x not in construdicates_names]

# print('in construdicates_names and not in predicates_list or constructions_list:')
# print(unknown)
# print('in predicates_list or constructions_list and not in construdicates_names:')
# print(too_much1 + too_much2)

# into yamls
# make file list that group togthere all the construdicates that have the same type (construction \ predicate) and complexity
files_list = {}
for construdicate in construdicates_names:
    if construdicate in constructions_list:
        construdicate_type = 'construction'
    else:
        construdicate_type = 'predicate'
    complexity = construdicate_complexity[construdicate]
    file_name = f'{construdicate_type}_{complexity}'
    if file_name in files_list.keys():
        files_list[file_name][construdicate] = construdicates_database[construdicate]
    else:
        files_list[file_name] = {construdicate: construdicates_database[construdicate]}

# clear folders
files = glob.glob('rules/constructions_and_predicates/hierarchy/predicates/*')
for f in files:
    os.remove(f)
files = glob.glob('rules/constructions_and_predicates/hierarchy/constructions/*')
for f in files:
    os.remove(f)

# enter files
for file_name in list(files_list.keys()):
    if file_name.split('_')[0] == 'predicate':
        with open(f'rules/constructions_and_predicates/hierarchy/predicates/{file_name}.yml', 'w+') as outfile:
            yaml.dump(files_list[file_name], outfile)  # , default_flow_style=False)
    if file_name.split('_')[0] == 'construction':
        with open(f'rules/constructions_and_predicates/hierarchy/constructions/{file_name}.yml', 'w+') as outfile:
            yaml.dump(files_list[file_name], outfile)  # , default_flow_style=False)
