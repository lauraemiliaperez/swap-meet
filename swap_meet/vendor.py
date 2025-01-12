class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []

        self.inventory = inventory


    def add(self, item):
        """Adds item to the inventory"""
        self.inventory.append(item)
        return item

    def remove(self, item):
        """Removes the matching item from the inventory"""
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        
        return False

    # ----- Wave 2 -----------------------------

    def get_by_id(self, id):
        """Returns the item with matching id from inventory"""
        for item in self.inventory:
            if item.id == id:
                return item

        return None
    
    # ----- Wave 3 -----------------------------

    def swap_items(self, other_vendor, my_item, their_item):
        """Removes my_item from self.inventory, 
        and adds it to the other_vendor's inventory
        Removes their_item from the other_vendor's inventory, 
        and adds it to self.inventory"""
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            
            return False

        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        
        return True
    
    # ----- Wave 4 -----------------------------
    def swap_first_item(self, other_vendor): 
        """removes the first item from its inventory, and adds the other_vendor's first item
        Removes the first item from the other_vendor's inventory, and adds the instances first item"""
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            
            return False
        
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

        return True
        

    # --- Wave 6 -------------------------------
    def get_by_category(self, category):
        """Argument: a string. 
        Returns a list of objects (in that category) from the inventory"""
        item_by_category = []
        for item in self.inventory:
            if category == item.get_category():
                item_by_category.append(item)
        return item_by_category
    
    def get_best_by_category(self, category):
        """Return the item with the best condition in a certain category"""
        item_by_category = self.get_by_category(category)
        if not item_by_category:
            return None
        best_item = item_by_category[0]
        for item in item_by_category:
            if item.condition > best_item.condition:
                best_item = item
        return best_item


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """ This method swaps the best item of certain categories with another Vendor"""
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        if not self.get_by_category(their_priority) or not other_vendor.get_by_category(my_priority):
            return False
        
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)
        self.swap_items(other_vendor,my_best,their_best)
        return True


    def get_the_newest(self):
        """Return the newest item in the inventory"""
        newest_item = self.inventory[0]
        for item in self.inventory:
            if item.age < newest_item.age:
                newest_item = item
        return newest_item

    def swap_by_newest(self, other_vendor):
        """Swap the newest item in the inventory with another vendor's newest item"""
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        my_newest = self.get_the_newest()
        other_vendor_newest = other_vendor.get_the_newest()
        self.swap_items(other_vendor, my_newest, other_vendor_newest)
        return True