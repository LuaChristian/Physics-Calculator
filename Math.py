class Math:

    def speed(self, distance, time):
        speed = distance / time
        return speed

    def distance(self, speed, time):
        distance = speed * time
        return distance

    def acceleration(self, dv, time):
        acceleration = dv / time
        return acceleration

    def density(self, mass, volume):
        density = mass / volume
        return density

    def force(self, mass, acceleration):
        force = mass * acceleration
        return force
