def toh(n_disk, source, helper, destination):
    if n_disk == 0:
        return
    toh(n_disk - 1, source, destination, helper)
    print(f"{source} -> {destination}")
    toh(n_disk - 1, helper, source, destination)

toh(3, "A", "B", "C")
