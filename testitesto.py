def TowersOfHanoi():
    def move(n, source, target, auxiliary):
        if n == 1:
            print(f"Move disk 1 from {source} to {target}")
            return
        move(n - 1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        move(n - 1, auxiliary, target, source)

    n = 3  # Number of disks
    move(n, 'A', 'C', 'B')  # A is the source, C is the target, B is the auxiliary  
    