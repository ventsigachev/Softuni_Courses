class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        [self.photos.append([]) for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return PhotoAlbum(photos_count // 4)

    def add_photo(self, label: str):
        for p in range(len(self.photos)):
            if len(self.photos[p]) < 4:
                self.photos[p].append(label)
                return f'{label} photo added successfully on page {p + 1} slot {len(self.photos[p])}'
        return "No more free spots"

    def display(self):
        result = "-----------\n"
        for p in self.photos:
            if p:
                result += " ".join("[]" for _ in range(len(p)))
            result += "\n" + "-----------\n"
        return result


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
