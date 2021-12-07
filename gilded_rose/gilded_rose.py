class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.max_val= 50
        self.min_val = 0
    

    def quality_increase(self, item, value):
        if (item.quality + value) < self.max_val:
            item.quality += value 

    def quality_decrease(self, item, value):
        if (item.quality - value) >= self.min_val:
            item.quality -= value

    def sellin_decrease(self, item):
        item.sell_in -= 1 #no check as it can be negative
        
    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < self.max_val:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            self.quality_increase(item, 1)
                        if item.sell_in < 6:
                            self.quality_increase(item, 1)
            else:
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    self.quality_increase(item, 1)

    
        # for item in self.items:
        #     if item.name == "Aged Brie":
        #         self.sellin_decrease(item)
        #         self.quality_increase(item,1)
        #         if item.sell_in < 0:
        #             self.quality_increase(item,1)
                    
        #     elif item.name == "Backstage passes to a TAFKAL80ETC concert":
        #         self.quality_increase(item,1)
        #         if item.sell_in < 11:
        #             self.quality_increase(item,1)
        #         if item.sell_in < 6:
        #             self.quality_increase(item,1)
        #         if item.sell_in <= 0:
        #             item.quality = 0
        #         self.sellin_decrease(item)

        #     elif "Conjured" in item.name:
        #         self.sellin_decrease(item)
        #         self.quality_decrease(item,2)

        #     elif item.name != "Sulfuras, Hand of Ragnaros":
        #         self.sellin_decrease(item)
        #         self.quality_decrease(item,1)
        #         if item.sell_in < 0:
        #             self.quality_decrease(item,1)