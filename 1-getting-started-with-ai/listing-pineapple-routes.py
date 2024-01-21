portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    # Write your recursive code here
    if ports:
        for i in range(len(ports)):
            updated_route = route + [ports[i]]
            rest_ports = ports[:i] + ports[i+1:]
            permutations(updated_route, rest_ports)
    else:
    # Print the port names in route when the recursion terminates
      print(' '.join([portnames[i] for i in route]))


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))
