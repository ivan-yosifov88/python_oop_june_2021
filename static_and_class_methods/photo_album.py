class PhotoAlbum:
    MAX_PHOTOS_ON_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.get_pages()

    def get_pages(self):
        photos = []
        for _ in range(self.pages):
            photos.append(list())
        return photos

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count//cls.MAX_PHOTOS_ON_PAGE)

    def add_photo(self, label):
        for i in range(1, len(self.photos) + 1):
            if len(self.photos[i - 1]) < PhotoAlbum.MAX_PHOTOS_ON_PAGE:
                self.photos[i - 1].append(label)
                return f"{label} photo added successfully on page {i} slot {len(self.photos[i-1])}"
        return "No more free slots"

    def display(self):
        line_with_dashes = f"{11 * '-'}\n"
        result = line_with_dashes
        for page in self.photos:
            photos_on_page = ["[]"] * len(page)
            result += f"{' '.join(photos_on_page)}\n"
            result += line_with_dashes
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
