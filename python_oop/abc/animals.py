#!/usr/bin/env python3
"""Abstract Animal class and its concrete subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """A dog."""

    def sound(self):
        """Return the dog sound."""
        return "Bark"


class Cat(Animal):
    """A cat."""

    def sound(self):
        """Return the cat sound."""
        return "Meow"
