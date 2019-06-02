#  Copyright (c) 2019. Created by Tomasz Piechocki

from Organisms.organism import Organism
from World.Field.field import Field
from World.Directions.direction import Direction
from World.Directions.squareDirection import SquareDirection


class Animal(Organism):
    def __init__(self, x, y, wrld):
        super().__init__(x, y, wrld)

    def _travel(self, field: Field, direction: Direction):
        """
        Travel in the given direction.
        :param field: Actual field of organism
        :param direction: direction of move
        :return: None
        """
        target: Field = field.getNeighbour(direction)
        self._previous_x = self._x
        self._previous_y = self._y

        if target is not None:
            self._x = target.getX()
            self._y = target.getY()
            field.setOrganism(None)

            if target.isEmpty():
                target.setOrganism(self)
            elif type(self) is type(target.getOrganism()):
                self.__breed(target.getOrganism())
            else:
                target.getOrganism()._collision(self)

    def __breed(self, other: Organism):
        """
        Breed for two organisms of the same kind
        :param other: other organism
        :return: None
        """
        self.setPreviousXY()

        field = self._world.getField(other.getX(), other.getY())
        if field.hasEmptyNeighbour():
            field: Field = field.randomEmptyNeighbour()
        else:
            return

        new_org: Organism = other.createNewInstance(field.getX(), field.getY(), self._world)
        self._world.addOrganism(new_org)
        self._world.addNotification(repr(self) + ": Zwierzę się rozmnożyło.")

    def action(self):
        field = self._world.getField(self._x, self._y)
        direction = field.getDirection().randomDirection()

        self._travel(field, direction)

