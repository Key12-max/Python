""" this is sample code to show the process on validation
from flask import flash
class Burger:"""
"""    # Other Burger methods up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_burger(burger):
        is_valid = True # we assume this is true
        if len(burger['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(burger['bun']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if int(burger['calories']) < 200:
            flash("Calories must be 200 or greater.")
            is_valid = False
        if len(burger['meat']) < 3:
        flash("Meat must be at least 3 characters.")
            is_valid = False
        return is_valid"""

