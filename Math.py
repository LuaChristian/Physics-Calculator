class Math:

    def speed(self, distance, time):
        speed = distance / time
        return speed

    def time_speed(self, distance, speed):
        time = distance / speed
        return time

    def distance_speed(self, speed, time):
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
