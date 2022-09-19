class House:
    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        buckets_needed_for_one_square = 2.5
        total_buckets = self.wall_area * buckets_needed_for_one_square
        return total_buckets


class Paint:
    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19


class DiscountedPaint(Paint):
    def discounted_price(self, discount_percentage):
        total_price = self.total_price()
        discounted_price = total_price * (discount_percentage / 100)
        return total_price - discounted_price


