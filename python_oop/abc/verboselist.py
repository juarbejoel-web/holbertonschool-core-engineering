#!/usr/bin/env python3
"""VerboseList: a list that prints a message on every change."""


class VerboseList(list):
    """A list that notifies when items are added or removed."""

    def append(self, item):
        """Append an item and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extend the list and print how many items were added."""
        items = list(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Print a notification and remove the item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print a notification and pop the item at index."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
