from abc import ABC, abstractmethod  # For Builder classes


# valeteam
# GOKTUG SELCUK AND GUNGOR YOLAC

# Final Product########################

class Robot:
    def __init__(self):

        self.description = None
        self.pedals = None
        self.wheels = None
        self.wings = None
        self.blades = None
        self.arms = None
        self.traversal = []
        self.detection_systems = []

    def setPedals(self, pedals):
        self.pedals = pedals

    def setArms(self, arms):
        self.arms = arms

    def setWheels(self, wheels):
        self.wheels = wheels

    def setWings(self, wings):
        self.wings = wings

    def setBlades(self, blades):
        self.blades = blades

    def setDescription(self, description):
        self.description = description

    # SPECIFICATION FUNCTION
    def printInfo(self):

        print(self.description)
        print("\n")
        print("traversal modules installed:")
        for component in self.traversal:
            print(component)
        print("\n")
        print("detection systems installed: ")
        for detectionsystem in self.detection_systems:
            print(detectionsystem)
        print("----------------------------------")
        print("\n")


# PARTS OF ROBOT #############################

class Pedals:
    numberofPedals = None

    def stringreturn(self, numberofPedals):
        component = numberofPedals + " pedals"
        return component


class Wheels:
    numberofWheels = None

    def stringreturn(self, numberofWheels):
        component = numberofWheels + " wheels"
        return component


class Arms:
    numberofArms = None

    def stringreturn(self, numberofArms):
        component = numberofArms + " arms"
        return component


class Wings:
    numberofWings = None

    def stringreturn(numberofWings):
        strWings = str(numberofWings)
        component = strWings, "wings"
        return component


class Blades:
    numberofBlades = None

    def stringreturn(numberofBlades):
        strBlades = str(numberofBlades)
        component = strBlades, "blades"
        return component


class DetectionSystem:
    type = None


###BUILDER CLASSES###########################

class RobotBuilder(ABC):

    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def getTraversal(self):
        pass

    @abstractmethod
    def getDetectionSystems(self):
        pass


class AndroidBuilder(RobotBuilder):
    androidTraversal = []
    detectionSystems = []

    def getDescription(self):
        desc = "BIPEDAL ROBOT "
        return desc

    def getPedals(self):
        pedals = Pedals()
        pedals.numberofPedals = "two"
        self.androidTraversal.append(pedals.stringreturn(pedals.numberofPedals))
        return pedals

    def getArms(self):
        arms = Arms()
        arms.numberofArms = "two"
        self.androidTraversal.append(arms.stringreturn(arms.numberofArms))
        return arms

    def getTraversal(self):
        return self.androidTraversal

    def getDetectionSystems(self):
        detectionSystems = []
        detectionsys = DetectionSystem()
        detectionsys.type = "cameras"
        detectionSystems.append(detectionsys.type)
        return detectionSystems


class AutonomousCarBuilder(RobotBuilder):
    androidTraversal = []
    detectionSystems = []

    def getDescription(self):
        desc = "ROBOT ON WHEELS"
        return desc

    def getWheels(self):
        wheels = Wheels()
        wheels.numberofWheels = "four"
        self.androidTraversal.append(wheels.stringreturn(wheels.numberofWheels))
        return wheels

    def getTraversal(self):
        return self.androidTraversal

    def getDetectionSystems(self):
        detectionSystems = []
        detectionsys = DetectionSystem()
        detectionsys.type = "infrared"
        detectionSystems.append(detectionsys.type)
        return detectionSystems

    # DIRECTOR CLASS #############################


class Director:
    def make_robot(self, builder):
        if isinstance(builder, AndroidBuilder):

            android = Robot()
            pedal = builder.getPedals()
            android.setPedals(pedal)

            arm = builder.getArms()
            android.setArms(arm)

            description = builder.getDescription()
            android.setDescription(description)

            traversals = builder.getTraversal()
            android.traversal = traversals

            detectionsys = builder.getDetectionSystems()
            android.detection_systems = detectionsys

            return android

        elif isinstance(builder, AutonomousCarBuilder):
            car = Robot()

            wheel = builder.getWheels()
            car.setWheels(wheel)

            description = builder.getDescription()
            car.setDescription(description)

            traversals = builder.getTraversal()
            car.traversal = traversals

            detectionsys = builder.getDetectionSystems()
            car.detection_systems = detectionsys

            return car


def main():
    director = Director()

    builder = AndroidBuilder()

    Asimo = director.make_robot(builder)
    Asimo.printInfo()

    builder = AutonomousCarBuilder()
    tesla = director.make_robot(builder)
    tesla.printInfo()


if __name__ == '__main__':
    main()