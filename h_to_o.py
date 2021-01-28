from collections import defaultdict


def get_atom_dict(m, q=1):
    atom_dict = defaultdict(lambda: 0)
    number_string = ""
    current_atom = ""

    for char in m:
        if char.isnumeric():
            number_string += char
        else:
            if current_atom:
                atom_dict[current_atom] += from_number_string(number_string) * q
                number_string = ""
            current_atom = char

    if current_atom:
        atom_dict[current_atom] += from_number_string(number_string) * q

    return atom_dict


def from_number_string(ns):
    if ns:
        return int(ns)
    else:
        return 1


molecule, molecule_quantity = input().split()
molecule_quantity = int(molecule_quantity)
output = input()

existing_molecules = get_atom_dict(molecule, molecule_quantity)
output_molecules = sorted(get_atom_dict(output).items(), key=lambda x:-x[1])

output_quantity = 1000000000
for tup in output_molecules:
    m, q = tup
    output_quantity = min(existing_molecules[m]//q, output_quantity)

print(output_quantity)